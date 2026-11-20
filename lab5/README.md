Задание.py
-----
### Генератор, применяющий заданную функцию к каждому элементу последовательности N раз. Верните только те элементы, которые изменились значительно (зависит от N и типа данных).
``` python
def apply_n_times_gen(iterable, func, n):
    """Генератор, применяющий функцию func к каждому элементу последовательности n раз."""
    if n < 0:
        raise ValueError("Количество применений N должно быть неотрицательным.")

    for item in iterable:
        current = item
        for _ in range(n):
            current = func(current)
        yield item, current


def is_significantly_changed(pair, n, base_threshold=1.0):
    """
    Проверяет, изменился ли элемент значительно.
    Порог значительности зависит от N и типа данных.
    """
    original, transformed = pair

    # 1. Для числовых типов: разница должна превышать (base_threshold * n)
    if isinstance(original, (int, float)) and not isinstance(original, bool):
        return abs(transformed - original) >= base_threshold * n

    # 2. Для строк: изменение длины или число изменённых символов >= n
    if isinstance(original, str):
        len_diff = abs(len(transformed) - len(original))
        char_diffs = sum(1 for a, b in zip(original, transformed) if a != b) + len_diff
        return char_diffs >= n

    # 3. Для коллекций: изменение количества элементов >= n
    if isinstance(original, (list, tuple, set, dict)):
        return abs(len(transformed) - len(original)) >= n

    return original != transformed and n > 0


def process_sequence(iterable, func, n, base_threshold=1.0):
    """Связывает генератор с filter и map для получения итогового результата."""
    gen = apply_n_times_gen(iterable, func, n)
    # Применяем filter к генератору для отбора значительно изменившихся элементов
    significant_pairs = filter(
        lambda pair: is_significantly_changed(pair, n, base_threshold),
        gen
    )
    # Применяем map для извлечения итоговых значений
    return map(lambda pair: pair, significant_pairs)


if __name__ == "__main__":
    print("Выберите тип данных для обработки:")
    print("1 — Числа (увеличение на 10% за каждый шаг, порог изменения >= 2.0 * N)")
    print("2 — Строки (добавление '!' к строкам короче 6 символов, порог изменения >= N символов)")
    choice = input("Ваш выбор (1 или 2): ").strip()

    try:
        n = int(input("Введите количество применений функции N (целое число >= 1): "))
        if n < 1:
            raise ValueError
    except ValueError:
        print("Ошибка: N должно быть целым положительным числом.")
        exit(1)

    if choice == "1":
        raw_input = input("Введите числа через пробел (например: 10 20 30 40 50): ")
        try:
            sequence = [float(x) for x in raw_input.split()]
        except ValueError:
            print("Ошибка: нужно ввести корректные числа.")
            exit(1)

        threshold = 2.0
        func = lambda x: round(x * 1.1, 2)
        result = list(process_sequence(sequence, func, n=n, base_threshold=threshold))

        print(f"\nИсходный список: {sequence}")
        print(f"Порог значительного изменения для N={n}: >= {threshold * n}")
        print(f"Значительно изменившиеся элементы: {result}")

    elif choice == "2":
        raw_input = input("Введите слова через пробел: ")
        sequence = raw_input.split()

        func = lambda s: s + "!" if len(s) < 6 else s
        result = list(process_sequence(sequence, func, n=n))

        print(f"\nИсходный список: {sequence}")
        print(f"Порог значительного изменения для N={n}: >= {n} символов")
        print(f"Значительно изменившиеся элементы: {result}")

    else:
        print("Неизвестный выбор. Запустите программу снова и введите 1 или 2.")

```
### Результат:

<img width="1290" height="792" alt="изображение" src="https://github.com/user-attachments/assets/0a53ead6-de2c-4822-a549-015696f82c94" />


[Генераторы в питон](https://python-teach.ru/python-dlya-nachinayushhih/generatory-v-python/)
