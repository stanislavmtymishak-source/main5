import random
import time
import sys

sys.setrecursionlimit(20000)


def generate_float_array(length: int, min_val: float = 1.0, max_val: float = 100.0) -> list[float]:
    """Генерує масив випадкових дробових чисел[cite: 4]."""
    return [round(random.uniform(min_val, max_val), 2) for _ in range(length)]


def print_array(arr: list) -> None:
    """Виводить масив у форматі: {[cell - 0, value - 4.2], [cell - 1, value - 10.5]...}"""
    formatted_elements = [f"[cell - {i}, value - {v}]" for i, v in enumerate(arr)]
    print("{" + ", ".join(formatted_elements) + "}")


def is_sorted(arr: list[float], ascending: bool = True) -> bool:
    """
    Приймає масив чисел та напрямок сортування[cite: 4].
    Повертає True, якщо масив впорядкований, і False у протилежному випадку[cite: 4].
    """
    for k in range(len(arr) - 1):
        if ascending and arr[k] > arr[k + 1]:
            return False
        if not ascending and arr[k] < arr[k + 1]:
            return False
    return True



def partition(arr: list[float], low: int, high: int, ascending: bool) -> int:
    """
    Розбиття масиву за схемою з методички (Рис. 2)[cite: 2]:
    - Півота (p) — останній елемент підмасиву (arr[high])[cite: 2].
    - Індекси i та j керують обмінами менших/більших елементів[cite: 2].
    """
    pivot = arr[high]
    i = low

    for j in range(low, high):

        condition = (arr[j] < pivot) if ascending else (arr[j] > pivot)
        if condition:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1


    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort_recursive(arr: list[float], low: int, high: int, ascending: bool) -> None:
    """Рекурсивний виклик QuickSort для підмасивів[cite: 1, 3]."""
    if low < high:

        pivot_idx = partition(arr, low, high, ascending)

