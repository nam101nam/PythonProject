# class_diagram_simplified.py
class Person:
    def __init__(self, name: str = "", age: int = 0, gender: str = ""):
        self._name = name
        self._age = age
        self._gender = gender

    def input(self):
        self._name = input('Nhập tên: ')
        self._age = int(input('Nhập tuổi: '))
        self._gender = input('Nhập giới tính: ')

    def output(self):
        print(f"Tên: {self._name}")
        print(f"Tuổi: {self._age}")
        print(f"Giới tính: {self._gender}")

    def __str__(self):
        return f"Tên: {self._name}, Tuổi: {self._age}, Giới tính: {self._gender}"

class Address:
    def __init__(self, city: str = "", district: str = ""):
        self._city = city
        self._district = district

    def input(self):
        self._city = input('Nhập thành phố: ')
        self._district = input('Nhập quận/huyện: ')

    def output(self):
        print(f"Thành phố: {self._city}")
        print(f"Quận/Huyện: {self._district}")

    def __str__(self):
        return f"{self._district}, {self._city}"


class Student(Person):
    def __init__(self, name: str = "", age: int = 0, gender: str = "",
                 student_id: int = 0, address: Address = None, gpa: float = 0.0):
        super().__init__(name, age, gender)
        self._id = student_id
        self._address = address if address is not None else Address()
        self._gpa = gpa

    def input(self):
        super().input()
        self._id = int(input('Nhập ID sinh viên: '))
        print("--- Nhập thông tin địa chỉ ---")
        self._address.input()
        self._gpa = float(input('Nhập GPA (0.0 - 4.0): '))

    def output(self):
        super().output()
        print(f"ID: {self._id}")
        self._address.output()
        print(f"GPA: {self._gpa:.2f}")

    def __str__(self):
        return (f"Student: ID={self._id}, Tên={self._name}, Tuổi={self._age}, "
                f"Giới tính={self._gender}, GPA={self._gpa:.2f}, "
                f"Địa chỉ: ({self._address})")


class Classroom:
    def __init__(self, class_id: int = 0, students: list = None):  # Thay list[Student] thành list cho đơn giản
        self._class_id = class_id
        self._list_students = students if students is not None else []
        self._number_of_student = len(self._list_students)

    def input(self):

        self._class_id = int(input('Nhập ID lớp học: '))  # Bỏ qua kiểm tra lỗi input

        num_students = int(input('Nhập số lượng sinh viên trong lớp: '))  # Bỏ qua kiểm tra lỗi input

        self._list_students = []
        print(f"--- Nhập thông tin cho {num_students} sinh viên ---")
        for i in range(num_students):
            print(f"\nNhập thông tin sinh viên thứ {i + 1}:")
            student = Student()
            student.input()
            self._list_students.append(student)
        self._number_of_student = len(self._list_students)

    def output(self):
        print(f"\n--- Thông tin Lớp học ID: {self._class_id} ---")
        print(f"Tổng số sinh viên: {self._number_of_student}")
        if self._number_of_student > 0:
            print("\nDanh sách sinh viên:")
            for i, student in enumerate(self._list_students):
                print(f"Sinh viên {i + 1}:")
                student.output()
                print("-" * 20)
        else:
            print("Chưa có sinh viên nào trong lớp.")

    def search_by_name(self, name: str) -> list:  # Thay list[Student] thành list cho đơn giản
        found_students = []
        search_name_lower = name.lower()
        for student in self._list_students:
            # Truy cập trực tiếp thuộc tính _name vì không có getter
            if search_name_lower in student._name.lower():
                found_students.append(student)
        return found_students

    def __str__(self):
        return f"Classroom ID: {self._class_id}, Số lượng sinh viên: {self._number_of_student}"


# --- Hàm Main để tương tác với người dùng ---
# def main():
#     print("--- CHƯƠNG TRÌNH QUẢN LÝ LỚP HỌC VÀ SINH VIÊN ---")
#
#     my_classroom = Classroom()
#
#     print("\n[Bước 1: Nhập thông tin lớp học và sinh viên]")
#     my_classroom.input()
#
#     print("\n[Bước 2: Hiển thị thông tin đã nhập]")
#     my_classroom.output()
#
#     print("\n[Bước 3: Tìm kiếm sinh viên theo tên]")
#     if my_classroom._number_of_student > 0:
#         search_query = input("Nhập tên (hoặc một phần tên) sinh viên cần tìm: ")
#         found_students = my_classroom.searchByName(search_query)
#
#         if found_students:
#             print(f"\nTìm thấy {len(found_students)} sinh viên với tên '{search_query}':")
#             for i, student in enumerate(found_students):
#                 print(f"Kết quả {i + 1}:")
#                 student.output()
#                 print("-" * 20)
#         else:
#             print(f"Không tìm thấy sinh viên nào với tên '{search_query}'.")
#     else:
#         print("Lớp học chưa có sinh viên nào để tìm kiếm.")
#
#     print("\n--- Kết thúc chương trình ---")
#
#
# if __name__ == "__main__":
#     main()
