# You don't have to choose fin. I just chose it because it is a common name for an object used for input.
fin = open('words.txt')

def has_no_e(word):
    for char in word:
        if char in 'e':
            return False
    return True     # This causes only the words without an e to appear

count = 0      # It starts at 0 and it will soon contain the total # of eligible words
for line in fin:
    word = line.strip() #Strip gets rid of the whitespace
    if has_no_e(word):
        count += 1
        print word

percent = (count / 113809.0) * 100 # The reason you divide by 113809.0 is because that is how many words there are.
#  the .0 makes it a float and if you didn't have it the percent gathered below would say 0%

print str(percent) + "% of the words don't have an 'e'."
