num = int(input('Сколько записей вносится в протокол? '))
participant_list = {}

for i_num in range(num):
    score, participant = input(f'{i_num + 1}-я запись: ').split()
    score = int(score)
    if participant in participant_list:
            if score > participant_list[participant][0]:
            	participant_list[participant][0] = score
            participant_list[participant][1] = i_num
    else:
        participant_list[participant] = [score, i_num]
        
sort_winners = sorted(participant_list.items(), key=lambda x: ((x[1][0]), -1 * x[1][1]), reverse=True)

for num in range(3):
	print(f'{num+1}-й победитель {sort_winners[num][0]} {sort_winners[num][1][0]}')
