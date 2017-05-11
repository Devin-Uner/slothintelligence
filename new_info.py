#!/usr/bin/python
import cgi
form = cgi.FieldStorage()



# ##snippet 1o ##### read in all the data
all_users = {}
file = open("user_data.txt", "r")
for line in file:
	# print 'line.split(" ")[0], line.split(" ")[1]'
	all_users[line.split(" ")[0]] = line.split(" ")[1]
file.close()
##snippet 1c ##### 





print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


print '	<head>'
print '	<title>sign up</title>'
print ' </head>'

print '<body>'

try:
	username = form["username"].value
	password = form["password"].value
	# print all_users[username], str(hash(password)), str(hash(password))==all_users[username]
	if(str(hash(password))==all_users[username]):
		print '<p>logged in, welcome ', username, ' please enter in data below </p>'
	else:
		print '<p>incorrect login data, please try again </p>'
		print '<form action = "new_info.py" method = "post">'
		print 'username: <input type="text" name="username" size="10"><br> '
		print 'password: <input type="password" name="password" size="15"><br>'
		print '<input type="submit">'
		print '</form>'
	
except:
	print '<form action = "new_info.py" method = "post">'
	print 'username: <input type="text" name="username" size="10"><br> '
	print 'password: <input type="password" name="password" size="15"><br>'
	print '<input type="submit">'
	print '</form>'
	print ' <p> asda asd ad a ds </p>'
print '</body>'



