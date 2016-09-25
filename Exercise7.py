# You don't have to choose fin. I just chose it because it is a common name for an object used for input.
fin = open('words.txt')

def is_three_consecutive_double_letters(word):
# Here is where we test what words have 3 consecutive double letters
    i = 0
    count = 0  # It starts at 0 and it will soon contain the total # of eligible words
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3: # We only want words with 3 consecutive double letters to appear
                return True # This causes only the words without an e to appear
            i = i + 2 # QUESTION (As I looked for the answer from what was given, but I do not understand why this had to be a 2.
        else:
            count = 0
            i = i + 1
    return False


def find_three_consecutive_double_letters():
    # Here is where the words will be printed once verified
    fin = open('words.txt')
    for line in fin:
        word = line.strip() #Strip gets rid of the whitespace
        if is_three_consecutive_double_letters(word):
            print word

print 'Here are the few words in the text file that have three consecutive double letters.'
find_three_consecutive_double_letters()
print ''
