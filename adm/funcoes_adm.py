import os
import msvcrt

# FUNÇÕES


def limpa():
    os.system("cls")


def pausa():
    print('\nPressione qualquer tecla para continuar...\n')
    char = msvcrt.getch()


def menu():
    print('1 - Adicionar pontos turísticos\n')
    print('2 - Atualizar ponto turístico\n')
    print('3 - Visualizar pontos cadastrados\n')
    print('4 - Remover ponto turísitico\n')
    print('5 - Consultar notas do hotel/Eventum\n')
    print('0 - Sair\n')


def exibe_ponto(ponto):
    print(f'Nome do estabelecimento: {(ponto["NOME"]).title()};')
    print(f'Nota do estabelecimento: {ponto["NOTA"]};')
    print(f'Localização do ponto: {ponto["LOCALIZAÇÃO"]} do hotel;')
    print(f'Descrição do ponto: {ponto["DESCRIÇÃO"]};')
