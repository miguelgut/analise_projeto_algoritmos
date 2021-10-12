import utils

def insertionSort(inputArray):
    arr = [item for sublist in inputArray for item in sublist]

    # Percorre de 1 ao tamanho do array
    for i in range(1, len(arr)):

        key = arr[i]

        # Move os elementos de arr[0..i-1], que são maiores que a chave atual, 
        # Para uma posição adiante da sua atual
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

    return arr

def main():
    inputArray = utils.generateRandom(1,999, 6)
    print("Input array = ", inputArray)

    output = insertionSort(inputArray)
    print("Insertion sort = ", output)

def multiTest():
    executionTime = []
    for x in utils.getFiles():
        start = utils.getTime()
        insertionSort(x)
        end = utils.getTime()
        executionTime.append([len(x)+1, end-start])
        print(len(x)+1) 
        print("--- %s seconds ---" % (end-start))

    utils.saveDataFrame(executionTime, 'insertionSort')

def test():
    executionTime = []
    start = utils.getTime()
    insertionSort(utils.getFile("10_320,000"))
    end = utils.getTime()
    executionTime.append([len(x)+1, end-start])
    print(len(x)+1) 
    print("--- %s seconds ---" % (end-start))

multiTest()