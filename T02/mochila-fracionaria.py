import utils

# Criação da classe ItemValue para facilitar o armazenamento
class ItemValue:
  
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
  
    def __lt__(self, other):
        return self.cost < other.cost
  
class mochilaFracionaria:
    @staticmethod
    def getMaxValue(wt, val, capacity):
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
  
        # Ordena os itens por valor
        iVal.sort(reverse=True)
  
        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue
  

def mochilaPequena():
    return [[60, 100, 120], [10,20,30]]

def mochilaGrande():
    return [[60, 100, 120, 500, 200, 30, 50, 600, 100], [10, 20,  30,  50,  10,  10, 20, 15, 10]]


def testeMochilaPequena():
    print("----------- Iniciando rotina com mochila de tamanho pequeno --------------")
    W = 50
    val, wt = mochilaPequena()    
    start = utils.getTime()
    result = mochilaFracionaria.getMaxValue(wt, val, W)
    end = utils.getTime()
    print("--- %s seconds ---" % (end-start))
    print("O maximo valor para a mochila é de " + str(result) + "\n")

def testeMochilaGrande():
    print("----------- Iniciando rotina com mochila de tamanho grande --------------")
    W = 50
    val, wt = mochilaGrande()    
    start = utils.getTime()
    result = mochilaFracionaria.getMaxValue(wt, val, W)
    end = utils.getTime()
    print("--- %s seconds ---" % (end-start))
    print("O maximo valor para a mochila é de " + str(result) + "\n")

def main():
    testeMochilaPequena()
    testeMochilaGrande()

main()