import numpy as np
m=int(input('So hang='))
n=int(input('So cot='))
arr1=((input(f'Nhập phần tử của matrix {m}x{n} gom {m*n} phan tu:')).split())
arr11=[int(x) for x in arr1]
matrix1=np.array(list(arr11)).reshape(m,n)
arr2=((input(f'Nhập phần tử của matrix {n}x{m} gom {m*n} phan tu:')).split())
arr12=[int(x) for x in arr2]
matrix2=np.array(list(arr12)).reshape(n,m)
print('Tich cua 2 ma tran:')
print(np.dot(matrix1,matrix2))
