# s='abaa cdcc'
s='paper little'
n=s.split()
def kiem_tra(n):
    if len(n[0])!=len(n[1]):
        return 'No'
    else:
        for i in range(0,len(n[0])):
            if n[0].count(n[0][i])!=n[1].count(n[1][i]):
                return 'No'
    return 'Yes'
print(n)
print(kiem_tra(n))