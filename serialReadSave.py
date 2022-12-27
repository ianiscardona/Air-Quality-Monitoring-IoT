from serial.tools import list_ports
import serial
import time
import csv

ports = list_ports.comports()
for port in ports: print(port)

f = open("data.csv", "w", newline='')
f.truncate()

serialCom = serial.Serial('COM5',9600)

serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

kmax = 5
for k in range(kmax):
    try:
        s_bytes = serialCom.readline()

        decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
        print(decoded_bytes)

        if k == 0:
            values = decoded_bytes.split(",")
        else:
            values = [float(x) for x in decoded_bytes.split()]
        print(values)

        writer = csv.writer(f, delimiter=",")
        writer.writerow(values)

    except:
        print("ERROR. Line was not recorded.")

f.close()