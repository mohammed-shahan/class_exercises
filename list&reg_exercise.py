import re

_list = [75,78,23,43,11,24,56,22,45,50]


# 1.Sort the list in ascending order and print the first element in the list
 _list.sort()
print(_list[0]) 


#2.Python program to find second largest number in a list
_list.sort()
print(_list[-2])


#3.Python program to print odd numbers and even numbers seperately in a list of [1,2,3,4,5,6,7,8,9,10]
_l = [1,2,3,4,5,6,7,8,9,10]
odd = []
even = []
for i in _l:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even : ", even)
print("odd : ", odd) 



#4.Program for reversing a list
_newlist = _list[::-1]
print(_newlist) 



#5.program to print all odd numbers from 1-50
 odd = []
for i in range(1,51):
    if i%2!=0:
        odd.append(i)
print(odd)



#6.program to count even and odd numbers in a list
odd = []
even = []
for i in _list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("no of odd nos. : ",len(odd))
print("no of even nos. : ", len(even)) 

#########################################

#1.Write a python program to remove the zeros from an IP address ("216.08.094.196")
_ipaddr = '216.08.094.196'
print(_ipaddr.replace('0', ''))


#2.Write a python program that matches a string tha has an 'a' followed by anything, ending in 'b'
text = 'abb'
print(re.search('a.*?b$', text))




#3.Replace all occurences of 6 with six and 10 with ten for the given string They ate 6 apples and 10 banana
phrase = 'They ate 6 apples and 10 banana'
inter_phrase = re.sub('6', 'six', phrase)
final_phrase = re.sub('10', 'ten', inter_phrase)
print(final_phrase)