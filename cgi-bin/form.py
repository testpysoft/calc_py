#!/usr/bin/env python3
import cgi
import functools
import sys


def trace(func=None, *, handle=sys.stdout):
    #  зі скобкам
    if func is None:
        return lambda func: trace(func, handle=handle)

    # без скобок
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name, args, kwargs)
        return   func(*args, **kwargs)
    return inner







@trace
def add(x,y):
    return x+y

def divide(x,y):
    if (y == 0):
        print('division by zero')
        return
    return x/y
def multiply(x, y):
    return x*y
def subtract(x, y):
    return x-y

form = cgi.FieldStorage()
number_a = float(form.getfirst("number_a", "0"))
  
    

number_b= float(form.getfirst("number_b", "0"))
oper = form.getfirst("action", "add")

actions = {'add': add, 'multiply': multiply,'divide':divide,'subtract': subtract}
result=actions[oper](number_a, number_b)


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
print("<p {}</p>".format(oper))
print("<p> y: {}</p>".format(number_b))
print("<p> result: {}</p>".format(result))
print("""<p> <a href="/"><button>again computer    </button> </a></p>""")
print("""</body>
</html>""")

