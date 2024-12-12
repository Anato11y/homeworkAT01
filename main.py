def modulo(a, b):
    """Функция для вычисления остатка от деления a на b."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a % b
