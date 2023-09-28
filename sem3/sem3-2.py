num = int(input())
def prime_factors(num):    
    
    # пока число четное считаем кол-во множителей 2
    
    while num % 2 == 0: 
        print(2, end = " ") 
        num = num / 2 
        
    # перебираем простые делители числа с шагом 2 
 
    for i in range(3, int(num**0.5) + 1, 2):  
        
        while num % i == 0: 
            print(i, end = " ") 
            num = num / i 
    
    if num > 2: 
        print(int(num))
    
print(1, end = " ")
    
prime_factors(num) 
