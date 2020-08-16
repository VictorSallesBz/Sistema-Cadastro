from random import randint
from os import system
from os import name

# Cores para usar no print
COLOR_MENU = "\033[;1m\033[0;32m"
COLOR_ERROR = "\033[;1m\033[1;31m"
COLOR_ITEM = "\033[1;34m"
COLOR_INPUT = "\033[1;33m"
COLOR_RESET = "\033[0;0m"


# Banco de dados.
database = []


# Define o comando clear para limpar o terminal de acordo com o sistema operacional.
if name == 'nt':
    clear = 'cls'
else:
    clear = 'clear'


# Banners para deixar mais bonitinho kçkçkçkç
def banner():
    system(clear)
    n = randint(1, 5)
    if n == 1:
        print(COLOR_ITEM +
              " ______      # ______      # ______    # ______      # ______       # _________  # ______      #\n"
              "/_____/\     #/_____/\     #/_____/\   #/_____/\     #/_____/\      #/________/\ #/_____/\     #\n"
              "\::::_\/_    #\::::_\/_    #\:::_ \ \  #\:::_ \ \    #\:::_ \ \     #\__.::.__\/ #\::::_\/_    #\n"
              " \:\/___/\   # \:\/___/\   # \:(_) \ \ # \:\ \ \ \   # \:(_) ) )_   #   \::\ \   # \:\/___/\   #\n"
              "  \::___\/_  #  \_::._\:\  #  \: ___\/ #  \:\ \ \ \  #  \: __ `\ \  #    \::\ \  #  \::___\/_  #\n"
              "   \:\____/\ #    /____\:\ #   \ \ \   #   \:\_\ \ \ #   \ \ `\ \ \ #     \::\ \ #   \:\____/\ #\n"
              "    \_____\/ #    \_____\/ #    \_\/   #    \_____\/ #    \_\/ \_\/ #      \__\/ #    \_____\/ #\n"
              "             ##            ##          ##            ##             ##           ##            ##"
              + COLOR_RESET)
    elif n == 2:
        print(COLOR_ITEM +
              " _______      _______..______     ______   .______      .___________. _______ \n"
              "|   ____|    /       ||   _  \   /  __  \  |   _  \     |           ||   ____|\n"
              "|  |__      |   (----`|  |_)  | |  |  |  | |  |_)  |    `---|  |----`|  |__ \n"
              "|   __|      \   \    |   ___/  |  |  |  | |      /         |  |     |   __| \n"
              "|  |____ .----)   |   |  |      |  `--'  | |  |\  \----.    |  |     |  |____ \n"
              "|_______||_______/    | _|       \______/  | _| `._____|    |__|     |_______|\n"
              + COLOR_RESET)

    elif n == 3:
        print(COLOR_ITEM +
              'ooooooooooo  oooooooo8  oooooooooo    ooooooo   oooooooooo  ooooooooooo ooooooooooo \n'
              '888        888          888    888 o888   888o  888    888     888      888      \n'
              '888ooo8     888oooooo   888oooo88  888     888  888oooo88      888      888ooo8 \n'    
              '888                888  888        888o   o888  888  88o       888      888     \n'  
              'o888ooo8888 o88oooo888  o888o         88ooo88   o888   88o     o888o    o888ooo8888 \n'
              + COLOR_RESET)

    elif n == 4:
        print(COLOR_ITEM +
              " _______   _______   _______   _______   _______  _________  _______ \n"
              "(  ____ \ (  ____ \ (  ____ ) (  ___  ) (  ____ ) \__   __/ (  ____ \n"
              "| (    \/ | (    \/ | (    )| | (   ) | | (    )|    ) (    | (    \/ \n"
              "| (__     | (_____  | (____)| | |   | | | (____)|    | |    | (__ \n"
              "|  __)    (_____  ) |  _____) | |   | | |     __)    | |    |  __) \n"
              "| (             ) | | (       | |   | | | (\ (       | |    | ( \n"
              "| (____/\ /\____) | | )       | (___) | | ) \ \__    | |    | (____/\ \n"
              "(_______/ \_______) |/        (_______) |/   \__/    )_(    (_______/ \n"
              + COLOR_RESET)

    elif n == 5:
        print(COLOR_ITEM +
              "(_)(_)(_)(_)(_)   _(_)(_)(_)(_)_   (_)(_)(_)(_)_    _(_)(_)(_)(_)_   (_)(_)(_)(_) _   (_)(_)(_)(_)(_)  (_)(_)(_)(_)(_)\n"
              "(_)              (_)          (_)  (_)        (_)  (_)          (_)  (_)         (_)        (_)        (_)  \n"
              "(_) _  _         (_)_  _  _  _     (_) _  _  _(_)  (_)          (_)  (_) _  _  _ (_)        (_)        (_) _  _  \n"
              "(_)(_)(_)          (_)(_)(_)(_)_   (_)(_)(_)(_)    (_)          (_)  (_)(_)(_)(_)           (_)        (_)(_)(_)  \n"
              "(_)               _           (_)  (_)             (_)          (_)  (_)   (_) _            (_)        (_)     \n"
              "(_) _  _  _  _   (_)_  _  _  _(_)  (_)             (_)_  _  _  _(_)  (_)      (_) _         (_)        (_) _  _  _  _  \n"
              "(_)(_)(_)(_)(_)    (_)(_)(_)(_)    (_)               (_)(_)(_)(_)    (_)         (_)        (_)        (_)(_)(_)(_)(_)   \n"
              + COLOR_RESET)


# Tela de menu principal
def menu():
    system(clear)
    escolha = 0
    while escolha < 1 or escolha > 4:
        banner()
        print(COLOR_MENU + "O que você deseja fazer?\n"
              "1 - Inserir\n"
              "2 - Remover\n"
              "3 - Imprimir\n"
              "4 - Sair\n" + COLOR_RESET)
        try:
            escolha = int(input(COLOR_INPUT + "Selecionar: " + COLOR_RESET))
            system(clear)
        except:
            print(COLOR_ERROR + "Digite apenas números!" + COLOR_RESET)

    return escolha


# Tratamento de erros dos dados inseridos pelos usuários.
def tratamento_erro():
    system(clear)
    while True:
        try:
            escolha = int(input(COLOR_MENU + "Entrada inválida, deseja tentar de novo?\n"
                                         "1 - Quero tentar de novo.\n"
                                         "2 - Voltar ao menu inicial. Todos os dados inseridos anteriormente serão perdidos!" + COLOR_RESET))
            system(clear)
            return escolha
        except:
            continue


# Trata a entrada de esportes, paises e características.
# Recebe a string digitada pelo usuário e retorna uma lista com as palavras escolhidas.
def tratamento_alpha(entrada):
    palavra = []
    saida = []

    if entrada[-1] != ';':
        entrada += ';'
    for x in entrada:
        if x == ';':
            if palavra:
                aux = ''.join(palavra).lower().capitalize()
                saida.append(aux)
                palavra = []
        else:
            palavra.append(x)
    return saida


# Trata entrada de números para adição de características e exibicao.
# Recebe a string digitada pelo usuário e retorna uma lista com os números escolhidos.
def tratamento_numero(entrada):
    numero = []
    saida = []

    if not entrada:
        return tratamento_erro()

    if entrada[-1] != ';':
        entrada += ';'
    for x in entrada:
        if x.isnumeric():
            numero.append(x)
        elif numero and x == ';':
            numero_str = ''.join(numero)
            num = int(numero_str)
            saida.append(num)
            numero = []
        else:
            return tratamento_erro()
    return saida


# Retorna uma lista de características escolhidas.
def tratar_caracteristicas():
    system(clear)
    # Ao inserir ou remover modalidades, tomar cuidado com a posição dela no Menu
    modalidades = ['Aquático', 'Velocidade', 'Bola', 'Força', 'Luta', 'Atletismo', 'Inteligência', 'E-sport', 'Quadra',
                   'Praia', 'Campo', 'Mão', 'Pé', 'Rede', 'Veículo', 'Autódromo', 'Urbano', 'Radical', 'Arma', 'Neve',
                   'Gelo', 'Taco', 'Tecnológico', 'Ginástica']
    # Armazena as características escolhidas
    caracteristicas = []
    print(COLOR_MENU + "Selecione as características do esporte separadas por ponto e vírgula ';'!\n"
          "1 - Aquático                 11 - Campo                  21 - Gelo        \n"
          "2 - Velocidade               12 - Mão                    22 - Taco        \n"
          "3 - Bola                     13 - Pé                     23 - Tecnológico \n"
          "4 - Força                    14 - Rede                   24 - Ginástica   \n"
          "5 - Luta                     15 - Veículo                                 \n"
          "6 - Atletismo                16 - Autódromo                               \n"
          "7 - Inteligência             17 - Urbano                                  \n"
          "8 - E-sport                  18 - Radical                                 \n"
          "9 - Quadra                   19 - Arma                                    \n"
          "10 - Praia                   20 - Neve                                    \n" + COLOR_RESET)
    escolha = input(COLOR_INPUT + "Exemplo -> Aquático, Praia e Mão: 1;10;12;\n" + COLOR_RESET)
    numeros = tratamento_numero(escolha)
    if numeros == 1:
        return tratar_caracteristicas()
    elif numeros == 0:
        return 0

    numeros.sort()
    for n in numeros:
        if (n < 1) or (n > 24):
            erro = tratamento_erro()
            if erro == 1:
                return tratar_caracteristicas()
            else:
                return 0
        else:
            if modalidades[n - 1] not in caracteristicas:
                caracteristicas.append(modalidades[n - 1])

    return caracteristicas


# Insere esporte
def inserir():
    item = {}

    while True:
        system(clear)
        esporte = input(COLOR_INPUT + "Qual esporte deseja adicionar? " + COLOR_RESET).lower().capitalize()
        if esporte and ';' not in esporte:
            for x in database:
                if esporte == x['Esporte']:
                    print(COLOR_ERROR + "Esporte já cadastrado!\n" + COLOR_RESET)
                    input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)
                    return
            break
        else:
            print(COLOR_ERROR + "Digite uma entrada válida para o esporte!\n\n" + COLOR_RESET)
            input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)

    while True:
        system(clear)
        try:
            ano = int(input(COLOR_INPUT + "Qual o ano de criação do esporte? " + COLOR_RESET))
            system(clear)
            break
        except:
            print(COLOR_ERROR + "Ano precisa ser um número!\n\n" + COLOR_RESET)
            input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)

    while True:
        system(clear)
        pais = input(COLOR_INPUT + "Qual o pais de origem? " + COLOR_RESET).lower().capitalize()
        if not pais:
            pais = 'Desconhecido'
        if pais and ';' not in pais:
            break
        else:
            print(COLOR_ERROR + "Digite uma entrada válida para o esporte!\n\n" + COLOR_RESET)
            input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)

    system(clear)
    caracteristicas = tratar_caracteristicas()

    if caracteristicas == 0:
        print(COLOR_ITEM + "Inserção cancelada!\n" + COLOR_RESET)
        input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)
        return

    else:
        system(clear)
        # Overview e confirmação de inserção de esporte
        escolha = 0
        while escolha < 1 or escolha > 3:
            print(COLOR_MENU + "Confirme os dados para inserção\n" + COLOR_RESET)
            print(COLOR_ITEM + "Esporte: ", esporte,
                  "\nAno de Criação: ", ano,
                  "\nPaís de origem: ", pais,
                  "\nCaracterísticas do esporte: " + COLOR_RESET, end='')
            for x in caracteristicas:
                if x != caracteristicas[-1]:
                    print(COLOR_ITEM + x, ", " + COLOR_RESET, end=' ')
                else:
                    print(COLOR_ITEM + x + COLOR_RESET)
            print(COLOR_MENU + "\nDeseja confirmar?\n"
                               "1 - Confirmar\n"
                               "2 - Refazer\n"
                               "3 - Cancelar\n" + COLOR_RESET)
            try:
                escolha = int(input(COLOR_INPUT + "Selecionar: " + COLOR_RESET))
                system(clear)
            except:
                print(COLOR_ERROR + "Digite apenas números!\n" + COLOR_RESET)

            if escolha == 1:
                item['Esporte'] = esporte
                item['Ano de Criação'] = ano
                item['País de Origem'] = pais
                item['Características'] = caracteristicas
                database.append(item)
                print(COLOR_ITEM + "Inserção Completa" + COLOR_RESET)
            elif escolha == 2:
                inserir()
            elif escolha == 3:
                print(COLOR_ITEM + "Nenhum dado foi inserido!" + COLOR_RESET)
                input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)


# Pega esportes com os nomes digitados pelo usuario
def pegar_esportes():
    system(clear)
    esportes = []

    esportes_escolhidos = input(COLOR_INPUT + "Digite os esportes?\n\n"
                                              "Exemplo: Futebol;Basquete;Surf\n" + COLOR_RESET)
    system(clear)
    escolha = tratamento_alpha(esportes_escolhidos)

    if type(escolha) == int:
        if escolha == 1:
            return pegar_esportes()
        else:
            return 0
    for esporte in database:
        for y in escolha:
            if esporte['Esporte'] == y:
                esportes.append(esporte)
                break

    return esportes


# Pega esportes que tiveram origem nos anos digitados pelo usuário
def pegar_ano_origem():
    system(clear)
    esportes = []
    anos_escolhidos = input(COLOR_INPUT + "Digite os anos que originaram os esportes?\n\n"
                                          "Exemplo: 1387;1912;2014;\n" + COLOR_RESET)
    system(clear)
    anos = tratamento_numero(anos_escolhidos)

    if anos == 1:
        return pegar_ano_origem()
    elif anos == 0:
        return 0
    else:
        for esporte in database:
            for ano in anos:
                if esporte['Ano de Criação'] == ano:
                    esportes.append(esporte)
                    break

    return esportes


# Pega esportes que foram originados nos países digitados pelo usuário
def pegar_paises_origem():
    system(clear)
    esportes = []

    paises_escolhidos = input(COLOR_INPUT + "Digite os países de origem dos esportes?\n\n"
                                            "Exemplo: Brasil;Inglaterra;Coréia do Sul;\n" + COLOR_RESET)
    system(clear)
    paises = tratamento_alpha(paises_escolhidos)

    if type(paises) == int:
        if paises == 1:
            return pegar_paises_origem()
        else:
            return 0

    for esporte in database:
        for pais in paises:
            if esporte['País de Origem'] == pais:
                esportes.append(esporte)
                break

    return esportes


# Pega esportes que contenham as características digitadas pelo usuário
def pegar_caracteristicas():
    system(clear)
    esportes = []

    caracteristicas = tratar_caracteristicas()
    if caracteristicas == 0:
        return 0

    system(clear)
    operador = input(COLOR_INPUT + "1 - Contenha pelo menos 1 característica \n"
                                   "2 - Contenha todas essas características \n" + COLOR_RESET)
    system(clear)
    if operador == '1':
        for esporte in database:
            for x in esporte['Características']:
                for y in caracteristicas:
                    if x == y and esporte not in esportes:
                        esportes.append(esporte)
                        break
    elif operador == '2':
        for esporte in database:
            if esporte['Características'] == caracteristicas:
                esportes.append(esporte)

    return esportes


# Exibe menu para o usuário escolher baseado em que os esportes devem ser excluídos.
def menu_remover():
    escolha = 0
    while escolha < 1 or escolha > 5:
        system(clear)
        print(COLOR_MENU + "1 - Remover esportes pelo nome\n"
                           "2 - Remover esportes pelo ano de criação\n"
                           "3 - Remover esportes pelo país de origem\n"
                           "4 - Remover esportes pelas características\n"
                           "5 - Voltar\n" + COLOR_RESET)
        try:
            escolha = int(input(COLOR_INPUT + "Selecionar: " + COLOR_RESET))
        except:
            print(COLOR_ERROR + "Escolha precisa ser um número!\n" + COLOR_RESET)
            input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)
    return escolha


# Remove esporte que coincidem com a pesquisa.
# Recebe uma lista com os dicionarios de esportes e remove do database.
def remover(esportes):
    system(clear)
    if esportes:
        print(COLOR_MENU + "Esportes removidos!\n" + COLOR_RESET)
        for esporte in esportes:
            print(COLOR_ITEM + esporte["Esporte"] + '\n' + COLOR_RESET)
            database.remove(esporte)
    else:
        print(COLOR_ERROR + "Nenhum esporte encontrado!\n\n" + COLOR_RESET)
    input(COLOR_INPUT + "Pressione ENTER para voltar ao menu inicial: " + COLOR_RESET)


# Função principal para remoção
def principal_remover():
    escolha = menu_remover()

    if escolha == 1:
        esportes = pegar_esportes()
    elif escolha == 2:
        esportes = pegar_ano_origem()
    elif escolha == 3:
        esportes = pegar_paises_origem()
    elif escolha == 4:
        esportes = pegar_caracteristicas()
    else:
        return

    if esportes != 0:
        remover(esportes)


# Exibe os esportes que coincidem com a pesquisa.
# Recebe uma lista com os dicionarios de esportes e printa.
def exibir(esportes):
    system(clear)
    if esportes:
        for esporte in esportes:
            print(COLOR_ITEM + "Esporte: ", esporte['Esporte'], "\n"
                  "Ano de Criação: ", esporte['Ano de Criação'], "\n"
                  "País de origem: ", esporte['País de Origem'], "\n"
                  "Características do esporte: " + COLOR_RESET, end='')
            caracteristicas = esporte['Características']
            for caracteristica in caracteristicas:
                if caracteristica != caracteristicas[-1]:
                    print(COLOR_ITEM + caracteristica, ", " + COLOR_RESET, end='')
                else:
                    print(COLOR_ITEM + caracteristica + COLOR_RESET, '\n')
    else:
        print(COLOR_ERROR + "Nenhum esporte encontrado!" + COLOR_RESET)

    input(COLOR_INPUT + "Pressione ENTER para voltar ao menu inicial: " + COLOR_RESET)


# Exibe menu para o usuário escolher baseado em que os esportes devem ser exibidos.
def menu_exibicao():
    escolha = 0
    while escolha < 1 or escolha > 6:
        system(clear)
        print(COLOR_MENU + "1 - Todos esportes\n"
                           "2 - Nome do esporte\n"
                           "3 - Ano de criação\n"
                           "4 - País de Origem\n"
                           "5 - Características\n"
                           "6 - Voltar\n" + COLOR_RESET)
        try:
            escolha = int(input(COLOR_INPUT + "Selecionar: " + COLOR_RESET))
        except:
            print(COLOR_ERROR + "Escolha precisa ser um número!" + COLOR_RESET)
            input(COLOR_INPUT + "Pressione Qualquer tecla para continuar!" + COLOR_RESET)

    return escolha


# Função principal para exibição
def principal_exibir():
    escolha = menu_exibicao()
    if escolha == 1:
        esportes = database
    elif escolha == 2:
        esportes = pegar_esportes()
    elif escolha == 3:
        esportes = pegar_ano_origem()
    elif escolha == 4:
        esportes = pegar_paises_origem()
    elif escolha == 5:
        esportes = pegar_caracteristicas()
    else:
        return

    exibir(esportes)


# Linha de execução principal do programa.
def main():
    escolha_menu = 0

    while escolha_menu != 4:
        escolha_menu = menu()
        if escolha_menu == 1:
            try:
                inserir()
            except:
                print(COLOR_ERROR + "O esporte não foi adicionado!" + COLOR_RESET)

        elif escolha_menu == 2:
            try:
                principal_remover()
            except:
                print(COLOR_ERROR + "Erro ao remover!" + COLOR_RESET)

        elif escolha_menu == 3:
            try:
                principal_exibir()
            except:
                print(COLOR_ERROR + "Erro no banco de dados!" + COLOR_RESET)


main()

'''
Dividir a função Inserir para ficar mais enxuta
Revisar Todo o código em busca de melhoria e Comentar algo que possa parecer confuso
'''
