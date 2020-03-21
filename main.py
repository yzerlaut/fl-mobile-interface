import os

path = os.path.join('/run/user/1000/gvfs/',
                    'mtp:host=%5Busb%3A001%2C010%5D',
                    'Phone', 'FLM User Files', 'My Recordings')
print(os.listdir(path))
