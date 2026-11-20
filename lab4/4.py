import math
from functools import wraps


def validate_args(expected_type=(int, float), min_val=None, max_val=None):
    """Декоратор для проверки аргументов на тип и диапазон значений (по умолчанию границы не ограничены)."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_args = list(args) + list(kwargs.values())

            for arg in all_args:
                if isinstance(arg, bool) or not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Неверный тип аргумента: {arg!r} ({type(arg).__name__}). "
                        f"Ожидался тип: {expected_type}"
                    )
                if math.isnan(arg) or math.isinf(arg):
                    raise ValueError(f"Недопустимое числовое значение: {arg}")

                if min_val is not None and arg < min_val:
                    raise ValueError(
                        f"Значение {arg} меньше допустимого минимума ({min_val})"
                    )
                if max_val is not None and arg > max_val:
                    raise ValueError(
                        f"Значение {arg} больше допустимого максимума ({max_val})"
                    )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def make_average_calculator():
    """Замыкание для накопительного расчёта среднего значения."""
    total = 0.0
    count = 0

    def add_values(*args):
        nonlocal total, count
        if not args:
            return total / count if count > 0 else 0.0

        total += sum(args)
        count += len(args)
        return total / count

    return add_values


def parse_token(token):
    """Преобразует числовую строку в int или float, а текст оставляет строкой для проверки декоратором."""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


# Применяем декоратор к замыканию без ограничения границ (min_val=None, max_val=None)
calc_avg = validate_args(expected_type=(int, float), min_val=None, max_val=None)(
    make_average_calculator()
)


if __name__ == "__main__":
    print("Вводите любые числа через пробел — положительные, отрицательные, дробные (для выхода введите 'exit'):")

    while True:
        user_input = input("> ")
        if user_input.strip().lower() == "exit":
            break
        if not user_input.strip():
            continue

        items = [parse_token(x) for x in user_input.split()]

        try:
            result = calc_avg(*items)
            print(f"Текущее среднее: {result}")
        except (TypeError, ValueError) as e:
            print(f"Декоратор отклонил ввод -> {e}")
