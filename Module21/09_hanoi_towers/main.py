# TODO здесь писать код

def hanoi_tower(num, tow_1=1, tow_3=3):
    if num <= 0:
        return
    tow_2 = 6 - tow_1 - tow_3
    hanoi_tower(num-1, tow_1, tow_2)
    print('перенсти диск ', num, 'со стержня ', tow_1, 'на стержень ', tow_3)
    hanoi_tower(num-1, tow_2, tow_3)


num_disk = int(input('Сколько дисков в башне: '))
hanoi_tower(num_disk)