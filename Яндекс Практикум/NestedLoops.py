# A
# n = int(input())
# resstr = ""
# for i in range(1, n + 1):
#     resstr = " ".join(str(i * j) for j in range(1, n + 1))
#     print(f'{resstr}')
#     resstr = ""
# B
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f'{j} * {i} = {i * j}')
# C
# def build_math_tree(n):
#     current_num = 1
#     row = 1
#
#     while current_num <= n:
#         for i in range(row):
#             print(current_num, end=" ")
#             current_num += 1
#             if current_num > n:
#                 break
#         print()
#         row += 1
#
#
# n = int(input())
# build_math_tree(n)
# D
# def sum_of_digits(n):
#     total_sum = 0
#
#     for _ in range(n):
#         num = int(input())
#         while num > 0:
#             total_sum += num % 10
#             num //= 10
#
#     print(total_sum)
#
#
# n = int(input())
# sum_of_digits(n)
# E
# def count_zayka(n):
#     count = 0
#
#     for _ in range(n):
#         found_zayka = False
#         while True:
#             line = input()
#             if line == 'ВСЁ':
#                 break
#             if 'зайка' in line:
#                 found_zayka = True
#
#         if found_zayka:
#             count += 1
#
#     print(count)
#
#
# n = int(input())
# count_zayka(n)
# F
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# def find_gcd(numbers):
#     result = numbers[0]
#     for num in numbers[1:]:
#         result = gcd(result, num)
#     return result
#
#
# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# print(find_gcd(numbers))
# # G
# num_racers = int(input())
#
# for i in range(3, num_racers + 3):
#     for j in range(i):
#         print(f"До старта {i - j} секунд(ы)")
#     print(f"Старт {i - 2}!!!")
# H
# def sum_of_digits(num):
#     return sum(int(digit) for digit in num)
#
#
# num_children = int(input())
# max_sum = 0
# winner = ""
#
# for _ in range(num_children):
#     name = input()
#     number = input()
#     current_sum = sum_of_digits(number)
#     if current_sum >= max_sum:
#         max_sum = current_sum
#         winner = name
#
# print(winner)
# I
# def build_largest_number(numbers):
#     largest_number = ""
#     for num in numbers:
#         max_digit = ""
#         for digit in num:
#             if digit > max_digit:
#                 max_digit = digit
#         largest_number += max_digit
#     return largest_number
#
#
# num_children = int(input())
# numbers = []
# for _ in range(num_children):
#     numbers.append(input().strip())
#
# result = build_largest_number(numbers)
# print(result)
# J
# def split_orange(num_segments):
#     ways = []
#     for a in range(1, num_segments):
#         for b in range(1, num_segments - a):
#             c = num_segments - a - b
#             ways.append((a, b, c))
#     return ways
#
#
# num_segments = int(input())
# ways = split_orange(num_segments)
#
# print("А Б В")
# for way in ways:
#     print(" ".join(map(str, way)))
#
# Функция map() в Python позволяет применить указанную функцию к каждому
# элементу входного итерируемого объекта (например, списку)
# и вернуть новый итератор с результатами.
# Синтаксис функции map() выглядит следующим образом:
# map(function, iterable)
# - function - функция, которую нужно применить к каждому элементу
# входного итерируемого объекта.
# - iterable - итерируемый объект (например, список, кортеж, строка),
# элементы которого будут передаваться в функцию.
# Пример использования map():
# # Пример 1: Применение функции к списку
# def square(x):
#     return x ** 2
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]
#
# # Пример 2: Применение встроенной функции к списку
# names = ["Alice", "Bob", "Charlie"]
# uppercase_names = list(map(str.upper, names))
# print(uppercase_names)  # Вывод: ['ALICE', 'BOB', 'CHARLIE']
#
# # Пример 3: Использование map с lambda-функцией
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]
# K
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# N = int(input())
# count_primes = 0
#
# for _ in range(N):
#     number = int(input())
#     if is_prime(number):
#         count_primes += 1
#
# print(count_primes)
# L
# rows = int(input())
# cols = int(input())
# len = len(str(rows * cols))
#
# start = 1
# for i in range(rows):
#     for j in range(cols):
#         print(f'{start:{len}}', end=" ")
#         start += 1
#     print()
# M
# rows = int(input())
# cols = int(input())
# len = len(str(rows * cols))
#
# for i in range(rows):
#     for j in range(cols):
#         print(f'{(i + 1 + j * rows):{len}}', end=" ")
#     print()
# N
# rows = int(input())
# cols = int(input())
# len = len(str(rows * cols))
#
# for i in range(rows):
#     for j in range(cols):
#         if i % 2 == 0:
#             print(f'{(i * cols + j + 1):{len}}', end=" ")
#         else:
#             print(f'{(i * cols + cols - j):{len}}', end=" ")
#     print()
# O
# rows = int(input())
# cols = int(input())
# len = len(str(rows * cols))
#
# for i in range(rows):
#     for j in range(cols):
#         if j % 2 == 0:
#             print(f'{(i + 1 + j * rows):{len}}', end=" ")
#         else:
#             print(f'{(-i + j * rows + rows):{len}}', end=" ")
#     print()
# P
# rows = int(input())
# cols = int(input())
# col_width = cols
# string_length = rows * col_width + (rows - 1)
#
# for i in range(1, rows + 1):
#     for j in range(1, cols + 1):
#         result = i * j
#         print(f'{result:^{col_width}}', end='|' if j < cols else '\n')
#     if i < rows:
#         print('-' * string_length)
#
# size = int(input())
# ceil_width = int(input())
#
# string_length = size * ceil_width + (size - 1)
#
# for row in range(size):
#     for column in range(size):
#         print(f'{((row + 1) * (column + 1)): ^{ceil_width}}', end='')
#         if column == size - 1:
#             print()
#         else:
#             print('|', end='')
#     if row + 1 != size:
#         print('-' * string_length)
# Q
# count = 0
#
# for _ in range(int(input())):
#     number = int(input())
#     original_num = number
#     reversed_num = 0
#
#     while number > 0:
#         digit = number % 10
#         reversed_num = reversed_num * 10 + digit
#         number //= 10
#
#     if original_num == reversed_num:
#         count += 1
#
# print(count)
# R
# limit = int(input())
#
# counter = 0
# width = 1
# max_length = 0
#
# while counter <= limit:
#     string_length = 0
#     for position in range(width):
#         counter += 1
#         if counter <= limit:
#             string_length += len(str(counter))
#         if position < width - 1 and counter < limit:
#             string_length += 1
#
#     if max_length < string_length:
#         max_length = string_length
#
#     width += 1
#
# counter = 0
# width = 1
#
# while counter <= limit:
#     string = ''
#     for position in range(width):
#         counter += 1
#         if counter <= limit:
#             string += str(counter)
#         if position < width - 1 and counter < limit:
#             string += ' '
#     width += 1
#     print(f'{string:^{max_length}}')
#
# def draw_tree(num):
#     width = len(str(num))
#     current = 1
#     level = 1
#     while current <= num:
#         line = ""
#         for _ in range(level):
#             if current <= num:
#                 line += f"{current} "
#                 current += 1
#         print(f"{line:^{num}}".rstrip())
#         level += 1
#
#
# num = int(input())
# draw_tree(num)
# # S
# size = int(input())
# cell_width = len(str((size + 1) // 2))
# for i in range(size):
#     for j in range(size):
#         print(f'{min(i + 1, j + 1, size - i, size - j):>{cell_width}}', end=' ')
#     print()
#
# def draw_number_square(size):
#     for i in range(size):
#         for j in range(size):
#             print(f'{min(i + 1, j + 1, size - i, size - j)}', end=' ')
#         print()
#
#
# size = int(input())
# draw_number_square(size)
# T
number = int(input())

best_value = 0
best_base = 0

for base in range(10, 1, -1):
    summa = 0
    num = number
    while num > 0:
        summa += (num % base)
        num //= base
    if summa >= best_value:
        best_value = summa
        best_base = base

print(best_base)
