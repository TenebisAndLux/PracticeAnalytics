import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('Pokemon.csv')

# Визуализация данных
print("Визуализация данных:")
print(df)

# Топ-3 самых частых типов покемонов (Type 1)
top_common_types = df['Type 1'].value_counts().head(3)
print("\nТоп-3 самых частых типов покемонов (Type 1):")
print(top_common_types)

# Топ-3 самых редких типов покемонов (Type 1)
bottom_common_types = df['Type 1'].value_counts().tail(3)
print("\nТоп-3 самых редких типов покемонов (Type 1):")
print(bottom_common_types)

# Анализ зависимости общей силы покемона (Total) и статуса "Легендарный"
top_types = top_common_types.index.tolist()
top_pokemon = df[df['Type 1'].isin(top_types)]

print("\nЗависимость между общей силой покемона (Total) и статусом 'Легендарный' у покемонов с наиболее распространенными типами:")
print(top_pokemon.groupby('Legendary')['Total'].mean())

# Средняя общая сила легендарных и обычных покемонов
mean_total_legendary = df[df['Legendary'] == True]['Total'].mean()
mean_total_non_legendary = df[df['Legendary'] == False]['Total'].mean()

print("\nСредняя общая сила легендарных покемонов:", mean_total_legendary)
print("\nСредняя общая сила обычных покемонов:", mean_total_non_legendary)

# Самый сильный и слабый покемоны среди легендарных и обычных покемонов
strongest_legendary = df[df['Legendary'] == True]['Total'].idxmax()
weakest_legendary = df[df['Legendary'] == True]['Total'].idxmin()
strongest_non_legendary = df[df['Legendary'] == False]['Total'].idxmax()
weakest_non_legendary = df[df['Legendary'] == False]['Total'].idxmin()

print("\nСамый сильный легендарный покемон:", df.loc[strongest_legendary]['Name'])
print("\nСамый слабый легендарный покемон:", df.loc[weakest_legendary]['Name'])
print("\nСамый сильный обычный покемон:", df.loc[strongest_non_legendary]['Name'])
print("\nСамый слабый обычный покемон:", df.loc[weakest_non_legendary]['Name'])