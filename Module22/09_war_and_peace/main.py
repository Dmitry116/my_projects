# TODO здесь писать код
import zipfile


def unpacking_zip():
    archive = 'voyna-i-mir.zip'
    with zipfile.ZipFile(archive, 'r') as zip_file:
        zip_file.extractall()


def sort_symbol(text_file, sort_file):
    symbol_dict = {}
    for word in text_file:
        for symbol in word:
            if symbol.isalpha():
                if symbol in symbol_dict:
                    symbol_dict[symbol] += 1
                else:
                    symbol_dict[symbol] = 1

    sort_symbol = sorted(symbol_dict.items(), key=lambda x: ((x[0]), -1 * x[1]))
    for i_symbol in sort_symbol:
        print(i_symbol)
        sort_file.write(str(i_symbol))
        sort_file.write('\n')



unpacking_zip()
text_file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
sort_symbol_file = open('sort_file.txt', 'w', encoding='utf-8')
sort_symbol(text_file, sort_symbol_file)
text_file.close()
sort_symbol_file.close()