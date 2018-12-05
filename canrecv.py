"""Connect to CANable; print and echo any received frames"""
from pyvit import can
from pyvit.hw.cantact import CantactDev
from time import time
from mpu6050 import mpu6050
import sys, os

timestamp = time()

try:
	dev = cantact.CantactDev("/dev/ttyACM0") # Connect to CANable
except Exception:
	print(device + " not found")
	exit()

dev.set_bitrate(500000) # Set the bitrate to a 500k baud
dev.start() # Go on the bus
file = open('./logs/log' + str(len(os.listdir('./logs'))), 'w+') # Create log file to write to

sensor = mpu6050(0x68)
accelerometor_data = sensor.get_accel_data()

count = 0

while True:
    count += 1
    frame = dev.recv() # Receive a CAN frame
    outputString = str(count) + "\t" + str(time() - timestamp) + "\t" + str(frame.id) + "\t" + accelerometor_data
    print outputString  # Print out the received frame
    file.write(outputString + "\n") # Write received frame to log file
