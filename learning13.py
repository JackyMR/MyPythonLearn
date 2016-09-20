#!usr/bin/env python3
#_*_ coding: utf-8 _*_

"a  test class";

__author__ = "Jacky Yuan";

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

hello = Hello();
hello.hello();

print(type(Hello));
print(type(hello));

# type()函数可以查看一个类型或变量的类型，
# Hello是一个class，它的类型就是type，
# 而h是一个实例，它的类型就是class Hello。

#MetaClass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass



class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id');
    name = StringField('username');
    email = StringField('email');
    password = StringField('password');

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd');
# 保存到数据库：
u.save();

class Field(object):

    def __init__(self, name, column_type):
        self.name = name;
        self.column_type = column_type;
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name);

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)');

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint');

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs);
        print('Found model: %s' % name);
        mappings = dict();
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v));
                mappings[k] = v;
        for k in mappings.keys():
            attrs.pop(k);
        attrs['__mappings__'] = mappings; # 保存属性和列的映射关系
        attrs['__table__'] = name; # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs);

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw);

    def __getattr__(self, key):
        try:
            return self[key];
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key);

    def __setattr__(self, key, value):
        self[key] = value;

    def save(self):
        fields = [];
        params = [];
        args = [];
        for k, v in self.__mappings__.items():
            fields.append(v.name);
            params.append('?');
            args.append(getattr(self, k, None));
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params));
        print('SQL: %s' % sql);
        print('ARGS: %s' % str(args));

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd');
u.save();

# 以下为输出结果:
# Found model: User
# Found mapping: email ==> <StringField:email>
# Found mapping: password ==> <StringField:password>
# Found mapping: id ==> <IntegerField:uid>
# Found mapping: name ==> <StringField:username>
# SQL: insert into User (password,email,username,id) values (?,?,?,?)
# ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]