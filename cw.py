class TextEditor:
    def __init__(self):
        self.text = []  # Текст по строкам
        self.undo_stack = []  # Стек отмены (массив таплов)
        self.redo_stack = []  # Стек возврата (массив таплов)
        self.max_history = 25  # Ограничение на размер истории

    def add_line(self, line):
        """Добавление новой строки."""
        self._add_to_undo(("delete", len(self.text), line))  # Сохраняем удаление для отмены
        self.redo_stack.clear()  # Очистка redo-истории
        self.text.append(line)  # Добавляем строку в конец

    def edit_line(self, index, new_line):
        """Редактирование строки."""
        if 0 <= index < len(self.text):
            self._add_to_undo(("edit", index, self.text[index]))  # Сохраняем старую строку
            self.redo_stack.clear()
            self.text[index] = new_line  # Редактируем строку по индексу
        else:
            print("Ошибка: Индекс вне диапазона")

    def delete_line(self, index):
        """Удаление строки."""
        if 0 <= index < len(self.text):
            self._add_to_undo(("add", index, self.text[index]))  # Сохраняем удаляемую строку для undo
            self.redo_stack.clear()
            del self.text[index]  # Удаляем строку по индексу
        else:
            print("Ошибка: Индекс вне диапазона")

    def undo(self):
        """Отмена последнего действия."""
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)  # Переносим в стек redo
            self._apply_action(action, reverse=True)
        else:
            print("Нечего отменять")

    def redo(self):
        """Повтор действия (возврат)."""
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)  # Переносим обратно в undo
            self._apply_action(action, reverse=False)
        else:
            print("Нечего вернуть")

    def _apply_action(self, action, reverse):
        """Применение действия для undo/redo."""
        action_type, index, line = action
        if action_type == "add":
            if reverse:  # Отмена удаления (добавление строки)
                self.text.insert(index, line)  # Вставляем строку обратно по индексу
            else:  # Повтор удаления
                del self.text[index]
        elif action_type == "delete":
            if reverse:  # Отмена добавления (удаление строки)
                del self.text[index]
            else:  # Повтор добавления
                self.text.insert(index, line)
        elif action_type == "edit":
            self.text[index], action[2] = action[2], self.text[index]  # Обмен строк

    def _add_to_undo(self, action):
        """Добавление действия в стек undo с ограничением размера."""
        if len(self.undo_stack) >= self.max_history:
            self.undo_stack.pop(0)  # Удаляем самое старое действие
        self.undo_stack.append(action)

    def find(self, substring):
        """Поиск строки, содержащей подстроку."""
        results = [i for i, line in enumerate(self.text) if substring in line]
        return results

    def display(self):
        """Отображение текста."""
        for i, line in enumerate(self.text):
            print(f"{i}: {line}")

