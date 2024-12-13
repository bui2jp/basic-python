import sqlite3

print('start')

with(sqlite3.connect('test1.db')) as conn:
# with(sqlite3.connect(':memory:')) as conn:    
    try:
        print('try')
        curs = conn.cursor()
        #curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
        curs.execute('insert into persons(name) values("Mike1")')
        curs.execute('insert into persons(name) values("Mike2")')
        curs.execute('insert into persons(name) values("Mike3")')
        
        # update        
        curs.execute('update persons set name="Nancy" where name = "Mike1"')

        # delete        
        curs.execute('delete from persons where name like "Mike1"')

        # commit
        conn.commit()

        #
        curs.execute('select * from persons')
        print(curs.fetchall())

    finally:        
        print('finally')
        curs.close()

print('end')