
import math
x1, y1 = map(float, input("Nhập tọa độ A (x y): ").split())
x2, y2 = map(float, input("Nhập tọa độ B (x y): ").split())
x3, y3 = map(float, input("Nhập tọa độ C (x y): ").split())
a=math.sqrt(x1**2 + y1**2)
b=math.sqrt(x2**2 + y2**2)
c=math.sqrt(x3**2 + y3**2)
d=[a,b,c]
d.sort()
print("Nhà gần trường nhất: ",d[0])
print("Nhà xa xa trường nhất: ",d[2])
