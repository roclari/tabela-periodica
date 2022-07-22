import csv

tabela = list(csv.reader(open('elementos-quimicos.csv', encoding="utf-8"), delimiter=","))


def menu(linha=0):
    print('='*150)
    print(f'\033[1;35mSímbolo:\033[m \033[1;36m{tabela[linha][0]}\033[m')
    print(f'\033[1;35mNome:\033[m \033[1;36m{tabela[linha][1]}\033[m')
    print(f'\033[1;35mNúmero atômico:\033[m \033[1;36m{tabela[linha][2]}\033[m')
    print(f'\033[1;35mMassa atômica:\033[m \033[1;36m{tabela[linha][3]}\033[m')
    print(f'\033[1;35mPrótons:\033[m \033[1;36m{tabela[linha][4]}\033[m')
    print(f'\033[1;35mElétrons:\033[m \033[1;36m{tabela[linha][5]}\033[m')
    print(f'\033[1;35mNêutrons:\033[m \033[1;36m{tabela[linha][6]}\033[m')
    print(f'\033[1;35mConfiguração eletrônica:\033[m \033[1;36m{tabela[linha][7]}\033[m')
    print(f'\033[1;35mPeríodo:\033[m \033[1;36m{tabela[linha][8]}\033[m')
    print(f'\033[1;35mGrupo:\033[m \033[1;36m{tabela[linha][9]}\033[m')
    print(f'\033[1;35mEstado da matéria:\033[m \033[1;36m{tabela[linha][10]}\033[m')


def escolhas():
    print('\n\033[1;35mTABELA PERIÓDICA\033[m\n\n\033[1;36mEscolha uma opção:\n[1] Quero ver todos os elementos e seus dados\n[2] Quero buscar um elemento pelo seu símbolo\n[3] Quero buscar um elemento pelo seu nome\n[4] Quero buscar um elemento pelo seu número atômico\n[5] Sair do programa\033[m')


while True:
    escolhas()
    escolha = int(input('\n\033[1;35mDigite sua escolha: \033[m'))
    if(escolha == 5):
        print('\n\033[1;35mPrograma finalizado com sucesso.\033[m')
        break
    if(escolha == 0 or escolha > 5):
        print('\n\033[1;31mDigite uma escolha válida.\033[m')

    if(escolha == 1):
        for linha in tabela:
            print('='*150)
            print(f'\033[1;35mSímbolo:\033[m \033[1;36m{linha[0]}\033[m')
            print(f'\033[1;35mNome:\033[m \033[1;36m{linha[1]}\033[m')
            print(f'\033[1;35mNúmero atômico:\033[m \033[1;36m{linha[2]}\033[m')
            print(f'\033[1;35mMassa atômica:\033[m \033[1;36m{linha[3]}\033[m')
            print(f'\033[1;35mPrótons:\033[m \033[1;36m{linha[4]}\033[m')
            print(f'\033[1;35mElétrons:\033[m \033[1;36m{linha[5]}\033[m')
            print(f'\033[1;35mNêutrons:\033[m \033[1;36m{linha[6]}\033[m')
            print(f'\033[1;35mConfiguração eletrônica:\033[m \033[1;36m{linha[7]}\033[m')
            print(f'\033[1;35mPeríodo:\033[m \033[1;36m{linha[8]}\033[m')
            print(f'\033[1;35mGrupo:\033[m \033[1;36m{linha[9]}\033[m')
            print(f'\033[1;35mEstado da matéria:\033[m \033[1;36m{linha[10]}\033[m')
        print('='*150)

    if(escolha == 2):
        simbolo = input('\033[1;32mDigite o símbolo do elemento: \033[m').lower().title() #.lower().title() ignora o case-sensitive da entrada

        linha = [(i, elementos.index(simbolo)) for i, elementos in enumerate(tabela) if simbolo in elementos]

        if len(linha) > 0:
            menu(linha[0][0])
        else:
            print('\n\033[1;31mSímbolo inválido\033[m\n')
        print('='*150)


    if(escolha == 3):
        nome = input('\033[1;32mDigite o nome do elemento: \033[m').lower().title()

        linha = [(i, elementos.index(nome)) for i, elementos in enumerate(tabela) if nome in elementos]

        if len(linha) > 0:
            menu(linha[0][0])
        else:
            print('\n\033[1;31mNome inválido\033[m\n')

        print('='*150)

    if (escolha == 4):
        numato = input('\033[1;32mDigite o número atômico do elemento: \033[m')

        linha = [(i, elementos.index(numato)) for i, elementos in enumerate(tabela) if numato in elementos]

        if len(linha) > 0:
            for lista in linha:
                if lista[1] == 2:
                    menu(lista[0])
        else:
            print('\n\033[1;31mNúmero atômico inválido\033[m\n')
        print('='*150)