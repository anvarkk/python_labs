import pytest
import sys
from pathlib import Path

# Добавляем путь к src для импорта модулей
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from lab03.task1 import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    """Тест нормализации текста - базовые случаи"""
    # Обычный текст
    assert normalize("ПРИВЕТ МИР") == "привет мир"
    assert normalize("Hello World") == "hello world"
    # Текст с разными регистрами
    assert normalize("ТеСтОвЫй ТеКсТ") == "тестовый текст"


def test_normalize_special_chars():
    """Тест нормализации - спецсимволы"""
    # Спецсимволы должны удаляться
    assert normalize("привет, мир!") == "привет мир"
    assert normalize("текст... с точками") == "текст с точками"
    assert normalize("цифры 123 и символы @#$") == "цифры и символы"


def test_normalize_empty():
    """Тест нормализации - граничные случаи"""
    # Пустая строка
    assert normalize("") == ""
    # Только спецсимволы
    assert normalize("!@#$%") == ""


def test_tokenize_basic():
    """Тест токенизации - базовые случаи"""
    # Обычный текст
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello world") == ["hello", "world"]
    # Несколько слов
    assert tokenize("один два три") == ["один", "два", "три"]


def test_tokenize_special_chars():
    """Тест токенизации - спецсимволы"""
    # Текст со знаками препинания
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("текст. с точками") == ["текст", "с", "точками"]


def test_tokenize_empty():
    """Тест токенизации - граничные случаи"""
    # Пустая строка
    assert tokenize("") == []
    # Только спецсимволы
    assert tokenize("! @ # $") == []


def test_count_freq_basic():
    """Тест подсчета частот - базовые случаи"""
    # Обычные слова
    tokens = ["привет", "мир", "привет"]
    assert count_freq(tokens) == {"привет": 2, "мир": 1}

    # Разные слова
    tokens = ["один", "два", "три"]
    assert count_freq(tokens) == {"один": 1, "два": 1, "три": 1}


def test_count_freq_repeats():
    """Тест подсчета частот - повторения"""
    # Много повторений
    tokens = ["слово", "слово", "слово", "другое"]
    assert count_freq(tokens) == {"слово": 3, "другое": 1}


def test_count_freq_empty():
    """Тест подсчета частот - граничные случаи"""
    # Пустой список
    assert count_freq([]) == {}


def test_top_n_basic():
    """Тест топ-N слов - базовые случаи"""
    freq = {"привет": 5, "мир": 3, "тест": 1}
    # Топ-2
    assert top_n(freq, 2) == [("привет", 5), ("мир", 3)]
    # Топ-1
    assert top_n(freq, 1) == [("привет", 5)]


def test_top_n_equal_frequency():
    """Тест топ-N слов - одинаковая частота (сортировка по алфавиту)"""
    # При равной частоте сортируем по алфавиту
    freq = {"яблоко": 3, "апельсин": 3, "банан": 3}
    result = top_n(freq, 3)
    assert result == [("апельсин", 3), ("банан", 3), ("яблоко", 3)]


def test_top_n_more_than_available():
    """Тест топ-N слов - запрашиваем больше чем есть"""
    freq = {"один": 1, "два": 1}
    # Запрашиваем топ-5, но есть только 2

    assert top_n(freq, 5) == [("два", 1), ("один", 1)]


def test_top_n_empty():
    """Тест топ-N слов - граничные случаи"""
    # Пустой словарь
    assert top_n({}, 5) == []
    # N = 0
    assert top_n({"слово": 1}, 0) == []


# Параметризованные тесты для более полного покрытия
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("", ""),
        ("ПРИВЕТ", "привет"),
        ("ТеСт", "тест"),
        ("С Пунктуацией!", "с пунктуацией"),
    ],
)
def test_normalize_parametrized(input_text, expected):
    """Параметризованный тест нормализации"""
    assert normalize(input_text) == expected


@pytest.mark.parametrize(
    "tokens,n,expected",
    [
        (["а", "б", "в"], 2, [("а", 1), ("б", 1)]),
        (["а", "а", "б"], 1, [("а", 2)]),
        ([], 5, []),
    ],
)
def test_top_n_parametrized(tokens, n, expected):
    """Параметризованный тест топ-N слов"""
    freq = count_freq(tokens)
    assert top_n(freq, n) == expected
