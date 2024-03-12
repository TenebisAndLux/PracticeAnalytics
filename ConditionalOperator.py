# A
# name = input('Как Вас зовут?\n')
# print(f'Здравствуйте, {name}!')
# question = input('Как дела?\n')
# match question:
#     case 'хорошо':
#         print('Я за вас рада!\n')
#     case 'плохо':
#         print('Всё наладится!\n')
###############################
# B
# Petia = int(input())
# Vasia = int(input())
# res = 'Петя' if Petia > Vasia else 'Вася'
# print(f'{res}')
###############################
# C
# Petia = int(input())
# Vasia = int(input())
# Tolia = int(input())
# if Petia > Vasia:
#     if Petia > Tolia:
#         print('Петя')
#     else:
#         print('Толя')
# else:
#     if Vasia > Tolia:
#         print('Вася')
#     else:
#         print('Толя')
###############################
# D
# Petia = int(input())
# Vasia = int(input())
# Tolia = int(input())
# if Petia > Vasia:
#     if Petia < Tolia:
#         print('1. Толя \n2. Петя \n3. Вася')
#     elif Vasia > Tolia:
#         print('1. Петя \n2. Вася \n3. Толя')
#     else:
#         print('1. Петя \n2. Толя \n3. Вася')
# else:
#     if Vasia < Tolia:
#         print('1. Толя \n2. Вася \n3. Петя')
#     elif Petia > Tolia:
#         print('1. Вася \n2. Петя \n3. Толя')
#     else:
#         print('1. Вася \n2. Толя \n3. Петя')
###############################
# Petia = int(input())
# Vasia = int(input())
# Tolia = int(input())
#
# players = {'Петя': Petia, 'Вася': Vasia, 'Толя': Tolia}
#
# sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
#
# for i, (name, score) in enumerate(sorted_players, start=1):
#     print(f'{i}. {name}')
###############################
# E
# Petia = 7 - 3 + 2
# Vasia = 6 + 3
# N = int(input())
# M = int(input())
# print('Петя') if Petia + N > Vasia + M else print('Вася')
###############################
# F
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return "YES"
#     else:
#         return "NO"
#
#
# year = int(input())
# result = is_leap_year(year)
#
# print(result)
###############################
# G
# str = input()
# print("YES") if str == str[::-1] else print("NO")
###############################
# H
# str = input()
# print("YES") if 'зайка' in str else print("NO")
###############################
# I
# name_1 = (input())
# name_2 = (input())
# name_3 = (input())
#
# res = name_1 if name_1[0] < name_2[0] else (name_2 if name_2[0] < name_3[0] else name_3)
# print(f'{res}')
###############################
# name_1 = input()
# name_2 = input()
# name_3 = input()
#
# names = [name_1, name_2, name_3]
# names.sort()
#
# print(names[0])
###############################
# J
# num = (input())
# sum_1 = int(num[-1]) + int(num[-2])
# sum_2 = int(num[0]) + int(num[1])
# res = str(sum_1) + str(sum_2) if sum_1 > sum_2 else str(sum_2) + str(sum_1)
# print(res)
###############################
# K
# def is_beautiful_number(number):
#     digits = [int(digit) for digit in str(number)]
#     min_digit = min(digits)
#     max_digit = max(digits)
#     if (min_digit + max_digit) == (sum(digits) - min_digit - max_digit) * 2:
#         return "YES"
#     else:
#         return "NO"
#
#
# number = int(input())
# result = is_beautiful_number(number)
# print(result)
###############################
# L
# a + b > c, a + c > b и b + c > a
# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print('YES')
# else:
#     print('NO')
###############################
# M
# def find_common_digit(elf_number, gnome_number, human_number):
#     elf_str = str(elf_number)
#     gnome_str = str(gnome_number)
#     human_str = str(human_number)
#     for i in range(len(elf_str)):
#         if elf_str[i] == gnome_str[i] == human_str[i]:
#             return int(elf_str[i])
#
#
# elf_number = int(input())
# gnome_number = int(input())
# human_number = int(input())
# result = find_common_digit(elf_number, gnome_number, human_number)
# print(result)
###############################
# N
# def split_number(number):
#     number_str = str(number)
#     digits = list(map(int, number_str))
#     digits.sort()
#     if digits[0] == 0:
#         min_number = str(digits[1]) + str(digits[0])
#     else:
#         min_number = str(digits[0]) + str(digits[1])
#     max_number = str(digits[2]) + str(digits[1])
#     return min_number, max_number
#
#
# input_number = int(input())
# min_split, max_split = split_number(input_number)
# print(min_split, max_split)
###############################
# O
# z1 = input()
# z2 = input()
#
# max_digit = str(max(int(x) for x in z1 + z2))
# min_digit = str(min(int(x) for x in z1 + z2))
# sum_digits = sum(int(x) for x in z1 + z2) - int(max_digit) - int(min_digit)
#
# magic_number = max_digit + str(sum_digits)[-1] + min_digit
# print(magic_number)
###############################
# P
# speed_petya = float(input())
# speed_vasya = float(input())
# speed_tolya = float(input())
#
# racers = [("Петя", speed_petya), ("Вася", speed_vasya), ("Толя", speed_tolya)]
# racers.sort(key=lambda x: x[1], reverse=True)
# for i, (name, _) in enumerate(racers):
#     if i == 0:
#         print(' ' * 10, f"{name}")
#     elif i == 1:
#         print(' ' * 2, f"{name}")
#     else:
#         print(' ' * 18, f"{name}")
# print(' ' * 3, 'II', ' ' * 6, 'I', ' ' * 6, 'III', ' ' * 3)
###############################
# Q
# import math
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("Infinite solutions")
#         else:
#             print("No solution")
#     else:
#         x = -c / b
#         print("{:.2f}".format(x))
# else:
#     D = b ** 2 - 4 * a * c
#     if D < 0:
#         print("No solution")
#     elif D == 0:
#         x = -b / (2 * a)
#         print("{:.2f}".format(x))
#     else:
#         x1 = (-b + math.sqrt(D)) / (2 * a)
#         x2 = (-b - math.sqrt(D)) / (2 * a)
#         print("{:.2f} {:.2f}".format(min(x1, x2), max(x1, x2)))
###############################
# R
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
#     print("100%")
# elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or a ** 2 + c ** 2 < b ** 2:
#     print("велика")
# else:
#     print("крайне мала")
###############################
# S
# x = float(input())
# y = float(input())
#
# if (x >= 0) and (y >= 0) and x ** 2 + y ** 2 <= 25:
#     print("Опасность! Покиньте зону как можно скорее!")
# elif (y <= 0) and (x / 2 + 0.5) ** 2 - 9 < y:
#     print("Опасность! Покиньте зону как можно скорее!")
# elif (x <= 0) and (y >= 0) and y <= 5 and (10 * (7 - 5) - 5 * x + 4 * 7) <= 0:
#     print("Опасность! Покиньте зону как можно скорее!")
# elif x ** 2 + y ** 2 <= 100:
#     print("Зона безопасна. Продолжайте работу.")
# else:
#     print("Вы вышли в море и рискуете быть съеденным акулой!")
###############################
# T
road = [input() for _ in range(3)]

found = False
lenMAX = 'яяяяяяяяя'
result = ""

for line in road:
    if "зайка" in line:
        found = True
        if line.split(' ')[0] < lenMAX:
            lenMAX = line.split(' ')[0]
            result = line

if found:
    print(result, len(result))
else:
    print("Зайки не найдено")
###############################
