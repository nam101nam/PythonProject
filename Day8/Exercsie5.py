def findlongest(s,l,r):
    while l>=0 and r<len(s) and s[l]==s[r]:
        l-=1
        r+=1
    return s[l+1:r]
s=input('Nhập chuỗi:')
longest=''
for i in range(len(s)):
    odd=findlongest(s,i,i+1)
    even=findlongest(s,i,i)
    if len(odd)>len(longest):
        longest=odd
    if len(even)>len(longest):
        longest=even
print(longest)