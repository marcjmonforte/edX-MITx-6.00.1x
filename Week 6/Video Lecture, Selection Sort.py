def selectionSort(L):
	suffixSt = 0
	while suffixSt != len(L):
		for i in range(suffixSt, len(L)):
			if L[i] < L[suffixSt]:
				L[suffixSt], L[i] = L[i], L[suffixSt]
		suffixSt += 1

def selSort(L):
	for i in range(len(L) - 1):
		print(L)
		minIndx = i
		minVal = L[i]
		j = i + 1
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal = L[j]
			j += 1
		temp = L[i]
		L[i] = L[minIndx]
		L[minIndx] = temp

test = [1, 5, 3, 8, 4, 9, 6, 2]
selSort(test)
print(test)