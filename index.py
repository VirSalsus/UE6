#!python
# -*- encoding: utf-8 -*-
import cgi
import cgitb
import random

cgitb.enable()

form = cgi.FieldStorage()
result = form.getvalue('result', '')
message = ""
fak1 = 0
fak2 = 0

if result == '':
    message = "specht du dummer nutten"
    fak1 = random.randint(1, 10)
    fak2 = random.randint(1, 10)

    # fak1String = str(fak1)
    # fak2String = str(fak2)
    # valueFak1 = "value='" + fak1String + "'"
    # valueFak2 = "value='" + fak2String + "'"
else:
    fak1 = form.getvalue('fak1', '')
    fak2 = form.getvalue('fak2', '')

    print(fak1)
    print(fak2)

    if fak1 * fak2 == result:
        message = "richtig"
    else:
        message = "falsch"

print("Content-type: text/html")
print()

print('<p> ', result, ' </p>')

print("""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Einmaleins</title>
    <link href="../Style.css" rel="stylesheet">
</head>
""")

print('<h1> Einmaleins - Trainer </h1>')
print('<form action="index.py" method="GET" >')
print('<input id="fak1" name="fak1" type="number" value="%i"> *' % fak1)
print('<input id="fak2" name="fak2" type="number" value="%i"> =' % fak2)
print('<input required id="result" type="text">')
print('<br> <br>')
print('<input type="submit" value="Prüfen">')
print('</form>')
print('<p> ', message, ' </p>')
