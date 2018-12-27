import requests
import time
import datetime

def online(substnId,stnId,time):
    try:
        payload = {"subnetId":substnId,"stnId":stnId,"time":time}
        print(payload)
        res = requests.post("http://192.168.145.116:8182/baselineResolver/station/goonline", data=payload)
        print(res.text)
    except:
        print("%d,上线错误",stnId)

def offline(substnId,stnId,time):
    try:
        payload = {"subnetId":substnId,"stnId":stnId,"time":time}
        print(payload)
        res = requests.post("http://192.168.145.116:8182/baselineResolver/station/gooffline", data=payload)
        print(res.text)
    except:
        print("%d，下线错误",stnId)
def systnonoff(sleep):
    t = time.time()
    offline(1002,10025,int(t))
    time.sleep(sleep)
    t = time.time()
    online(1002,10025,int(t))


if __name__ == '__main__':
    try:
        while True:
            systnonoff(10)
            time.sleep(10)
    except:
        print("error")

