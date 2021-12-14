from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义Student对象
class Student(Base):
    # 表的名字
    __tablename__ = 'students'

    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    sex = Column(String(16))
    age = Column(Integer)
    home = Column(String(128))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:ljk0204LJK!@localhost:3306/tests')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

if __name__ == '__main__':
    # 创建session对象:
    session = DBSession()
    # 创建新Student对象:
    # new_student = Student(id=7, name='周雪冰', sex='女', age=23, home='海南海口')
    # 添加到session:
    # session.add(new_student)
    # 查询id为4的学生:
    student_1 = session.query(Student).filter(Student.id == 4)
    print(student_1)
    print(type(student_1))
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
