import string                             #нужен для работы со строками
stroka = input ("Введите строку:  ")
count_low=0
count_high=0
count_number=0
count_punkt=0     
punctuation_chars = string.punctuation     #содержит массив из символов пунктуации
for char in stroka:
    if char.isupper(): 
            count_high += 1
    else: 
         if char.islower():
            count_low += 1
         else:
             if char.isdigit():
                   count_number += 1
             else:
                   if char in punctuation_chars:
                         count_punkt += 1                  

print(f"low: {count_low} high: {count_high} number: {count_number} punkt: {count_punkt}")
