an=float(input("An: "))
linh=float(input("Linh: "))
duc=float(input("Đức: "))
nam=float(input("Nam: "))
ds=[("An", an), ("Linh", linh), ("Đức", duc), ("Nam", nam)]
high=ds[0]
for x in ds[1:]:
    high=(x[0],x[1]*(x[1]>high[1])+high[1]*(x[1]<=high[1]))
    high=(x[0],x[1])if x[1]>high[1] else high
print(high[0])
