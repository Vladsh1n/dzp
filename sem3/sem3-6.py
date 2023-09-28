import random

countI = int(input())

Xi = [i for i in range(countI)]
sumXi = 0
for i in range(0, len(Xi)):
    sumXi += Xi[i]
Xisqr = []
for i in range(0, len(Xi)):
    Xisqr.append(Xi[i] * Xi[i])
sumXisqr = 0
for i in range(0, len(Xisqr)):
    sumXisqr += Xisqr[i]
Yi = []
for i in range(countI):
    Yi.append(random.randint(1,200))
sumYi = 0
for i in range(0, len(Yi)):
    sumYi += Yi[i]
XiYi = []
for i in range(0, len(Xi)):
    XiYi.append(Xi[i] * Yi[i])
sumXiYi = 0
for i in range(0, len(XiYi)):
    sumXiYi += XiYi[i]

print(Xi)
print(sumXi)
print(Xisqr)
print(sumXisqr)
print(Yi)
print(sumYi)
print(XiYi)
print(sumXiYi)

a = (countI * sumXiYi - sumXi * sumYi) / (countI * sumXisqr - (sumXi ** 2))
print(a)

b = (sumYi - a * sumXi) / countI
print(b)