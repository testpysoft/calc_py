#!/usr/bin/env python3
import cgi


def add(x,y):
    return x+y
def multiply():
     return x*y
def divide(x,y):
    if (number_b== 0):
        print('division by zero')
        return
    return a/b
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y

form = cgi.FieldStorage()
number_a = form.getfirst("number_a", "100")
number_b= form.getfirst("number_b", "100")
oper = form.getfirst("action", "add")

actions = {'add': add, 'multiply': multiply,'divide':divide,'subtract': subtract}
result=actions[oper](number_a,number_b)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>Form calc</title>
</head>
<body>""")

print("<h1>We all done!</h1>")
print("<p> x: {}</p>".format(number_a))
print("<p> action: {}</p>".format(oper))
print("<p> y: {}</p>".format(number_b))
print("<p> result: {}</p>".format(result))
print("""<p> <a href="/"><button>again computer    </button> </a></p>""")
print("""</body>
</html>""")