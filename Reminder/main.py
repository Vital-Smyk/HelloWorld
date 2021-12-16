import sqlalchemy as db
from sqlalchemy.orm import Session, session
from sqlalchemy.sql.expression import select
import constructor as cons
from sqlite3.dbapi2 import Connection, Cursor

engine = db.create_engine('sqlite:///db.sqlite3')
connetion = engine.connect()

session =  Session(engine) 
bike1 = cons.Bike('Rose', 14,2)
bike2 = cons.Bike('Green', 10,3)
bike3 = cons.Bike('Black', 19,2)
session.add(bike1)
session.add(bike2)
session.add(bike3)
session.commit()

# bikes = session.execute(select(app3.Bike).all())

session.close()
# app3.Bike
connetion.close()