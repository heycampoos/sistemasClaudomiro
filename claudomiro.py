#var
m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = m9 = m10 = m11 = m12 = m13 = m14 = m15 = m16 = "00000000"
#menu
while True:
    print()
    escolha_menu = str(input("""\033[34mOlá, seja bem-vindo ao nosso simulador de memória!
Escolha uma opção para começar:
[R]ead data
[W]rite data
[L]ist memory states
[E]xit\033[m\n""")).strip().upper()
    while escolha_menu not in "RWLE":
        escolha_menu = str(input('''\033[31mOPA! Parece que algo deu errado!\033[m
\033[35mVamos tentar de novo. Responda apenas com a opção do menu acima!\033[m''')).upper()

    #para a opçao de listar os dados
    if escolha_menu == "L":
        print(f"""Os estados atuais da memória são:
              \033[33m{m1}
              {m2}
              {m3}
              {m4}
              {m5}
              {m6}
              {m7}
              {m8}
              {m9}
              {m10}
              {m11}
              {m12}
              {m13}
              {m14}
              {m15}
              {m16}\033[m""")

    #para a opção de ler um espaço de memória
    if escolha_menu == "R":
        print()
        escolha_lerEspaco = str(input("""\033[35mMuito legal sua escolha!
Agora, por favor, insira o endereço que deseja ler (em forma binária de 4 bits)\033[m\n"""))
        while len(escolha_lerEspaco) < 4 or len(escolha_lerEspaco) > 4:
            escolha_lerEspaco = str(input("""\033[31mOPA! ALGO DEU ERRADO!
Certifique-se se o seu endereço tem 4 bits e está em binário. Tente de novo\033[m\n"""))
        if escolha_lerEspaco == "0000":
            print(f"\033[33mA memória para {escolha_lerEspaco} está agora como {m1}")
        elif escolha_lerEspaco == "0001":
            print(f"A memória para {escolha_lerEspaco} está agora como {m2}")
        elif escolha_lerEspaco == "0010":
            print(f"A memória para {escolha_lerEspaco} está agora como {m3}")
        elif escolha_lerEspaco == "0011":
            print(f"A memória para {escolha_lerEspaco} está agora como {m4}")
        elif escolha_lerEspaco == "0100":
            print(f"A memória para {escolha_lerEspaco} está agora como {m5}")
        elif escolha_lerEspaco == "0101":
            print(f"A memória para {escolha_lerEspaco} está agora como {m6}")
        elif escolha_lerEspaco == "0110":
            print(f"A memória para {escolha_lerEspaco} está agora como {m7}")
        elif escolha_lerEspaco == "0111":
            print(f"A memória para {escolha_lerEspaco} está agora como {m8}")
        elif escolha_lerEspaco == "1000":
            print(f"A memória para {escolha_lerEspaco} está agora como {m9}")
        elif escolha_lerEspaco == "1001":
            print(f"A memória para {escolha_lerEspaco} está agora como {m10}")
        elif escolha_lerEspaco == "1010":
            print(f"A memória para {escolha_lerEspaco} está agora como {m11}")
        elif escolha_lerEspaco == "1011":
            print(f"A memória para {escolha_lerEspaco} está agora como {m12}")
        elif escolha_lerEspaco == "1100":
            print(f"A memória para {escolha_lerEspaco} está agora como {m13}")
        elif escolha_lerEspaco == "1101":
            print(f"A memória para {escolha_lerEspaco} está agora como {m14}")
        elif escolha_lerEspaco == "1100":
            print(f"A memória para {escolha_lerEspaco} está agora como {m15}")
        elif escolha_lerEspaco == "1111":
            print(f"A memória para {escolha_lerEspaco} está agora como {m16}\033[m")

    #para a opçao de escrever um dado na memória
    if escolha_menu == "W":

        escolha_endereco = str(input("""\033[33mÓtima escolha, companheiro!
Por favor, insira o endereço, na forma de 4 bits: """))
        while len(escolha_endereco) < 4 or len(escolha_endereco) > 4:
            escolha_endereco = str(input("""\033[31mOPA! Algo deu errado!
    Certifique-se que seu dado tem 4 bits e tente novamente!\n"""))
        escolha_dados = str(input("Agora, por favor, o seu dado em forma de 8 bits: "))
        while len(escolha_dados) < 8 or len(escolha_dados) > 8:
            escolha_dados = str(input("""\033[31mOPA! Algo deu errado!
Certifique-se que seu dado tem 8 bits e tente novamente!\n"""))
        if escolha_endereco == "0000":
            m1 = escolha_dados
        elif escolha_endereco == "0001":
            m2 = escolha_dados
        elif escolha_endereco == "0010":
            m3 = escolha_dados
        elif escolha_endereco == "0011":
            m4 = escolha_dados
        elif escolha_endereco == "0100":
            m5 = escolha_dados
        elif escolha_endereco == "0101":
            m6 = escolha_dados
        elif escolha_endereco == "0110":
            m7 = escolha_dados
        elif escolha_endereco == "0111":
            m8 = escolha_dados
        elif escolha_endereco == "1000":
            m9 = escolha_dados
        elif escolha_endereco == "1001":
            m10 = escolha_dados
        elif escolha_endereco == "1010":
            m11 = escolha_dados
        elif escolha_endereco == "1011":
            m12 = escolha_dados
        elif escolha_endereco == "1100":
            m13 = escolha_dados
        elif escolha_endereco == "1101":
            m14 = escolha_dados
        elif escolha_endereco == "1100":
            m15 = escolha_dados
        elif escolha_endereco == "1111":
           m16 = escolha_dados

#para parar o programa
    if escolha_menu == "E":
        print("\033[33mIsso é um adeus? Obrigado por usar este programa! :'(")
        break