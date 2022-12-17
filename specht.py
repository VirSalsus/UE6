import cgi
from random import randrange
import cgitb

cgitb.enable()

felder = cgi.FieldStorage()
xString = felder.getValue("x", "")
yString = felder.getValue("y", "")
zString = felder.getValue("z", "")

print("Content-Type: text/html")
print()

korrektString = """        
        <p>Korrekt.</p>
        <p><a href="index.py">Nochmal spielen</a></p>")
    """

fehlerString = """
        <p>Leider nicht korrekt. Bitte Produkt korrigieren</p>
        <p><button type="submit">Nochmal prüfen</button></p>
        """

print("""
    <html>
        <head>
            <title>Einmaleins</title>
        </head>

        <body>
            <h1>Einmaleins-Trainer</h1>
            <from method="get" action="index.py">
""")

if xString != "":
    x = int(xString)
else:
    x = randrange(1, 11)
xValueString = "value" + str(x)

if yString != "":
    y = int(yString)
else:
    y = randrange(1, 11)
yValueString = "value" + str(y)

if zString != "":
    zValueString = f"value='{zString}'"
    z = int(zString)
else:
    zValueString = ""

print("""
    <input id="x" name="x" type="number" min="1" max="10" step="1" readonly value='{xValueString}'>*
    <input id="x" name="x" type="number" min="1" max="10" step="1" readonly value='{xValueString}'>=
    <input id="x" name="x" type="number" min="1" max="100" step="1" value = '{xValueString}' >
        """)

if xString != "" and yString != "" and xString != "":
    if x * y == result
        korrekt = True
        print(korrektString)
    else:
        korrekt = False
        print(fehlerString)
else:
    print("""<p><button type="Submit ">Prüfen</button></p>""")

    print("""
        < / form >
            < / body >
                < / html > \
                    """)
