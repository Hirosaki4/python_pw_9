from collections.abc import Iterable

def process_data(data, operation, target='values'):
    """
    Обробляє елементи колекції за допомогою переданої функції.

    Параметри:
    - data: list, tuple або dict – колекція для обробки.
    - operation: функція, яка приймає один аргумент і повертає результат.
    - target: для словників – 'keys', 'values', або 'items'.

    Повертає: нову колекцію того ж типу.
    """
    try:
        if isinstance(data, dict):
            if target == 'keys':
                return {operation(k): v for k, v in data.items()}
            elif target == 'values':
                return {k: operation(v) for k, v in data.items()}
            elif target == 'items':
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                raise ValueError("Неправильне значення 'target' для словника.")
        elif isinstance(data, list):
            return [operation(item) for item in data]
        elif isinstance(data, tuple):
            return tuple(operation(item) for item in data)
        else:
            raise TypeError("Підтримуються лише list, tuple або dict.")
    except Exception as e:
        return f"Помилка обробки: {e}"

def filter_data(data, predicate):
    """
    Фільтрує колекцію відповідно до предикат-функції.

    Параметри:
    - data: list, tuple або dict.
    - predicate: функція, що повертає True або False.

    Повертає: нову колекцію того ж типу з елементами, що відповідають умові.
    """
    try:
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if predicate((k, v))}
        elif isinstance(data, list):
            return [item for item in data if predicate(item)]
        elif isinstance(data, tuple):
            return tuple(item for item in data if predicate(item))
        else:
            raise TypeError("Підтримуються лише list, tuple або dict.")
    except Exception as e:
        return f"Помилка фільтрації: {e}"

def combine_values(*args, separator=None, initial=None):
    """
    Комбінує значення (числа або рядки) залежно від типу першого аргументу.

    Параметри:
    - *args: довільна кількість значень.
    - separator: рядок для розділення при об'єднанні рядків.
    - initial: початкове значення для чисел.

    Повертає: комбіноване значення або повідомлення про помилку.
    """
    try:
        if not args:
            return initial if initial is not None else ""
        
        first = args[0]
        if isinstance(first, (int, float)):
            result = initial if initial is not None else 0
            for item in args:
                if not isinstance(item, (int, float)):
                    raise TypeError("Усі значення повинні бути числами.")
                result += item
            return result
        elif isinstance(first, str):
            result = list(map(str, args))
            return (separator or "").join(result)
        else:
            raise TypeError("Перший аргумент має бути числом або рядком.")
    except Exception as e:
        return f"Помилка об'єднання: {e}"

# === Тестування функцій ===

# process_data
print("=== process_data ===")
print(process_data([1, 2, 3], lambda x: x ** 2))                      # [1, 4, 9]
print(process_data((1, 2, 3), lambda x: x + 1))                       # (2, 3, 4)
print(process_data({'a': 1, 'b': 2}, lambda x: x * 10, target='values'))  # {'a': 10, 'b': 20}

# filter_data
print("\n=== filter_data ===")
print(filter_data([1, 2, 3, 4, 5], lambda x: x % 2 == 0))             # [2, 4]
print(filter_data((1, 2, 3, 4), lambda x: x > 2))                     # (3, 4)
print(filter_data({'a': 1, 'b': 2}, lambda kv: kv[1] > 1))            # {'b': 2}

# combine_values
print("\n=== combine_values ===")
print(combine_values(1, 2, 3, 4))                                     # 10
print(combine_values("Python", "is", "cool", separator=" "))         # "Python is cool"
print(combine_values(1.5, 2.5, initial=1.0))                          # 5.0
