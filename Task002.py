# Крестики-нолики

def correct_move(move, cell_test): # проверка правильности указания координат хода
    if len(move) != 2: 
        return False      
    elif not move[0].isdigit() and not move[1].isdigit(): 
        return False
    elif isinstance(move[0], float) == True  or isinstance(move[1], float) == True: 
        return False
    elif int(move[0]) < 0 or int(move[0]) > 2: 
        return False
    elif int(move[1]) < 0 or int(move[1]) > 2: 
        return False
    elif cell_test[int(move[0])][int(move[1])] != '*': 
        return False 
    else:
        return True


def print_cell(lst): # функция печати ячеек
    for i in lst:
        for j in i:
            print(j, end=" ")
        print()    


def check_end (cell_test): # проверка на выигрыш
    if cell_test[0][0] == cell_test[1][1] == cell_test[2][2] and cell_test[0][0] != "*": return True
    elif cell_test[2][0] == cell_test[1][1] == cell_test[0][2] and cell_test[2][0] != "*": return True
    elif cell_test[0][0] == cell_test[0][1] == cell_test[0][2] and cell_test[0][0] != "*": return True
    elif cell_test[1][0] == cell_test[1][1] == cell_test[1][2] and cell_test[1][0] != "*": return True
    elif cell_test[2][0] == cell_test[2][1] == cell_test[2][2] and cell_test[2][0] != "*": return True
    elif cell_test[0][0] == cell_test[1][0] == cell_test[2][0] and cell_test[0][0] != "*": return True
    elif cell_test[1][0] == cell_test[1][1] == cell_test[2][1] and cell_test[1][0] != "*": return True    
    elif cell_test[2][0] == cell_test[2][1] == cell_test[2][2] and cell_test[2][0] != "*": return True
    else: 
        return False
    



counter = 0

while True:
    print_cell(cell)
    while True:
        player_1 = input("Первый игрок - ведите координаты хода через пробел - строку и столбец: ").split()
        if correct_move(player_1, cell):
            break
        else:
            print('Неверный ввод!')        
    cell[int(player_1[0])][int(player_1[1])] = 1
    print_cell(cell)

    if check_end(cell) == True:
        counter += 1
        break
    while True:
        player_2 = input("Второй игрок - ведите координаты хода через пробел - строку и столбец: ").split()
        if correct_move(player_2, cell):
            break
        else:
            print('Неверный ввод!')    
    cell[int(player_2[0])][int(player_2[1])] = 2

    if check_end(cell) == True: break

if counter == 0:
    print("Ура! Победил ВТОРОЙ игрок!")
else:
    print("Ура! Победил ПЕРВЫЙ игрок!")
print_cell(cell)