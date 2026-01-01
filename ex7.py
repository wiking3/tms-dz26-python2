#скрипт принимает 2 строки и сравнивает их посимвольно - и выводит общие символы
input_string1 = input("Введите первую строку: ")
input_string2 = input("Введите вторую строку: ")
len_string1 = len (input_string1)                 #находим длину 1й строки 
len_string2 = len (input_string2)                 #находим длину 2й строки

common_symbols=[]                                 #инициализируем общий пустой список
for x in range(0,len_string1):                    #сравниваем посимвольно
    for y in range(0,len_string2) :
        if input_string1[x] == input_string2[y] : 
             common_symbols.append(input_string1[x])

print(f"comon_symbols is {common_symbols}") 
