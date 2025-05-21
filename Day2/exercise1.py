n=int(input("Nhập số bạn được nhận quà: "))
m=int(input("Nhập số hộp quà: "))
k=int(input("Nhập số túi quà trong mỗi hộp: "))
tongtui=m*k
if tongtui % n==0:
    print("Chia đều được cho các bạn")
else:
    print("Không chia đều được cho các bạn")
