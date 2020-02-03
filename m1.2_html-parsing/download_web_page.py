from urllib.request import urlopen
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
ans = []
state = 0
for c in s:
    if c == '<':
        state = 1
    if c == '>':
        state = 0
    elif state == 0:
        ans.append(c)
s = ''.join(ans)
print(s.count('C++'))