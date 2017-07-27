def bubbleSort(L):
	swap = False
	while not swap:
		swap = True
		print(L)
		for j in range(1, len(L)):
			if L[j-1] > L[j]:
				swap = False
				temp = L[j]
				L[j] = L[j-1]
				L[j-1] = temp

test = [1, 5, 3, 8, 4, 9, 6, 2]
bubbleSort(test)