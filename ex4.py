#вводится строка цифр + проверка на не-число(если строку ввели) и сортируется по убыванию массив
def safe_convert(s):             #фунция конвертер строк в цифры с проверкой на не-число при введении данных
    try:
        return int(s)
    except ValueError:
        return None


input_string = input("Введите элементы строки через пробел: ")
string_list = input_string.split()           # Разбиваем строку по пробелам, получая список строк
array_str=[]                          # инициализируем массив для строк  


array_str = list(map(safe_convert, string_list))  # Преобразуем каждую строку в целое число и создаем список, map - аналог for применяется ко всем элементами строки

number_array_int=[]            # инициализируем массив чисел для сортировки         
for item in array_str:         # чистим массив от None  - если на первичном вводе ввели строку вместо цифр
    if item is not None:
        number_array_int.append(item)

print (f"до сортировки {number_array_int}")
number_array_int.sort(reverse=True)                # сортируем массив по убыванию 
print(f"Отсортированный список: {number_array_int}")
