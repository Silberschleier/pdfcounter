import slate


def contains_word(word, word_list):
    for key in word_list:
            if key.lower() in word.lower():
                word_list[key] += 1

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
        contains_word(word, words_negative)
        contains_word(word, words_positive)


count_negative = 0
count_positive = 0

print "Positive:"
print "---------"
for key, value in sorted(words_positive.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    count_positive += value
    print "%s: %s" % (key, value)


print "\n\nNegative:"
print "---------------"
for key, value in sorted(words_negative.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    count_negative += value
    print "%s: %s" % (key, value)


print "Total: postive = %s, negative = %s" % (count_positive, count_negative)