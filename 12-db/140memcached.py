# docker run --name my-memcache -p 11211:11211 -d memcached
# key-value storeです
import memcache

db = memcache.Client(['127.0.0.1:11211'])

db.set('web_page', 'value2')
#db.set('counter', 0)
db.incr('counter', 2)

print(db.get('web_page'))
print(db.get('counter'))