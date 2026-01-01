#скрипт получает строку (элементы,разделенные пробелом) - преобразует в кортеж и проверяет на уникальность все элементы кортежа

def are_elements_unique_loop(my_tuple):     # функция проверяет, все ли элементы в кортеже уникальны, используя цикл
  seen = []
  for element in my_tuple:
    if element in seen:
      return False                          # Найден дубликат
    seen.append(element)
  return True                               # Дубликатов не найдено

input_string = input("Введите символы, разделенные пробелом: ")
list_of_chars = input_string.split()
char_tuple = tuple(list_of_chars)           #Преобразуем список в кортеж


if are_elements_unique_loop(char_tuple)==False :          #вызываем функцию на "уникальность кортежа" и проверяем ее результат
   print ("Кортеж не уникален - есть повторяющиеся символы")
else : 
   print ("Все символы в кортеже  уникалены")
