#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("number_a", "не задано")
text2 = form.getfirst("number_b", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>Обработка данных форм</title>
</head>
<body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p> number_a: {}</p>".format(number_a))
print("<p> number_b: {}</p>".format(number_b))

print("""</body>
</html>""")