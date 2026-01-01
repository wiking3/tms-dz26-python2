# вводим 2 списка и скрипт ищет общие элементы в обоих введеных списках

input_string1 = input("Введите элементы списка 1 через пробел: ")
 my_list1 = input_string1.split()
input_string2 = input("Введите элементы списка 2 через пробел: ")
 my_list2 = input_string2.split()

print(f"Вы ввели список 1 : {my_list1}")
print(f"Вы ввели список 2 : {my_list2}")

temp_list2 = list(my_list2)   #создаем копию 2ого списка
common_elements = [] 


for item1 in my_list1:
    if item1 in temp_list2:
        common_elements.append(item1)
        temp_list2.remove(item1)      # Удаляем найденный элемент из временного списка, чтобы учесть дубликаты

print("Общие элементы (с учетом дубликатов):", common_elements)
