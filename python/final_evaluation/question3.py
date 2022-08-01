#The denominations in Indian currency are:
#|1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
#Given an amount N, print how many coins/notes make up N

currenncy_denominations = {2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
amount = int(input("Please enter the amount: "))
value = amount

for currency in currenncy_denominations.keys():
    if value != 0:
        currenncy_denominations[currency] = value // currency
        value = value % currency
    
for currency in currenncy_denominations.keys():
    if currenncy_denominations[currency] != 0:
        print('%d: %d' %(currency, currenncy_denominations[currency]))

ver=0
#verifying
for currency in currenncy_denominations.keys():
    ver=ver+(currency*currenncy_denominations[currency])

if ver==amount:
    print("verified Denomination")
else:
    print("Incorrect Denominations ")
