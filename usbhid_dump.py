import subprocess
import re
import shlex

def dump_stream(bus, devices, timeout, callback):
	if len(devices) == 1:
		dev = devices[0]
	else:
		dev = 0

	cmd = "usbhid-dump -a {}:{} -es -t {}".format(bus, dev, timeout)
	
	process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
	last_device_id = None
	last_rep_id = None
	last_timestamp = None

	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			
			# Check if line is a device ID and timestamp line
			m = re.search('\d{3}:(\d{3}):(\d{3}):STREAM\s+([0-9\.]+)', str(output).strip())

			if m is not None:
				last_device_id = m.group(1)
				last_rep_id = m.group(2)
				last_timestamp = m.group(3)
				continue

			# Check if line is a report payload
			m = re.search('((?:[0-9A-Fa-f][0-9A-Fa-f]\s?){1,8})', str(output).strip())

			if m is not None:
				data = bytes.fromhex(m.group(1).replace(" ", ""))

				# Call callback function if device was included in list
				if last_device_id in devices:
					callback(last_device_id, last_rep_id, last_timestamp, data)
		
			
	rc = process.poll()
	return rc
