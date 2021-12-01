import utils

def countingSort(inputArray):
    inputArray = [item for sublist in inputArray for item in sublist]
    # Encontra o elemento máximo
    maxElement= max(inputArray)
    if(isinstance(maxElement, list)):
        maxElement = max(maxElement)

    countArrayLength = maxElement+1

    # Inicializa o countArray com (max+1) zeros
    countArray = [0] * countArrayLength

    # 1 -> Percorre o inputArray e aumenta a contagem correspondente de cada elemento em 1
    for el in inputArray: 
        countArray[el] += 1

    # 2 -> Para cada elemento no countArray, soma seu valor com o do elemento antigo
    # salvando esse valor como o do elemento antigo
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    # 3 -> Calcula a posição do elemento baseado nos valores do countArray
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray

def main():
    inputArray = utils.generateRandom(1,999, 5)
    print("Input array = ", inputArray)

    output = countingSort(inputArray)
    print("Counting sort = ", output)

def multiTest():
    executionTime = []
    count = 0
    for x in utils.getFiles():
        start = utils.getTime()
        output = countingSort(x)
        end = utils.getTime()
        executionTime.append([len(x)+1, end-start])
        print(len(x)+1) 
        print("--- %s seconds ---" % (end-start))

    utils.saveDataFrame(executionTime, 'results/countingSort')

def test():
    executionTime = []
    start = utils.getTime()
    countingSort(utils.getFile("10_320,000"))
    end = utils.getTime()
    executionTime.append([len(file)+1, end-start])
    print(len(file)+1) 
    print("--- %s seconds ---" % (end-start))

multiTest()