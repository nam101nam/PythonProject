a = ('tài', 'thùy', 'thạch', 'trường', 'tiến')
a1=set(a)
b = ('hải', 'tài', 'nhật minh', 'cao minh', 'đặng anh', 'hùng', 'trường')
b1=set(b)
ab=a1&b1
print(a1-ab)
print(b1-ab)
