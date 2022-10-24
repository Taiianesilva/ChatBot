def linhas():
    print("-=" *10)
    
def chatbot ():
    while True:
        linhas() 
        print("Ola, seja bem-vindo(a) ao Cakes mania")
        linhas()
        print(""""
    Opcoes: Escolha UMA:
     1- Ver Cardapio
     2- Ver promocoes
     3- Preço de produtos
     4- Falar com um dos nossos atendentes
     5- Encerrar programa
        """)
        escolha = str(input("Escolha uma opção de 1 a 5:")).lower().strip()
        produtos = ["Bolo brigaderiro", "Bolo ninho", "Bolo baunilha",
                    "Bolo leite moca", "Bolo doce de leite"]
        Promocoes =["Chocolate" , "Agua"]
        preço_produtos =[9.40 , 6.78 , 4.50 , 9.90 , 5.58]
        atendente = "Olá, eu me chamo Tai, e vou dar sequencia ao seu atendimento."
        if  escolha == "1":
            linhas()
            for item in produtos:
                print(item)
            linhas()
        elif escolha == "2":
            linhas()
            for item in Promocoes:
                print(item)
            linhas()
        elif escolha == "3":
            linhas()
            for item in preço_produtos:
                print(item)
            linhas()
        elif escolha == "4":
            linhas()
            print(atendente)
            linhas()
        elif escolha == "5":
            break
        else:
            print("Opção inválida, tente novamente!")
            continue
        
        
        
        
chatbot()