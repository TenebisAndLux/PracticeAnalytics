import pandas as pd

name = input('Введите наименование файла: ')
df = pd.read_csv(f'{name}.csv', delimiter=',')

# Сохраняем данные в Excel файл
df.to_excel(f'{name}.xlsx')
