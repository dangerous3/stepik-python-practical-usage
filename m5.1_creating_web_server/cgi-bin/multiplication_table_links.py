#!/usr/bin/env python3

print("Content-Type: text/html\n\n")
print("<html>")
print("<body>")
print("<table>")
for i in range(1,11):
    print("<tr>")
    for j in range(1,11):
        res = i*j
        print("<td>" + "<a href=http://" + str(res) + ".ru>" + str(res) + "</a>" + "</td>")
    print("</tr>")
print("</table>")
print("</body>")
print("</html>")