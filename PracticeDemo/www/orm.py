#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' type the description of this module file here'
#                ┏┓      ┏┓
#             ┏┛┻━━━┛┻┓
#             ┃      ☃      ┃
#             ┃  ┳┛  ┗┳  ┃
#             ┃      ┻      ┃
#             ┗━┓      ┏━┛
#                 ┃      ┗━━━┓
#                 ┃  神兽保佑    ┣┓
#                 ┃　永无BUG！   ┏┛
#                 ┗┓┓┏━┳┓┏┛
#                   ┃┫┫  ┃┫┫
#                   ┗┻┛  ┗┻┛
#
# -------------------------------------------------------------------------------

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates
import asyncio,aiomysql,time,uuid,sys
import logging
from logging import log
# from .models import User ---这里导入包有问题

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

# 创建连接池, 不需要反复的打开和关闭数据库，能复用的就尽情的复用
# TypeError: create_pool() missing 1 required positional argument: 'loop'
@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    #创建连接池，全局变量__pool来存储连接池
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )
# event loop is closed 报错的修改方法
@asyncio.coroutine
def destory_pool(): #销毁连接池
    global __pool
    if __pool is not None:
        __pool.close()
        yield from  __pool.wait_closed()


# 封装数据库的select，作用 需要传入sql语句和参数，然后返回筛选的结果。
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    # 使用with as 不用担心关闭连接 -*- yield from 从连接池中返回一个连接
    with (yield from __pool) as conn:
        # 创建游标对象
        cur = yield from conn.cursor(aiomysql.DictCursor)
        # 执行sql，使用占位符 mysql的占位符是%s SQL的是？
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            # 获取指定数量的数据
            rs = yield from cur.fetchmany(size)
        else:
            # 获取所有的数据
            rs = yield from cur.fetchall()
        # 这个游标还是得要关闭的，也是一个资源对象
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

#Insert, Update, Delete
@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            # SQL语句的占位符为?，MySQL的占位符为%s
            yield from cur.execute(sql.replace('?', '%s'), args)
            # 返回非查询语句的执行结果，有多少行受到了影响
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        # 这个好像才是关键，关于连接池还要多了解，数据库方面的东西
        finally:
            conn.close()
        return affected

# 根据输入的参数生成占位符列表
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    # 生成 ?,?,? 返回的是一个字符串
    return ', '.join(L)

# region   Field 的作用就是将用户传入的数据转换为数据库可以使用的字段类型对象，负责保存(数据库)表的字段名和字段类型
class Field(object):
    # 初始化一个字段的基本信息
    def __init__(self, name, column_type, primary_key, default):
        self.name = name # 字段名
        self.column_type = column_type # 字段类型
        self.primary_key = primary_key # 字段是否为主键
        self.default = default # 默认值
    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)
class StringField(Field):
    # 注意 这里子类的构造函数还是传递给父类来构造的 ddl还是赋值给了column_type了。
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)
class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)
class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)
class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)
# endregiond


# 这是一个元类，元类的作用：让子类隐含的继承一些东西（ModelMetaclass元类定义了所有Model基类(继承ModelMetaclass)的子类实现的操作）
# 所有的元类都继承自type
# -*-ModelMetaclass的工作主要是为一个数据库表映射成一个封装的类做准备：
# ***读取具体子类(user)的映射信息
# 创造类的时候，排除对Model类的修改
# 在当前类中查找所有的类属性(attrs)，如果找到Field属性，就将其保存到__mappings__的dict中，同时从类属性中删除Field(防止实例属性遮住类的同名属性)
# 将数据库表名保存到__table__中
# 完成这些工作就可以在Model中定义各种数据库的操作方法
class ModelMetaclass(type):
    # __new__控制__init__的执行，所以在其执行之前
    # cls:代表要__init__的类，此参数在实例化时由Python解释器自动提供(例如下文的User和Model)
    # bases：代表继承父类的集合
    # attrs：类的方法集合
    def __new__(cls, name, bases, attrs):
        if name=='Model':   #如果是类的名字就是model（不是User类调用的，那么直接返回不修改）
            return type.__new__(cls, name, bases, attrs)
        # 获取table名字，如果没有设置__table__属性就让类名作为它的表名
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        # 获取Field和主键名
        mappings = dict()
        fields = []
        primaryKey = None #记录哪个是主键
        # User类（这里只是举例，要被实例化的类）的所有属性，来获取其字段及值而准备操作数据库
        for k, v in attrs.items():
            # v是字段类型的话（上方定义的那种类型）
            if isinstance(v, Field):
                # logging.info('  found mapping: %s ==> %s' % (k, v))
                # 将这些东西全部映射到map中
                mappings[k] = v
                if v.primary_key:
                    # 找到主键: 如果主键已经存在了说明主键重复（忽略联合主键）
                    if primaryKey:
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    # 如果不是主键，说明就是普通的字段，加入字段分区
                    fields.append(k)
        # 如果没有主键
        if not primaryKey:
            raise RuntimeError('Primary key not found.')
        # 从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
        for k in mappings.keys():
            attrs.pop(k) # 这里面pop的是类的attrs的，mapping已经将他们全部保存了

        # 保存除主键外的属性名为``（``里面的内容转换为字符串）列表形式
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = tableName #表名
        attrs['__primary_key__'] = primaryKey # 主键属性名
        attrs['__fields__'] = fields # 除主键外的属性名
        # 构造sql语句
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)


# 定义ORM所有映射的基类：Model
# Model类的任意子类可以映射一个数据库表
# Model类可以看作是对所有数据库表操作的基本定义的映射

# 基于字典查询形式
# Model从dict继承，拥有字典的所有功能，可以这样使用class[attr]
# 同时实现特殊方法__getattr__和__setattr__，能够实现属性操作（也就说这两个方法就是为了使得可以class.attr可以使用）
# 实现数据库操作的所有方法，定义为class方法，所有继承自Model都具有数据库操作方法
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value
###########################这里面就可以写实体类对数据库的具体作用了###########################################
    # 类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]
        if where:
            # 带where 就把where 附上去
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        # 是否需要排序
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        #limit 是抽取多少条到多少条数据
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)# 使用的是元类的select
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        ' find object by primary key. '
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.info('failed to insert record: affected rows: %s' % rows)

    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.info('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.info('failed to remove by primary key: affected rows: %s' % rows)

# #  具体应用
# class User(Model):
#         # 定义类的属性到列的映射： 需要和数据库里面的表对应
#         id = IntegerField('id', primary_key=True)
#         name = StringField('username')
#         email = StringField('email')
#         password = StringField('password')
#
# # # 创建一个实例：
# # u = User(id=12345, name='justin', email='zhrlova@hotmail.com', password='password')
# # print(u)
# # # 保存到数据库：
# # u.save()
# # print(u)
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    # Field的参数是很有必要的，可以将default传入一个函数，这样可以对传入的参数进行自动计算
    created_at = FloatField(default=time.time)

loop = asyncio.get_event_loop()
# event loop is closed报错处理
@asyncio.coroutine
def test():
    #将数据保存到数据库
    yield from create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='zhao@qq.com', passwd='1234567890', image='about:blank')
    yield from u.save()
    yield from destory_pool()

loop.run_until_complete(test())
loop.close()
if loop.is_closed():
        sys.exit(0)

for x in test():
    pass

