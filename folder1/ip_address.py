import re
n = int(input())
s4 = ('^'+"{v}\."*3+"{v}$").format(v = "(25[0-5]|2[0-4]\d|[01]?\d?\d)")
s6 = ('^'+"{v}:"*7+"{v}$").format(v = "[\da-f]{1,4}")
ip4 = re.compile(s4)
ip6 = re.compile(s6)
while n:
    s = input()
    if ip4.match(s):
        print('IPv4')
    elif ip6.match(s):
        print('IPv6')
    else:
        print('Neither')
    n-=1