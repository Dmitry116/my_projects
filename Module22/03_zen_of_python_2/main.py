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
        for word_str in text_str.split():
            count_word += 1
    return count_word


text_list = []
text_file = open('zen.txt', 'r')
read_text(text_file)

print('Количество букв в файле: ', sum_symbol(text_list))
print('Количество слов в файле: ', sum_word(text_list))
print('Количество строк в файле: ', len(text_list))
print('Наиболее редкая буква: ')

text_file.close()
