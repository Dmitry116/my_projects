import json
def site_phone():
    name_phone = input('Введите название продукта для нового сайта: ')
    print(f'Сайт для {name_phone}: ')
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
    print(json.dumps(site, indent=3, ensure_ascii=False))


def site_numbers(number):
    site_phone()
    if number != 1:
        a = number - 1
        site_numbers(a)


num_site = int(input('Сколько будет сайтов: '))
site_numbers(num_site)