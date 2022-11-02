# TODO здесь писать код
def read_text(text_data):
    for text_str in text_data:
        text_list.append(text_str)


def reverse_text(text):
    for i_num in range(1, len(text_list) + 1):
        print(text[-i_num], end='')
        text_file_reverse.write(text[-i_num])


text_file = open('zen.txt', 'r')
text_file_reverse = open('reverse_text.txt', 'w')
text_list = []

read_text(text_file)
reverse_text(text_list)

text_file.close()
text_file_reverse.close()
