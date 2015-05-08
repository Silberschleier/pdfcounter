import slate

words_positive = []
words_negative = []

file_positive = open("../wordlist_positive.txt")
for line in file_positive:
    words_positive.append((line.rstrip('\n'), 0))

file_negative = open("../wordlist_negative.txt")
for line in file_negative:
    words_negative.append((line.rstrip('\n'), 0))


print words_positive
print words_negative

with open('../text.pdf') as file:
    document = slate.PDF(file)

for page in document:
    words = page.split(" ")
