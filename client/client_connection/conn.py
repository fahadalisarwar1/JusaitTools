import socket
from utils.core import DisplayMsg

class ClientConnection:
    def __init__(self, server_ip="0.0.0.0", server_port=8080):
        self.ip = server_ip
        self.port = server_port
        self.DELIMETER = "<THIS_IS_THE_END_OF_DATA>"
        self.CHUNK_SIZE = 1024

    def connect_with_server(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        self.server_addr = (self.ip, self.port)
        self.socket.connect(self.server_addr)
        DisplayMsg("Connection established with ", self.server_addr[0])

