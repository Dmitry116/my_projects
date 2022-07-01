# TODO здесь писать код
import random

team_1 = [round(float(random.uniform(0.0,9.99)), 2) for i in range(10)]
team_2 = [round(float(random.uniform(0.0,9.99)), 2) for i in range(10)]
winners = [(team_1[id] if team_1[id] > team_2[id] else team_2[id]) for id in range(10)]

print('Первая команда: ', team_1)
print('Вторая команда: ', team_2)
print('Победители тура: ',winners )
