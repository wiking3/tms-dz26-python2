#скрипт ищет уникальные элементы в двух введенных строчках и выводит их

input_string1 = input("Введите 1й список через пробел: ")
list_of_chars1 = input_string1.split()                            
input_string2 = input("Введите 2й список через пробел: ")
list_of_chars2 = input_string2.split()

universal_symbols=[]
sym1=[]
sym2=[]
for x in range(0,len(list_of_chars1)): 
    universal_symbols.insert(len(list_of_chars1),list_of_chars1[x])
    for y in range(0,len(list_of_chars2)) :
        sym1=list_of_chars1[x]
        sym2=list_of_chars2[y]
        if list_of_chars1[x]==list_of_chars2[y] : universal_symbols.remove(sym2)


print (f"{universal_symbols}")
