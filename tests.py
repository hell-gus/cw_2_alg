import pytest
from cw import TextEditor # Импорт редактора из основного файла

@pytest.fixture
def editor():
    """Фикстура для создания нового текстового редактора перед каждым тестом."""
    return TextEditor()

def test_add_line(editor):
    """Тест добавления строк."""
    editor.add_line("Первая строка")
    editor.add_line("Вторая строка")
    assert editor.text == ["Первая строка", "Вторая строка"]

def test_edit_line(editor):
    """Тест редактирования строки."""
    editor.add_line("Первая строка")
    editor.add_line("Вторая строка")
    editor.edit_line(1, "Обновленная строка")
    assert editor.text == ["Первая строка", "Обновленная строка"]

def test_delete_line(editor):
    """Тест удаления строки."""
    editor.add_line("Первая строка")
    editor.add_line("Вторая строка")
    editor.delete_line(0)
    assert editor.text == ["Вторая строка"]

def test_undo_add(editor):
    """Тест отмены добавления строки."""
    editor.add_line("Первая строка")
    editor.undo()
    assert editor.text == []

def test_undo_edit(editor):#not working
    """Тест отмены редактирования строки."""
    editor.add_line("Первая строка")
    editor.add_line("Вторая строка")
    editor.edit_line(1, "Обновленная строка")
    editor.undo()
    assert editor.text == ["Первая строка", "Вторая строка"]

def test_undo_delete(editor):
    """Тест отмены удаления строки."""
    editor.add_line("Первая строка")
    editor.add_line("Вторая строка")
    editor.delete_line(0)
    editor.undo()
    assert editor.text == ["Первая строка", "Вторая строка"]

def test_redo(editor):
    """Тест возврата изменений."""
    editor.add_line("Первая строка")
    editor.undo()
    editor.redo()
    assert editor.text == ["Первая строка"]

def test_find(editor):
    """Тест поиска строки."""
    editor.add_line("Первая строка")
    editor.add_line("Вторая строка")
    assert editor.find("Вторая") == [1]

def test_max_history(editor):
    """Тест ограничения размера истории."""
    for i in range(30):  # Добавляем 30 строк
        editor.add_line(f"Строка {i}")
    assert len(editor.undo_stack) == editor.max_history  # Максимальный размер истории
