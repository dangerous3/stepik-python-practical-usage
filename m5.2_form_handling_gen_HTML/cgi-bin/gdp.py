#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
substr = form.getfirst("TEXT_1", "не задано")
fin = open('../samples/gdp.tsv')
lines = fin.readlines()
fin.close()



print("Content-Type: text/html\n\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Внутренний валовый продукт</title>
        </head>
        <body>""")
print("<table>")
for line in lines:
    data = line.split('\t')
    name, gdp = data[1:]
    if substr in name:
        print("<tr><td>", name, "</td><td>", gdp, "</td></tr>")
print("</table>")
print("""</body>
        </html>""")