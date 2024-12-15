import tkinter as tk
from tkinter import messagebox
from cw import TextEditor  # Импортируем класс TextEditor из файла cw.py


class TextEditorGUI:
    def __init__(self, root):
        self.editor = TextEditor()
        self.root = root
        self.root.title("Текстовый редактор")

        # Основная область для отображения текста
        self.text_display = tk.Text(root, height=30, width=60)
        self.text_display.pack(padx=10, pady=10)

        # Панель для кнопок
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Кнопки
        self.add_button = tk.Button(self.button_frame, text="Добавить строку", command=self.add_line)
        self.add_button.grid(row=0, column=0, padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Редактировать строку", command=self.edit_line)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Удалить строку", command=self.delete_line)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.undo_button = tk.Button(self.button_frame, text="Отменить действие", command=self.undo)
        self.undo_button.grid(row=0, column=3, padx=5)

        self.redo_button = tk.Button(self.button_frame, text="Вернуть действие", command=self.redo)
        self.redo_button.grid(row=0, column=4, padx=5)

        self.find_button = tk.Button(self.button_frame, text="Найти строку", command=self.find)
        self.find_button.grid(row=0, column=5, padx=5)

        self.update_text_display()  # Инициализируем отображение текста

    def add_line(self):
        """Добавление новой строки."""
        new_line = simpledialog.askstring("Добавить строку", "Введите текст новой строки:")
        if new_line:
            self.editor.add_line(new_line)
            self.update_text_display()

    def edit_line(self):
        """Редактирование строки."""
        try:
            index = int(simpledialog.askstring("Редактировать строку", "Введите индекс строки для редактирования:"))
            new_line = simpledialog.askstring("Редактировать строку", "Введите новый текст строки:")
            if new_line:
                self.editor.edit_line(index, new_line)
                self.update_text_display()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный индекс.")

    def delete_line(self):
        """Удаление строки."""
        try:
            index = int(simpledialog.askstring("Удалить строку", "Введите индекс строки для удаления:"))
            self.editor.delete_line(index)
            self.update_text_display()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный индекс.")

    def undo(self):
        """Отмена последнего действия."""
        self.editor.undo()
        self.update_text_display()

    def redo(self):
        """Повтор действия (возврат)."""
        self.editor.redo()
        self.update_text_display()

    def find(self):
        """Поиск строки."""
        substring = simpledialog.askstring("Поиск строки", "Введите подстроку для поиска:")
        if substring:
            results = self.editor.find(substring)
            if results:
                messagebox.showinfo("Результаты поиска", f"Строки найдены на индексах: {results}")
            else:
                messagebox.showinfo("Результаты поиска", "Совпадений не найдено.")

    def update_text_display(self):
        """Обновление отображаемого текста в текстовом поле."""
        self.text_display.delete(1.0, tk.END)  # Очистка текущего текста
        for i, line in enumerate(self.editor.text):
            self.text_display.insert(tk.END, f"{i}: {line}\n")


# Основная часть программы для запуска GUI
if __name__ == "__main__":
    import tkinter.simpledialog as simpledialog

    root = tk.Tk()
    gui = TextEditorGUI(root)
    root.mainloop()
