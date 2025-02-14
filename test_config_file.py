
#TODO: Test file and add more possibilites
def creat_config(API_token):
    f = open("dwave.conf", "a")
    f.write('[defaults] \n')
    f.write(f'token={API_token}')
    f.close()

creat_config("ABC-Test")