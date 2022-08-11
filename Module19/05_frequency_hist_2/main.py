# TODO здесь писать код

text = input('Введите текст: ')
text_dict = {}
second_text_dict = {}

print('Оригинальный словарь частот: ')
for symbol in text:
    if symbol in text_dict:
        text_dict[symbol] += 1
    else:
        text_dict[symbol] = 1

for i_key, i_value in text_dict.items():
    print(i_key, ':', i_value)

for i_letter, i_num in text_dict.items():
    second_text_dict.setdefault(i_num, []).append(i_letter)
print()
print('Инвертированный словарь частот:')
for i in second_text_dict:
    print(i, ':', second_text_dict[i])


