# 1. Вариант С РЕКУРСИЕЙ
def calc_ab_recursive(k):
    if k < 1:
        raise ValueError("k должно быть натуральным числом (k >= 1)")
    if k == 1:
        return 1, 1
    
    a_prev, b_prev = calc_ab_recursive(k - 1)
    a_curr = 2 * b_prev + a_prev
    b_curr = 2 * a_prev + b_prev
    return a_curr, b_curr


# 2. Вариант БЕЗ РЕКУРСИИ (итеративно)
def calc_ab_iterative(k):
    if k < 1:
        raise ValueError("k должно быть натуральным числом (k >= 1)")
    
    a, b = 1, 1
    for _ in range(2, k + 1):
        a, b = 2 * b + a, 2 * a + b
    return a, b


# Проверка работы
k = 5
print(f"Расчёт для k = {k}:")
print("С рекурсией (a_k, b_k): ", calc_ab_recursive(k))
print("Без рекурсии (a_k, b_k):", calc_ab_iterative(k))
