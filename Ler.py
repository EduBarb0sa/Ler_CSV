import csv

def ler_csv(nome_arquivo, encoding='utf-8'):
    linhas = []
    with open(nome_arquivo, 'r', newline='', encoding=encoding) as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            linhas.append(linha)
    return linhas

def ler_csv2(nome_arquivo, encoding='utf-8'):
    linhas = []
    with open(nome_arquivo, 'r', newline='', encoding=encoding) as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            linhas.extend(linha)
    return linhas


def contar_elemento3(lista, elemento3, elemento8, elemento6, elemento9, elemento12, elemento15):
    contador = 0
    for linha in lista:
        for item in linha:
            if item == elemento3:
                contador += 1
            if item == elemento8:
                contador += 1
            if item == elemento6:
                contador += 2
            if item == elemento9:
                contador += 3
            if item == elemento12:
                contador += 4
            if item == elemento15:
                contador += 5
    return contador

def contar_elemento5(lista, elemento5, elemento8, elemento10, elemento155, elemento20, elemento25, elemento30, elemento36):
    contador = 0
    for linha in lista:
        for item in linha:
            if item == elemento5:
                contador += 1
            if item == elemento8:
                contador += 1
            if item == elemento10:
                contador += 2
            if item == elemento155:
                contador += 3
            if item == elemento20:
                contador += 4
            if item == elemento25:
                contador += 5
            if item == elemento30:
                contador += 6
            if item == elemento36:
                contador += 7
    return contador

def pega_elementos_indie4(lista):
    elementos = []
    for i, item in enumerate(lista):
        if i != 4 and (i + 4) % 5 == 3:
            elementos.append(item)
    return elementos


nome_arquivo = "t.csv" # Insira aqui o nome do arquivo em CSV que você quer ler

todos_os_elementos = ler_csv2(nome_arquivo)
indices_divisives4 = pega_elementos_indie4(todos_os_elementos) 


todas_as_linhas = ler_csv(nome_arquivo)
itens_para_remover = ["3","6","9","12","15","8.15","5.15","10.3","15.45","20.6","25.75","30.9",'36.05']

for item in itens_para_remover:
    while item in indices_divisives4:
        indices_divisives4.remove(item)
    for item in indices_divisives4[:]: 
        if str(item).startswith("-"):
            indices_divisives4.remove(item)

print(indices_divisives4)


número_procurado3 = '3'
número_procurado6 = '6'
número_procurado8 = '8.15'
número_procurado9 = '9'
número_procurado12 = '12'
número_procurado15 = '15'
vezes3 = contar_elemento3(todas_as_linhas, número_procurado3, número_procurado8, número_procurado6, número_procurado9, número_procurado12, número_procurado15)
total3 = vezes3 * 3
print(f"Foram vendidos {vezes3} brownies, totalizando {total3}.")


número_procurado5 = '5.15'
número_procurado8 = '8.15'
número_procurado10 = '10.3'
número_procurado155 = '15.45'
número_procurado20 = '20.6'
número_procurado25 = '25.75'
número_procurado30 = '30.9'
número_procurado36 = '36.05'
vezes5 = contar_elemento5(todas_as_linhas, número_procurado5, número_procurado8, número_procurado10, número_procurado15, número_procurado20, número_procurado25, número_procurado30, número_procurado36)
total5 = vezes5 * 5.15
print(f"Foram vendidos {vezes5} Red Bulls, totalizando {total5}")
print(f'Totalizando R${total3 + total5} vendidos na Sede')
