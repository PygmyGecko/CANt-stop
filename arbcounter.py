from pyvit import can
from pyvit.hw.cantact import CantactDev
import sys


try:
	dev = CantactDev("/dev/ttyACM0") # Connect to CANable
except Exception:
	print("CAN device not found")
	exit()

dev.set_bitrate(500000) # Set the bitrate to a 500k baud
dev.start() # Go on the bus

try:
	arb_count = 0

	while True:
		if dev.recv().arb_ID == sys.argv[1]:
			arb_count = arb_count + 1
			print arb_count

except KeyboardInterrupt:
	print("Keyboard Interrupt Detected.  Exiting...")