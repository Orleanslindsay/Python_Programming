def find(word,letter):
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return "Character not in Sequence!"


print(find("Python","y"))