import slate

''' Each wordlist contains tuples containing the words and the number of appearances '''
words_positive = {}
words_negative = {}

''' Reading the wordlists and initialize each counter with zero '''
file_positive = open("../wordlist_positive.txt")
for line in file_positive:
    words_positive[line.rstrip('\n')] = 0

file_negative = open("../wordlist_negative.txt")
for line in file_negative:
    words_negative[line.rstrip('\n')] = 0


with open('../text.pdf') as file:
    document = slate.PDF(file)


for page in document:
    words = page.split(" ")
    for word in words:
        for i in words_negative:
            if i.lower() in word.lower():
                words_negative[i] = words_negative[i] + 1

print words_negative
