import funcoes_adm

funcoes_adm.limpa()

# PONTOS TURÍSTICOS CADASTRADOS
pontos = [{'NOME': 'RESTAURANTE A', 'NOTA': 9.45,
           'LOCALIZAÇÃO': '300m de distância',
           'DESCRIÇÃO':
           'Restaurante familiar, bem localizado, com uma grande variedade de comidas regionais.'},
          {'NOME': 'BAR B', 'NOTA': 9.05,
           'LOCALIZAÇÃO': '600m de distância',
           'DESCRIÇÃO':
           'Bar conhecido por noites com música e preço baixo.'},
          {'NOME': 'PRAIA C', 'NOTA': 8.75,
           'LOCALIZAÇÃO': '100m de distância',
           'DESCRIÇÃO':
           'Uma das praias mais procuradas de Maceió, o local perfeito para aproveitar um dia de sol.'},
          {'NOME': 'PASSEIO D', 'NOTA': 8.50,
           'LOCALIZAÇÃO': '1km de distância',
           'DESCRIÇÃO':
           'Um passeio inesquecível para Maceió, preço baixo e melhor qualidade.'},
          {'NOME': 'CAFÉ E', 'NOTA': 9.85,
           'LOCALIZAÇÃO': '400m de distância',
           'DESCRIÇÃO':
           'Ambiente familiar, com uma grande variedade de refeições para agradar todos os gostos.'},
          {'NOME': 'LUAU F', 'NOTA': 7.95,
           'LOCALIZAÇÃO': '800m de distância',
           'DESCRIÇÃO':
           'Um ambiente ideal para casais que querem aproveitar o Maceió da forma mais romântica.'}]

op = 1
print('BEM VINDO AO SETOR ADMINISTRATIVO DO EVENTUM!\n')
while op != 0:
    funcoes_adm.menu()
    op = int(input('Selecione uma das opções e tecle ENTER: '))
    funcoes_adm.limpa()
    if op == 1:  # ADICIONAR NOVO PONTO TURÍSTICO
        d = {'NOME': '', 'NOTA': 0.0, 'LOCALIZAÇÃO': '', 'DESCRIÇÃO': ''}
        d['NOME'] = input('Informe o nome do estabelecimento: ').upper()
        d['NOTA'] = float(input('Informe a nota do estabelecimento: '))
        d['LOCALIZAÇÃO'] = input('Informe a distância do ponto para o hotel: ')
        d['DESCRIÇÃO'] = input('Informe a descrição do ponto: ')
        pontos.append(d)
        print('Ponto adicionado com sucesso!')
        funcoes_adm.pausa()
    elif op == 2:  # ATUALIZAR PONTO TURÍSTICO
        nome = input(
            'Informe o nome do estabelecimento que deseja atualizar: ').upper()
        ponto_local = list(filter(lambda p: p['NOME'] == nome, pontos))
        if len(ponto_local) < 1:
            print('Este ponto não está registrado.')
        else:
            print(
                f'Informe as atualizações do ponto {(ponto_local[0]["NOME"]).title()}')
            d = {'NOTA': 0.0, 'LOCALIZAÇÃO': '', 'DESCRIÇÃO': ''}
            print(f'Nota anterior: {ponto_local[0]["NOTA"]}')
            d['NOTA'] = float(input('Informe a nova nota: '))
            print(f'Localização anterior: {ponto_local[0]["LOCALIZAÇÃO"]}')
            d['LOCALIZAÇÃO'] = input('Informe a nova localização: ')
            print(f'Descrição anterior: {ponto_local[0]["DESCRIÇÃO"]}')
            d['DESCRIÇÃO'] = input('Informe a nova descrição: ')
            ponto_local[0].update(d)
            print('Ponto atualizado com sucesso!')
        funcoes_adm.pausa()
    elif op == 3:  # EXIBIR TODOS OS PONTOS CADASTRADOS
        for i in range(len(pontos)):
            funcoes_adm.exibe_ponto(pontos[i])
            funcoes_adm.pausa()
    elif op == 4:  # REMOVER UM PONTO REGISTRADO
        nome = input(
            'Informe o nome do estabelecimento que deseja remover: ').upper()
        ponto_local = list(filter(lambda p: p['NOME'] == nome, pontos))
        if len(ponto_local) < 1:
            print('Este ponto não está registrado.')
        else:
            print(
                f'Tem certeza que deseja deletar o ponto {ponto_local[0]["NOME"]}?')
            cert = input('').upper()
            if cert[0] == 'S':
                pontos.remove(ponto_local[0])
                print('Ponto removido com sucesso!')
            else:
                print('Operação cancelada.')
        funcoes_adm.pausa()
    elif op == 5:  # CONSULTAR NOTAS DO HOTEL E DO APP
        aux = True
        while aux:
            print('1 - Notas do Eventum')
            print('2 - Comentários sobre o Eventum')
            print('3 - Notas do Hotel')
            print('4 - Comentários sobre o Hotel')
            print('0 - Sair')
            opt = int(input(('Selecione a opção que deseja consultar: ')))
            funcoes_adm.limpa()
            if opt == 1:
                soma = 0.0
                file = open('notas_eventum.txt', 'r')
                lista = file.readlines()
                print('Lista de notas dadas ao Eventum:\n')
                for i in range(len(lista)):
                    print(lista[i])
                    soma = soma + float(lista[i])
                media = soma / len(lista)
                print(f'Média geral do app: {media:.2f}')
                file.close()
            elif opt == 2:
                file = open('comentario_eventum.txt', 'r', encoding='utf-8')
                lista = file.readlines()
                print('Lista de comentarios feitos sobre o Eventum:\n')
                for i in range(len(lista)):
                    print(lista[i])
                file.close()
            elif opt == 3:
                soma = 0.0
                file = open('notas_hotel.txt', 'r')
                lista = file.readlines()
                print('Lista de notas dadas ao Hotel:\n')
                for i in range(len(lista)):
                    print(lista[i])
                    soma = soma + float(lista[i])
                media = soma / len(lista)
                print(f'Média geral do hotel: {media:.2f}')
                file.close()
            elif opt == 4:
                file = open('comentario_hotel.txt', 'r', encoding='utf-8')
                lista = file.readlines()
                print('Lista de comentarios feitos sobre o Hotel:\n')
                for i in range(len(lista)):
                    print(lista[i])
                file.close()
            elif opt == 0:
                print('Operação encerrada.')
                aux = False
            else:
                print('Opção inválida.')
            funcoes_adm.pausa()
            funcoes_adm.limpa()
    elif op == 0:  # ENCERRAR OPERAÇÃO
        print('Operação encerrada.')
        funcoes_adm.pausa()
    else:  # OPÇÃO INVÁLIDA
        print('Opção inválida.')
        funcoes_adm.pausa()
    funcoes_adm.limpa()
