from threading import Thread
import requests, sys
from queue import Queue

concurrent = 200
URL = "https://your_url.com/"

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        print(status)
        q.task_done()

def getStatus(ourl):
    try:
        res = requests.get(ourl)
        return res.status_code, ourl
    except:
        return "error", ourl

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for i in range(5000):
        q.put(URL)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)