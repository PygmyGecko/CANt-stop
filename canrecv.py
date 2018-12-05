"""Connect to CANable; print and echo any received frames"""
from pyvit import can
from pyvit.hw.cantact import CantactDev
from time import time
from mpu6050 import mpu6050
import sys, os


timestamp = time()

#initialize CAN device
try:
	dev = cantact.CantactDev("/dev/ttyACM0") # Connect to CANable
except Exception:
	print("CAN device not found")
	exit()

dev.set_bitrate(500000) # Set the bitrate to a 500k baud
dev.start() # Go on the bus

#initialize accel/gyro
try:
    sensor = mpu6050(0x68)
except Exception:
    print("MPU6050 accel/gyro not found")
    exit()

file = open('./logs/log' + str(len(os.listdir('./logs'))), 'w+') # Create log file to write to


count = 0
while True:
    count += 1
    
    #frame = dev.recv() # Receive a CAN frame
    
    outputString = (str(count) + "\t" + str("{0:.3f}".format(time() - timestamp))
    + "\t" + "dev.recv().id"  #Print Arbitration ID of CAN msg
    + "\t" + str("{0:.3f}".format(sensor.get_accel_data()['x']))  #Print accel x value
    + "\t" +  str("{0:.3f}".format(sensor.get_accel_data()['y']))  #Print accel y value 
    + "\t" +  str("{0:.3f}".format(sensor.get_accel_data()['z'])))   #Print accel z value

    print(outputString)  # Print out the received frame
    file.write(outputString + "\n") # Write received frame to log file
