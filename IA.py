import socket
import sys
import time
import json

with socket.socket() as s:

    address = ("localhost", 3000) #cette ligne définit l'adresse IP et le port utilisés pour se connecter au serveur
    port = 4444

    sub_message = {  #cette ligne définit un message JSON contenant les informations nécessaires pour s'abonner au serveur
        "request": "subscribe",
        "port": port,
        "name": "Les FROAT",
        "matricules": ["20369", "21003"]
    }

    try: #cette partie du code tente de se connecter au serveur en utilisant l'adresse définie précédemment. Si une exception est levée, le code affiche un message d'erreur et se termine en utilisant la fonction sys.exit()
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
print("ok")

with socket.socket() as s:
    s.settimeout(0.5)
    s.bind(("localhost", 4444)) #cette ligne lie le socket à l'adresse IP et au port spécifiés pour écouter les connexions entrantes
    print(2)
    s.listen()
    print(3)
    
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

#Quelque chose ne fonctionne pas à partir de là
# Création de la socket et écoute sur le port de souscription
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as p:
    p.listen()

    while True:
        p.settimeout(5)
        try: 
            client_socket, client_address = p.accept()
            with client_socket:
                def reponse() :
                    toile = dict(message['state']['tile'])
                    toile['N']= message['state']['tile']['W']
                    toile['E']= message['state']['tile']['N']
                    toile['S']= message['state']['tile']['E']
                    toile['W']= message['state']['tile']['S']
                    position_actuelle = message['state']['current']
                    if position_actuelle == 0 :
                        if message['state']['board'][int(position_actuelle)]['E'] == True and message['state']['board'][int(position_actuelle+1)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['S'] == True and message['state']['board'][int(position_actuelle+7)]['N'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle in [1,2,3,4,5] :
                        if message['state']['board'][int(position_actuelle)]['E'] == True and message['state']['board'][int(position_actuelle+1)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['S'] == True and message['state']['board'][int(position_actuelle+7)]['N'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['W'] == True and message['state']['board'][int(position_actuelle-1)]['E'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle == 48 :
                        if message['state']['board'][int(position_actuelle)]['W'] == True and message['state']['board'][int(position_actuelle-1)]['E'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['N'] == True and message['state']['board'][int(position_actuelle-7)]['S'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle in [43,44,45,46,47] :
                        if message['state']['board'][int(position_actuelle)]['E'] == True and message['state']['board'][int(position_actuelle+1)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['N'] == True and message['state']['board'][int(position_actuelle-7)]['S'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['W'] == True and message['state']['board'][int(position_actuelle-1)]['E'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle == 6 :
                        if message['state']['board'][int(position_actuelle)]['W'] == True and message['state']['board'][int(position_actuelle-1)]['E'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['S'] == True and message['state']['board'][int(position_actuelle+7)]['N'] == True:
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle == 42 :
                        if message['state']['board'][int(position_actuelle)]['E'] == True and message['state']['board'][int(position_actuelle+7)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['N'] == True and message['state']['board'][int(position_actuelle-7)]['S'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle % 7 == 0 :
                        if message['state']['board'][int(position_actuelle)]['E'] == True and message['state']['board'][int(position_actuelle+7)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['S'] == True and message['state']['board'][int(position_actuelle+7)]['N'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['N'] == True and message['state']['board'][int(position_actuelle-7)]['S'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle % 7 == 1 or position_actuelle % 7 == 2 or position_actuelle % 7 == 3 or position_actuelle % 7 == 4 or position_actuelle % 7 == 5 :
                        if message['state']['board'][int(position_actuelle)]['E'] == True and message['state']['board'][int(position_actuelle+1)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['W'] == True and message['state']['board'][int(position_actuelle-1)]['E'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 1}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['S'] == True and message['state']['board'][int(position_actuelle+7)]['N'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['N'] == True and message['state']['board'][int(position_actuelle-7)]['S'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                    elif position_actuelle % 7 == 6 :
                        if message['state']['board'][int(position_actuelle)]['N'] == True and message['state']['board'][int(position_actuelle-7)]['S'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle - 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['W'] == True and message['state']['board'][int(position_actuelle-1)]['W'] == True :
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle -1 }
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                        elif message['state']['board'][int(position_actuelle)]['S'] == True and message['state']['board'][int(position_actuelle+7)]['N'] == True:
                            jouer = {"tile":toile, "gate":"B", "new_position":position_actuelle + 7}
                            send = {"response":"move", "move":jouer, "message":"GOAT"}
                            client_socket.sendall(json.dumps(send).encode())
                print('Connexion de', client_address)
                # Réception du message envoyé par le serveur
                data = client_socket.recv(10000).decode()
                print('Reçu', repr(data))
                # Analyse du message reçu et envoi de la réponse appropriée
                message = json.loads(data)
                if message['request'] == 'ping':
                    response = {"response": "pong"}
                    print(response)
                    client_socket.sendall(json.dumps(response).encode())
                elif message['request'] == 'play':
                    reponse()
        except socket.timeout:
            pass
            
