
from pathlib import Path


def criar_arquivo(nome):
    Path(nome).touch()
    print(f"Arquivo '{nome}' criado com sucesso.")
    return nome

def Dados_Arquivo(nome,tab):
    arq = open(nome, 'at')
    cab = f'{"N° Parc.":>24};{"Saldo Devedor Inicial":>24};{"Prestação":>24};{"Juros":>24};{"Amortização":>24};{"Saldo Devedor Final":>24}'
    arq.write(cab)
    arq.write('\n')
    for c in range(len(tab)):
        linha = ';'.join(f'{v:>24}' for v in tab[c].values())
        arq.write(linha + '\n')





