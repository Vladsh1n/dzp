a =[int(x) for x in input().split()]
print(*(a[x] for x in range(0, len(a)) if all((a[x]^a[i]!=0 or x==i) for i in range(0, len(a)))))