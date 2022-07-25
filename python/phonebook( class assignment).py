
#program for phonebook management using file
class PhoneBook:

    def __init__(self, filename):
        self.filename = filename
        file = open(filename, "r")
        self.pb = dict()
        for line in file:
            contact = line.split()
            self.pb.update({contact[0]:contact[1]})
        file.close()

    def listContacts(self):
        print("Name\t\tPhone")
        for i in sorted(self.pb.keys()):
            print("{}\t\t{}".format(i, self.pb[i]))

    def addContact(self, name, phno):
        if name not in self.pb.keys():
            self.pb.update({name:phno})
            print("1 entry added")
        else:
            print("entry exists")

    def searchByName(self, name):
        if name in self.pb.keys():
            print("entry found - ", name, "-", self.pb[name])
        else:
            print("entry not found")
    
    def searchByNumber(self, phno):
        if phno in self.pb.values():
            for k,v in self.pb.items():
                if phno == v:
                    name = k
                    break   
            print("entry found - ", name, "-", phno)
        else:
            print("entry not found")

    def deleteContact(self, name):
        if name in self.pb.keys():
            del self.pb[name]
            print("1 entry ({}) deleted".format(name))
        else:
            print("entry does not exist")

    def commit(self):
        file = open(self.filename, "w")
        for k,v in self.pb.items():
            file.write("{} {}\n".format(k,v))
        print("Committed edits")
        file.close()

    
ph_book = PhoneBook("phonebook.txt")
ph_book.listContacts()
ph_book.addContact("shahan", "5635656265")
ph_book.listContacts()
ph_book.commit()