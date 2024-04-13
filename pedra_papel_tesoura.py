'''cores:
limpo \033[m
vermelho \033[31m
verde \033[32m
amarelo \033[33m'''

import random
inicio = str(input("Deseja iniciar o jogo de pedra papel tesoura(S/N)?")).capitalize()
while inicio == "S":
    opcoes = ["Pedra","Papel","Tesoura"]
    escolha = (random.choice(opcoes))
    jogada = str(input("Digite sua jogada:")).capitalize()
    resultado = jogada, escolha 
    if escolha == jogada:
        print("Você escolheu {} e o computador escolheu {}, tivemos um \033[33mEMPATE\033[m!".format(jogada.lower(),escolha.lower()))
    if resultado == ("Papel", "Pedra"):
        print("Você escolheu papel e o computador escolheu pedra, você \033[32mGANHOU\033[m!")
    if resultado == ("Papel", "Tesoura"):
        print("Você escolheu papel e o computador escolheu tesoura, você \033[31mPERDEU\033[m!")
    if resultado == ("Tesoura", "Papel"):
        print("Você escolheu tesoura e o computador escolheu papel, você \033[32mGANHOU\033[m")
    if resultado == ("Tesoura", "Pedra"):
        print("Você escolheu tesoura e o computador escolheu pedra, você \033[31mPERDEU\033[m!")
    if resultado == ("Pedra", "Tesoura"):
        print("Você escolheu pedra e o computador escolheu tesoura, você \033[32mGANHOU\033[m!")
    if resultado == ("Pedra", "Papel"):
        print("Você escolheu pedra e o computador escolheu papel, você \033[31mPERDEU\033[m!")
    
    inicio = str(input("Deseja jogar novamente(S/N)?")).capitalize()
