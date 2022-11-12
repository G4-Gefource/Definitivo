#  IMPORTAÇÃO DE BIBLIOTECAS E FUNÇÕES EXTERNAS
import msvcrt
import funcoes
import bot_pt
import bot_es

# INÍCIO DO CÓDIGO

pontos = [{'NOME': 'RESTAURANTE A',
           'NOTA': 9.45, 'LOCALIZAÇÃO': '300m de distância',
           'DESCRIÇÃO_PT':
           'Restaurante familiar, bem localizado, com uma grande variedade de comidas regionais.',
           'DESCRIÇÃO_ES':
           'Restaurante familiar, bien ubicado, con una amplia variedad de comidas regionales.'},
          {'NOME': 'BAR B', 'NOTA': 9.05,
           'LOCALIZAÇÃO': '600m de distância',
           'DESCRIÇÃO_PT':
           'Bar conhecido por noites com música e preço baixo.',
           'DESCRIÇÃO_ES':
           'Bar conocido por las noches con música y precios bajos.'},
          {'NOME': 'PRAIA C', 'NOTA': 8.75,
           'LOCALIZAÇÃO': '100m de distância',
           'DESCRIÇÃO_PT':
           'Uma das praias mais procuradas de Maceió, o local perfeito para aproveitar um dia de sol.',
           'DESCRIÇÃO_ES':
           'Una de las playas más solicitadas de Maceió, el lugar perfecto para disfrutar de un día soleado.'},
          {'NOME': 'PASSEIO D', 'NOTA': 8.50,
           'LOCALIZAÇÃO': '1km de distância',
           'DESCRIÇÃO_PT':
           'Um passeio inesquecível para Maceió, preço baixo e melhor qualidade.',
           'DESCRIÇÃO_ES':
           'Un tour inolvidable a Maceió, bajo precio y la mejor calidad.'},
          {'NOME': 'CAFÉ E', 'NOTA': 9.85,
           'LOCALIZAÇÃO': '400m de distância',
           'DESCRIÇÃO_PT':
           'Ambiente familiar, com uma grande variedade de refeições para agradar todos os gostos.',
           'DESCRIÇÃO_ES':
           'Ambiente familiar, con una gran variedad de comidas para todos los gustos.'},
          {'NOME': 'LUAU F', 'NOTA': 7.95,
           'LOCALIZAÇÃO': '800m de distância',
           'DESCRIÇÃO_PT':
           'Um ambiente ideal para casais que querem aproveitar o Maceió da forma mais romântica.',
           'DESCRIÇÃO_ES':
           'Un entorno ideal para parejas que quieran disfrutar de Maceió de la forma más romántica.'}]
op = 1  # VARIÁVEL AUXILIAR PARA LAÇO DE REPETIÇÃO
while op != 0:
    funcoes.limpa()
    print('Bem vindo ao Eventum!')
    print('Bienvenido al Eventum!')
    print('\nGostaria da versão em espanhol?')
    print('¿Te Gustaria la version en español?')
    # UPPER() -> TRANSFORMA TODAS OS CARACTERES INSERIDOS EM MAIÚSCULO
    idioma = input('S - Sim(Sí)\nN - Não(No)\n').upper()
    funcoes.limpa()

    if idioma[0] == 'N':  # SELECIONA OPÇÃO EM PORTUGUÊS
        print('Você selecionou a opção em Português!\n')
        opt = 1
        while opt != 0:
            funcoes.menu_pt()   # CHAMA A FUNÇÃO MENU_PT
            opt = int(input('Selecione uma das opções e tecle ENTER: '))
            funcoes.limpa()
            if opt == 1:  # ENCONTRAR PONTOS TURÍSTICOS
                aux = 1
                while aux != 0:
                    pt = input(
                        'Você já sabe o tipo de ponto turístico que está procurando?\n(S - Sim/N - Não)\n')
                    funcoes.limpa()
                    if (pt[0]).upper() == 'S':
                        aux_ponto = True
                        while aux_ponto:
                            procura = input(
                                'Insira o nome ponto que está procurando: ').upper()
                            ponto_local = list(
                                filter(lambda p: p['NOME'] == procura, pontos))
                            funcoes.limpa()
                            if len(ponto_local) < 1:
                                print('Este ponto não está registrado.')
                                funcoes.pausa_pt()
                                funcoes.limpa()
                            else:
                                funcoes.exibir_pt(ponto_local[0])
                                print('Gostaria de um arquivo sobre esse ponto?')
                                arq = input('(S - Sim/N - Não)\n').upper()
                                if arq[0] == 'S':
                                    print('Gerando arquivo...')
                                    funcoes.pausa_pt()
                                    aux_ponto = False
                                else:
                                    print('Gostaria de procurar outro ponto?')
                                    novo = input('(S - Sim/N - Não)\n').upper()
                                    if novo[0] == 'S':
                                        funcoes.limpa()
                                    else:
                                        print('Operação encerrada.')
                                        funcoes.pausa_pt()
                                        aux_ponto = False
                        funcoes.limpa()
                    elif (pt[0]).upper() == 'N':
                        print(
                            'Gostaria da ajuda da Iara para garantir uma experiência personalizada para você?')
                        bot = input('')
                        funcoes.limpa()
                        if (bot[0]).upper() == 'S':
                            bot_pt.chat()
                    else:
                        print('Opção inválida.')
                        funcoes.pausa_pt()
                        funcoes.limpa()
                    aux = 0
            elif opt == 2:  # DAR FEEDBACK SOBRE O HOTEL
                hotel = 1
                while hotel != 0:
                    v = ['Como você avalia sua estadia no hotel?', 'Como você avalia seu conforto no hotel?',
                         'Como você avalia a localização do hotel?', 'Como você avalia a limpeza do hotel?',
                         'Como você avalia o atendimento dos funcionários?']
                    print('1 - Saint Patrick Praia Hotel')
                    print('2 - Hotel Des Basques')
                    print('3 - Pousada Nossa Casa')
                    print('4 - Saint Patrick Grand Hotel')
                    hotel = int(
                        input(('Informe o hotel em que ficou hospedado: ')))
                    hosped = ''
                    if hotel == 1:
                        hosped = 'Saint Patrick Praia Hotel'
                    elif hotel == 2:
                        hosped = 'Hotel Des Basques'
                    elif hotel == 3:
                        hosped = 'Pousada Nossa Casa'
                    elif hotel == 4:
                        hosped = 'Saint Patrick Grand Hotel'
                    elif hotel == 0:
                        print('Operação encerrada pelo usuário.\n')
                        funcoes.pausa_pt()
                        funcoes.limpa()
                    else:
                        print('Opção inválida.')
                        funcoes.pausa_pt()
                        funcoes.limpa()
                    print(f'Responda as perguntas sobre o hotel {hosped}.\n')
                    soma = 0.0
                    i = 0
                    while i in range(len(v)):
                        print(v[i])
                        a = float(input('Informe uma nota de 0 a 5: '))
                        if a > 5 or a < 0:
                            print('Esta nota não pode ser inserida.')
                            i = i - 1
                        else:
                            soma = soma + a
                            i = i + 1
                    media = soma / len(v)
                    file = open('notas_hotel.txt', 'a')
                    file.write(str(media)+"\n")
                    file.close()
                    funcoes.limpa()
                    print(
                        f'Você avaliou o hotel {hosped} com {media:.2f} estrelas.')
                    print(
                        f'Gostaria de deixar um comentário sobre o hotel {hosped}?')
                    av = input('').upper()
                    if av[0] == 'S':
                        coment = input('Informe aqui seu comentário: ')
                        arquivo = open('comentario_hotel.txt',
                                       'a', encoding='utf-8')
                        arquivo.write(coment+"\n")
                        arquivo.close()
                        funcoes.limpa()
                    print('Obrigado pela sua avaliação!')
                    hotel = 0
                    funcoes.pausa_pt()
                    funcoes.limpa()
            elif opt == 3:  # DAR FEEDBACK SOBRE O EVENTUM
                v = ['Como você avalia a facilidade de navegação do Eventum?',
                     'Como você avalia o design do Eventum?', 'Como você avalia a praticidade do Eventum?',
                     'Quão satisfeito você está com o uso do Eventum?']
                i = 0
                soma = 0.0
                while i in range(len(v)):
                    print(v[i])
                    a = float(input('Informe uma nota de 0 a 10: '))
                    if a > 10 or a < 0:
                        print('Esta nota não pode ser inserida.')
                        i = i - 1
                    else:
                        soma = soma + a
                        i = i + 1
                media = soma / len(v)
                file = open('notas_eventum.txt', 'a')
                file.write(str(media)+"\n")
                file.close()
                funcoes.limpa()
                print(f'Você avaliou o Eventum com média {media:.2f}.')
                print(f'Gostaria de deixar um comentário sobre o Eventum?')
                av = input('').upper()
                if av[0] == 'S':
                    coment = input('Informe aqui seu comentário: ')
                    arquivo = open('comentario_eventum.txt',
                                   'a', encoding='utf-8')
                    arquivo.write(coment+"\n")
                    arquivo.close()
                    funcoes.limpa()
                print('Obrigado pela sua avaliação!')
                funcoes.pausa_pt()
                funcoes.limpa()
            elif opt == 0:
                print('Obrigado por usar o Eventum!')
                funcoes.pausa_pt()
                funcoes.limpa()
                op = 0
            else:
                print('Opção inválida.')
                funcoes.pausa_pt()
                funcoes.limpa()
    elif idioma[0] == 'S':  # SELECIONA OPÇÃO EM ESPANHOL
        print('¡Ha seleccionado la opción en Español!')
        opt = 1
        while opt != 0:
            funcoes.menu_es()   # CHAMA A FUNÇÃO MENU_ES
            opt = int(input('Seleccione una de las opciones y presione ENTER: '))
            funcoes.limpa()
            if opt == 1:  # ENCONTRAR PONTOS TURÍSTICOS
                aux = 1
                while aux != 0:
                    aux = 1
                    while aux != 0:
                        pt = input(
                            '¿Ya sabes el tipo de lugar turístico que estás buscando?\n(S - Si/N - No)\n')
                        funcoes.limpa()
                        if (pt[0]).upper() == 'S':
                            aux_ponto = True
                            while aux_ponto:
                                procura = input(
                                    'Introduzca el nombre del punto que está buscando: ').upper()
                                ponto_local = list(
                                    filter(lambda p: p['NOME'] == procura, pontos))
                                funcoes.limpa()
                                if len(ponto_local) < 1:
                                    print('Este punto no está registrado.')
                                    funcoes.pausa_es()
                                    funcoes.limpa()
                                else:
                                    funcoes.exibir_es(ponto_local[0])
                                    print(
                                        '¿Desea un archivo sobre este punto?')
                                    arq = input('(S - Si/N - No)\n').upper()
                                    if arq[0] == 'S':
                                        print('Generando archivo...')
                                        funcoes.pausa_es()
                                        aux_ponto = False
                                    else:
                                        print(
                                            '¿Te gustaría buscar otro punto?')
                                        novo = input(
                                            '(S - Si/N - No)\n').upper()
                                        if novo[0] == 'S':
                                            funcoes.limpa()
                                        else:
                                            print('Operación cerrada.')
                                            funcoes.pausa_es()
                                            aux_ponto = False
                            funcoes.limpa()
                        elif (pt[0]).upper() == 'N':
                            print(
                                'Gostaria da ajuda da Iara para garantir uma experiência personalizada para você?')
                            bot = input('')
                            funcoes.limpa()
                            if (bot[0]).upper() == 'S':
                                bot_es.chat()
                        else:
                            print('Opção inválida.')
                            funcoes.pausa_es()
                            funcoes.limpa()
                        aux = 0
            elif opt == 2:    # DAR FEEDBACK SOBRE O HOTEL
                hotel = 1
                while hotel != 0:
                    v = ['¿Cómo califica su estancia en el hotel?', '¿Cómo califica su comodidad en el hotel?',
                         '¿Cómo califica la ubicación del hotel?', '¿Cómo califica la limpieza del hotel?',
                         '¿Cómo califica el servicio de los empleados?']
                    print('1 - Saint Patrick Praia Hotel')
                    print('2 - Hotel Des Basques')
                    print('3 - Pousada Nossa Casa')
                    print('4 - Saint Patrick Grand Hotel')
                    hotel = int(
                        input('Informar al hotel donde se hospedó: '))
                    hosped = ''
                    if hotel == 1:
                        hosped = 'Saint Patrick Praia Hotel'
                    elif hotel == 2:
                        hosped = 'Hotel Des Basques'
                    elif hotel == 3:
                        hosped = 'Pousada Nossa Casa'
                    elif hotel == 4:
                        hosped = 'Saint Patrick Grand Hotel'
                    elif hotel == 0:
                        print('Operación terminada por el usuario.\n')
                        funcoes.pausa_es()
                        funcoes.limpa()
                    else:
                        print('Opción no válida.')
                        funcoes.pausa_es()
                        funcoes.limpa()
                    print(f'Responder preguntas sobre el hotel {hosped}.\n')
                    soma = 0.0
                    i = 0
                    while i in range(len(v)):
                        print(v[i])
                        a = float(
                            input('Introduzca una puntuación de 0 a 5: '))
                        if a > 5 or a < 0:
                            print('Esta nota no se puede ingresar.')
                            i = i - 1
                        else:
                            soma = soma + a
                            i = i + 1
                    media = soma / len(v)
                    file = open('notas_hotel.txt', 'a')
                    file.write(str(media)+"\n")
                    file.close()
                    funcoes.limpa()
                    print(
                        f'Ha calificado el hotel {hosped} con {media:.2f} estrellas.')
                    print(
                        f'¿Le gustaría dejar una reseña sobre el hotel {hosped}?')
                    av = input('').upper()
                    if av[0] == 'S':
                        coment = input('Ingrese su comentario aquí: ')
                        arquivo = open('comentario_hotel.txt',
                                       'a', encoding='utf-8')
                        arquivo.write(coment+"\n")
                        arquivo.close()
                        funcoes.limpa()
                    print('¡Gracias por tu valoración!')
                    hotel = 0
                    funcoes.pausa_es()
                    funcoes.limpa()
            elif opt == 3:  # DAR FEEDBACK SOBRE O EVENTUM
                v = ['¿Cómo califica la facilidad de navegación de Eventum?',
                     '¿Cómo valoras el diseño de Eventum?', '¿Cómo califica la practicidad de Eventum?',
                     '¿Qué tan satisfecho está con el uso de Eventum?']
                i = 0
                soma = 0.0
                while i in range(len(v)):
                    print(v[i])
                    a = float(input('Introduzca una puntuación de 0 a 10: '))
                    if a > 10 or a < 0:
                        print('Esta nota no se puede ingresar.')
                        i = i - 1
                    else:
                        soma = soma + a
                        i = i + 1
                media = soma / len(v)
                file = open('notas_eventum.txt', 'a')
                file.write(str(media)+"\n")
                file.close()
                funcoes.limpa()
                print(f'Calificaste Eventum con promedio {media:.2f}.')
                print(f'¿Quieres dejar un comentario sobre Eventum?')
                av = input('').upper()
                if av[0] == 'S':
                    coment = input('Ingrese su comentario aquí: ')
                    arquivo = open('comentario_eventum.txt',
                                   'a', encoding='utf-8')
                    arquivo.write(coment+"\n")
                    arquivo.close()
                    funcoes.limpa()
                print('¡Gracias por tu valoración!')
                funcoes.pausa_es()
                funcoes.limpa()
            elif opt == 0:
                print('¡Gracias por usar Eventum!')
                funcoes.pausa_es()
                funcoes.limpa()
                op = 0
            else:
                print('Opción no válida.')
                funcoes.pausa_es()
                funcoes.limpa()
    else:
        print('Opção inválida inserida.')
        print('Opción no válida ingresada.')
        print('Pressione qualquer tecla para continuar...\n')
        print('Pulse cualquier tecla para continuar...\n')
        char = msvcrt.getch()
