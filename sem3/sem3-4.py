size, symbol = map (str, input().split())
size = int(size) 
# create the func
def triangle(size, symbol):
    
    for i in range(1, size + 1):
        print(symbol * i)
    for j in range(size -1, 0, -1):
        print(symbol * j)
        
triangle(size, symbol)
