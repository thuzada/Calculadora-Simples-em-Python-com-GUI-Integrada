import tkinter as tk
from tkinter import Toplevel
from math import sqrt, pow

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("320x420")
        self.master.resizable(False, False)
        self.master.configure(bg="#f0f0f0")
        self.historico = []
        self.tema_claro = True

        self.create_widgets()
        self.master.bind("<Key>", self.key_press)

    def create_widgets(self):
        # Display
        self.entry = tk.Entry(self.master, width=20, font=("Arial", 18), justify="right", bg="white", fg="black")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")
        
        # Botões
        buttons = [
            "Tema",
             "√", "x²", "Hist",
             "/","7","8","9",
             "*","4","5","6",
             "-","1","2","3", 
             "+","C","0","=", 
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            
            tk.Button(self.master, text=button, width=5, height=2, font=("Arial", 14), bg="#e6e6e6", fg="black",
                      command=lambda b=button: self.on_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configuração de peso para responsividade
        for i in range(5):
            self.master.rowconfigure(i, weight=1)
            self.master.columnconfigure(i, weight=1)

    def on_click(self, button_text):
        if button_text == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.historico.append(f"{expression} = {result}")
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif button_text == "C":
            self.entry.delete(0, tk.END)
        elif button_text == "√":
            try:
                num = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(sqrt(num)))
            except:
                self.entry.insert(tk.END, "Erro")
        elif button_text == "x²":
            try:
                num = float(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(pow(num, 2)))
            except:
                self.entry.insert(tk.END, "Erro")
        elif button_text == "Hist":
            self.exibir_historico()
        elif button_text == "Tema":
            self.alternar_tema()
        else:
            self.entry.insert(tk.END, button_text)

    def exibir_historico(self):
        top = Toplevel(self.master)
        top.title("Histórico")
        top.geometry("300x200")
        top.configure(bg="#f0f0f0")
        tk.Label(top, text="Histórico de cálculos", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
        historico_text = "\n".join(self.historico[-10:])
        tk.Label(top, text=historico_text, font=("Arial", 12), bg="#f0f0f0", justify="left").pack(pady=10)

    def alternar_tema(self):
        if self.tema_claro:
            self.master.configure(bg="#2c2c2c")
            self.entry.configure(bg="#3c3c3c", fg="white")
            self.tema_claro = False
        else:
            self.master.configure(bg="#f0f0f0")
            self.entry.configure(bg="white", fg="black")
            self.tema_claro = True

    def key_press(self, event):
        if event.char.isdigit() or event.char in "+-*/.":
            self.entry.insert(tk.END, event.char)
        elif event.keysym == "Return":
            self.on_click("=")
        elif event.keysym == "BackSpace":
            self.entry.delete(len(self.entry.get()) - 1, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
