def check(dict1):
    dict2 = {}
    for key, value in dict1.items():
        if len(value['tenmonhoc'].split())>5 and value['sotinchi']>=3:
            dict2[key] = value
    return dict2
ma_hoc_phan = ["IT6002", "IT6126", "IT6067", "IT6120"]
chi_tiet=[
    {'tenmonhoc':'Cau truc du lieu va giai thuat','sotinchi':3},
    {'tenmonhoc':'He thong co so du lieu','sotinchi':4},
    {'tenmonhoc':'Kien truc may tinh va he dieu hanh','sotinchi':3},
    {'tenmonhoc':'Lap trinh huong doi tuong','sotinchi':3}
]
dict1={
}
dict1=dict(zip(ma_hoc_phan,chi_tiet))
print(dict1)
dict2={

}
dict2=check(dict1)
print(dict2)