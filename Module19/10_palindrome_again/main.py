# TODO здесь писать код

#string = input('Введите строку: ')
#a = string
#for i in range(len(string)):
#    a = a[1:] + a[:1]
#    if a == a[::-1]:
#        print('Можно сделать палиндромом')
#        break
#    print('Нельзя сделать палиндромом')
#    break

#----------------------------------------------------------------------------------------
#Этот код из разбора.

def is_poly(string):
  char_dict = {}
  for i_sym in string:
    char_dict[i_sym] = char_dict.get(i_sym, 0) + 1

  odd_count = 0
  for i_value in char_dict.values():
    if i_value % 2 != 0:
      odd_count += 1

  return odd_count <= 1


my_string = input('Введите строку: ')
if is_poly(my_string):
  print('Можно сделать палиндромом')
else:
  print('Нельзя сделать палиндромом')