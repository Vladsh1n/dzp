N = int(input())
def fibonacci(n):
    if N == 1:
        return 0 
    elif n < 4:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(N))