###############################
# C
# inp = input()
# print(f'{inp} \n' * 3)
###############################
# D
# paid = input()
# print(f'{int(float(paid) - 2.5 * 38)}')
###############################
# E
# price = input()
# weight = input()
# paid = input()
# print(f'{int(float(paid) - float(price) * float(weight))}')
###############################
# F
# name = input()
# price = input()
# weight = input()
# paid = input()
# print('Чек')
# print(f'{name} - {weight}кг - {price}руб/кг')
# print(f'Итого: {int(float(price) * float(weight))}руб')
# print(f'Внесено: {paid}руб')
# print(f'Сдача: {int(float(paid) - float(price) * float(weight))}руб')
###############################
# G
# n = input()
# inp = "Купи слона!"
# print(f'{inp} \n' * int(n))
###############################
# H
# n = input()
# inp = input()
# print(f'Я больше никогда не буду писать "{inp}"! \n' * int(n))
###############################
# I
# N = int(input())
# M = int(input())
# print(f'{int((N * M) / 2)} ')
###############################
# J
# name = input()
# number = input()
# print(f'Группа №{number[0]}.')
# print(f'{number[2]}. {name}.')
# print(f'Шкафчик: {number}.')
# print(f'Кроватка: {number[1]}.')
###############################
# K
# number = input()
# print(number[1] + number[0] + number[3] + number[2])
###############################
# # L
# num1 = (input())
# num2 = (input())
# len1 = len(num1)
# len2 = len(num2)
# last_digit = ((int(num1[len1 - 1]) if len1 > 0 else 0) + (int(num2[len2 - 1]) if len2 > 0 else 0)) % 10
# carry_over = ((int(num1[len1 - 2]) if len1 > 1 else 0) + (int(num2[len2 - 2]) if len2 > 1 else 0)) % 10
# tens_sum = ((int(num1[len1 - 3]) if len1 > 2 else 0) + (int(num2[len2 - 3]) if len2 > 2 else 0)) % 10
# res = tens_sum * 100 + carry_over * 10 + last_digit
# print(f"{res}")
# M
children = int(input())
candies = int(input())
candies_per_child = candies // children
remaining_candies = candies % children
print(candies_per_child)
print(remaining_candies)
