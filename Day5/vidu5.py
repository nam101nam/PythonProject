def tim(s, k):
    vitri=[]
    i = 0
    while i <= len(s) - len(k):
        if s[i:i+len(k)] == k:
            vitri.append((i, i + len(k) - 1))
        i += 1
    return vitri
s = "aaadaa"
k = "aa"
# s=input()
# k=input()
result = tim(s, k)
print(result)
