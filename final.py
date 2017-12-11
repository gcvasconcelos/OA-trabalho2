# checa a existencia de indices repetidos
def verificaIndices(arq_registros):
    registros = []
    for lines in arq_registros:
        dados = dados = lines.split(',')
        registros.append(dados[0])
    # compara a quantidade de registros com a quantidade de registros sem repetições
    if len(registros) == len(set(registros)):
        # nao ha arquivos repetidos
        return 1
    else:
        # arquivo invalido
        return 0

# escreve arquivo contentdo apenas indices e posicoes
def criaArqIndice(arq_registros, arq_indices):
    pos = 0
    for lines in arq_registros:
        dados = lines.split(',')
        arq_indices.write(dados[0] + ' ' + str(pos) + '\n')
        pos += 1
    return

# o que será uma página:
# pagina = {}
# int totalChaves
# int chaves = [128]
# 
#
#

regs = 'data2.txt'
arq_registros = open(regs,'r')
validade = verificaIndices(arq_registros)
if validade:
    arq_indices = open('indice.txt','w')
    arq_registros = open(regs,'r')
    criaArqIndice(arq_registros, arq_indices)
    arq_indices.close()
    arq_registros.close()
else:
    print 'arquivo invalido'
