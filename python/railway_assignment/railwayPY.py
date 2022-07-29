import pyodbc
import functools

def db(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conString = 'Driver={SQL Server};Server=DESKTOP-4D00VLG\SQLEXPRESS01;Database=Railway;Trusted_Connection=yes;'
            myconn = pyodbc.connect(conString)
        except:
            print('Connection Error')
            return None
        else:
            mycursor = myconn.cursor()
            value = func(mycursor, *args)
            myconn.commit()
            myconn.close()
            return value
    return innerWrapper
    
@db
def getStops(mycursor: pyodbc.Cursor) -> dict:
    mycursor.execute('SELECT * FROM stops')
    stops = dict()
    for id, stop in mycursor:
        stops[id] = stop
    return stops

@db
def getTrains(mycursor: pyodbc.Cursor) -> dict:
    mycursor.execute('SELECT id, code, dest, berth, waitlist FROM trains')
    trains = dict()
    for id, code, dest, berth, waitlist in mycursor:
        trains[id] = {'code' : code, 'dest' : dest, 'berth' : berth, 'waitlist' : waitlist}
    return trains

@db
def getTrWL(mycursor: pyodbc.Cursor) -> dict:
    mycursor.execute('EXEC getTrWL')
    wl = dict()
    for code, dest, max_waitlist, booked_waitlist, available_waitlist in mycursor:
        wl[code] = {
            'dest' : dest, 
            'max_waitlist' : max_waitlist,
            'booked_waitlist' : booked_waitlist if booked_waitlist is not None else 0,
            'available_waitlist' : available_waitlist if available_waitlist is not None else max_waitlist
        }
    return wl


@db
def getTrSeats(mycursor: pyodbc.Cursor) -> dict:
    mycursor.execute('EXEC getTrSeats')
    seats = dict()
    for code, max_berth, booked_berth, available_berth in mycursor:
        seats[code] = {
            'max_berth' : max_berth,
            'booked_berth' : booked_berth if booked_berth is not None else 0,
            'available_berth' : available_berth if available_berth is not None else max_berth
        }
    return seats

@db
def getPassengers(mycursor: pyodbc.Cursor) -> dict:
    mycursor.execute('SELECT * FROM passengers')
    passengers = dict()
    for id, name, age, dest, train, waitlist in mycursor:
        passengers[id] = {'name' : name, 'age' : age, 'dest' : dest, 'train' : train, 'waitlist' : waitlist}
    return passengers


@db
def addPassenger(mycursor: pyodbc.Cursor):
    dests = getStops()
    name = input('Name: ')
    age = int(input('Age: '))
    while(True):
        print('Destinations: ')
        for key, val in dests.items():
            print(f'{key}. {val}')
        dest  = int(input('> '))
        if dest in dests.keys():
            break
        print('Invalid input')
    trains = getTrains()
    seats = getTrSeats()
    booked = False
    for id, train in trains.items():
        if train['dest'] >= dest:
            if seats[train['code']]['available_berth'] > 0:
                mycursor.execute(
                    'INSERT INTO passengers VALUES (?, ?, ?, ?, ?)', 
                    (name, age, dest, id, 0)
                )
                print('Berth booked')
                print('Train:', train['code'])
                booked = True
                break
    wlBooked  = False
    if not booked:
        waitlist = getTrWL()
        for code, wt in waitlist.items():
            if wt['dest'] >= dest:
                if wt['available_waitlist'] > 0:
                    for id, train in trains.items():
                        if train['code'] == code:
                            mycursor.execute(
                                'INSERT INTO passengers VALUES (?, ?, ?, ?, ?)',
                                (name, age, dest, id, 1)
                            )
                            print('Booked into waitlist')
                            print('Train: ', train['code'])
                            break
                    wlBooked = True
                if wlBooked:
                    break
    if not (booked or wlBooked):
        print('No berth and waitlist full')


while True:
    print("Welcome to IRCTC")
    print("1. Book Passenger\n 2. List Passenger\n 3. List Trains\n 4. Exit")
    opt = int(input("Select your option:"))
    match opt:
        case 1: addPassenger()
        case 2: 
            dests = getStops()
            trains = getTrains()
            print('Passengers:')
            for id, p in getPassengers().items():
                print('ID:', id)
                print('Name:', p['name'])
                print('Age:', p['age'])
                print('Dest:', dests[p['dest']])
                print('Train:', trains[p['train']]['code'])
                print('Status:', 'Waitlist' if p['waitlist'] else 'Booked')
                print()
        case 3: 
            trains = getTrains()
            for train in trains.values():
                print('Train:', train['code'])
        case 4: break
        case _: print("Invalid choice")