# You don't have to choose fin. I just chose it because it is a common name for an object used for input.
fin = open('words.txt')
for line in fin:
	word = line.strip() #Strip gets rid of the whitespace
	if len(word) > 20:   # This is where you set the limit as to how many characters the words should have.
		print (word)


