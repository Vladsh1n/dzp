def horzisontal(x,i, count, side): 
    """Функция отвечает за заполнение строки, изначально идет слева направо, потом в цикле меняется направление
    (за это отвечает side), count заполняет каждую ячейку (считай глобальная переменная, можно было кстати ее глобальной обьявить
    ), i отвечает за номер заполняемой строки, x - массив;;; возвращает функция count, поскольку надо чтобы число в каждой клетке увеличивалось
    каждую итерацию, а также ans - последний столбец, заполенный этой функцией (в следующей, последняя заполненная строка)"""
    ans = 0 
    if side == True:
        for j in range(0, len(x[i])):
            if x[i][j] == 0:
                x[i][j] = count
                count += 1
                ans = j
    else:
        for j in range(len(x[i])-1, -1,-1):
            if x[i][j] == 0:
                x[i][j] = count
                count += 1
                ans = j
    return count, ans

def vertical(x, j, count , side):
    ans = 0
    if side == True:
        for i in range(0, len(x)):
            if x[i][j] == 0:
                x[i][j] = count
                count += 1
                ans = i
    else:
        for i in range(len(x)-1, -1, -1):
            if x[i][j]==0:
                x[i][j]=count
                count+=1
                ans=i
    return count, ans
n, m = map(int, input().split())
count = 1
matrix = []
for i in range(m):
    matrix.append([0]*n)
sideHor  = True
sideVert = True
i = j = 0
for a in range(0, n+m-2):
    count, j = horzisontal(matrix, i, count, sideHor)
    sideHor=False if sideHor==True else True # если sideHor==True, то sideHor=False, иначе sideHor =True; ниже аналогично#
    count, i = vertical(matrix, j, count, sideVert)
    sideVert=False if sideVert==True else True
for t in matrix:
    print(t)

print('')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] *= i
for t in matrix:
    print(t)