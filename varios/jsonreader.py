import json
from datetime import datetime


def todate(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object


def prepareaddres(address_from_file):
    # transforms coords array to latitude and longitude properties
    address_prep = {
        "address": {
            "building": address_from_file["building"],
            "latitude": address_from_file["coord"][0],
            "longitude": address_from_file["coord"][1],
            "street": address_from_file["street"],
            "zipcode": address_from_file["zipcode"]
        }
    }
    return address_prep


with open('prueba.json', 'r') as jsonfile:
    data = jsonfile.read()

restaurant = json.loads(data)

print("mi json: ".format(address))
with open('myjson.json', 'w') as myfile:
    json.dump(address, myfile)

print('address: {}'.format(address))
"""
print('borough: {}'.format(restaurant["borough"]))
print('cuisine: {}'.format(restaurant["cuisine"]))
print('grades: {}'.format(restaurant["grades"]))
print('name: {}'.format(restaurant["name"]))
print('restaurant_id: {}'.format(restaurant["restaurant_id"]))

_date = restaurant["grades"][0]["date"]["$date"]
print(_date)
"""
with open('myjson.json', 'r') as addresfile:
    data1 = addresfile.read()

direccion = json.loads(data1)

print(direccion["address"])

# print('Date : {}'.format(todate(_date)))
# 1393804800000
