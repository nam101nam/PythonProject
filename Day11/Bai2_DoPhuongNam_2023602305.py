class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
class SoftCoverBook(Book):
    def __init__(self,title,author,price,discount):
        super().__init__(title,author,price)
        self.discount=discount
    def getter_dis(self):
        return self.discount
    def setter_dis(self,value):
        self.discount=value
    def calculate_discounted_price(self):
        return float(self.price-(self.price*self.discount)/100)
class HardCoverBook(Book):
    def __init__(self,title,author,price,weight):
        super().__init__(title,author,price)
        self.weight=weight
    def calculate_shipping_cost(self):
        return float(self.weight*15000)
class BookStore:
    def __init__(self,books):
        self.books=books
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,book):
        self.books.remove(book)
    def total_revenue(self):
        total=0
        for book in self.books:
            if isinstance(book,SoftCoverBook):
                total+=book.calculate_discounted_price()
            else:
                total+=book.calculate_shipping_cost()
        return total
softbook1=SoftCoverBook("Sách 1",'Tác giả 1',1000,10)
hardbook1=HardCoverBook('Sách 2','Tác giả 2',1000,1)
books=[softbook1,hardbook1]
a=BookStore(books)
print('Tổng tiền trước cập nhập=',a.total_revenue())
softbook1.setter_dis(20)
print('Discount sau khi cập nhập',softbook1.getter_dis())
print('Tổng tiền sau cập nhập=',a.total_revenue())