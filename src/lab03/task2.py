import sys
from task1 import normalize, tokenize, count_freq, top_n

# Читаем с правильной кодировкой
text = sys.stdin.buffer.read().decode('utf-8')

normalized_text = normalize(text)
tokens = tokenize(normalized_text)
freq = count_freq(tokens)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for word, count in top_n(freq, 5):
    print(f"{word}:{count}") 