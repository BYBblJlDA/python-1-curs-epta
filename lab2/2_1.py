import itertools

# Алфавит и длина последовательности
alphabet = 'КАТЕР'
length = 6
count = 0

# Перебираем все возможные комбинации длиной 6
for seq in itertools.product(alphabet, repeat=length):
    # Проверяем, что первая буква 'Р', а последняя 'К'
    if seq[0] == 'Р' and seq[-1] == 'К':
        count += 1

print(f"Количество подходящих последовательностей: {count}")
