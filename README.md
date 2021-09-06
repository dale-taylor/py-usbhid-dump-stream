# py-usbhid-dump-stream
A limited Python wrapper for usbhid-dump (stream entity only). Accepts a bus ID, and an optional array of device IDs, and a callback function. Launches usbhid-dump in stream mode, parses output in real time and passes raw HID reports for specified devices to the callback function.

See https://github.com/DIGImend/usbhid-dump

## Example
```python
import usbhid_dump

def output(dev_id, rep_id, timestamp, data):
	print("Dev: {} Rep: {} Data: {}".format(dev_id, rep_id, data.hex()))

bus_id = 2
device_ids = [76, 77]
timeout = 60000

usbhid_dump.dump_stream(bus_id, device_ids, timeout, output)
```

Example output:
```
Dev: 076 Rep: 000 Data: 0100feff05000000
Dev: 076 Rep: 000 Data: 0100ffff05000000
Dev: 076 Rep: 000 Data: 0100ffff05000000
Dev: 076 Rep: 000 Data: 0100ffff04000000
Dev: 077 Rep: 000 Data: 00001d0000000000
Dev: 077 Rep: 000 Data: 0000000000000000
Dev: 077 Rep: 000 Data: 0000060000000000
Dev: 077 Rep: 000 Data: 0000000000000000
Dev: 077 Rep: 000 Data: 0000190000000000
```
