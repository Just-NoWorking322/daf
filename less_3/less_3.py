# """ ИНКАПУСЛЯЦИЯ """

# class Publicexample:
#     def __init__(self, value):
#         self.value = value
        
#     def info(self):
#         print( self.value )   


# public = Publicexample(42)

# public.info()
# public.value

# class Public_example:
#     def __init__(self, value):
#         self.value = value
        
#     def info(self):
#         return self.value  


# public = Public_example(42)

# print(public.value)
# print(public.info())



# class ProtecktedExample:
#     def __init__(self, value):
#         self._value = value #Защищенный атрибут 
        
#     def _info(self):
#         return self._value #Защищенный метов
    
    
# protected = ProtecktedExample(40)
# print(protected._info()) # Это работает, но это противоречит правилам инкапсуляции
# print(protected._value) # моэно получить значение на прямую но это не рекомендуется

# # ПРИВАТНЫЙ МЕТОД ИНКАПСУЛЯЦИИ

# class PrivateExample:
#     def __init__(self, value):
#         self.__value = value #ПРИВАТНЫЙ АРТИБУТ
#     def __info(self):
#         return self.__value #ПРИВАТНЫЙ МЕТОД
    # def accesss_private(self):
    #     return self.__info() #ПУБЛИЧНЫЙ МЕТОД ГДЕ МЫ ПОЛУЧАЕМ ДОСТУП К ПРИВАТНОМУ ЭлМЕНТ
    
# private = PrivateExample(300)


# print(private.__info())    
#ПРЯМОЙ ВЫЗОВ ПРИВАТНОГО МЕТОДА ВЫЗОВЕТ ОШИБКУ

# private(private.__value)
#ПРЯМОЙ ВЫЗОВ ПРИВАТНОГО АТРИБУТА ВЫЗОВЕТ ОШИБКУ

# print(private.accesss_private())
# ДОСТУП ЧЕРЕЗ ПУБЛИЧНЫЙ МЕТОД

# print(private._PrivateExample__value)
#Доступ к приватному методу через (Name mangling)


class MobileLegends:
    def __init__(self, person, rang, item, history):
        self.person = person
        self.rang = rang
        self._item = item
        self.__history = history
        
    # def player_info(self):
    #     print(f"Персонаж - {self.person},Ранг - {self.rang},Сумка - {self._item},История - {self.history},")
        
    def _item_player(self):
        person = input('Выберите героя: ')
        rang = input("ВЫберите ранг: ")
        bag = input("Введите предметы: ")
        self._item = bag 
        
    def __history_player(self):
        defeat = 160
        victory = 16 
        winrate = victory / defeat
        print(f'{winrate} %')
         
    def accesss_history_player(self):
        return self.__history_player
    
mobile =  MobileLegends("НАНА","Бронза", 'Облик','-6 звезд')

print(mobile._item_player())  
# mobile.player_info()  
print(mobile.access_history_player())
