import socket
from huffman import*
from AES import*

UDP_IP = "0.0.0.0" # listen to everything
UDP_PORT = 12345 # port

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

count = 0
f = open("data_output.txt", "w")

while True:
	data = str(sock.recvfrom(512)[0], 'utf-8') # random buffer size, doesn't matter here..
	print("received message:", data)

	if data == "compress":
		compress_file("data_output.txt")

	elif count%9 == 0:
		f.write(data+", ")
		print("magX = ", data)
		count += 1

	elif count%9 == 1:
		f.write(data+", ")
		print("magY = ", data)
		count += 1

	elif count%9 == 2:
		f.write(data+", ")
		print("magZ = ", data)
		print("")
		count += 1

	elif count%9 == 3:
		f.write(data+", ")
		print("accX = ", data)
		count += 1

	elif count%9 == 4:
		f.write(data+", ")
		print("accY = ", data)
		count += 1

	elif count%9 == 5:
		f.write(data+", ")
		print("accZ = ", data)
		print("")
		count += 1

	elif count%9 == 6:
		f.write(data+", ")
		print("gryX = ", data)
		count += 1

	elif count%9 == 7:
		f.write(data+", ")
		print("gyrY = ", data)
		count += 1

	elif count%9 == 8:
		f.write(data)
		f.write("\n")
		print("gyrZ = ", data)
		print("")
		print("====================================")
		print("")
		count += 1

#simplest way to react.. of course, a better parser should be used, and add GPIO code, etc..
"""if data==b'LED=1\n':
    print("LED ON")
  elif data==b'LED=0\n':
    print("LED OFF")"""
