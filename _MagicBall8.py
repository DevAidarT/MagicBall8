# Magic Ball 8
import random  # импортировали модуль random
'''
Функция для рандомного выбора значений из заданного диапазона (1-8) и вывода 
на основе значения различных фраз. В основу написания легла игрушка "Шар судьбы" 
или "Шар предсказаний".
'''


def get_answer(answer_number):  # функция
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Without a doubt'
    elif answer_number == 4:
        return 'As I see it, yes'
    elif answer_number == 5:
        return 'Most likely'
    elif answer_number == 6:
        return 'Outlook good'
    elif answer_number == 7:
        return 'Reply hazy, try again'
    elif answer_number == 8:
        return 'Ask again later'


r = random.randint(1, 8)
fortune = get_answer(r)
print('Your answer is: ' + fortune)

# or another variant
# print('Your answer is: ' + get_answer(random.randint(1, 8)))

# or another better variant
# import random
'''messages = ['It is certain', 'It is decidedly so', 'Without a doubt', 'As I see it, yes', 'Most likely', 
'Outlook good', 'Reply hazy, try again', 'Ask again later']
print(messages[random.randint(0, len(messages) - 1))])'''
