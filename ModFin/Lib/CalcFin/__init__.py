from ModFin.Lib.InterFace import *
import numpy_financial as npf

def ParcFin(i=0,npr=0, pv=0):
    i = i/100
    parc = npf.pmt(i,npr,pv)
    return abs(parc)

def processar_sist(op):
    i = InputNumFloat('Taxa de Juros')
    npr = InputNumInt('Período (Mês)')
    pv = InputNumFloat('Valor financiado')
    if op == 'Price':
        SummaryPrice(i, npr, pv)
        price = SistPrice(i, npr, pv)
        return price
    if op == 'SAC':
        SummarySAC(i, npr, pv)
        sac = SistSac(i, npr, pv)
        return sac

def SummaryPrice(i=0,npr=0, pv=0):
    print('¬'*57)
    print(f'{"Resumo Sistema Price":^57}')
    print('¬' * 57)
    tdev = ParcFin(i, npr, pv) * npr
    tjur = tdev - pv
    print(f'{"Valor Financiado: ":<44}{pv:>13.2f}')
    print(f'{"Valor parcelas: ":<44}{ParcFin(i, npr, pv) :>13.2f}')
    print(f'{"Total juros no período ("}{f'{i:.2f}'"% mês):":<20}{tjur:>13.2f}')
    print(f'{"Saldo devedor com juros: ":<44}{tdev:>13.2f}')
    print('¬' * 57)

def SistPrice(i=0,npr=0, pv=0):
    j = (i / 100)
    saldo = pv
    pmt = ParcFin(i, npr, pv)
    price = []
    print()
    print(f'{"Tabela de Amortização pelo Sistema Price":<60}')
    print('-' * 129)
    print(f'{"Parcela":>8}{"Saldo Devedor Inicial":>24}{"Prestação":>24}{"Juros":>24}{"Amortização":>24} '
          f'{"Saldo Devedor Final":>24}')
    print('-' * 129)
    for c in range(1,npr+1):
        juros = saldo * j
        amort = abs(npf.ppmt(j,c,npr,pv))
        saldo_final = saldo - amort
        parc = {'N° Parc.': c, 'Saldo': saldo, 'PMT': pmt, 'Juros': juros, 'amort': amort, 'SaldoFinal': saldo_final}
        print(f'{c:8}{saldo:24.2f}{pmt:24.2f}{juros:24.2f}'
              f'{amort:24.2f}{saldo_final:25.2f}')
        saldo = saldo_final
        price.append(parc)
    return price


def SummarySAC(i,npr,pv):
    i = i/100
    saldo = pv
    amort = pv / npr
    tjur = 0
    pmt_1 = amort + (pv * i)
    pmt_ult = amort + (amort*i)
    print('¬' * 57)
    print(f'{"Resumo Sistema SAC":^57}')
    print('¬' * 57)
    for c in range(1,npr+1):
        juros = saldo * i
        saldofinal = saldo - amort
        saldo = saldofinal
        tjur += juros
    tdev = tjur+pv
    print(f'{"Valor Financiado: ":<44}{pv:>13.2f}')
    print(f'{"Valor da 1º Prestação: ":<44}{pmt_1:>13.2f}')
    print(f'{"Valor da ultima Prestação: ":<44}{pmt_ult:>13.2f}')
    print(f'{"Total juros no período ("}{f'{i*100:.2f}'"% mês):":<20}{tjur:>13.2f}')
    print(f'{"Saldo devedor com juros: ":<44}{tdev:>13.2f}')
    print('¬' * 57)

def SistSac(i, npr, pv):
    i = i / 100
    saldo = pv
    amort = pv / npr
    sac = []
    print()
    print(f'{"Tabela de Amortização pelo Sistema SAC":<60}')
    print('-' * 129)
    print(f'{"Parcela":>8}{"Saldo Devedor Inicial":>24}{"Prestação":>24}{"Juros":>24}{"Amortização":>24} '
          f'{"Saldo Devedor Final":>24}')
    print('-' * 129)
    for c in range(1, npr + 1):
        juros = saldo * i
        pmt = juros+amort
        saldofinal = saldo - amort
        parc = {'N° Parc.': c,'Saldo': saldo, 'PMT': pmt, 'Juros': juros, 'amort': amort, 'SaldoFinal': saldofinal}
        print(f'{c:8}{saldo:24.2f}{pmt:24.2f}{juros:24.2f}'
             f'{amort:24.2f}{saldofinal:25.2f}')
        saldo = saldofinal
        sac.append(parc)
    return sac



