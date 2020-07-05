import socket


class ServerConnection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.DELIMETER = "<THIS_IS_THE_END_OF_DATA>"
    
    def connect_with_victim(self):
        """[summary]
            This function helps with connecting with the client
        """        
        