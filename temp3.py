import random
import numpy as np
import matplotlib.pyplot as plt
import operator

def get_remainder(x, y):
    return div(x, y)[1]

def get_degree_term(x, k):
    return x << k

def div(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

def count_ones(x):
    res = 0
    while x > 0:
        if x & 1:
            res += 1
        x >>= 1
    return res

def mul(x, y):
    res = 0
    while y > 0:
        if y & 1:
            res ^= x
        x <<= 1
        y >>= 1
    return res

def left_shift(x, n):
    return (x << 1) ^ (x >> (n - 1))

def right_shift(x, n):
    return (x >> 1) ^ (x << (n - 1))

def we_can_search(w, t):
    return w <= t

def fix_error(F, g, n, t):
    shift = 0
    while shift < n:
        if F & (1 << shift) != 0:
            F ^= g << (shift - n + 1)
            if count_ones(F) <= t:
                return F
        shift += 1
    return None

m = 0b1010  # Пример двоичного числа m
g = 0b1101  # Пример двоичного числа g
k = 4  # Пример значения k
F = mul(m, get_degree_term(g, k)) + get_remainder(mul(m, get_degree_term(g, k)), g)
print("F = ", bin(F))

t = 3  # Пример значения t
F_err = 0b11010  # Пример значения F_err
div_comb = div(F_err, g)
w = get_remainder(F_err, g)

print("F с ошибкой = ", bin(F_err))
print("w = ", bin(w))
if we_can_search(w, t):
    print("Мы можем правильно декодировать с одного прохода", " w =", w, " t =", t)
    print("Полученная сумма:", bin(F_err ^ w))
else:
    corrected_F = fix_error(F_err, g, k, t)
    if corrected_F is not None:
        print("Потребовалось несколько проходов. Полученное сообщение: ", bin(corrected_F))
        print("Сравнение F с полученным F: ", bin(F), " <> ", bin(corrected_F))
    else:
        print("Не удалось исправить ошибку")