import zmq
import sys
import json
import time
import unicodedata
import urllib

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    url = urllib.urlopen('http://jsonrates.com/get/?from=IDR&to=USD&apiKey=jr-9ad516c8b5a8d4e15065d8251c947552').read()

    result = json.loads(url)
    # print 'IDR to USD rates:', result['rate']

    topic = result['rate']
    senddata = topic.encode('ascii', 'ignore')
    print senddata
    retval = socket.send(senddata)
    print  retval
    time.sleep(2)