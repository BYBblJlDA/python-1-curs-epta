# Вычисляем значение исходного выражения
expr = 216**6 + 216**4 + 36**6 - 6**14 - 24

# Множество для хранения уникальных цифр шестеричной записи
unique_digits = set()
temp = expr

# Переводим число в систему счисления с основанием 6
while temp > 0:
    digit = temp % 6
    unique_digits.add(digit)
    temp //= 6

print(f"Количество различных цифр: {len(unique_digits)}")
print(f"Найденные цифры: {sorted(unique_digits)}")
