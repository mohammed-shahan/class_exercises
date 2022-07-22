


#simple phonebook app using dictionary

addressbook = dict()

def getNameFromPhno(phno):
    for k,v in addressbook.items():
        if phno == v:
            return k

def searchno(phno):
    if phno in addressbook.values():
        print("user found - ", getNameFromPhno(phno), "-", phno)
    else:
        print("user not found")

def searchname(name):
    if name in addressbook.keys():
        print("user found - ", name, "-", addressbook[name])
    else:
        print("user not found")

def add(name, phno):
    if name not in addressbook.keys():
        addressbook.update({name:phno})
        print("1 user added")
    else:
        print("user exists")

def delete(name):
    if name in addressbook.keys():
        del addressbook[name]
        print("User deleted")
    else:
        print("user does not exist")

def sort():
    print("Address Book (Sorted)")
    print("Name\t\tPhone")
    for i in sorted(addressbook.keys()):
        print("{}\t\t{}".format(i, addressbook[i]))


while(True):
    print("1. List Contacts")
    print("2. Add user")
    print("3. Delete user")
    print("4. Search by name")
    print("5. Search by number")
    print("6. Exit")
    _userselection = int(input("Your selection : "))
    match _userselection:
         case 1:
            sort()
         case 2:
            name = input("Enter name : ")
            phno = input("Enter phone no : ")
            add(name, phno)
         case 3:
            name = input("Enter name : ")
            delete(name)
         case 4:
            name = input("Enter name : ")
            searchname(name)
         case 5:
            phno = input("Enter phone no : ")
            searchno(phno)
         case 6:
            break