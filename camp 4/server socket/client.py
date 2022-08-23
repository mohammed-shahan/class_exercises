import json
import socket

def client_program():
    host = socket.gethostname() 
    
    port = 5000 
    
   
    client_socket = socket.socket()

   
    client_socket.connect((host,port)) 

    choice = 0

    while choice != '6':
        client_socket.send(choice.encode())

        print("MENU:\n1.List all contacts\n2.Add a new contact\n3.Delete a contact\n4.Search a contact\n5.Search a contact with number\n6.Exit")
        choice = input("Enter your choice: ")

        if choice=='1':
            data = client_socket.recv(1024).decode()
            details = json.loads(data)
            for i in sorted(details.keys()):
                print(f"{i}:{details[i]}")
        elif choice=='2':
            data = client_socket.recv(1024).decode()
            print(data)
            name = input()
            client_socket.send(name.encode())
            data = client_socket.recv(1024).decode()
            print(data)
            phno = input()
            client_socket.send(phno.encode())
        elif choice=='3':
            data = client_socket.recv(1024).decode()
            print(data)
            name = input()
            client_socket.send(name.encode())
        elif choice=='4':
            data = client_socket.recv(1024).decode()
            print(data)
            name = input()
            client_socket.send(name.encode())
            data = client_socket.recv(1024).decode()
            print(data)
        elif choice=='5':
            data = client_socket.recv(1024).decode()
            print(data)
            num = input()
            client_socket.send(num.encode())
            data = client_socket.recv(1024).decode()
            print(data)
        else:
            print("Wrong choice")



       
    
    client_socket.close()

if __name__ == '__main__':
    client_program()