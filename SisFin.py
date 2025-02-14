
from ModFin.Lib.InterFace import *
from ModFin.Lib.Arquivo import *
from ModFin.Lib.CalcFin import *

while True:
    m1 = menu1(['Sistema Price', 'Sistema SAC', 'Encerrar'])
    if m1 == 1:
        price = processar_sist('Price')
        m2 = menu2()
        if m2 == 1:
            nome = criar_arquivo(f'{input('Digite o nome do arquivo: ')}_price.txt')
            Dados_Arquivo(nome,price)
            print('Retornando ao menu principal')
            sleep(0.5)
        elif m2 == 2:
            continue
        elif m2 == 3:
            break
        else:
            print('Digite uma opção válida')
    elif m1 == 2:
        sac = processar_sist('SAC')
        m2 = menu2()
        if m2 == 1:
            nome = criar_arquivo(f'{input("Digite o nome do arquivo: ")}_SAC.txt')
            Dados_Arquivo(nome,sac)
            print('Retornando ao menu principal')
            sleep(0.5)
        elif m2 == 2:
            continue
        elif m2 == 3:
            break
        else:
            print('Digite uma opção válida')
    elif m1 == 3:
        print('Encerrando sistema!!')
        print()
        break
    else:
        print('Digite uma opção válida')

print('Encerrado')
