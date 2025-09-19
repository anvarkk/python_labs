"""
Задание 6* - Подсчет участников по формату обучения
"""

n = int(input())  # Читаем количество участников

count_onsite = 0  # Счетчик очников
count_online = 0   # Счетчик заочников

for _ in range(n):
    line = input().split()  # Разбиваем строку на части
    format_str = line[-1]   # Берем последний элемент (формат обучения)
    
    if format_str == "True":  # Если очный формат
        count_onsite += 1
    else:  # Если заочный формат
        count_online += 1

# Выводим результат
print(count_onsite, count_online)
