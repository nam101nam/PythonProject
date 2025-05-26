class Person:
    def __init__(self, name: str='',age:int=0,gender:str=''):
        self._name = name
        self._age = age
        self._gender = gender
    def input(self):
        self._name=input('Nhập tên:')
        self._age=int(input('Nhập tuổi:'))
        self._gender=input('Nhập giới tính:')
    def output(self):
        print('Ten:',self._name)
        print('Tuoi:',self._age)
        print('Gioi tinh:',self._gender)

class Address:
    def __int__(self,city:str='',district:str=''):
        self._city = city
        self._district = district
    def input(self):
        self._city=input('Nhap thanh pho:')
        self._district=input('Nhap quan/huyen:')
    def output(self):
        print('Thanh pho:',self._city)
        print('Quan/huyen:',self._district)

class Student(Person):
    def __init__(self, name: str='',age:int=0,gender:str='',id:int =0,address: Address=None,gpa:float =0.0):
        super().__init__(name,age,gender)
        self._id = id
        self._address = address if address is not None else Address()
        self._gpa = gpa
    def input(self):
        super().input()
        self._id=int(input('Nhap id:'))
        self._gpa=float(input('Nhap gpa:'))
        self._address.input()
    def output(self):
        super().output()
        print('ID:',self._id)
        print('Gpa:', self._gpa)
        self._address.output()

class ClassRoom:
    def __init__(self,classID: int=0,numberOfStudents:int=0,listStudents:list=[]):
        self._classID = classID
        self._numberOfStudents = numberOfStudents
        self._listStudents = listStudents if listStudents is not None else []
    def input(self):
        self._numberOfStudents=int(input('Nhap so luong hoc sinh:'))
        for i in range(self._numberOfStudents):
            print('_'*100)
            print(f'Nhap hoc sinh thu {i+1}')
            student=Student()
            student.input()
            self._listStudents.append(student)
    def output(self):
        j=1
        for i in self._listStudents:
            print('_' * 100)
            print(f'Thong tin hoc sinh thu {j}')
            j+=1
            i.output()
    def searchByName(self,name:str):
        listName=[]
        for i in self._listStudents:
            if i._name==name:
                listName.append(i)
        return listName
a=ClassRoom()
a.input()
a.output()
name=input('Nhap ten muon tim kiem:')
list=a.searchByName(name)
for i in list:
    i.output()
