file_open = input("Введіть шлях до текстового файлу: ")
try:
    file = open(file_open, 'r', encoding="utf-8")
    line_number = 1
    for line in file:
        words = line.split()
        line = line.rstrip()
        word_count = len(words)
        print(f"Рядок {line_number}: Кількість слів - {word_count}")
        char_count = len(line)
        print(f"Кількість символів з врахуванням пробілів - {char_count}, Без - {char_count - len(words) + 1}")
        line_number += 1
except FileNotFoundError:
    print(f"Файл {file_open} не знайдено.")
except Exception as e:
    print(f"Виникла помилка: {e}")
