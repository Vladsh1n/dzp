vvod = input().split()
vvod[::2], vvod[1::2] = vvod[1::2], vvod[::2] 
for i in vvod: print(i, '', end='')