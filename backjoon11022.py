cases = int(input())

for i in range(cases):
    a, b = map(int, input().split())
    ans = a + b
    print("Case #%s: %d + %d = %s" % (i+1, a, b, ans))
