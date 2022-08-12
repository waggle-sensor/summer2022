import serial 

ser = serial.Serial('COM5', 115200)
while True:
    print(ser.readline())

