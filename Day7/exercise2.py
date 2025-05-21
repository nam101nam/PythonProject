# a='apple banana banana apple kiwi apple kiwi grape apple mango apple kiwi'
a='zzz z zz z zz zzzz z'
a=a.split(' ')
b=set(a)
mydict={
}
for x in a:
    if x not in mydict:
        mydict[x] =1
    else:
        mydict[x]+=1
print(sorted(mydict.items(),key=lambda x:x[1],reverse=True))