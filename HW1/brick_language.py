import argparse

def to_brick_language(message):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  # русские гласные
    result = []

    for char in message:
        if char in vowels:
            result.append(char + 'с' + char)  # добавляем 'с' и повторяем гласную
        else:
            result.append(char)

    return ''.join(result)

if __name__ == "__main__":
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Шифрование на кирпичном языке")
    
    # Добавляем параметр для ввода сообщения
    parser.add_argument('message', nargs='?', default=None, help="Сообщение для шифрования")
    
    # Считываем параметры из командной строки
    args = parser.parse_args()

    if args.message is None:
        example_phrase: str = "кирпичный язык"
        print('Передайте аргументом слово, которое хотите зашифровать.')
        print(f'Ниже представлен пример шифрования на кирпичный язык фразы "{example_phrase}"')
        print("Зашифрованное сообщение: ", to_brick_language(example_phrase), end='\n\n')
    else: 
        # Печатаем зашифрованное сообщение
        print("Исходное сообщение: ", to_brick_language(args.message))
        print("Зашифрованное сообщение: ", to_brick_language(args.message))
