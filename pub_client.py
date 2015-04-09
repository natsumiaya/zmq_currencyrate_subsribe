import sys
import zmq

port = "5556"
int(port)
ipaddr = "localhost"
if len(sys.argv) > 2:
    ipaddr = sys.argv[1]
    print ipaddr
    print type(ipaddr)

    port = sys.argv[2]
    int(port)
    print port
    print type(port)

elif len(sys.argv) > 1:
    ipaddr = sys.argv[1]
    print ipaddr
    print type(ipaddr)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Collecting updates from server..."
socket.connect ("tcp://%s:%s" % (ipaddr, port))

socket.setsockopt(zmq.SUBSCRIBE, '')

while True:
    data = socket.recv()
    print data