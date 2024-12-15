from cw import TextEditor  # Импортируем класс TextEditor из файла cw.py


def main():
    editor = TextEditor()

    # Добавляем 25 строк в текстовый редактор
    for i in range(1, 26):
        editor.add_line(f"Строка {i}")

    print("Текстовый редактор запущен с 25 строками.")  # Отладочная строка для проверки

    while True:
        print("\nТекущий текст:")
        editor.display()
        print("\nВыберите действие:")
        print("1. Добавить строку")
        print("2. Редактировать строку")
        print("3. Удалить строку")
        print("4. Отменить действие (Undo)")
        print("5. Вернуть действие (Redo)")
        print("6. Найти строку")
        print("7. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            line = input("Введите строку для добавления: ")
            editor.add_line(line)
        elif choice == "2":
            index = int(input("Введите индекс строки для редактирования: "))
            new_line = input("Введите новый текст строки: ")
            editor.edit_line(index, new_line)
        elif choice == "3":
            index = int(input("Введите индекс строки для удаления: "))
            editor.delete_line(index)
        elif choice == "4":
            editor.undo()
        elif choice == "5":
            editor.redo()
        elif choice == "6":
            substring = input("Введите подстроку для поиска: ")
            results = editor.find(substring)
            if results:
                print("Строки найдены на индексах:", results)
            else:
                print("Совпадений не найдено.")
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


# Добавьте эту строку в конце файла, чтобы убедиться, что main() вызывается только при запуске скрипта напрямую
if __name__ == "__main__":
    main()
