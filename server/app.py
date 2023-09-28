import socket
from dotenv import load_dotenv
import os
from response import handle_requests


def runServer():
    try:
        load_dotenv()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #added time out of 20 seconds
        server.settimeout(20)
        host = os.getenv('HOST')
        port = int(os.getenv("PORT"))
        print(port)
        server.bind((host, port))
        server.listen(5)
        print("Server is running")
        while True:
            connection, _ = server.accept()
            request = connection.recv(1024).decode('utf-8')
            request = eval(request)
            event = request['event']
            data = request['data']

            print('event', event)
            print('data', data)

            handle_requests(event, connection, data)
            connection.close()

    except KeyboardInterrupt:
        #Thiss allows ctrl+c to exit server
        print("\nShutting down the server.")

    except Exception as e:
        print(e)
        print("Server is not running")

    finally:
        server.close()



if __name__ == '__main__':
    print("server is running")
    runServer()
