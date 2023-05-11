import socket
import sys
import time
import json


with socket.socket() as s:

    address = ("localhost", 10000)  #cette ligne définit l'adresse IP et le port utilisés pour se connecter au serveur

    sub_message = {                 #cette ligne définit un message JSON contenant les informations nécessaires pour s'abonner au serveur
        "request": "subscribe", 
        "port": 10000,
        "name": "AbdelBadi Lababidi , Zakaria Zaryouh", 
        "matricules": ["20369", "2103"]
    }

    try:  #cette partie du code tente de se connecter au serveur en utilisant l'adresse définie précédemment. Si une exception est levée, le code affiche un message d'erreur et se termine en utilisant la fonction sys.exit()
        s.connect(address)
    except Exception as error:
        print(error)
        sys.exit()

    s.send(json.dumps(sub_message).encode()) #cette ligne envoie le message JSON encodé à l'aide de la méthode json.dumps() et de la méthode encode() pour l'envoyer en tant que séquence d'octets sur la connexion de socket

    response = s.recv(2048).decode() #cette ligne lit la réponse du serveur en utilisant la méthode recv() qui lit au plus 2048 octets de données et la méthode decode() pour décoder les données en UTF-8
    print(response)

    jsonrep = json.loads(response) #cette ligne analyse la réponse JSON du serveur à l'aide de la méthode json.loads() et stocke le résultat dans la variable jsonrep

    if jsonrep["response"] == "error": #cette ligne vérifie si la réponse JSON contient une erreur et affiche le message d'erreur correspondant dans la console.
        print(jsonrep["error"])

time.sleep(1)
print("pong")

with socket.socket() as s:
    s.settimeout(0.5)
    s.bind(("localhost", 10000)) #cette ligne lie le socket à l'adresse IP et au port spécifiés pour écouter les connexions entrantes
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

