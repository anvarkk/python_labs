import re
from collections import Counter


def normalize(text: str) -> str:
    """
    Нормализует текст: приводит к нижнему регистру и удаляет знаки препинания.
    """
    if not text:
        return ""

    # Приводим к нижнему регистру
    text = text.lower()

    # Удаляем все знаки препинания и цифры, оставляем только буквы и пробелы
    text = re.sub(r"[^а-яa-zё\s]", "", text)

    # Убираем лишние пробелы
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на слова.
    """
    if not text:
        return []

    # Используем регулярное выражение для извлечения слов (только буквы)
    words = re.findall(r"[а-яa-zё]+", text)

    return words


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоту слов.
    """
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """
    Возвращает топ-N самых частых слов.
    При равной частоте сортирует по алфавиту.
    """
    if not freq or n <= 0:
        return []

    # Сортируем сначала по убыванию частоты, потом по возрастанию слова (алфавит)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Возвращаем первые n элементов (или все если n больше длины)
    return sorted_items[:n]


# Убираем тестовый код или оборачиваем в if __name__
if __name__ == "__main__":
    # Тестовый код только при прямом запуске
    text = "ПрИвЕт\nМИр\tёжик"
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top = top_n(freq, 3)

    print("Нормализовано:", normalized)
    print("Токены:", tokens)
    print("Частоты:", freq)
    print("Топ-3:", top)
