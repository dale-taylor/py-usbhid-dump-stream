# py-usbhid-dump-stream
A limited Python wrapper for usbhid-dump (stream entity only). Accepts a bus ID, and an optional array of device IDs, and a callback function. Launches usbhid-dump in stream mode, parses output in real time and passes raw HID reports for specified devices to the callback function.

See https://github.com/DIGImend/usbhid-dump
