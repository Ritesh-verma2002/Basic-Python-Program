n = int(input())
s = input()
t = int(input())
while t:
    p = int(input())
    c = s[p-1]
    print(s[:p-1].count(c))
    t -= 1