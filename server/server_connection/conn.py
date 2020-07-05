import socket
from utils.core import DisplayMsg

class ServerConnection:
    def __init__(self, ip="0.0.0.0", port=8080):
        self.ip = ip
        self.port = port
        self.DELIMETER = "<THIS_IS_THE_END_OF_DATA>"
        self.CHUNK_SIZE = 1024
        self.addr = (ip, port)
    
    def connect_with_victim(self):
        """[summary]
            This function helps with connecting with the client
        """        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.addr)

    def listen(self):
        DisplayMsg("Listening for Incoming Connections: "+self.ip+ " "+str(self.port))
        self.socket.listen()
        self.conn, self.client_addr = self.socket.accept()
        DisplayMsg("Connection established: ", self.client_addr[0])
