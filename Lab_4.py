import tkinter as tk  # графический интерфейс
from threading import Thread  # обрабатывает события на клавиатуре
import keyboard  # отработка нажатий клавиш


# этот класс создает виртуальную клавиатуру
class VirtualKeyboard:
    # в этом конструкторе создается интерфейс, переменные, клавиши
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Keyboard")
        self.text = tk.StringVar()
        self.text.set("")

        self.key_mapping = {
            'Q': 'A',  # Q на A
            'A': 'Q',  # A на Q
        }

        self.text_entry = tk.Entry(root, textvariable=self.text)
        self.text_entry.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.create_keyboard_buttons()
        self.undo_button = tk.Button(root, text="Отменить", command=self.undo_action)
        self.undo_button.pack()

        self.history = []  # история
        self.clipboard = ""  # буфер
        self.pending_1 = False  # Флаг ожидания второй цифры после 1

        self.keyboard_thread = Thread(target=self.listen_keyboard)
        self.keyboard_thread.daemon = True
        self.keyboard_thread.start()

    # метод создания кнопок
    def create_keyboard_buttons(self):
        keyboard_layout = [
            '1234567890',
            'QWERTYUIOP',
            'ASDFGHJKL',
            'ZXCVBNM',
        ]

        for row in keyboard_layout:
            row_frame = tk.Frame(self.button_frame)
            row_frame.pack()
            for char in row:
                button = tk.Button(row_frame, text=char, command=lambda c=char: self.add_character(c))
                button.pack(side=tk.LEFT)

    # метод добавления символа на клавиатуру 12 -> B
    def add_character(self, char):
        if self.pending_1:
            if char == '2':
                self.text.set(self.text.get() + 'B')
                self.pending_1 = False
            else:
                self.text.set(self.text.get() + '1' + char)
        else:
            if char == '1':
                self.pending_1 = True
            mapped_char = self.key_mapping.get(char, char)
            self.text.set(self.text.get() + mapped_char)
            self.history.append(char)

    # отмена действия
    def undo_action(self):
        if self.history:
            last_char = self.history.pop()
            if self.pending_1:
                self.pending_1 = False
            current_text = self.text.get()
            if current_text:
                self.text.set(current_text[:-1])

    # запускает граф. интерфейс
    def run(self):
        self.root.mainloop()

    # обрабатывает поток символов и добавляя 12 - В
    def listen_keyboard(self):
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                self.add_character(event.name)


# симуляция нажатия клавиш в отдельном потоке
def simulate_typing(keyboard, text_to_type):
    for char in text_to_type:
        keyboard.add_character(char)


if __name__ == "__main__":
    root = tk.Tk()
    keyboard = VirtualKeyboard(root)

    simulation_thread = Thread(target=simulate_typing, args=(keyboard, "Hello, World!"))
    simulation_thread.start()

    keyboard.run()