# docker run --name some-mysql --rm -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.4.3 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

import mysql.connector

print('start')
# conn = mysql.connector.connect(host='127.0.0.1', user='root', password='my-secret-pw')
# curs = conn.cursor()
# curs.execute(
#     'create database test_mysql_db'
# )
# curs.close()
# conn.close()

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='my-secret-pw', database='test_mysql_db')
curs = conn.cursor()
# curs.execute(
#     'create table persons('
#     'id int NOT NULL AUTO_INCREMENT,'
#     'name varchar(14) NOT NULL,'
#     'PRIMARY KEY(id))'
# )

# insert
curs.execute('insert into persons(name) values("Mike1")')
curs.execute('insert into persons(name) values("Mike2")')
curs.execute('insert into persons(name) values("Mike3")')

curs.execute('select * from persons')
for row in curs:
    print(row)

conn.commit()

curs.close()
conn.close()

print('end')