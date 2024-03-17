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
my_sum = 0
while float(number := input()) != 0:
    if float(number) >= 500.0:
        my_sum += float(number) * 0.9
    else:
        my_sum += float(number)
print(my_sum)
###########################################
# F

