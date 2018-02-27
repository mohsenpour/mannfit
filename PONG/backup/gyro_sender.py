
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


# import smbus library
import smbus
import ssl
import os
import time
import socket

UDP_IP = "10.64.228.230"
UDP_PORT = 5005


##########################################################################################
##################################### SENSOR SETUPS ######################################
##########################################################################################

# get I2C bus
bus = smbus.SMBus(1)
# sensor is located at register 0x53
#0x2C is the bandwidth rate register
#	we would set it to x0A(10) for normal mode(output data rate = 100Hz)
bus.write_byte_data(0x53,0x2C,0x0A)
#0x2D is the power control register
#	we would set it to 0x2D(45) for Auto sleep node off
bus.write_byte_data(0x53,0x2D,0x08)
#0x31 is the data format register
#	we would set it to 0x08 for self test disabled and 4-wire interface and full resolution rang=+/-2g
bus.write_byte_data(0x53,0x31,0x08)
time.sleep(0.5)


##########################################################################################
##################################### AWS SETUPS ######################################
##########################################################################################

#myMQTTClient = AWSIoTMQTTClient("test")
## "1"
#myMQTTClient.configureEndpoint("a3us1z2o4e8c6h.iot.us-east-1.amazonaws.com", 8883)
## "2"
#myMQTTClient.configureCredentials("./SSH/root-ca-cert.pem", "SSH/4c53c9289b-private.pem.key", "SSH/4c53c9289b-certificate.pem.crt")
## "3"
#myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
## "4"
#myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
## "5"
#myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
## "6"
#myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
## "starting to connect"
#myMQTTClient.connect()
## "connected"
#myMQTTClient.publish("myTopic", "myPayload", 0)
#myMQTTClient.subscribe("myTopic", 1, customCallback)
#myMQTTClient.unsubscribe("myTopic")
#myMQTTClient.disconnect()


##########################################################################################
##################################### UDP SOCKET SETUP ###################################
##########################################################################################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)





def read_sensor_data():
	#read data back for X axis
	data0 = bus.read_byte_data(0x53,0x32)
	data1 = bus.read_byte_data(0x53, 0x33)
	#convert data to 10 base
	xAccl = ((data1 & 0x03)*256) + data0
	if xAccl > 551 :
		xAccl -= 1024
	#read data for the Y axis
	data0 = bus.read_byte_data(0x53, 0x34)
	data1 = bus.read_byte_data(0x53, 0x35)

	# Convert the data to 10-bits
	yAccl = ((data1 & 0x03) * 256) + data0
	if yAccl > 551 :
		yAccl -= 1024

	# read data for Z axix
	data0 = bus.read_byte_data(0x53, 0x36)
	data1 = bus.read_byte_data(0x53, 0x37)

	# Convert the data to 10-bits
	zAccl = ((data1 & 0x03) * 256) + data0
	if zAccl > 551 :
		zAccl -= 1024

	return xAccl,yAccl,zAccl	



def get_rotation_degree(axis):
	try:
		xAccl,yAccl,zAccl = read_sensor_data()
	except:
		return
	if (xAccl >= 0):	
		x_rotation_degree = xAccl*(90/280.0)
		if (x_rotation_degree > 90):
			x_rotation_degree = 90
	if (xAccl < 0):
		x_rotation_degree = xAccl*(90/245.0)	
		if (x_rotation_degree < -90):
			x_rotation_degree = -90

	if (yAccl >= 0):	
		y_rotation_degree = yAccl*(90/280.0)
		if (y_rotation_degree > 90):
			y_rotation_degree = 90
	if (yAccl < 0):
		y_rotation_degree = yAccl*(90/245.0)	
		if (y_rotation_degree < -90):
			y_rotation_degree = -90

	if (zAccl >= 0):	
		z_rotation_degree = zAccl*(90/280.0)
		if (z_rotation_degree > 90):
			z_rotation_degree = 90
	if (zAccl < 0):
		z_rotation_degree = zAccl*(90/245.0)	
		if (z_rotation_degree < -90):
			z_rotation_degree = -90
	if(axis == 'x'):
		return x_rotation_degree
	if(axis == 'y'):
		return y_rotation_degree
	if(axis == 'z'):
		return z_rotation_degree


#while True:
	#sock.sendto(str(get_rotation_degree('x')), (UDP_IP, UDP_PORT))
	#(get_rotation_degree('x'))
