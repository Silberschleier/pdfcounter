import slate
import string

''' Counting function '''
def count_words(word, word_list):
    for key in word_list:
        if key.lower() == word.lower().translate(string.maketrans("", ""), string.punctuation):
            word_list[key] += 1
            break

words_positive = {}
words_negative = {}

''' Reading the wordlists and initialize each counter with zero '''
file_positive = open("../wordlist_positive.txt")
for line in file_positive:
    words_positive[line.rstrip('\n')] = 0

file_negative = open("../wordlist_negative.txt")
for line in file_negative:
    words_negative[line.rstrip('\n')] = 0

''' Load pdf and convert to strings '''
with open('../text.pdf') as file:
    document = slate.PDF(file)

''' Iterate through data '''
for page in document:
    words = page.split(" ")
    for word in words:
        count_words(word, words_positive)
        count_words(word, words_negative)



''' Print the results '''

count_negative = 0
count_positive = 0

print "Positive:"
print "-------------------------------"
print "|   # |            Word | val |"
print "-------------------------------"
idx = 1
for key, value in sorted(words_positive.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    if value > 0:
        count_positive += value
        print "| %3s | %15s | %3s |" % (idx, key, value)
        idx += 1
print "-------------------------------"


print "\n\nNegative:"
print "-------------------------------"
print "|   # |            Word | val |"
print "-------------------------------"
idx = 1
for key, value in sorted(words_negative.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    if value > 0:
        count_negative += value
        print "| %3s | %15s | %3s |" % (idx, key, value)
        idx += 1
print "-------------------------------"


print "Total: postive = %s, negative = %s" % (count_positive, count_negative)