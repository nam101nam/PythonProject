# # # # # # # # # while True:
# # # # # # # # #     a=int(input('Nhap='))
# # # # # # # # #     if a==0: break
# # # # # # # # #     print(a)
# # # # # # # #
# # # # # # # # for a in [1,2,3,4,5,6,7,8,9,10]:
# # # # # # # #     print(a)
# # # # # # # numbers = [2,3,7,1,8,9]
# # # # # # # tongChan = 0
# # # # # # # for number in numbers:
# # # # # # #   if(number % 2 == 0):
# # # # # # #     tongChan += number
# # # # # # # print(tongChan)
# # # # # # #in ra các số từ 0 đến 5
# # # # # # # for i in range(1,6):
# # # # # # #   print(i)
# # # # # # # a=[1,2,3,4,5,6]
# # # # # # # for i, j in enumerate(a,1):
# # # # # # #     print(i,j)
# # # # # # i=0
# # # # # # while i<5:
# # # # # #     print(i)
# # # # # #     i=i+1
# # # # # # else: print('In xong')
# # # # # # for i in range(5):
# # # # # #     print(i)
# # # # # # else: print('In xong')
# # # # # for i in range(1,100,1):
# # # # #     if(i%10==0):
# # # # #         continue
# # # # #     elif(i%2==0):
# # # # #         print(i)
# # # # L = ["abc", "123", 123, ' b ', [4, 6, 7, 8]]
# # # # L[:0]='1'
# # # # print(L)
# # # # L[len(L):]='100'
# # # # print(L)
# # # # del L[1:4]
# # # # print(L)
# # # oldlsit=[1,2,3,4,5,5]
# # # print(oldlsit)
# # # newlist1=oldlsit.copy()
# # # newlist=oldlsit[:]
# # # newlist1[0]=10
# # # newlist[0]=10
# # # print(newlist1)
# # # print(oldlsit)
# # # print(newlist)
# # # print(newlist1.count(5))
# # from operator import index
# #
# # list=[0,1,2,3,4,5]
# # list.append(6)
# # list.extend([7,8,5])
# # print(list)
# # print(list.count(5))
# # print(list.index(8,0,len(list)-1))
# #
# L=[x**2 for x in range(0,5,1)]
# print(L)
list=[0,1,2,3,4,5]
L=[x for x in list if x>3]
print(L)
iss=1,2,3,4,5
print(iss)
a,b,c,d,e=iss
print(a,b,c,d,e)
