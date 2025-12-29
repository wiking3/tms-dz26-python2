#скрипт пингует из списка IP, которые вводит пользователь  и записывает результат пинга в файл result.log 
import ipaddress      #нужен чтобы проверить что указанная строка - это ip
import subprocess     #нужен чтобы выполнить команду ping

def ping(host):
    result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE)
    return  host+' пингуется!' if result.returncode == 0 else host+' нет пинга!'


ip_list = []    #пустой список
count = input ("Input count of IP: ")
if count.isdigit() :
   count=int(count)
   while count>0:
     user_input = input("Введите IP-адрес: ")

     try:
        ip_obj = ipaddress.ip_address(user_input)  #проверяем что это IP
        ip_list.append(str(ip_obj)) # Добавляем как строку в список  
        print(f"IP-адрес {ip_obj} добавлен.")
     except ValueError:
        print(f"Ошибка: '{user_input}' не является корректным IP-адресом.")

     count-=1

with open('result.log', 'w'):              #очищаем файл
    pass


with open("result.log", "a") as file:      #открываем файл для дозаписи (append)

  for ip in ip_list:
     result=ping(ip)
     file.write(result+"\n")
