from operator import index

age=[2, 18, 24, 35, 70, 45]
oldest=age[0]
youngest=age[0]
for i in age:
    if i > oldest:
        oldest=i
    if i<youngest:
        youngest=i
print(age.index(oldest))
print(age.index(youngest))

