# SQLAlchemy (ORM Lib)
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from sqlalchemy import asc, desc

engine = sqlalchemy.create_engine('mysql+pymysql://root:my-secret-pw@127.0.0.1:3306/test_mysql_db2')

# Base = sqlalchemy.ext.declarative.declarative_base()
Base = sqlalchemy.orm.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True        
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
sess = Session()

person = Person(name='Mike')
sess.add(person)
person2 = Person(name='Mike2')
sess.add(person2)
person3 = Person(name='Mike3')
sess.add(person3)
sess.commit()


p4 = sess.query(Person).filter(Person.id == 4).first()
p4.name = 'changed'
sess.add(p4)
sess.commit()

persons = sess.query(Person).order_by(desc(Person.id)).all()
for p in persons:
    print(p.id, p.name)