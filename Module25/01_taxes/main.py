# TODO здесь писать код
class Property:

    def __init__(self, worth=0):
        self.worth = worth

    def get_tax_car(self):
        return self.worth / 200

    def get_tax_apartment(self):
        return self.worth / 1000

    def get_tax_countru_hounse(self):
        return self.worth / 500


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)


amount_money = int(input('Введите количество имеющихся денег: '))

worth_apartment = int(input('\nВведите стоимость квартиры: '))
apartment = Apartment(worth_apartment)
print(f'Налог на квартиру: {apartment.get_tax_apartment()}')

worth_car = int(input('\nВведите стоимость машины: '))
car = Car(worth_car)
print(f'Налог на автомобиль: {car.get_tax_car()}')

worth_country_house = int(input('\nВведите стоимость загородный дом: '))
country_house = CountryHouse(worth_country_house)
print(f'Налог на загородный дом: {country_house.get_tax_countru_hounse()}')

total_tax = apartment.get_tax_apartment() + car.get_tax_car() + country_house.get_tax_countru_hounse()
print(f'\nИтого налог на имущество составляет: {round(total_tax, 2)}')

if amount_money < total_tax:
    print(f'Нехватает денег для оплаты налога: {round((amount_money - total_tax), 2)}')