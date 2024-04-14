import itertools

all_codes = list(itertools.product(range(10), repeat=6))
valid_codes = [code for code in all_codes if any(code.count(i) >= 3 for i in range(10))]

print(f"Количество различных кодов удовлетворяющих требованиям: {len(valid_codes)}")
