import time, requests, random, sched

ip = "172.16.48.1"

def dopost(temp, now_epoch_s):
    url = "http://" + ip + ":8086/write?db=particulaInfluxDB&precision=s"

    payload = "sensors,sensor_id=sensor_02 temp={} {}".format(temp, now_epoch_s)
    headers= {}

    requests.request("POST", url, headers=headers, data = payload)
    print("send temp: {}".format(temp))    

def doget():
    url = "http://" + ip + ":8086/query?db=particulaInfluxDB&q=select * from sensors"

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
