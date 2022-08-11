goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for goods_name, goods_code in goods.items():
    total_price = 0
    total_product = 0
    for i_store in store[goods_code]:
        total_product += i_store['quantity']
        total_price += i_store['quantity'] * i_store['price']

    print(goods_name, ' - ', total_product, 'стоимостью', total_price , 'рубля')

# TODO здесь писать код

