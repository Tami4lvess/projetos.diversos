import os
import tkinter as tk
#caminho do arquivo 
pasta = 'c:\\Pyhon'
arquivo = os.path.join (pasta,'exemplo_tkinter.txt')

mensagens =[]
#1.criar pasta se nao existir
if not os.path.exists (pasta):
    os.makedirs(pasta)
    mensagens.append(f"Pasta criada em:{pasta}")

#2.Criar arquiivo e escrever conteudo
f = open(arquivo, "w")
f.write("linha 1: Arquivo criado com tkinter.\n")
f.write("linha 2: Aprendendo Python com interface grafica.\n")
f.close()
mensagens.append("Arquivo criado e conteudo escrito.")

#3. Adicionar nova linha
f = open(arquivo, "a")
f.write("linha 3: conteudo Adicionado depois\n")
f.close()
mensagens.append("linha adicinada ao arquivo.")
#4. Ler o conteudo do arquivo 
f = open(arquivo,"r")
conteudo =f.read()
f.close()
mensagens.append("arquivo lido com sucesso.") 
#5. obter tamanho do arquivo
tamanho = os.path.getsize(arquivo)
mensagens.append(f"tamanho do arquivo:{tamanho}bytes")
mensagens.append(f"caminho completo do arquivo:{arquivo}")

#6. criar janela com tkinter
janela = tk.Tk()
janela.title("manipulacao de arquivo em python")
janela.geometry("600x400")
 
#titulo
titulo = tk.Label(janela, text="resultado a manipulacao de arquivo", font=("arial",14))
titulo.pack(pady=10)

#caixa de texto para exibir informacoes
caixa_texto = tk.Text(janela, wrap=tk.WORD, font =("courier new",10))
caixa_texto.pack(expand= True, fill="both",padx=10,pady=10)
 
#inserir mensagens e conteudo do arquivo na caixa de texto
caixa_texto.insert("1.0","\n".join(mensagens)+"\n\nconteudo do arquivo:\n" + conteudo)
caixa_texto.config(state="disabled")#deixar como somente leitura
 #executar janela
janela.mainloop()
