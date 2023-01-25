# TODO здесь писать код
import random
from home import Home
from people import Husband, Wife, Child
from cats import Cats

apartment = Home()
apartment.print_info_home()

husband = Husband('Met', apartment)
husband.print_info_human()

wife = Wife('Emily', apartment)
wife.print_info_human()

child = Child('Ted', apartment)
child.print_info_human()

cat_Tom = Cats('Tom', apartment)
cat_Tom.print_info_cat()

cat_Butch = Cats('Butch', apartment)
cat_Butch.print_info_cat()

while apartment.GAME == True:

    apartment.COUNT_DAYS += 1
    print(f'День: {apartment.COUNT_DAYS}')
    #enter = input('Нажмите Enter чтобы продолжить')
    print()

    """Действие мужа"""

    husband.check_dirt()
    husband.choice = random.choice([husband.human_eating, husband.takes_cats,
                                    husband.plays_pc, husband.going_work])
    husband.choice()
    husband.print_info_human()
    husband.check_human_happy_satiety()
    apartment.print_info_home()

    """Действие Жены"""

    wife.check_dirt()
    wife.choice = random.choice([wife.human_eating, wife.takes_cats, wife.going_shop,
                                 wife.buy_fur_coat, wife.cleaning_home])
    wife.choice()
    wife.print_info_human()
    wife.check_human_happy_satiety()
    apartment.print_info_home()

    """Действие ребенка"""

    child.check_dirt()
    child.choice = random.choice([child.human_eating, child.takes_cats, child.going_school, child.walks])
    child.choice()
    child.print_info_human()
    child.check_human_happy_satiety()
    apartment.print_info_home()

    """Действие первого кота"""

    cat_Tom.check_cat_satiety()
    cat_Tom.choice = random.choice([cat_Tom.cat_eating, cat_Tom.sleeps,
                                    cat_Tom.runing_for_mouse, cat_Tom.bad_games ])
    cat_Tom.choice()
    cat_Tom.print_info_cat()
    apartment.print_info_home()

    """Действие второго кота"""

    cat_Butch.check_cat_satiety()
    cat_Butch.choice = random.choice([cat_Butch.cat_eating, cat_Butch.sleeps,
                                    cat_Butch.runing_for_mouse, cat_Butch.bad_games ])
    cat_Butch.choice()
    cat_Butch.print_info_cat()
    apartment.print_info_home()

    """Ежедневное загрязнение дома"""

    apartment.dirt_every_day()

print(f'Кол-во прожитых дней: {apartment.COUNT_DAYS}')
