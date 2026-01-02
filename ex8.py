#скрипт проверяет на ввод что введены только цифры и ищет медиану (если нечетное кол-во введено цифр - то показывает нечетный элемент, если четное - складывает 2 средних и делит на 2)
def contains_only_digit_strings(lst):
    return all(isinstance(item, str) and item.isdigit() for item in lst)

input_string = input("Введите числа через пробел: ")
list_of_chars = input_string.split()
count = len (list_of_chars) 

if contains_only_digit_strings(list_of_chars):
    sorted_list= sorted(list_of_chars, key=int)
    print(f"Отсортированный список  {sorted_list}")

    if count % 2 == 0:
       print(f"В списке четное кол-во чисел") 
       middle_count = int (count / 2) 
       a = int( list_of_chars[middle_count-1] )   # нумерация с 0 
       b = int( list_of_chars[middle_count] )
       mediana = int((a + b)/2) 
       print (f"{mediana}")
    else:
       print(f"Число нечетное кол-во чисел")
       medium_position = count // 2  # так как нумерация с нуля
       print (f"mediana:  {sorted_list[medium_position ]}" )
else: 
    print("В списке есть не цифры !!")
    
