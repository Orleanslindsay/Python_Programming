def find(word,letter):
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return "Character not in Sequence!"


print(find("Python","y"))
""""The code is to check the index of a word. Now the function (find) is defined 
which contains parameter, word and letter respectively.
so, if the letter is not found in the word, it return the string, Character not in sequence.
But if the letter is found in the word(1st parameter), it will print out it 
index for the user"""