n=int(input('Nhập số đồng xu:'))
so_tang=0
so_xu=0
for i in range(1,n):
    if so_xu+i>n:
        print(f'So xu can cho tang {i} la',i,',So xu thua',n- so_xu)
        break
    else:
        so_xu+=i
        so_tang+=1
print('So xu da dung:',so_xu,'So tang da xay',so_tang)