import random 

user_points = 0
computer_points = 0

options = ["1","2","3"]

while True:
    user_choice = input("Escolha 1 (pedra) / 2 (tesoura) / 3 (papel) ou 0 para sair.")

    if user_choice == "0":
        break

    computer_choice = random.randint(0,2)
    # 0:1 , 1:2 , 2:3
    computer_option  =  options[computer_choice]

    print("o computador escolheu " + computer_option)

    if user_choice == computer_option:
        print("Empate!")
    elif user_choice == "1" and computer_option == "t": 
        print("Você ganhouu !!! ")
        user_points = user_points + 1   
    elif user_choice == "2" and computer_option == "1": 
        print("Você ganhouu !!! ")
        user_points = user_points + 1  
    elif user_choice == "3" and computer_option == "2": 
        print("Você ganhouu !!! ")
        user_points = user_points + 1          
    else:
        print("Você perdeu...") 
        computer_points += 1

print("Sua pontuação: " + user_points)  
print("Pontuação do computador: " + computer_points)

if computer_points > user_points:
    print("Derrota...")
elif computer_points == user_points:
    print("Empate")    
else:
    print("VITORIA!!!")    

print("GOODBYE!!!")