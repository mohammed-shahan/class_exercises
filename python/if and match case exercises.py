#personality inputs
personality = (
    {
    1: "People born in January are bold and alert",
    2: "People born in February are lucky",
    3: "People born in March are naughty an genius",
    4: "People born in April are caring and strong",
    5: "People born in May are loving and practical",
    6: "People born in June are romantic and curious",
    7: "People born in July are adventurous and honest",
    8: "People born in August are active and hardworking",
    9: "People born in September are sensitive and pretty",
    10: "People born in October are stylish and friendly",
    11: "People born in November are nice and creative",
    12: "People born in December are confident and freedom loving"
})

#birthstone inputs
birthstone = ({
    1: "Garnet",
    2: "Amethyst",
    3: "Aquamarine",
    4: "Diamond",
    5: "Emerald",
    6: "Alexandrite",
    7: "Ruby",
    8: "Peridot",
    9: "Sapphire",
    10: "Tourmaline",
    11: "Citrine",
    12: "Zircon"
})

#month inputs
month = ({
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
})

def print_details(mon):
    print("Month :", month.get(mon))
    print("Birthstone :", birthstone.get(mon))
    print("Personality :", personality.get(mon))

mon = int(input("Enter month number : "))


print_details(mon)

#if elif else method

 if mon == 1:
    print_details(1)
elif mon == 2:
    print_details(2)
elif mon == 3:
    print_details(3)
elif mon == 4:
    print_details(4)
elif mon == 5:
    print_details(5)
elif mon == 6:
    print_details(6)
elif mon == 7:
    print_details(7)
elif mon == 8:
    print_details(8)
elif mon == 9:
    print_details(9)
elif mon == 10:
    print_details(10)
elif mon == 11:
    print_details(11)
elif mon == 12:
    print_details(12)
else:
    print("Wrong Entry") 




#match case method

""" match mon:
    case 1: print_details(1)
    case 2: print_details(2)
    case 3: print_details(3)
    case 4: print_details(4)
    case 5: print_details(5)
    case 6: print_details(6)
    case 7: print_details(7)
    case 8: print_details(8)
    case 9: print_details(9)
    case 10: print_details(10)
    case 11: print_details(11)
    case 12: print_details(12)
    case _: print("Wrong Entry") """