def simpleSort(unsortInput, sortInput = []):
	if len(unsortInput) == 0:
		return sortInput
	else:
		i = unsortInput.index(min(unsortInput))
		x = unsortInput.pop(i)
		sortInput.append(x)
		return simpleSort(unsortInput, sortInput)
