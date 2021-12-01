import utils

# Retorna o valor máximo que pode ser colocado em uma 
# Mochila Booleana de capacidade W
def mochilaBooleana(W, wt, val):
    n = len(val)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Constrói a tabela K[][] de maneira "bottom-up"
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

def mochilaPequena():
    return [[60, 100, 120], [10,20,30]]

def mochilaGrande():
    return [[60, 100, 120, 500, 200, 30, 50, 600, 100], [10, 20,  30,  50,  10,  10, 20, 15,  10]]

def testeMochilaPequena():
    print("----------- Iniciando rotina com mochila de tamanho pequeno --------------") 
    W = 50
    val, wt = mochilaPequena()
    start = utils.getTime()
    result = mochilaBooleana(W, wt, val)
    end = utils.getTime()
    print("--- %s seconds ---" % (end-start))
    print("O maximo valor para a mochila é de " + str(result) + "\n")

def testeMochilaGrande():
    print("----------- Iniciando rotina com mochila de tamanho grande --------------")
    W = 50
    val, wt = mochilaGrande()    
    start = utils.getTime()
    result = mochilaBooleana(W, wt, val)
    end = utils.getTime()
    print("--- %s seconds ---" % (end-start))
    print("O maximo valor para a mochila é de " + str(result) + "\n")

def main():    
    testeMochilaPequena()
    testeMochilaGrande()

main()
 