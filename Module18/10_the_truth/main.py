# TODO здесь писать код

abc_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

first_text = ''
for symbol in text:
    if symbol in abc_list:
        a = (abc_list.index(symbol) - 1) % len(abc_list)
        first_text += abc_list[a]
    else:
        first_text += symbol

second_text = first_text.split()

last_text = []
shift = 3
for word in second_text:
    word = word[-shift % len(word):]+word[:-shift % len(word)]
    if '/' in word:
        shift += 1
        last_text.append(word)
    else:
        last_text.append(word)

last_text = ' '.join(last_text)
last_text = last_text.replace('(', '`')
last_text = last_text.replace('+', '*')
last_text = last_text.replace('-', ',')
last_text = last_text.replace('"', '!')
last_text = last_text.replace('..', '--')
last_text = last_text.replace('/', '.\n')
print(last_text)








