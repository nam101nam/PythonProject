import math
ab=int(input('Nhập cạnh AB:'))
bc=int(input('Nhập cạnh BC:'))
tan=float(bc/ab)
actan=math.atan(tan)
print(math.degrees(actan))