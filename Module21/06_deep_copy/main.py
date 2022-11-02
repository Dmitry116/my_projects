import json
import copy


def site_phone():
    name_phone = input('Введите название продукта для нового сайта: ')
    name_site = f'Сайт для {name_phone}: '
    print(name_site)
    site = {
        'html': {
            'head': {
                'title': f'Куплю/продам {name_phone} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {name_phone}',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }
    get_file(site)


def get_file(site):
    data_sites.append(copy.deepcopy(site))
    print(json.dumps(data_sites, indent=3, ensure_ascii=False))


def site_numbers(number):
    site_phone()
    if number != 1:
        count_site = number - 1
        site_numbers(count_site)


data_sites = []
num_site = int(input('Сколько будет сайтов: '))
site_numbers(num_site)
