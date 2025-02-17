import random
from dwave.cloud import Client
from dwave.cloud.config import load_config

#print(get_configfile_paths())

path = './config/dwave.conf'

config = load_config(path)
print(config)

#client = Client().from_config(path)
#sample code
#client.close