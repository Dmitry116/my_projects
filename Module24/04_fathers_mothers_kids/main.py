from parents import Parent
from children import Children
import random


def main():
    father = Parent('Bill', 32)
    child_1 = Children('Tom', 6)
    child_2 = Children('John', 3)
    father.add_child(child_1.name_child, child_1.year_child)
    father.add_child(child_2.name_child, child_2.year_child)
    father.print_info()

    kids = (child_1, child_2)

    for i_child in kids:
        num_mood = random.randint(0, 1)
        num_hunger = random.randint(0, 1)
        i_child.mood_child(num_mood)
        i_child.hunger_child(num_hunger)
        i_child.print_info()
        if num_mood == 0:
            father.play_with_child(i_child.name_child)
        elif num_mood == 1:
            i_child.mood_child(num_mood)

        if num_hunger == 0:
            father.feed_child(i_child.name_child)
        elif num_hunger == 0:
            father.feed_child(num_hunger)

        print()


main()
