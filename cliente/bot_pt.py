#  IMPORTAÇÃO DE BIBLIOTECAS E FUNÇÕES EXTERNAS
import msvcrt
import funcoes


def chat():
    # DICIONARIOS COM PONTOS TURÍSTICOS
    ponto_a = {'NOME': 'RESTAURANTE A',
               'NOTA': 9.45, 'LOCALIZAÇÃO': '300m de distância',
               'DESCRIÇÃO_PT':
               'Restaurante familiar, bem localizado, com uma grande variedade de comidas regionais.',
               'DESCRIÇÃO_ES':
               'Restaurante familiar, bien ubicado, con una amplia variedad de comidas regionales.'}
    ponto_b = {'NOME': 'BAR B', 'NOTA': 9.05,
               'LOCALIZAÇÃO': '600m de distância',
               'DESCRIÇÃO_PT':
               'Bar conhecido por noites com música e preço baixo.',
               'DESCRIÇÃO_ES':
               'Bar conocido por las noches con música y precios bajos.'}
    ponto_c = {'NOME': 'PRAIA C', 'NOTA': 8.75,
               'LOCALIZAÇÃO': '100m de distância',
               'DESCRIÇÃO_PT':
               'Uma das praias mais procuradas de Maceió, o local perfeito para aproveitar um dia de sol.',
               'DESCRIÇÃO_ES':
               'Una de las playas más solicitadas de Maceió, el lugar perfecto para disfrutar de un día soleado.'}
    ponto_d = {'NOME': 'PASSEIO D', 'NOTA': 8.50,
               'LOCALIZAÇÃO': '1km de distância',
               'DESCRIÇÃO_PT':
               'Um passeio inesquecível para Maceió, preço baixo e melhor qualidade.',
               'DESCRIÇÃO_ES':
               'Un tour inolvidable a Maceió, bajo precio y la mejor calidad.'}
    ponto_e = {'NOME': 'CAFÉ E', 'NOTA': 9.85,
               'LOCALIZAÇÃO': '400m de distância',
               'DESCRIÇÃO_PT':
               'Ambiente familiar, com uma grande variedade de refeições para agradar todos os gostos.',
               'DESCRIÇÃO_ES':
               'Ambiente familiar, con una gran variedad de comidas para todos los gustos.'}
    ponto_f = {'NOME': 'LUAU F', 'NOTA': 7.95,
               'LOCALIZAÇÃO': '800m de distância',
               'DESCRIÇÃO_PT':
               'Um ambiente ideal para casais que querem aproveitar o Maceió da forma mais romântica.',
               'DESCRIÇÃO_ES':
               'Un entorno ideal para parejas que quieran disfrutar de Maceió de la forma más romántica.'}
    func = True
    while func is True:
        print('Olá! Eu sou a Iara, vou te ajudar a escolher o ponto que te dará a melhor experiência!')
        num = input(
            'Primeiro me diga, você está viajando sozinho?\n')
        funcoes.limpa()
        if (num[0]).upper() == 'N':
            comp = ''
            print('Perfeito! Com quem você está viajando?')
            print('1 - Em família')
            print('2 - Com amigos')
            print('3 - Em casal')
            op = int(input('Selecione uma das opções e tecle ENTER: '))
            funcoes.limpa()
            if op == 1:
                comp = 'FAMILIA'
            elif op == 2:
                comp = 'AMIGOS'
            elif op == 3:
                comp = 'CASAL'
            hora = ''
            print('Perfeito! Agora fala um pouco da disponibilidade de horário de vocês!')
            print('1 - Manhã')
            print('2 - Tarde')
            print('3 - Noite')
            op = int(input('Selecione uma das opções e tecle ENTER: '))
            funcoes.limpa()
            if op == 1:
                hora = 'MANHA'
            elif op == 2:
                hora = 'TARDE'
            elif op == 3:
                hora = 'NOITE'
            print('Encontrei o passeio perfeito para vocês!')
            if comp == 'FAMILIA' and hora == 'MANHA':
                funcoes.exibe_ponto_pt(ponto_c)
            elif comp == 'FAMILIA' and hora == 'TARDE':
                funcoes.exibe_ponto_pt(ponto_d)
            elif comp == 'FAMILIA' and hora == 'NOITE':
                funcoes.exibe_ponto_pt(ponto_a)
            elif comp == 'AMIGOS' and hora == 'MANHA':
                funcoes.exibe_ponto_pt(ponto_c)
            elif comp == 'AMIGOS' and hora == 'TARDE':
                funcoes.exibe_ponto_pt(ponto_d)
            elif comp == 'AMIGOS' and hora == 'NOITE':
                funcoes.exibe_ponto_pt(ponto_b)
            elif comp == 'CASAL' and hora == 'MANHA':
                funcoes.exibe_ponto_pt(ponto_e)
            elif comp == 'CASAL' and hora == 'TARDE':
                funcoes.exibe_ponto_pt(ponto_c)
            elif comp == 'CASAL' and hora == 'NOITE':
                funcoes.exibe_ponto_pt(ponto_f)
            print('Gostaria de um arquivo externo desse passeio?')
            arq = input('')
            if arq[0].upper() == 'S':
                print('Estou gerando o arquivo para você!')
            print('Obrigado por usar minha ajuda!')
            funcoes.pausa_pt()
            funcoes.limpa()
            func = False
        elif (num[0]).upper() == 'S':
            hora = ''
            print('Perfeito! Agora fala um pouco da sua disponibilidade de horário!')
            print('1 - Manhã')
            print('2 - Tarde')
            print('3 - Noite')
            op = int(input('Selecione uma das opções e tecle ENTER: '))
            funcoes.limpa()
            if op == 1:
                hora = 'MANHA'
            elif op == 2:
                hora = 'TARDE'
            elif op == 3:
                hora = 'NOITE'
            print('Encontrei o passeio perfeito para você!')
            if hora == 'MANHA':
                funcoes.exibe_ponto_pt(ponto_c)
            elif hora == 'TARDE':
                funcoes.exibe_ponto_pt(ponto_a)
            elif hora == 'NOITE':
                funcoes.exibe_ponto_pt(ponto_b)
            print('Gostaria de um arquivo externo desse passeio?')
            arq = input('')
            if arq[0].upper() == 'S':
                print('Estou gerando o arquivo para você!')
            print('Obrigado por usar minha ajuda!')
            funcoes.pausa_pt()
            funcoes.limpa()
            func = False
        else:
            print(
                'Desculpe, não entendi, pressione qualquer tecla para voltar ao início.')
            char = msvcrt.getch()
            funcoes.limpa()
