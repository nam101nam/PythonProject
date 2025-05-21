def tinh_fibonacci(n):
    fibo=[0,1]
    a, b = 0, 1
    for i in range(2,n+1,1):
        c=fibo[i-1]+fibo[i-2]
        fibo.append(c)
    return fibo
print(tinh_fibonacci(10))
