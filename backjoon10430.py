a, b, c = input().split()

c1 = (int(a)+int(b)) % int(c)
c2 = ((int(a) % int(c)) + (int(b) % int(c))) % int(c)
c3 = (int(a)*int(b)) % int(c)
c4 = (int(a) % int(c)) * (int(b) % int(c)) % int(c)

print(c1)
print(c2)
print(c3)
print(c4)
