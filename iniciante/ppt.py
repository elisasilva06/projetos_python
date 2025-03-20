import random 

user_points = 0
computer_points = 0

options = ["1","2","3"]

print("-="*15)
print("BEM-VINDO AO JOGO DE ...")
print("PEDRA , PAPEL E TESOURA ")
print("-="*15)

while True:
    user_choice = input("Escolha : \n 1 (pedra) \n 2 (tesoura) \n 3 (papel) \n 0 para encerrar \n digite sua resposta: ")

    if user_choice == "0":
        break
    if user_choice not in options:
        print("Escolha inválida! Tente novamente.")
        continue    

    computer_choice = random.randint(0,2)
    # 0:1 , 1:2 , 2:3
    computer_option  =  options[computer_choice]

    if computer_option == "1":
        print("O computador escolheu PEDRA")
    elif computer_option == "2":
        print("O computador escolheu TESOURA")
    else:
        print("O computador escolheu PAPEL")

    if user_choice == "1":
        print("Você escolheu PEDRA")
    elif user_choice == "2":
        print("Você escolheu TESOURA")
    else:
        print("Você escolheu PAPEL")                


    if user_choice == computer_option:
        print("Empate!")
    elif user_choice == "1" and computer_option == "2": 
        print("<<< Você ganhouu !!! >>>")
        user_points = user_points + 1   
    elif user_choice == "2" and computer_option == "3": 
        print("<<< Você ganhouu !!! >>>")
        user_points = user_points + 1  
    elif user_choice == "3" and computer_option == "1": 
        print("<<< Você ganhouu !!! >>>")
        user_points = user_points + 1          
    else:
        print("--- Você perdeu... ---") 
        computer_points += 1

print("Sua pontuação: " , user_points)  
print("Pontuação do computador: " , computer_points)

if computer_points > user_points:
    print("Derrota...")
elif computer_points == user_points:
    print("Empate")    
else:
    print("VITORIA!!!")    

print("GOODBYE!!!")