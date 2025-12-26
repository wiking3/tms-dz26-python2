Работа с IP адресами
import ipaddress
>>> ipaddress.ip_address('192.0.2.1')    # IPv4Address('192.0.2.1')
>>> ipaddress.ip_address('2001:DB8::1')  # IPv6Address('2001:db8::1')
>>> ip_obj = ipaddress.ip_address(user_input)   #проверяем что это IP

Оба специфичных для модуля исключения имеют ValueError в качестве родительского класса, поэтому, если не беспокоит конкретный тип ошибки, все равно можно написать код, подобный следующему:
try:
    network = ipaddress.IPv4Network(address)
except ValueError:
    print('address/netmask is invalid for IPv4:', address)
    

https://docs-python.ru/standart-library/modul-ipaddress-python/

