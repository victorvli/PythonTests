# -*- coding:utf-8 -*-
# @Author: LiJunKai
# @Date: 2021/08/03 10:38

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, inspect, create_engine

engine = create_engine("presto://192.168.0.37:8080/mysql/mydb")
session = sessionmaker(bind=engine)()

# 将数据库的表反射出来
metadata = MetaData(bind=engine)
metadata.reflect(bind=engine, schema="victor", only=["students"])
Base = automap_base(metadata=metadata)
Base.prepare()

# ow就是students表对应的类
students = getattr(Base.classes, "students")
# 获取主键
primary_key = inspect(students).primary_key
print(primary_key)  # (Column('id', INTEGER(), table=<overwatch>, primary_key=True, nullable=False),)
# 由于会有多个主键，所以是一个序列。这里我们只有一个主键，所以取第一个，然后拿到名字
print(primary_key[0].name)  # id
# 那么如何拿到表的所有字段名呢？
print(inspect(students).c.keys())  # ['id', 'name', 'age', 'hp', 'attack', 'role', 'ultimate', 'country']
# 那如何拿到字段的类型呢？
columns = inspect(students).columns
print(list(columns))
"""
[Column('id', INTEGER(), table=<overwatch>, primary_key=True, nullable=False),
Column('name', VARCHAR(length=255), table=<overwatch>, nullable=False),
Column('age', INTEGER(), table=<overwatch>), Column('hp', INTEGER(), table=<overwatch>),
Column('attack', VARCHAR(length=255), table=<overwatch>),
Column('role', VARCHAR(length=255), table=<overwatch>),
Column('ultimate', VARCHAR(length=255), table=<overwatch>),
Column('country', VARCHAR(), table=<overwatch>)]
"""
# 以上便是每一个字段的属性组成的列表，每一个元素都是<class 'sqlalchemy.sql.schema.Column'>类型
# 那么我们便可以拿到相应的属性
for col_attr in columns:
    print(f"字段名:{col_attr.name},"
          f"是否为主键:{col_attr.primary_key},"
          f"字段类型:{str(col_attr.type)},"
          f"是否允许非空:{col_attr.nullable}",
          f"注释:{col_attr.comment}")
"""
字段名:id,是否为主键:True,字段类型:INTEGER,是否允许非空:False 注释:英雄的id
字段名:name,是否为主键:False,字段类型:VARCHAR(50),是否允许非空:False 注释:英雄的姓名
字段名:age,是否为主键:False,字段类型:INTEGER,是否允许非空:True 注释:英雄的年龄
字段名:hp,是否为主键:False,字段类型:INTEGER,是否允许非空:True 注释:英雄的血量
字段名:attack,是否为主键:False,字段类型:VARCHAR(255),是否允许非空:True 注释:攻击类型
字段名:role,是否为主键:False,字段类型:VARCHAR(255),是否允许非空:True 注释:英雄定位
字段名:ultimate,是否为主键:False,字段类型:VARCHAR(255),是否允许非空:True 注释:终极技能
字段名:country,是否为主键:False,字段类型:TEXT,是否允许非空:True 注释:英雄的国籍
"""