# """                                         
# Объектно ориентирование програмирование            
# """


# """
# Наследование и множественное наследование                             
# """





# class Game:
#     def __init__(self, game_name, graphics, game_year,company):
#         self.game_name = game_name
#         self.graphics = graphics
#         self.game_year = game_year
#         self.company = company

#     def info(self):
#         print(f'Название игры - {self.game_name}, Графика - {self.graphics}, Год релиза - {self.game_year}, Создатели - {self.company} ') #Мультиплеер - {self.multiplayer}
        
# game = Game('Counter-strike Global-Offensive', 'Full HD 4k', 2012, 'Valve')


# class Poblox(Game):
#     def __init__(self, game_name, graphics, game_year, company, multiplayer):
#         super().__init__(game_name, graphics, game_year, company)
#         self.multiplayer = multiplayer
#         self.name = 'Player'
#         self.gender = 'Man'
#         self.skin = 'Asia'
#         self.hp = 100
    
#     def info_player(self):
#         print(f'Игрок - {self.name}, Пол - {self.gender}, Скин - {self.skin}, Здоровье - {self.hp},')
#         print('=============================================================\n Roblox - start game!')
    
#     def edit_player(self):
#         name = input('Введите имя игрока: ')
#         gender = input('Введите пол игрока: ')
#         skin = input('Введите облик игрока: ')
        
#         self.name = name
#         self.gender = gender
#         self.skin = skin
        
# roblox = Poblox('Roblox', 'Ultra', 2006, 'Roblox Corporation', 'есть') 
     
# # game.info()
# roblox.info()
# roblox.info_player()
# roblox.edit_player()
     
        
# class Snake(Poblox):   
#     def __init__(self, name, gender, skin):
#         self.name = name
#         self.gender = gender
#         self.skin = skin
#         self.hp = 100
    
# snake = Snake('Бека',"Муж","Платиновый")
# snake.info_player()
# snake.edit_player()
        
        
# """
# class Poblox(Game):
#     def __init__(self, game_name, graphics, game_year, company):
#         Game.__init__(game_name, graphics, game_year, company)
# """



class Animal:
    def __init__(self, name):
     self.name = name
 
    def eat(self):
     print(f'{self.name} - ест')
     
    def sleep(self):
     print(f'{self.name} - спит ')
animal = Animal('Животное')

animal.eat()
animal.sleep()

class Walker(Animal): 
    def __init__(self, name):
      super().__init__(name)
      
    def walker(self):
          print(f"{self.name} - ходит")
animal = Walker('Животное')   
animal.walker()  

class Swimmer(Walker): 
    def __init__(self, name):
      super().__init__(name)
      
    def swimer(self):
          print(f"{self.name} - плавает")
          
animal = Swimmer('Рыба')          
animal.swimer()


class Flayer(Animal): 
    def __init__(self, name):
      super().__init__(name)
      
    def fly(self):
          print(f"{self.name} - летает")
animal = Flayer('Птица')          
animal.fly()          
          

class Bat(Swimmer): 
   def __init__(self, name):
      super().__init__(name)
      
   def default(self):
          print(f"{self.name} - умеет летать")
animal = Flayer('Летучая мышь умеет летать')          
animal.fly()          
          
