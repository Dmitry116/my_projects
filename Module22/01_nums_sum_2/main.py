# TODO здесь писать код
def search_num(data):
    for i_num in data:
        for i in i_num:
            if i.isdigit():
                num_list.append(int(i))


num_file = open('numbers.txt', 'r')
answer = open('answer.txt', 'w')

num_list = []
search_num(num_file)
print('Сумма в файле: ', sum(num_list))
answer.write(str(sum(num_list)))
num_file.close()
answer.close()
