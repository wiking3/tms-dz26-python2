#скрипт запрашивает абсолютный путь к папке (проверяет сущесвует ли она) -если есть, сохраняет в список имена файлов 
#и делает поиск в именах файлов по ключевому слову  (которое ввел пользователь)
import os     # Импортируем модуль os для работы с файловой системой

def find_files_with_substring(file_list, substring):  # Находит файлы из списка, чьи имена содержат заданную подстроку.
    found_files = []                                  # Создаем пустой список для найденных файлов
    for file_path in file_list:
        file_name = os.path.basename(file_path)       # Получаем только имя файла из полного пути
        if substring.lower() in file_name.lower():    # Проверяем, есть ли подстрока в имени файла (без учета регистра для большей гибкости)
            found_files.append(file_name)             # Добавляем имя файла в список
    return found_files

dir_path = input("Укажите путь к папке где файлы (абсолютный путь): ")          #temp_dir = '/home/egorpc/python'

if os.path.isdir(dir_path):                                                     # Проверка, существует ли и является ли директорией 
    print(f"Директория '{dir_path}' существует.")
    search_term = input("Укажите ключевое слово для поиска в имени файлов: ")                      #слово для поиска в именах файлах в указанной директории search_term = "report"
    my_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path)]   # правильно формируем путь "для linux" - формируем список из имени файлов в указанной директории

    #print (f"Поиск будет среди файлов : \n")                              # выводим список файлов с абсолютными путями                        
    for item in my_files:
      print (f"{item}")   

    result = find_files_with_substring(my_files, search_term)              # Вызываем функцию поиска ключевого слова в имени файлов

    print(f"\n Файлы, содержащие в имени слово '{search_term}':")
    if result:                                                             # Если result не пустой - выводим име файла
       for file in result:
          print(f"- {file}")
    else:
        print("Файлы не найдены.")
else:
    print(f"Директории '{dir_path}' нет или это не папка.")
