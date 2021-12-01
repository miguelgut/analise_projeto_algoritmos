import utils
import pandas as pd

def mergeSort(list):
    # 1 -> Salva o tamanho da lista
    list_length = len(list)

    # 2 -> Lista com tamanho 1 já está ordenada
    if list_length == 1:
        return list

    # 3 -> Identifica o meio da lista e divide em esquerda e direita
    mid_point = list_length // 2

    # 4 -> Para garantir que todas as partições são divididas em seus componentes individuais,
    # o mergeSort é chamado e uma nova partição da lista é enviada como parâmetro
    left_partition = mergeSort(list[:mid_point])
    right_partition = mergeSort(list[mid_point:])

    # 5 -> O mergeSort retorna uma lista composta de parte esquerda e direita ordenadas
    return merge(left_partition, right_partition)

# 6 -> Recebe as duas listas e retorna uma nova lista feita com o conteúdo das duas outras
def merge(left, right):
    # 7 -> Inicializa uma lista em branco que vai ser populada com os elementos ordenados
    output = []
    
    # Inicializa as variáveis "i" e "j", usadas como ponteiros para iterar pelas listas
    i = j = 0

    # 8 -> Roda o loop principal se ambos ponteiros "i" e "j" são menores que o tamanho da lista esquerda e direita
    while i < len(left) and j < len(right):
        # 9 -> Compara os elementos em cada posição das listas durante cada iteração
        if left[i] < right[j]:
            # A lista resposta é populada com o menor valor
            output.append(left[i])
            # 10 -> Move o ponteiro para a direita
            i += 1
        else:
            output.append(right[j])
            j += 1

    # 11 -> Os remanescentes são selecionados pelo ponteiro atual até o fim da respectiva lista
    output.extend(left[i:])
    output.extend(right[j:])

    return output

def main():
    inputArray = utils.generateRandom(1,999, 6)
    print("Input array = ", inputArray)

    output = mergeSort(inputArray)
    print("Merge sort = ", output)

def multiTest():
    executionTime = []
    count = 0
    for x in utils.getFiles():
        start = utils.getTime()
        mergeSort(x)
        end = utils.getTime()
        executionTime.append([len(x)+1, end-start])
        print(len(x)+1) 
        print("--- %s seconds ---" % (end-start))

    utils.saveDataFrame(executionTime, 'results/mergeSort')

def test():
    executionTime = []
    start = utils.getTime()
    output = insertionSort(utils.getFile("10_320,000"))
    end = utils.getTime()
    executionTime.append([len(file)+1, end-start])
    print(len(file)+1) 
    print("--- %s seconds ---" % (end-start))

multiTest()