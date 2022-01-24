import socket
import random

random.seed()

serverS=socket.socket(socket.AF_INET, socket.SOCK_STREAM);

#bind and listen for data
serverS.bind(("127.0.0.1", 3031));
serverS.listen();
print("Socket listening on 3031")

client_connection, client_address = serverS.accept()
print("Connection:" + client_address[0] + ',' + str(client_address[1]))


text= client_connection.recv(4096)
decod= text.decode("utf-8")
print(decod)

#client side
data2="HTTP/1.1 200 OK\r\n"\
 "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
  "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n";

client_connection.sendall(data2.encode("utf-8"));
print("Data Received")

client_connection.close()
serverS.close()

#Resources: https://www.binarytides.com/python-socket-programming-tutorial/
# https://pythontic.com/modules/socket/send
