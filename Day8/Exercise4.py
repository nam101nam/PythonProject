str1='Welcome'
str2='home'
# str1 = "hello"
# str2 = "world"
# str1 = "abcdef"
# str2 = "xyz"
if len(str1)!=len(str2):
    if len(str1)>len(str2):
        lstr=str1
        sstr=str2
    else:
        lstr=str2
        sstr=str1
    gap=len(lstr)-len(sstr)
    newlstr=lstr[gap:len(lstr):1]+sstr
else:
    newlstr=str1+str2
print(newlstr)