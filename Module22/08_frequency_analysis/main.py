# TODO здесь писать код

def symbols_number(text_file):
    symbol_dict = {}
    count_symbol = 0
    for word in text_file:
        for symbol in word.lower():
            if symbol.isalpha():
                count_symbol += 1
                if symbol in symbol_dict:
                    symbol_dict[symbol] += 1
                else:
                    symbol_dict[symbol] = 1
    analysis(symbol_dict, count_symbol)


def analysis(symbol_dict, count_symbol):
    analysis_symbol = {}
    for key in symbol_dict:
        analysis_symbol[key] = round(symbol_dict[key] / count_symbol, 3)
    sorted_list(analysis_symbol)


def sorted_list(symbol_num):
    analysis_file = open('analysis.txt', 'w')
    sort_number = sorted(symbol_num.items(), key=lambda x: ((-1 * x[1]), x))
    for i_num in sort_number:
        print(*i_num)
        analysis_file.write(str(i_num))
        analysis_file.write('\n')
    analysis_file.close()


text_file = open('text.txt', 'r')
symbols_number(text_file)
text_file.close()

# Mama myla ramu.
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083
