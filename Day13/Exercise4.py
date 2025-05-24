class Person:
    def __init__(self,name: str, age: int, gender: str):
        self._name = name
        self._age = age
        self._gender = gender
    def input(self):
        self._name = input('Nhap ten:')
        self._age = int(input('Nhap tuoi:'))
        self._gender = input('Nhap gioi tinh:')
    def output(self):
        print('Ten la',self._name)
        print('Tuoi ', self._age)
        print('Gioi tinh', self._gender)
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_gender(self):
        return self._gender
    def set_name(self, name:str):
        self._name= name
    def set_age(self, age:int):
        self._age = age
    def set_gender(self, gender:str):
        self._gender = gender

class Student(Person):
    def __init__(self,name: str,age: int,gender: str,id: int,address,gpa:float ):
        super().__init__(name,age,gender)
        self._id = id
        self._address = address
        self._gpa = gpa
    def input(self):
        super().input()
        self._id = int(input('Nhap id:'))
        self._address.input()
        self._gpa = float(input('Nhap gpa:'))
    def output(self):
        super().output()
        print(f'id: {self._id}')
        self._address.output()
        print(f'Gpa:{self._gpa}')
    def get_id(self):
        return self._id
    def get_address(self):
        return self._address.get_address()
    def get_gpa(self):
        return self._gpa
    def set_id(self, id:int):
        self._id = id
    def set_address(self, address:str):
        self._address = address
    def set_gpa(self, gpa:float):
        self._gpa = gpa

class Address:
    def __init__(self,city: str,district:str):
        self._city = city
        self._district = district
    def input(self):
        self._city=input('Nhap city:')
        self._district=input('Nhap district:')
    def output(self):
        print(f'City: {self._city}')
        print(f'District: {self._district}')
    def get_address(self):
        return f'{self._city} {self._district}'
    def set_address(self, city:str, district:str):
        self._city = city
        self._district = district

class ClassRoom:
    def __init__(self,classId:int,numberOfStudent:int,listStudents):
        self._classId = classId
        self._numberOfStudent = numberOfStudent
        self._listStudents = listStudents
    def input(self):
        self._classId = int(input('Nhap classId:'))
        self._numberOfStudent = int(input('Nhap numberOfStudent:'))
        self._listStudents = []
        for i in range(0,self._numberOfStudent):
            a=Student()
            a.input()
            self._listStudents.append(a)
    def output(self):
        print(f'ClassId: {self._classId}')
        print(f'NumberOfStudent: {self._numberOfStudent}')
        for i in range(1,self._numberOfStudent):
            self._listStudents[i].output()


danh_sach_sinh_vien = []


address_hanoi = Address("Ha Noi", "Cau Giay")
address_hcm = Address("Ho Chi Minh City", "Quan 1")
address_danang = Address("Da Nang", "Hai Chau")


sinh_vien1 = Student("Nguyen Van An", 20, "Nam", 1001, address_hanoi, 3.5)
danh_sach_sinh_vien.append(sinh_vien1)

sinh_vien2 = Student("Tran Thi Binh", 21, "Nu", 1002, address_hcm, 3.9)
danh_sach_sinh_vien.append(sinh_vien2)

sinh_vien3 = Student("Le Van Cuong", 19, "Nam", 1003, address_hanoi, 3.2)
danh_sach_sinh_vien.append(sinh_vien3)

sinh_vien4 = Student("Pham Thi Dao", 22, "Nu", 1004, address_danang, 4.0)
danh_sach_sinh_vien.append(sinh_vien4)

classroom = ClassRoom(101,4,danh_sach_sinh_vien)
classroom.output()




