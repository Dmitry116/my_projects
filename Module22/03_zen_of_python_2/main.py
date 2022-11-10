# TODO здесь писать код


def read_text(text_data):
    for text_str in text_data:
        text_list.append(text_str)


def sum_symbol(file_data):
    count_symbol = 0
    for i_word in file_data:
        for symbol in i_word:
            if symbol.isalpha():
                count_symbol += 1
    return count_symbol


def sum_word(file_data):
    count_word = 0
    for text_str in file_data:
        count_word += len(text_str.split())
    return count_word


def rare_symbol(text):
    symbol_dict = {}
    for words in text:
        for symbol in words:
            if symbol.islower():
                if symbol in symbol_dict:
                    symbol_dict[symbol] += 1
                else:
                    symbol_dict[symbol] = 1
    sort_symbol = sorted(symbol_dict.items(), key=lambda x: ((x[1]), -1 * x[0]))
    return sort_symbol


text_list = []
text_file = open('zen.txt', 'r')
read_text(text_file)
symbol_dict = rare_symbol(text_list)

print('Количество букв в файле: ', sum_symbol(text_list))
print('Количество слов в файле: ', sum_word(text_list))
print('Количество строк в файле: ', len(text_list))
print('Наиболее редкая буква: ', *symbol_dict[0][0])

text_file.close()
