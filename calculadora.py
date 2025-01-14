import tkinter as tk
from tkinter import Toplevel
from math import sqrt, pow

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("375x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#000000")
        self.historico = []
        self.tema_claro = False

        self.create_widgets()
        self.master.bind("<Key>", self.key_press)

    def create_widgets(self):
        # Display
        self.entry = tk.Entry(self.master, width=17, font=("Arial", 24), justify="right", bg="#000000", fg="white", bd=0, highlightthickness=0)
        self.entry.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="nsew")

        # Buttons
        buttons = [
            'C', 'CE', '√', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '^', '='
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            
            if button in ['=']:
                bg_color = "#ff0000"
            else:
                bg_color = "#333333"
            tk.Button(self.master, text=button, width=5, height=2, command=action, bg=bg_color, fg="white", font=("Arial", 18), bd=0, highlightthickness=0).grid(row=row_val, column=col_val, pady=5, padx=5, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Adjust the 0 button to span two columns
        self.master.grid_rowconfigure(5, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        tk.Button(self.master, text='0', width=5, height=2, command=lambda: self.click_event('0'), bg="#333333", fg="white", font=("Arial", 18), bd=0, highlightthickness=0).grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky="nsew")

    def click_event(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.entry.get().replace('√', 'sqrt').replace('^', '**'))
                self.historico.append(self.entry.get() + " = " + str(result))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif button_text == "C":
            self.entry.delete(0, tk.END)
        elif button_text == "CE":
            self.entry.delete(len(self.entry.get())-1, tk.END)
        elif button_text == "√":
            self.entry.insert(tk.END, "√")
        elif button_text == "^":
            self.entry.insert(tk.END, "^")
        else:
            self.entry.insert(tk.END, button_text)

    def key_press(self, event):
        if event.char.isdigit() or event.char in "+-*/.=":
            self.click_event(event.char)
        elif event.keysym == "Return":
            self.click_event("=")
        elif event.keysym == "BackSpace":
            self.entry.delete(len(self.entry.get())-1, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()