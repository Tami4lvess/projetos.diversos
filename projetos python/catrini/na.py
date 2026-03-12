import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class JogoDaVelha:

    def __init__(self,root):
        self.root = root
        self.root.title("Jogo Da Velha")

        self.jogador = "X"
        self.buttons = [[None] * 3 for _ in range(3)]
        self.criartabuleiro()

    def criartabuleiro(self):
        for i in range(3):
            for j in range (3):
                btn = tk.Button(
                    self.root,
                    text="",
                    font=("Arial, 40"),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.jogar(i, j)
                )
                btn.grid(row =i, column=j)
                self.buttons[i][j] = btn

    def jogar(self, i, j):
        btn = self.buttons[i][j]
        if btn["text"] == "":
            btn["text"] = self.jogador
            if self.verificar_vencedor():
                messagebox.showinfo("fim de jogo", f"jogador{self.jogador} venceu!!")
                self.salvar_resultado(vencedor=self.jogador)
                self.resetar()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.salvar_resultado(vencedor="empate")
                self.resetar()
            else:
                self.jogador = "O" if self.jogador == "X" else "X"

    def verificar_vencedor(self):
        b = self.buttons
        #verifica linhas
        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != "":
                return True
        #verifica colunas
        for j in range(3):
            if b[0][j]["text"] == b [1][j]["text"] == b[2][j]["text"] != "":
                return True
        #verifica diagonais
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            return True
        return False
    
    def verificar_empate(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False
        return True
    def salvar_resultado(self,vencedor):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tabuleiro = ""

        for i in range(3):
            linha = " | ".join(
                self.buttons[i][j]["text"] if self.buttons[i][j] != "" else " "
                for j in range(3)
            )
            tabuleiro += linha + "\n"
            if i < 2:
                tabuleiro += "---+---+---\n"
            
        resultado = "Data: " +now + "\n"
        resultado += "Vencedor: "+ vencedor + "\n"
        resultado += "Tabuleiro Final: \n" + tabuleiro
        resultado += "=" * 30 + "\n"

        f = open("historico_jogo_da_velha.txt", "a", encoding="utf-8")
        f.write(resultado)
        f.close

    def resetar(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] == ""
            self.jogador = "X"

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()