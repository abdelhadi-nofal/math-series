def fibonacci (n):
     if n <= 1:
       return n
     else:
       return(fibonacci(n-1) + fibonacci(n-2))

def lucas (n):
    if n == 0:
            return 2
    if n == 1:
            return 1
    
    return lucas(n-1) + lucas(n - 2);       

def sum_series (n,a = 0, b = 1):
    if a == 0 and b == 1:
        return fibonacci(n)
    elif  a == 2 and b == 1:
        return lucas(n)
    else:
        if n == 0:
            return a
        if n == 1:
            return b
        return sum_series(n-1,a,b) + sum_series(n-2,a,b)