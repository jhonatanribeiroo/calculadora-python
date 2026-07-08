import tkinter as tk
from tkinter import ttk

# CORES DO TEMA
COR_FUNDO = "#1e1e1e"
COR_TELA = "#2d2d2d"
COR_TEXTO = "#ffffff"
COR_BOTAO_NUM = "#3c3c3c"
COR_BOTAO_OP = "#ff9500"  # laranja
COR_BOTAO_IGUAL = "#ff9500"
COR_BOTAO_LIMPAR = "#a5a5a5"
COR_TEXTO_ESCURO = "#000"

# Função dos botões
def clicar(botao):
    texto_atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto_atual + str(botao))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Pro")
janela.geometry("320x450")
janela.resizable(False, False)
janela.configure(bg=COR_FUNDO)

# Tela da calculadora
entrada = tk.Entry(janela, font=("Arial", 28, "bold"), justify="right", 
                   bg=COR_TELA, fg=COR_TEXTO, bd=0, insertbackground=COR_TEXTO)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we", ipady=10)

# Estilo dos botões
def criar_botao(texto, comando, cor_fundo, cor_texto, linha, coluna, col_span=1):
    btn = tk.Button(janela, text=texto, command=comando,
                    bg=cor_fundo, fg=cor_texto,
                    font=("Arial", 18, "bold"), bd=0,
                    activebackground="#555", activeforeground="white",
                    relief="flat", cursor="hand2")
    btn.grid(row=linha, column=coluna, columnspan=col_span, padx=5, pady=5, sticky="nsew", ipady=10)

# Layout dos botões CORRIGIDO
criar_botao("C", limpar, COR_BOTAO_LIMPAR, COR_TEXTO_ESCURO, 1, 0, 4)
criar_botao("7", lambda: clicar(7), COR_BOTAO_NUM, COR_TEXTO, 2, 0)
criar_botao("8", lambda: clicar(8), COR_BOTAO_NUM, COR_TEXTO, 2, 1)
criar_botao("9", lambda: clicar(9), COR_BOTAO_NUM, COR_TEXTO, 2, 2)
criar_botao("/", lambda: clicar('/'), COR_BOTAO_OP, COR_TEXTO, 2, 3) # DIVIDIR

criar_botao("4", lambda: clicar(4), COR_BOTAO_NUM, COR_TEXTO, 3, 0)
criar_botao("5", lambda: clicar(5), COR_BOTAO_NUM, COR_TEXTO, 3, 1)
criar_botao("6", lambda: clicar(6), COR_BOTAO_NUM, COR_TEXTO, 3, 2)
criar_botao("*", lambda: clicar('*'), COR_BOTAO_OP, COR_TEXTO, 3, 3) # VEZES

criar_botao("1", lambda: clicar(1), COR_BOTAO_NUM, COR_TEXTO, 4, 0)
criar_botao("2", lambda: clicar(2), COR_BOTAO_NUM, COR_TEXTO, 4, 1)
criar_botao("3", lambda: clicar(3), COR_BOTAO_NUM, COR_TEXTO, 4, 2)
criar_botao("-", lambda: clicar('-'), COR_BOTAO_OP, COR_TEXTO, 4, 3) # MENOS

criar_botao("0", lambda: clicar(0), COR_BOTAO_NUM, COR_TEXTO, 5, 0, 2)
criar_botao(".", lambda: clicar('.'), COR_BOTAO_NUM, COR_TEXTO, 5, 2)
criar_botao("+", lambda: clicar('+'), COR_BOTAO_OP, COR_TEXTO, 5, 3) # MAIS - ESSE FALTAVA
criar_botao("=", calcular, COR_BOTAO_IGUAL, COR_TEXTO, 6, 0, 4) # IGUAL MAIOR

# Ajusta o tamanho
for i in range(7):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()