# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

str_1 = 'AAAAaaaBBBBBB******'
counter = 1
lst = ""
for i in range (1, len(str_1)):    
    if str_1[i] == str_1[i-1]:
        counter += 1
    else:
        lst += (str_1[i-1] + str(counter))
        counter = 1
lst += (str_1[-1] + str(counter))
print(lst)

# расшифровка

for i in range (1, len(lst), 2):
    print(lst[i-1] * int(lst[i]), end = "")