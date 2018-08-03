#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 23:02
# @File    : orm.py
# @Software: PyCharm

import logging;

logging.basicConfig(level=logging.INFO)
import aiomysql


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


async def create_pool(**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
    )


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned:%s' % len(rs))
        return rs


async def execute(sql, args, autocommit=True):
    log(sql, args)
    async with __pool.acquire() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount  # 影响行数
                if not autocommit:
                    await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # 获取table名称
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        primaryKey = None
        fields = []
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                if v.primary_key:
                    if primaryKey:
                        raise RuntimeError('Duplicate primary key for field:%s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('PrimaryKey not found')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s`,%s from %s ' % (primaryKey, ','.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into %s (%s,%s) values (%s)' % (
            tableName, ','.join(fields), primaryKey, ','.join('?' * len(mappings)))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
            tableName, ','.join(map(lambda f: '`%s`=?' % f, fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Model" has no attribute %s' % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]  # 查取属性对应的列的数量类型默认值
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    async def find(cls, pk):
        'find object by primary key'
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), pk, 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get("orderBy", None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            if isinstance(limit, tuple) and len(limit == 2):
                sql.append('?,?')
                args.append(limit)
            else:
                raise ValueError('Invalid limit value :%s' % limit)
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    async def save(self):
        'save object'
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record:affected rows:%s' % rows)

    async def update(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update record:affected rows:%s' % rows)

    async def remove(self):
        args = self.getValue(self.__primary_key__)
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to delete record:affected rows:%s' % rows)


class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s,%s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class BooleanField(Field):
    def __init__(self, name=None, primary_key=False, default=False):
        super().__init__(name, 'boolean', primary_key, default)


class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


import asyncio

# if __name__ == '__main__':
#     class User(Model):  # 虽然User类乍看没有参数传入，但实际上，User类继承Model类，Model类又继承dict类，所以User类的实例可以传入关键字参数
#         id = IntegerField('id', primary_key=True)  # 主键为id， tablename为User，即类名
#         name = StringField('name')
#
#
#     loop = asyncio.get_event_loop()
#
#
#     async def tesst():
#         await create_pool(loop=loop, host='localhost', port=3306, user='root', password='123456', db='test222222',
#                           charset='utf8')
#         # 创建实例:
#         # user = User(id=1223, name='pit')
#         # r = await user.save()
#         # r = await User.find(123)
#         # print(r)
#         # r = await User.findAll(where='name = \'bob\'')
#         # print(r)
#         # user = User(id=1223, name='mike')
#         # r = await user.update()
#         # print(r)
#
#         user = User(id=1222, name='aaa')
#         r = await user.remove()
#         print(r)
#
# loop.run_until_complete(tesst())
# loop.close()
