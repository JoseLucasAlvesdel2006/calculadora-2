import tkinter as tk
from tkinter import messagebox
from tkinter import font


def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"A soma é: {resultado}")
    except ValueError:
        messagebox.showerror(
            "Erro", "É obrigatório preencher os campos. Por favor, insira números válidos.")


def subtrair():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        messagebox.showinfo("Resultado", f"A subtração é: {resultado}")
    except ValueError:
        messagebox.showerror(
            "Erro", "É obrigatório preencher os campos. Por favor, insira números válidos.")


def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        messagebox.showinfo("Resultado", f"A multiplicação é: {resultado}")
    except ValueError:
        messagebox.showerror(
            "Erro", "É obrigatório preencher os campos. Por favor, insira números válidos.")


def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 / num2
        messagebox.showinfo(
            "Resultado", f"A divisão dos números é: {resultado}")
    except ValueError:
        messagebox.showerror(
            "Erro", "É obrigatório preencher os campos. Por favor, insira números válidos.")


janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x150")

fonte_padrao = font.Font(size=10)

tk.Label(janela, text="Número 1").grid(row=0, column=0)
entry_num1 = tk.Entry(janela, width=30, font=fonte_padrao)
entry_num1.grid(row=0, column=1)

tk.Label(janela, text="Número 2").grid(row=1, column=0)
entry_num2 = tk.Entry(janela, width=30, font=fonte_padrao)
entry_num2.grid(row=1, column=1)

tk.Button(janela, text="Somar", command=somar).grid(
    row=2, column=0, padx=5, pady=5, sticky="ew")
tk.Button(janela, text="Subtrair", command=subtrair).grid(
    row=2, column=1, padx=5, pady=5, sticky="ew")
tk.Button(janela, text="Multiplicar", command=multiplicar).grid(
    row=3, column=0, padx=5, pady=5, sticky="ew")
tk.Button(janela, text="Dividir", command=dividir).grid(
    row=3, column=1, padx=5, pady=5, sticky="ew")

janela.mainloop()
