import requests
import time
import datetime

def online(time):
    payload = {'subnetId':1002,'stnId':10026,'time':time}
    res = requests.head("http://192.168.145.116:8182/baselineResolver/station/goonline")
    res = requests.post("http://192.168.145.116:8182/baselineResolver/station/goonline",json=payload)
    print(res.text)




if __name__ == '__main__':
    t = time.time()
    rst = online(int(t))