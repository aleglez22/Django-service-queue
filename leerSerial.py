import serial
ser = serial.Serial('/dev/ttyS2/', 9600)

while True:
	print (ser.readline())
