# Pedra, papel e tesoura em Python
#importando biblioteca random do python que adiciona funções aleatórias
import random
#loop de repetição onde acontece o jogo infinitamente
while True:
    #opçoes que o bot pode escolher
    opçoes = ['pedra','papel','tesoura']
    #escolha aleatoria do bot
    escolha_bot = random.choice(opçoes)
    #sistema pergunta se vc quer jogar
    input('vamos jogar um jogo?')
    #sistema pergunta sua escolha
    sua_escolha = (input('Pedra,Papel ou Tesoura? '))
    # função que verifica quem ganhou e todas as probabilidades de derrota e vitoria:
    def vitorioso(voce,bot):
        if voce == bot:
            print('você:',sua_escolha,'vs','bot:',escolha_bot,',deu impate')
        if voce == 'pedra' and bot == 'papel':
            print('você:',sua_escolha,'vs','bot:',escolha_bot,',você perdeu')
        if voce == 'papel' and bot == 'tesoura':
            print('você:',sua_escolha,'vs','bot:',escolha_bot,',você perdeu')
        if voce == 'tesoura' and bot == 'pedra':
            print('você:',sua_escolha,'vs','bot:',escolha_bot,',você perdeu')
        if bot == 'pedra' and voce == 'papel':
            print('você:',sua_escolha,'vs','bot:',escolha_bot,',você ganhou')
        if bot == 'papel' and voce == 'tesoura':
            print('você:',sua_escolha,'vs','bot:',escolha_bot,', você ganhou')
        if bot == 'tesouraescolha_bot' and voce == 'pedra':
            print('você:',sua_escolha,'vs','bot:',escolha_bot,'você ganhou')
    # resultado e tentar denovo:
    vitorioso(sua_escolha, escolha_bot)