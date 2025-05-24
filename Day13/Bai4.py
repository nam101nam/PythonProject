class Book:
    def __init__(self,price,title,author):
        self.price=price
        self.title=title
        self.author=author
class SoftCoverBook(Book):
    def __init__(self,price,title,author,discount):
        super().__init__(price,title,author)
        self._discount=discount
    def calculate_discount_price(self):
        return self.price*(100-self._discount)/100
class HardCoverBook(Book):
    def __init__(self,price,title,author,weigh):
        super().__init__(price,title,author)
        self._weigh=weigh
    def calculate_shipping_cost(self):
        return self._weigh*15000
class BookStore:
    def __init__(self):
        self._books=[]
    def add_book(self,book):
        self._books.append(book)
    def remove_book(self,book):
        self._books.remove(book)
    def total_revenu(self):
        revenu=0
        for book in self._books:
            if(isinstance(book,SoftCoverBook)):
                revenu+=book.calculate_discount_price()
            elif(isinstance(book,HardCoverBook)):
                revenu+=book.calculate_shipping_cost()+book.price
        return revenu
sachmem=SoftCoverBook(100000,'CauTrucDuLieu-GiaiThuat','Nam1',50)
sachcung=HardCoverBook(100000,'MangMayTinh','Nam2',10)
a=BookStore()
a.add_book(sachcung)
a.add_book(sachmem)
print(a.total_revenu())