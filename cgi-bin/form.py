#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("number_a", "�� ������")
text2 = form.getfirst("number_b", "�� ������")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>��������� ������ ����</title>
</head>
<body>""")

print("<h1>��������� ������ ����!</h1>")
print("<p> number_a: {}</p>".format(number_a))
print("<p> number_b: {}</p>".format(number_b))

print("""</body>
</html>""")