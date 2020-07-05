from server.server_connection.conn import ServerConnection

if __name__ == "__main__":
    server_conn = ServerConnection()
    server_conn.connect_with_victim()
    server_conn.listen()