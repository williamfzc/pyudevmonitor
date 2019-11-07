from pyudevmonitor.monitor import UDevMonitor

# init
m = UDevMonitor()
m.start()

# read single event
e = m.read_event()
print(e.desc)

# or, start a detector
# init a queue
import queue
q = queue.Queue()
# and bind it to monitor
# monitor will put new UEvent to queue
stop = m.loop_read(q)

# do some operations ... ( plug in and out )
import time
time.sleep(10)

# stop detector
stop()

# you will get series of UEvent object by order
for each in list(q.queue):
    print(each)
