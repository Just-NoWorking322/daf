"""ОБъектно ориентирование програмирование"""


full_name = 'Алишер' #Змеиный регистр

FullName = 'Жибек'   #Верблюживый регистр

class Car: # Шаблон или же чертёж  
    def __init__(self, model, marka, color): #__init__ (магический метод) конструктор
        #Атрибут объекта
        self.marka = marka
        self.model = model # self (ссылка на текущий объект)
        self.color = color 
        #Атрибут класса
        self.bak = 10
        self.is_start = False
        
        
    def info(self):
        print(f'Марка машины - {self.marka}, Модель машины - {self.model}, Цвет машины - {self.color}')
    
    def start(self):
        if self.bak > 0:
            self.is_start = True
            print(f'Машина {self.marka} - {self.model} заведена')
        else:
            print(f'Машина {self.marka} - {self.model} нет топлива')
            
    def stop(self):
         self.is_start = False
         print(F"Мотор {self.marka} - {self.model} заглушён")
    def drive(self,city):
        if self.is_start == True:
            print(F"Машина {self.marka} - {self.model} едет в {city}")
        else:
            print(f'Машина {self.marka} - {self.model} не заведена')

bmw = Car('BMW','m5 f90','black')


bmw.info()    
bmw.start()
bmw.drive('Дубай')
bmw.stop()

class Book:   
    def __init__(self, author, book_name, year):
        self.author = author
        self.book_name = book_name
        self.year = year
        
    def info(self):
        print( f"Author: {self.author}, Book Name: {self.book_name}, Year: {self.year}")
     
kniga = Book('Борис Акунин', 'Статский Советник', 1891)

kniga.info()
