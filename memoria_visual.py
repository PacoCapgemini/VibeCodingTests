import tkinter as tk
import random
from tkinter import messagebox

# Lista de iconos unicode para las cartas (8 pares)
ICONS = [
    '\u2600',  # Sol
    '\u2601',  # Nube
    '\u2602',  # Paraguas
    '\u2603',  # Muñeco de nieve
    '\u2665',  # Corazón
    '\u2666',  # Diamante
    '\u2663',  # Trébol
    '\u2660',  # Pica
]

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Juego de Memoria Visual')
        self.buttons = []
        self.first = None
        self.second = None
        self.lock = False
        self.create_board()

    def create_board(self):
        # Duplicar y mezclar iconos
        icons = ICONS * 2
        random.shuffle(icons)
        self.cards = icons
        self.revealed = [False] * 16
        for i in range(4):
            row = []
            for j in range(4):
                idx = i * 4 + j
                btn = tk.Button(self.root, text='?', width=6, height=3, font=('Arial', 24),
                                command=lambda idx=idx: self.reveal_card(idx))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def reveal_card(self, idx):
        if self.lock or self.revealed[idx]:
            return
        i, j = divmod(idx, 4)
        self.buttons[i][j]['text'] = self.cards[idx]
        self.buttons[i][j]['state'] = 'disabled'
        if self.first is None:
            self.first = idx
        elif self.second is None:
            self.second = idx
            self.root.after(500, self.check_match)

    def check_match(self):
        if self.cards[self.first] == self.cards[self.second]:
            self.revealed[self.first] = True
            self.revealed[self.second] = True
            if all(self.revealed):
                messagebox.showinfo('¡Felicidades!', '¡Has ganado!')
        else:
            for idx in [self.first, self.second]:
                i, j = divmod(idx, 4)
                self.buttons[i][j]['text'] = '?'
                self.buttons[i][j]['state'] = 'normal'
        self.first = None
        self.second = None

if __name__ == '__main__':
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
