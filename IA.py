import socket
import sys
import time
import json


with socket.socket() as s:

    address = ("localhost", 10000)

    sub_message = {
        "request": "subscribe",
        "port": 10000,
        "name": "AbdelBadi Lababidi , Zakaria Zaryouh",
        "matricules": ["20369", "2103"]
    }

    try:
        s.connect(address)
    except Exception as error:
        print(error)
        sys.exit()

    s.send(json.dumps(sub_message).encode())

    response = s.recv(2048).decode()
    print(response)

    jsonrep = json.loads(response)

    if jsonrep["response"] == "error":
        print(jsonrep["error"])

time.sleep(1)
print("pong")

with socket.socket() as s:
    s.settimeout(0.5)
    s.bind(("localhost", 10000))
    print(2)
    s.listen()
    print(3)
    while True:
        try:
            client, address = s.accept()
            print(4)
            with client:
                message = json.loads(client.recv(2048).decode())
                print(message)
                if message["request"] == "ping":
                    client.send('{"response": "pong"}'.encode())
        except socket.timeout:
            pass
