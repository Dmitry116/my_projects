# TODO здесь писать код

def get_input_parameters():
    order_dict = {}
    num = int(input('Введите количество заказов: '))
    for i in range(1, num+1):
        order = input(f'Введите {i}-й заказ: ')
        client, pizza, number = order.split()
        number = int(number)

        if client not in order_dict:
            order_dict[client] = {pizza: number}
        else:
            if pizza in order_dict[client]:
                order_dict[client][pizza] += number
            else:
                order_dict[client][pizza] = number

    return order_dict

def order_clients(order_dict):

    for name_client, pizza in order_dict.items():
        print(f'{name_client}:')
        for name_pizza, count_pizza in sorted(pizza.items()):
            print(f'\t{name_pizza}: {count_pizza}')



number = get_input_parameters()
order_clients(number)





