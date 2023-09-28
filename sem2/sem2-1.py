a=input().split()
sum=0
for i in ( a[1:] ):
    sum += int(i)
print((1 + int(a[0])) * (1 / 2) * int(a[0]) - sum)