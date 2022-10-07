def inter_value():

    string = 'abcd'
    numbers =  (10, 20, 30, 40)
    str_list = [i_num for i_num in string]
    value_zip = zip(str_list, numbers)
    return value_zip


def display_result(value_zip):

    for i_value in value_zip:
        print(i_value)


value = inter_value()
display_result(value)