num1, num2 = map(int, input().split() )
t = str()
u = str()
for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0: s = i
p = s*(2 + abs(2 * num1 * num2))
m = s*(2+abs(2 * num1 * num2))
for x in range(-m, m):
    y = (s - num1 * x) / num2
    for j in range(1,1 + int(abs(y))):
        if y % j == 0 and abs(x) + abs(y)<p:
            p = abs(x) + abs(y)
            t = str(x)
            u = str(int(y))
print(t, u, s)


