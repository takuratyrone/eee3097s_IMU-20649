import socket
import time 
import csv

magx = []
magy = []
magz = []
accx = []
accy = []
accz = []
gyrx = []
gyry = []
gyrz = []

UDP_IP = "192.168.137.219" # set it to destination IP.. RPi in this case
UDP_PORT = 12345

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

f = open("f0024.txt", "r")
#f.next()
for l in f:
    line = l.split(",")
    #m_x, m_y, m_z = map(str, l.split(", "))
    if len(line) > 9:
    	magx.append(line[0])
    	magy.append(line[1])
    	magz.append(line[2])
    	accx.append(line[3])
    	accy.append(line[4])
    	accz.append(line[5])
    	gyrx.append(line[6])
    	gyry.append(line[7])
    	gyrz.append(line[8])
    #f.next()

print("Sending data...")

for j in range(1, len(magx)):
  sock.sendto(magx[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  sock.sendto(magy[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  sock.sendto(magz[j].encode('utf-8'), (UDP_IP, UDP_PORT))

  sock.sendto(accx[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  sock.sendto(accy[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  sock.sendto(accz[j].encode('utf-8'), (UDP_IP, UDP_PORT))

  sock.sendto(gyrx[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  sock.sendto(gyry[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  sock.sendto(gyrz[j].encode('utf-8'), (UDP_IP, UDP_PORT))
  time.sleep(0.25)

compress_message = "compress"
sock.sendto(compress_message.encode('utf-8'), (UDP_IP, UDP_PORT))
f.close()
print("Done!")

"""while True:
  print("Turn ON")
  sock.sendto(b'LED=1\n', (UDP_IP, UDP_PORT))
  time.sleep(2)
  print("Turn OFF")
  sock.sendto(b'LED=0\n', (UDP_IP, UDP_PORT))
  time.sleep(2)"""
