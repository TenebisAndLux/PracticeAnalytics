# A
# while (command := input()) != 'Три!':
#     print('Режим ожидания...')
# print('Ёлочка, гори!')
###########################################
# B
# road = []
# while (command := input()) != 'Приехали!':
#     road.append(command)
#
# len_count = 0
# result = ""
#
# for line in road:
#     if "зайка" in line:
#         len_count += 1
#
# if len_count > 0:
#     print(len_count)
# else:
#     print("Зайки не найдено")
###########################################
# C
# k = int(input())
# n = int(input())
# mstr = ''
# for i in range(k, n + 1):
#     mstr += (f'{i} ')
# print(mstr)
###########################################
# D
# k = int(input())
# n = int(input())
# mstr = ''
# if n < k:
#     for i in reversed(range(n, k + 1)):
#         mstr += (f'{i} ')
# else:
#     for i in range(k, n + 1):
#         mstr += (f'{i} ')
#
#
# print(mstr)
###########################################
# E
# my_sum = 0
# while float(number := input()) != 0:
#     if float(number) >= 500.0:
#         my_sum += float(number) * 0.9
#     else:
#         my_sum += float(number)
# print(my_sum)
###########################################
# F
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# num1 = int(input())
# num2 = int(input())
# result = gcd(num1, num2)
# print(result)
###########################################
# G
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
#
# num1 = int(input())
# num2 = int(input())
# result = lcm(num1, num2)
# print(result)
###########################################
# H
# k = (input())
# n = int(input())
# for i in range(0, n):
#     print(k)
###########################################
# I
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# num = int(input())
# result = factorial(num)
# print(result)
###########################################
# J
# up_x = 0
# up_y = 0
# directions_x = {"ВОСТОК": 1, "ЗАПАД": -1}
# directions_y = {"СЕВЕР": 1, "ЮГ": -1}
# while (direction := input()) != 'СТОП':
#     n = int(input())
#     up_x += n * int(directions_x.get(direction, 0))
#     up_y += n * int(directions_y.get(direction, 0))
#
# print(up_y)
# print(up_x)
###########################################
# K
# digit_sum = sum([int(digit) for digit in input()])
# print(digit_sum)
###########################################
# L
# digit_max = max([int(digit) for digit in input()])
# print(digit_max)
###########################################
# M
# n = int(input())
# players = [input() for _ in range(n)]
# first_player = sorted(players)[0]
# print(first_player)
###########################################
# N
# def is_prime(n):
#     if n <= 1:
#         return "NO"
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return "NO"
#
#     return "YES"
#
#
# number = int(input())
# result = is_prime(number)
# print(result)
###########################################
# O
# n = int(input())
# count = 0
# for _ in range(n):
#     description = input()
#     if 'зайка' in description:
#         count += 1
#
#
# print(count)
###########################################
# P
# number = input()
# is_palindrome = "YES"
# for i in range(len(number) // 2):
#     if number[i] != number[-i - 1]:
#         is_palindrome = "NO"
#         break
#
# print(is_palindrome)
###########################################
# Q
# numbered = ''
# digits = [int(digit) for digit in input()]
# for digit in digits:
#     if digit % 2 == 1:
#         numbered += str(digit)
# print(numbered)
###########################################
# R
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i != 0:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
#
#
# n = int(input())
# factors = prime_factors(n)
#
# output = " * ".join(str(factor) for factor in factors)
# print(output)
###########################################
# S
# a = 0
# b = 1000
# number = (a + b) // 2
# print(number)
#
# flag = 0
# while (answer := input()) and flag <= 10:
#     if answer == 'Меньше':
#         b = number - 1
#     elif answer == 'Больше':
#         a = number + 1
#     else:
#         break
#     number = (a + b) // 2
#     print(f'{number}')
#     flag += 1
###########################################
# T
# h = (37 * (1 + 1 + 0)) % 256
# 256 * (r + m * 256) + h = b
# h = b % 256
# (b - h) / 256 = r + m * 256
# r = ((b - h) / 256) % 256
# m = ((b - r * 256 - h) / 256) % 256
n = int(input())
b = []
r = []
m = []
h = []
for i in range(n):
    step = i
    b.append(int(input()))
    h.append(b[i] % 256)
    if h[i] >= 100:
        print(i)
        break
    r.append(((b[i] - h[i]) // 256) % 256)
    m.append(((b[i] - r[i] * 256 - h[i]) // 256 ** 2))
    if i == 0:
        if (h[i] != (37 * (m[i] + r[i] + 0)) % 256):
            print(i)
            break
    else:
        if (h[i] != (37 * (m[i] + r[i] + h[i - 1])) % 256):
            print(i)
            break
if step == n - 1:
    print(-1)
###########################################