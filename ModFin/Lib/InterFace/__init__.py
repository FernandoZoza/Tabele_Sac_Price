from time import sleep
from ModFin.Lib.Arquivo import *

def TituloMenu1():
    tit = str('Calculo Financiamentos')
    return tit

def linha():
    comp = len(TituloMenu1())
    return '-' * comp

def cabecalho(texto):
    print(linha())
    print(f'{texto.center(len(linha()))}')
    print(linha())

def InputNumFloat(texto):
    while True:
        try:
            n = input(f'{texto}: ')
            n = n.replace(',','.')
            n = float(n)
            if n < 0:
                print(f'\033[31mDados inválidos - Valor deve ser positivo\033[m')
                continue
        except ValueError:
            print(f'\033[31mErro! Digite um número válido\033[m')
            continue
        if n < 0:
            print('Dados inválidos - Valor deve ser positivo')
            raise ValueError("Número negativo detectado")
        return n

def InputNumInt(texto):
    while True:
        try:
            n = int(input(f'{texto}: '))
            if n < 0:
                print(f'\033[31mDados inválidos - Valor deve ser positivo\033[m')
                continue
        except ValueError:
            print(f'\033[31mErro! Digite um número inteiro válido\033[m')
            continue
        return n

def InputAlphaNum (texto):
   while True:
        t = input(f'{texto}: ')
        if len(t) > 8:
            print('Dados inválidos - Digite no max. 8 caracteres')
        else:
            return t

def menu1 (lista):
    cabecalho(TituloMenu1())
    for c, op in enumerate(lista):
        print(f'{c+1} - {op}')
    print(linha())
    m = InputNumInt('Escolha um Calculo')
    return m

def menu2 ():
    while True:
        m2 = InputNumInt(f'[1] Gerar arquivo\n'
                            f'[2] Retornar\n'
                            f'[3] Encerrar\n'
                            f'Digite uma opção')
        return m2