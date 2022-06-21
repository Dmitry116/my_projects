shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count_detail = 0
total_price = 0
detail = input('Название детали: ')
count = 0

for i in shop:
    if detail in i:
        total_price += shop[count][1]
        count_detail += 1
    count += 1

print('Кол-во деталей — ', count_detail)

print('Общая стоимость — ', total_price)


# TODO здесь писать код
