'''
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

dividers = list(range(1,21))

for i in range(1000000,10000000000):
    count = 0
    for j in dividers:
        if i%j == 0:
            count += 1
    if count == 20:
        print(i)

#---------------------------------
# Проверка ответа
# dividers = list(range(1,21))
#x = 232_792_560
# for i in dividers:
#     print(f'{x} / {i} = {x/i}')


#--------------------------------
# Чужое решение
# x = 1
# status = True
# while status:
#     z = []
#     z = [i for i in range(1,21) if x%i == 0]
#     if len(z) == 20:
#         print(x)
#         status = False
#     x+=1
            


