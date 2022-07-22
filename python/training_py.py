import sys
import re

print ("Hello world")
#just printing the python version
just a
multiline comment
print(sys.version)



text = "{} is my country. All Indians are my brothers and sisters.".format('India')
print(text)

c = text.count('India')
print("Count of India in the text is {}".format(c))

myString = 'superman'
print(myString.endswith('man'))
print(myString.endswith('man',3))#start checking from index 3
print(myString.endswith('man',2,6))
print(myString.endswith(('man','ma'),2,6))


myString = "Good Morning"
print(myString.find('Mo'))
print(myString.find('Mo',3))
print(myString.find('Mo',3,7))
print(myString.index('M0o'))

#join() method to join items in a tuple with a separator
Separator = '*'
myTuple = ('h','e','l','l','o')
myNewString = Separator.join(myTuple)
print(myNewString)
print(myNewstring.lower())
print(myNewstring.upper())


#replace and split method
myString = "Hello World"
myString = myString.replace('o','i')
print(myString)
myStringSplit = myString.split(' ')
print(myStringSplit)


txt = "bits of paper, bits of paper"
x= re.findall("bi",txt)
print(x)

x= re.search("bi",txt)
print(x)

x= re.sub(" ","-",txt)
print(x)

#search using meta chars
txt ="hello world"
#find all lower case char between 'a' and 'm'
x=re.findall("[a-m]",txt)
print(x)


txt ="james bond is 007"
#find all the digits
x=re.findall("\d",txt)
print(x)

#look for a substr with j and have three char in b/w ends with s
x=re.findall("j...s",txt)
print(x)

#look for substr starting with'hello'
#using the metachar ^ and \A are same
txt = "hello world"
x=re.findall("^hello",txt)
print(x)

txt = "hello world"
x=re.findall("\Ahello",txt)
print(x)

#look for substr starting with 'world'
x=re.findall("world$",txt)
print(x)

#look for substr starting with 'wor'
x=re.findall("\wor",txt)
print(x)

#look if any word in the string starts with 'the'
txt="james watt invented the engine"
#look for substr starting with 'jam'
x=re.findall("\Ajam",txt)
print(x)

#using the metachar $
txt= "james watt invented sothe"
x=re.findall(r"the$",txt)
print(x)

#using the special sequence \b
txt= "james watt invented theso watt"
x=re.findall(r"\bthe",txt)
print(x)

#matching an email within a string using spcial sequence
mystring = "my email is tinu@tinu.com hope you will note it down"

#regular expression to match email
#check for non space chars before and  after '@'
regex='\S+@\S+'
x=re.findall(regex, mystring)
print(x)


#LIST AND LIST ACCESS OPTIONS
studentsAge = [18,39,23,13]
print(studentsAge)
print(studentsAge[2])#print the particular index
newStudentsAge=studentsAge[2:4]#starting from 2 till 4-1
print(newStudentsAge)
newStudentsAge=studentsAge[1:5:2]#starting from 1 till 5-1,every 2nd elemnts
print(newStudentsAge)
newStudentsAge=studentsAge[:3]#starting 0 index till 3-2 index
print(newStudentsAge)
newStudentsAge=studentsAge[::-1]#reverse the list
print(newStudentsAge)
newStudentsAge=studentsAge[-4]#reverse the list
print(newStudentsAge)

#append to add a value to the end of the list
studentsAge.append(16)

print(studentsAge)

#delete value from the list
del studentsAge[-1]
print(studentsAge)

#combine two list using extend()
studentsName =['Anu','Jobson','Tintu']
#studentsAge.extend(studentsName)
print(studentsAge)

#check if an item is in a list
print('Anu' in studentsName)

#get the no of items in the list
print(len(studentsName))

#reverse the contents 
studentsName.reverse()
print(studentsName)
studentsName.reverse()
print(studentsName)

#sort the list either alphabetically or numerically
studentsAge.sort()
print(studentsAge)

#list concatnation using + operator
print(studentsName+studentsName)
print(studentsName)

#list concatnation using * operator
print(studentsName*2)
print(studentsName)