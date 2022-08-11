# TODO здесь писать код
def get_input_parameters():

    country_list = {}
    number = int(input('Сколько стран: '))
    for i_num in range(number):
        country = input(f'Введите {i_num+1}-ю страну: ').split()

        for i_country in country[1:]:
            country_list[i_country] = [country[0]]

    print()
    return country_list


def search_city():
    for i_num_city in range(3):
        city = input(f'{i_num_city+1}-й город: ')

        display_result(country_list, city)


def display_result(country_list, city):
    if city in country_list:
        print(f'Город {city} расположен в стране {str(country_list[city])}.')
    else:
        print(f'По городу {city} данных нет.')
    print()


country_list = get_input_parameters()
search_city()

