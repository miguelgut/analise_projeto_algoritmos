def bubbleSort(lista):
	temp = ''
	tamanhoLista = len(lista) - 1
	for iterador in range(tamanhoLista,0,-1):
		print("----------------------------------")
		print("Lista Atual:")
		printLista(lista)
		for i in range(iterador):
			print("Percorrendo...")
			if lista[i] > lista[i+1]:
				temp = lista[i]
				lista[i] = lista[i+1]
				lista[i+1] = temp
				print("O digito ("+str(temp)+") deve ir da posicao [" + str(i) + "] para [" + str(i+1) +"]")
			else:
				print("A posicao ["+str(i)+"] e ["+str(i + 1)+"] ja esta ordenada")
		print("\n")


def printLista(lista):
	tamanhoLista = len(lista)
	for j in range(tamanhoLista):
		print(" " + str(j) + "  ", end='')
	print("\n" + str(lista))


lista = [54,26,93,17,77,31,44,55,20]
bubbleSort(lista)


