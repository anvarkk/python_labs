import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'е')
    text = re.sub(r'[\t\r\n]+', ' ', text)
    return re.sub(r' +', ' ', text.strip())

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

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