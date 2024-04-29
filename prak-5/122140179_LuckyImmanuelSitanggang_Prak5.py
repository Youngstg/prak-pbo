import tkinter as tk
import random
from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def __reset_game(self):
        pass

    @abstractmethod
    def play(self):
        pass

class TebakAngka(Game):
    def __init__(self, master):
        self.master = master
        self.master.title("Game Tebak Angka")
        self.master.configure(bg='lightblue')
        self.master.geometry("500x300") 
        self.__reset_game()

        self.label = tk.Label(self.master, text="TEBAK GAMBAR", fg="white", bg='midnight blue', font=('Calibri', 20))
        self.label.pack(pady=15)

        self.label = tk.Label(self.master, text="Masukkan angka antara 1 dan 100:", bg='lightblue', font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, textvariable=self.__tebakan, font=('Helvetica', 14))
        self.entry.pack(pady=10)

        self.button = tk.Button(self.master, text="Tebak", command=self.play, bg='green', fg='white', font=('Helvetica', 14))
        self.button.pack(pady=10)

        self.result = tk.Label(self.master, text="", bg='lightblue', font=('Helvetica', 14))
        self.result.pack(pady=10)

    def __reset_game(self):
        self.__angka_rahasia = random.randint(1, 100)
        self.__tebakan = tk.IntVar()

    def play(self):
        tebakan = self.__tebakan.get()
        if tebakan < self.__angka_rahasia:
            self.result.config(text="Terlalu rendah!", fg='red')
        elif tebakan > self.__angka_rahasia:
            self.result.config(text="Terlalu tinggi!", fg='red')
        else:
            self.result.config(text="Tebakan Anda benar! Game akan dimulai lagi.", fg='green')
            self.__reset_game() 

root = tk.Tk()
game = TebakAngka(root)
root.mainloop()
