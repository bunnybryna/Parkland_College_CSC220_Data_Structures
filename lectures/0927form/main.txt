#!/usr/local/bin/python3.5

# use the cgi library & show errors
import cgi, cgitb
cgitb.enable()
# use the date object from last class
from date import Date


# print the http response header
print ("Content-Type: text/html\n");

# create instance of FieldStorage 
# works with either POST or GET
form = cgi.FieldStorage() 

# get data from fields
m = form.getvalue('month')
d = form.getvalue('day')
y = form.getvalue('year')
webDate = Date(m, d, y)

# multiline print statement for chunks of html code
print ("""<html>
<head>
<title>Hello - Second CGI Program</title>
</head>
<body>
""");

print (str(webDate)) 

print ("<p>Thank you for entering the date</p>")

#print ("<hr>An error is next")
# cause an error
#print ("this is an error" + 6)
print ("</body>")
print ("</html>")

