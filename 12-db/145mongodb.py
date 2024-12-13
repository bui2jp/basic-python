from datetime import datetime, timezone

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

stack1 = {
    'name': 'test11',
    'datetime': datetime.now(timezone.utc)
}
stack2 = {
    'name': 'test12',
    'datetime': datetime.now(timezone.utc)
}

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack2).inserted_id
print(stack_id, type(stack_id))

print('#### fine_one')
print(db_stacks.find_one({'_id':stack_id}))

from bson.objectid import ObjectId
print(db_stacks.find_one({'_id':ObjectId('674fda4da0cd74f0cc8cc1a3')}))

print(db_stacks.find())
for stack in db_stacks.find():
    print(stack)
print('####')

current = datetime.now(timezone.utc)
print(current)
for stack in db_stacks.find({'datetime': {'$lt': current}}):
    print(stack)

print('update')
result = db_stacks.find_one_and_update(
    {'name': 'test12'}, {'$set':{'name': 'YYYY'}}
)

for stack in db_stacks.find({'name':'YYYY'}):
    print(stack)


print('delete start')
# result = db_stacks.delete_one({'name':'YYYY'})
# result = db_stacks.delete_one({'name':'YYYY'})
# result = db_stacks.delete_one({'name':'YYYY'})

for stack in db_stacks.find({'name':'YYYY'}):
    print(stack)

