# a=input('Nhập set 1:')
# b=input('Nhập set 2:')
# a=set(a)
# b=set(b)
a={4,2,1,3}
b={9,4,5,6}
ab=a|b
print('Tập  hợp:',ab)
agb=a&b
print('Giao:',agb)
print('Có ở a không ở b: ',a-b)
print('Có ở b không ở a: ',b-a)
if a.issubset(b):
    print('a là tập con')
else:
    print('a không phải tập con')
if a.issuperset(b):
    print('a l tập cha')
else:
    print('a không phải tập cha')

print('Dãy đã sắp xếp',ab)