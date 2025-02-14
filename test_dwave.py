import random
from dwave.cloud import Client
from dwave.cloud.config import load_config

#print(get_configfile_paths())

config = load_config('./dwave.conf')
print(config)

client = Client().from_config('./dwave.conf')
#sample code
client.close