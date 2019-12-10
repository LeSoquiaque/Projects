from google.cloud import datastore

def keys_only_query(client):

    # [START datastore_keys_only_query]
    query = client.query(kind='Resto')
    query.keys_only()
    # [END datastore_keys_only_query]

    keys = list([entity.key for entity in query.fetch()])

    return keys

if __name__ == '__main__':
	client = datastore.Client()
	llaves = keys_only_query(client)
	print(llaves)



