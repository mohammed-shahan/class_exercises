import json
import socket


phoneBook = {"Shahan":"95842621", "Tinu":"541515415", "Prince":"8586485224", "Preston": "70252848485174"}


def server_program():
    host = socket.gethostname() 
   
    server_socket = socket.socket()

    
    server_socket.bind((host,port))

   
    server_socket.listen(2)  

   
    conn, address = server_socket.accept()

    choice = '1'

    while(True):
        
        data = conn.recv(1024).decode()

        choice = data

        



        if choice=='1':
            phoneBookJson = json.dumps(phoneBook)
            conn.send(phoneBookJson.encode())
        elif choice=='2':
            keyreq = "Please enter name: "
            conn.send(keyreq.encode())
            key = conn.recv(1024).decode()
            valreq = "Please enter phone number: "
            conn.send(valreq.encode())
            val = conn.recv(1024).decode()
            phoneBook[key] = val
        elif choice=='3':
            keyreq = "Please enter name: "
            conn.send(keyreq.encode())
            key = conn.recv(1024).decode()
            del phoneBook[key]
        elif choice=='4':
            keyreq = "Please enter name: "
            conn.send(keyreq.encode())
            key = conn.recv(1024).decode()
            res = f"{key} : {phoneBook[key]}"
            conn.send(res.encode())
        elif choice=='5':
            numreq = "Please enter number: "
            conn.send(numreq.encode())
            num = conn.recv(1024).decode()
            for i in phoneBook:
                if phoneBook[i] == num:
                    res = f"{i} : {phoneBook[i]}"
                    conn.send(res.encode())
        else:
            res = "Wrong choice"
            conn.send(res.encode())

        
        if not data:
            break
    
    conn.close() 

if __name__ == '__main__':
    server_program()