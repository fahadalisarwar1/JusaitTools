from client.client_connection.conn import ClientConnection


if __name__ == "__main__":
    client_conn = ClientConnection()
    client_conn.connect_with_server()