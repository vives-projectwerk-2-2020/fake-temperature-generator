import time, requests, random, sched

ip = "localhost"
port = "32772"

def dopost(temp, now_epoch_s):
    url = "http://" + ip + ":"+ port +"/write?db=particulaInfluxDB&precision=s"

    payload = 'sensors,sensor_id=sensor-test humidity=59,location="lab2.80",pm10=23,pm25=12,temperature={} {}'.format(temp, now_epoch_s)
    headers= {}

    requests.request("POST", url, headers=headers, data = payload)
    print("send temp: {}".format(temp))    

def doget():
    url = "http://" + ip + ":"+ port +"/query?db=particulaInfluxDB&q=select * from sensors"

    payload = ""
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

def send_data_every_min(sc):
    now_epoch_s = int(time.time())
    temp = random.randint(18, 24)
    dopost(temp, now_epoch_s)

    s.enter(60, 1, send_data_every_min, (sc,))

s = sched.scheduler(time.time, time.sleep)
s.enter(60, 1, send_data_every_min, (s,))
s.run()
