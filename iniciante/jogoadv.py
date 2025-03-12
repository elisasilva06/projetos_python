import random

print("-="*10)
print("ACERTE O NÚMERO!")
print("-="*10)
print("nesse jogo você precisa adivinhar qual número o computador escolheu ...")

while True:
    limite = input("escolha um número de limite : 0 -> ")

    if limite.isdigit():
        limite = int(limite)
        break
    else:
        print("ERRO! digite apenas números...")
        quit

random_number = random.randint(0,limite)   
print("-="*10)
print("vamos começar ...")
tentativas = 0
while True:
    resposta = input("Adivinhe o número: ")
    tentativas = tentativas + 1
    if resposta.isdigit():
        resposta = int(resposta)
    else:
        print("O valor informado não é numérico .Informe um número !")
        continue    

    if resposta == random_number:
        print("acertou !!! ")
        break
    elif resposta > random_number:
        print("o número é menor ...")    
    elif resposta < random_number:
        print("o número é maior ...")    
print("-="*10)
print("Você acertou com {} tentativas".format(tentativas))


    


        

