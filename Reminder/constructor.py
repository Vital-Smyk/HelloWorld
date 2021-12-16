from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.sql.expression import false, true

Base = declarative_base()

class User(Base):
    __tablename__ =  'Users'
    user_id = Column(Integer, primary_key= True, autoincrement=True, nullable=False)
    login = Column(String,unique = True)
    password = Column(String,)
    first_name = Column(String,)
    last_name = Column(String,)
    dob = Column(Date,) 

    def __init__(self,__login,__password,__first_name,__lenght,__count):
        self.login = __login
        self.password = __password
        self.first_name = __first_name
        self.length = __lenght
        self.wheels_count =__count


class Reminder(Base):
    __tablename__ =  'Reminds'
    rem_id = Column(Integer, primary_key = True, autoincrement=True, nullable=False)
    content = Column(String,)
    dt = Column(Date,) 
    user = Column(Integer,)
    check = Column(Boolean,default= False)
    
    def __init__(self,__content,__dt,__user,__check):
        self.content = __content
        self.dt = __dt
        self.user = __user
        self.check = __check
