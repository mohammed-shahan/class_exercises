#patient management program

import pyodbc


class Hospital:
    def __init__(self):
        self.connString = 'Driver={SQL Server};Server=DESKTOP-4D00VLG\SQLEXPRESS01;Database=PatientMngmnt;Trusted_Connection=yes;'
        self.conn = pyodbc.connect(self.connString)

    def addPatient(self, id, name, gender, age, bloodgroup):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC addPatient {}, '{}', '{}', {}, '{}'".format(id, name, gender, age, bloodgroup))
            self.conn.commit()
            return True
        except Exception as ex:
            print(type(ex).__name__)

    def updatePatient(self, id, name, gender, age, bloodgroup):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC updatePatient {}, '{}', '{}', {}, '{}'".format(id, name, gender, age, bloodgroup))
            self.conn.commit()
            print("Updated details of patient")
        except Exception as ex:
            print(type(ex).__name__)


    def deletePatient(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC deletePatient {}".format(id))
            self.conn.commit()
            print("Deleted 1 patient")
        except Exception as ex:
            print(type(ex).__name__)

    def listPatients(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC listPatient")
            print("Patients\nID\t\tNAME\t\tGENDER\t\tAGE\t\tBLOODGROUP")
            for i in cursor:
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i[0], i[1], i[2], i[3], i[4]))
        except Exception as ex:
            print(type(ex).__name__)


    def searchPatient(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC searchPatient {}".format(id))
            if(cursor.rowcount == 0):
                print("Patient not in database")
            else:
                print("ID\t\tNAME\t\tGENDER\t\tAGE\t\tBLOODGROUP")
                for i in cursor:
                    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i[0], i[1], i[2], i[3], i[4]))
        except Exception as ex:
            print(type(ex).__name__)

def validate(string):
    if not (string == " " or string == "\n"):
        return string
    else:
        validate(input("Previous entry invalid\nPlease enter again : "))
def validateInt(num):
    if len(num) != 0:
        return int(num)
    else:
        return int(validateAndReturn(input("Previous entry invalid\nPlease enter again : ")))

hosp = Hospital()

#main function


while(True):
    print("""
        1. Add Patient
        2. Update Patient
        3. Delete Patient
        4. List Patients
        5. Search Patient
        6. Exit
        """)
   
   
    match int(input("Enter your choice: ")):
        case 1:
             hosp.addPatient(
                validateInt(input("Patient ID : ")),
                validate(input("Name : ")),
                validate(input("Gender : ")),
                validate(input("Age : ")),
                validate(input("Blood Group : "))
             )
            
           
        case 2:
            hosp.updatePatient(
                validateInt(input("Patient ID : ")),
                validate(input("Name : ")),
                validate(input("Gender : ")),
                validate(input("Age : ")),
                validate(input("Blood Group : "))
            )
        case 3:
            hosp.deletePatient(int(input("Patient ID : ")))
        case 4:
            hosp.listPatients()
        case 5:
            hosp.searchPatient(int(input("Patient ID : ")))
        case 6:
            hosp.conn.close()
            exit()
     