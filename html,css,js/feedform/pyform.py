#!C:\Users\Mohammed Shahan\AppData\Local\Programs\Python\Python310\python.exe

import os
import sys
import cgi
import cgitb
import html





print("Content-type: text/html\n\n")

cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('name')

mail = form.getvalue('email')
password = form.getvalue('password')
emotions  = form.getlist('emotions')
satisfaction = form.getvalue('satisfied')
if(form.getvalue('comment')):
    comments = form.getvalue('comment')
else:
    comments = "No comments"
photo = form['bio-photo']

if photo.filename:
    photo_data = photo.file.read()
    file_name = os.path.basename(photo.filename)
    with open ('img/'+file_name, 'wb') as f:
        f.write(photo_data)
        msg = True
else:
    msg = False

location = form.getvalue('location')

print("""<html>
<head>
<link type="text/css" rel="stylesheet" href="css/style.css"/>
<title>Your Profile</title>
</head>
<body>
<div class="container" style='height:100%'>
""")
if(msg):
    print('''<img src="img/{}" alt="{}" width="200" height="200">'''.format(file_name, file_name))
else:
    print("<p>No Bio-Pic</p>")
print("<p>Name: %s</p>" % name)
print("<p>Email: %s</p>" % mail)
print("<p>Password: %s</p>" % password)
print("<p> Emotions are:</p><ul>")
for i in emotions:
    print("<li>%s</li>" % i)
print("</ul><p>Level of Satisfaction: %s</p>" % satisfaction)
print("<p>Comments: %s</p>" % comments)
print("<p>Location: %s</p>" % location)


print('''</div></body>
</html>''')



