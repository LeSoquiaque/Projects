from google.cloud import datastore
import json


# Create, populate and persist an entity with keyID=1234
client = datastore.Client()
key = client.key('Resto',1341)
entity = datastore.Entity(key=key)
entity.update({
    'address': 'micas' ,
    'borough': 'nose',
    'cuisine': 'chingona',
    'grades': [{"date": {"$date": 1393804800000}, "grade": "A", "score": 2}, {"date": {"$date": 1378857600000}, "grade": "A", "score": 6}, {"date": {"$date": 1358985600000}, "grade": "A", "score": 10}, {"date": {"$date": 1322006400000}, "grade": "A", "score": 9}, {"date": {"$date": 1299715200000}, "grade": "B", "score": 14}],
    'name': 'piojhina'
})
client.put(entity)
# Then get by key for this entity
#result = client.get(key)
print('Exito')
