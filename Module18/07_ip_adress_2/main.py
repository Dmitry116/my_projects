# TODO здесь писать код
ip = input('Введите IP адрес: ')
ip_address = ip.split('.')

for ip_num in ip_address:

    if len(ip_address) < 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break

    elif not ip_num.isdigit():
        print(ip_num, ' — это не целое число.')
        break
    elif int(ip_num) > 255:
        print(ip_num, 'превышает 255.')
        break


else:
    print('IP-адрес корректен.')

