import socket
import random

#create client socket

clientS = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

#connect to server with random port
random.seed();
port=random.randint(1023,9000);

clientS.connect(("gaia.cs.umass.edu", 80));

data="GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n";

clientS.sendall(data.encode());

#printing data sent to server
print("Request:", data);

#receive data from server
data=clientS.recv(4096)
decod=data.decode()
print(decod)


#end of part 1
data1= "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n";
clientS.sendall(data1.encode());

#print request to server
print("Request:", data1);

#recv data from server
while 1:
	data1=clientS.recv(4096)
	decod=data1.decode()
	print(decod)

	#if the length of the decoded string is 0 then there is no more data
	if len(decod)==0:
		print("no more data")
		break


#end of part 2

clientS.close();

#Resources:
# https://docs.python.org/3.8/howto/sockets.html
# https://docs.python.org/3/library/socket.html
