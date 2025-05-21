# n=int(input('Nhập số mã cần kiểm tra:'))
list_the = [
    '4567890123456789',     # ✅ Hợp lệ (chỉ số, bắt đầu bằng 4)
    '5234-5678-1234-0000',  # ✅ Hợp lệ (dấu '-', đúng định dạng, bắt đầu bằng 5)
    '6123-4567-8912-3456',  # ✅ Hợp lệ (bắt đầu bằng 6)
    '1234567890123456',     # ❌ Bắt đầu bằng 1
    '4567-8912-3456',       # ❌ Thiếu nhóm -> sai độ dài sau khi bỏ dấu '-'
    '4567-89a2-3456-0000',  # ❌ Có ký tự lạ 'a'
    '4567_8912_3456_0000',  # ❌ Có ký tự lạ '_'
    '4567-8912-345-60000',  # ❌ Nhóm sai độ dài
    '45678901234567890',    # ❌ Dư số (17 số)
    '4-5678-9012-3456-789', # ❌ Quá nhiều dấu '-'
    '1234-5678-9012-3456',  # ❌ Bắt đầu bằng 1
    '5678567856785678',     # ✅ Hợp lệ
]
fist=['4','5','6']
# for i in range(n):
#     str=input('Nhập mã thẻ:')
#     list_the.append(str)
def check(str):
    cardclean=str.replace('-','')
    if len(cardclean)!=16:
        print('1:Không đủ dài')
        return False
    if str[0] not in fist:
        print('2: không khởi đầu bằng 3,4 hoặc 5')
        return False
    for i in str:
        if not (i.isdigit() or i =='-'):
            print('3: Trong có ký tự khác thường')
            return False
    if len(str)==19:
        if str[4] != '-' or str[9] != '-' or str[14] != '-':
            print('4: Không đúng cấu trúc xxxx-xxxx-xxxx-xxxx')
            return False
    return True
for card in list_the:
    print(f'Kiểm tra thẻ: {card}')
    print('Kết quả:', check(card))
    print('---')

