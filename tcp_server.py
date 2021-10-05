import socket

TCP_IP = '0.0.0.0' # this IP of my pc. When I want raspberry pi 2`s as a server, I replace it with its IP '169.254.54.195'
TCP_PORT = 5005
BUFFER_SIZE = 20 # Normally 1024, but I want fast response

print("Waiting for connection...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
conn.close()
