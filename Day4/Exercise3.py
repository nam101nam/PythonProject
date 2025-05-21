list1=('HAT', 'Min', 'Justatie', 'Bray', 'Kimises')
list2=('DSK', 'Thái VG', 'MCK', 'Bray', 'Pháo', 'Kimises')
list3=set(list1)
list4=set(list2)
a=list3 & list4
print(list3-a)
print(list4-a)
