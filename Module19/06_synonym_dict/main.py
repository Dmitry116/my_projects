# TODO здесь писать код

number = int(input('Введите количество пар слов: '))
text = {}
for i_num in range(number):
    two_words = input(f'{i_num+1}-я пара: ').split()
    text[two_words[0]] = two_words[1]
    text[two_words[1]] = two_words[0]

word = input('Введите слово: ')

if word in text:
    print('Синоним: ', text[word])
else:
    print('Такого слова в словаре нет.')


#Привет Здравствуйте
#Печально Грустно
#Весело Радостно