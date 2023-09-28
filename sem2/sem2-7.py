def numbers(x, a):
    count=0
    for i in range(0, len(a)):
        if a[i]==x: count+=1
    return count
a = [int(x) for x in input().split()]
mx_count=ans=0
for i in range(0, len(a)):
    if mx_count < numbers(a[i], a): 
        mx_count, ans = numbers(a[i], a), a[i]
print(ans)