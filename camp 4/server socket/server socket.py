import json
import socket


phoneBook = {}


def server_program():
    host = socket.gethostname() 
    port = 5000
    
    server_socket = socket.socket()

    
    server_socket.bind((host,port))

    
    server_socket.listen(2)  

   
    conn, address = server_socket.accept()

    choice = '1'

    while(True):
      
        data = int(conn.recv(1024).decode())

        choice = data

        
        match choice:
            case 1:
                phoneBookJson = json.dumps(phoneBook)
                conn.send(phoneBookJson.encode())
            case 2:
                keyreq = "Please enter name: "
                conn.send(keyreq.encode())
                key = conn.recv(1024).decode()
                valreq = "Please enter phone number: "
                conn.send(valreq.encode())
                val = conn.recv(1024).decode()
                phoneBook[key] = val
            case 3:
                keyreq = "Please enter name: "
                conn.send(keyreq.encode())
                key = conn.recv(1024).decode()
                del phoneBook[key]
            case 4:
                keyreq = "Please enter name: "
                conn.send(keyreq.encode())
                key = conn.recv(1024).decode()
                res = f"{key} : {phoneBook[key]}"
                conn.send(res.encode())
            case 5:
                numreq = "Please enter number: "
                conn.send(numreq.encode())
                num = conn.recv(1024).decode()
                for i in phoneBook:
                    if phoneBook[i] == num:
                        res = f"{i} : {phoneBook[i]}"
                        conn.send(res.encode())
            case 6:
                break
        
        
    
    conn.close() 

if __name__ == '__main__':
    server_program()