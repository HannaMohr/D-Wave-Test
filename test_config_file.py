import os


#TODO: Test file and add more possibilites
def creat_config(API_token, path):
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(path + "/dwave.conf", "a")
    f.write('[defaults] \n')
    f.write(f'token={API_token}')
    f.close()

creat_config("ABC-Test", "./config")