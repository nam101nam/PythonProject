def tim_cac_so_chan(n):
    a=[]
    for i in range(1,n+1):
        if i%2==0:
            a.append(i)
    return a
print(tim_cac_so_chan(10))
print(tim_cac_so_chan(20))