# 1. Вариант С РЕКУРСИЕЙ
def linearize_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


# 2. Вариант БЕЗ РЕКУРСИИ (через стек)
def linearize_iterative(lst):
    result = []
    stack = list(lst)
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            result.append(current)
    return result[::-1]


# Проверка работы
test_data = [1, 2, [3, 4, [5, [6, []]]]]
print("Исходный список:", test_data)
print("С рекурсией:    ", linearize_recursive(test_data))
print("Без рекурсии:   ", linearize_iterative(test_data))
