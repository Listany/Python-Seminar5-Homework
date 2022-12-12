# ИГРА ПРОТИВ УМНОГО БОТА
from random import randint

def correct_cand(x, y):
    if 0 < x < 29 and x <= y:
        return True
    else:
        return False



cand = 100
counter = 0
player_1 = 0
player_2 = 0
print(f"На столе всего {cand} конфет, начинаем игру!")

while cand > 0:
    
    player_1=int(input(f"Введите количество конфет для хода ПЕРВОГО игрока от 1 до 28 штук, на столе {cand} конфет: "))  
    while correct_cand(player_1, cand) == False:
        player_1=int(input(f"Неверное количество, попробуйте еще раз! На столе {cand} конфет: "))
        
        
    cand -= player_1
    print(f"На столе осталось {cand} конфет")
    counter +=1
    
    if cand == 0:
        break     
    
    
    if cand % 29 != 0:        
        player_2 = (cand) % 29
    else:
        player_2 = (29 - player_1)
    
            
    print(f"Второй игрок сделал ход на: {player_2} конфет")
    
    
    cand -= player_2
    print(f"На столе осталось {cand} конфет")
    counter +=1    
   
if counter % 2 == 0:
    print("Выиграл второй игрок! Поздравляем! ")
else:
    print("Выиграл первый игрок! Поздравляем! ")     

