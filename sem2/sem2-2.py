count_groups, groups = map(list, input().split())
palindrom = []
count=int(count_groups[0])
second = count-1
n=0
while n != count:   
    a=second
    for i in groups[second::-1]:
        palindrom.append(i)
        groups.pop(a)
        a-=1
    n+=1   
print(''.join(palindrom))
