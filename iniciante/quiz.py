print("-"*30)
print("BEM-VINDO AO QUIZ ")
print("-"*30)
opc = 0
historia = 0
literatura = 0
biologia = 0
geografia = 0
fisica = 0
nota_h = fim_h = 0
nota_l = fim_l = 0

while opc != 6:
     print(" [1]HISTÓRIA \n [2]LITERATURA \n [3]BIOLOGIA \n [4]GEOGRAFIA \n [5]FISICA \n [6]SAIR DA LISTA")
     print("-"*30)
     opc = int(input("Escolha a sua área: "))
     print("-"*30)
     if fim_h == 1 :
         while opc == 1 :
             print("voce ja respondeu esse quiz , tente novamente")
             opc = int(input("Escolha a sua área: "))
             print("-"*30)     
     if fim_l == 1 :
         while opc == 2 :
             print("voce ja respondeu esse quiz , tente novamente")
             opc = int(input("Escolha a sua área: "))
             print("-"*30)         

     match opc:
         case 1:
             print("Quem foi o primeiro imperador romano? \n [1]Julio Cesar \n [2]Augusto \n [3]Nero \n [4]Trajano")
             resp1 = int(input("resposta = "))
             if resp1 == 2:
                 print("correto!")
                 nota_h = nota_h + 1
             else :
                 print("incorreto")
             print("-"*30) 
             print("Qual foi a principal causa da Primeira Guerra Mundial? \n [1]A Revolução Industrial \n [2]O assassinato do arquiduque Francisco Ferdinando \n [3]A disputa por territórios coloniais \n [4]O fim do Império Austro-Húngaro")
             resp1 = int(input("resposta = "))
             if resp1 == 2:
                 print("correto!")
                 nota_h = nota_h + 1
             else :
                 print("incorreto")
             print("-"*30) 
             print("Onde e quando ocorreu a Batalha de Waterloo? \n [1]França, 1812 \n [2]Bélgica, 1815 \n [3]Alemanha, 1805 \n [4]Reino Unido, 1818")
             resp1 = int(input("resposta = "))
             if resp1 == 2:
                 print("correto!")
                 nota_h = nota_h + 1
             else :
                 print("incorreto")
             print("-"*30)
             print("Quem foi o líder da Revolução Francesa e como ele influenciou a história? \n [1]Robespierre, instaurando o Terror \n [2]Napoleão Bonaparte, coroando-se imperador \n [3]Luís XVI, que fugiu para a Áustria \n [4]Voltaire, defendendo a liberdade de expressão")
             resp1 = int(input("resposta = "))
             if resp1 == 1:
                 print("correto!")
                 nota_h = nota_h + 1
             else :
                 print("incorreto")
             print("-"*30)                              
             print("Qual foi o impacto da descoberta das Américas para os povos indígenas? \n [1]Grande desenvolvimento cultural e tecnológico \n [2]Estabelecimento de novas alianças comerciais com a Europa \n [3]Mortes em massa devido a doenças e escravidão \n [4]Crescimento da população indígena com novas técnicas agrícolas")
             resp1 = int(input("resposta = "))
             if resp1 == 3:
                 print("correto!")
                 nota_h = nota_h + 1
             else :
                 print("incorreto")
             print("-"*30)
             print("VOCE FINALIZOU O QUIZ DE HISTÓRIA")
             fim_h = 1
             print("-"*30)
         case 2:
             print("Quem escreveu Dom Quixote \n [1]Gabriel García Márquez \n [2]Miguel de Cervantes \n [3]William Shakespeare \n [4]Leo Tolstoy")
             resp1 = int(input("resposta = "))
             if resp1 == 2:
                 print("correto!")
                 nota_l = nota_l + 1
             else :
                 print("incorreto")
             print("-"*30)              
             print("Qual é o nome do protagonista de Moby Dick? \n [1]Ahab \n [2]Ishmael \n [3]Huck Finn \n [4]Robinson Crusoe")
             resp1 = int(input("resposta = "))
             if resp1 == 2:
                 print("correto!")
                 nota_l = nota_l + 1
             else :
                 print("incorreto")
             print("-"*30)              
             print("Em qual obra aparece o personagem Sherlock Holmes? \n [1]O Guia do Mochileiro das Galáxias \n [2]O Grande Gatsby \n [3]As Aventuras de Sherlock Holmes \n [4]Drácula")
             resp1 = int(input("resposta = "))
             if resp1 == 3:
                 print("correto!")
                 nota_l = nota_l + 1
             else :
                 print("incorreto")
             print("-"*30)
             print("Quem escreveu A Moreninha, considerado um\n dos primeiros romances do romantismo brasileiro? \n [1]José de Alencar \n [2]Machado de Assis \n [3]Joaquim Manuel de Macedo \n [4]Raul Pompeia")
             resp1 = int(input("resposta = "))
             if resp1 == 3:
                 print("correto!")
                 nota_l = nota_l + 1
             else :
                 print("incorreto")
             print("-"*30)            
             print("Qual desses livros foi escrito por Franz Kafka? \n [1]O Processo \n [2]Crime e Castigo \n [3]O Primo Basílio \n [4]Os Miseráveis")
             resp1 = int(input("resposta = "))
             if resp1 == 1:
                 print("correto!")
                 nota_l = nota_l + 1
             else :
                 print("incorreto")
             print("-"*30) 
             print("VOCE FINALIZOU O QUIZ DE LITERATURA")
             fim_l = 1
             print("-"*30)          