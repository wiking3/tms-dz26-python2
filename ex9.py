#скрипт принимает строку и в ней меняет гласные на символ - 
def replace_symbols(text):
    nabor_symbols = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU'
    new_text = text                              # формируем новую строку
    for symbol in  nabor_symbols  :
        new_text = new_text.replace(symbol, '-') # Используем метод replace() для замены в строке
    return new_text

input_string = input("Введите строку: ")
result = replace_symbols(input_string)           #запускаем функцию  по замене символов
print(result) 
