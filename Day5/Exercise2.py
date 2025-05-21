vowel=['A','E','I','O','U']
str='BANANA'
stuart_point=0
kevin_point=0
for i in range(len(str)):
    if str[i] in vowel:
        kevin_point+=len(str)-i
    else:
        stuart_point+=len(str)-i
print(kevin_point,stuart_point)