from pyudevmonitor.monitor import UDevMonitor


m = UDevMonitor()
m.start()
e = m.read_event()
print(e.desc)
