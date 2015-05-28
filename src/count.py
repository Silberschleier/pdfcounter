import slate
import string
import time

iterations = 0
number_words = 0

pdfpath = '../text.pdf'

''' Set page_begin < 0 and page_end < 0 to process whole file '''
page_begin = -1
page_end = -1


''' Counting function '''
def count_words(word, word_list):
    global iterations
    iterations += 1
    s = word.lower().translate(string.maketrans("", ""), string.punctuation)
    if word_list.get(s) is not None:
        word_list[s] += 1

words_positive = {}
words_negative = {}

''' Reading the wordlists and initialize each counter with zero '''
file_positive = open("../wordlist_positive.txt")
for line in file_positive:
    words_positive[line.rstrip('\n').lower()] = 0

print "Positive wordlist contains %s words." % len(words_positive)

file_negative = open("../wordlist_negative.txt")
for line in file_negative:
    words_negative[line.rstrip('\n').lower()] = 0

print "Negative wordlist contains %s words.\n" % len(words_negative)

''' Load pdf and convert to strings '''

print "Opening '%s'..." % pdfpath
time_start = time.time()

with open(pdfpath) as file:
    document = slate.PDF(file)

time_end = time.time()


print "Extracting text took %ss\n" % (time_end - time_start)
print "Document has %s pages.\n" % len(document)

if page_begin <= 0:
    page_begin = 1
if page_end < 0:
    page_end = len(document)

if page_begin > len(document):
    page_begin = len(document)
if (page_end > len(document)) or (page_end < page_begin):
    page_end = page_begin

print "Analyzing pages %s to %s...\n" % (page_begin, page_end)

''' Iterate through data '''

time_start = time.time()

for page in document[page_begin-1:page_end-1]:
    words = page.split(" ")
    number_words += len(words)
    for word in words:
        count_words(word, words_positive)
        count_words(word, words_negative)

time_end = time.time()

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

percent_positive = round(count_positive / float(number_words) * 100, 2)
percent_negative = round(count_negative / float(number_words) * 100, 2)

print "Total: positive = %s (%s%%), negative = %s (%s%%)\n" % (count_positive, percent_positive, count_negative, percent_negative)
print "Processed %s words." % number_words
print "Processing finished after %s iterations (time: %ss)" % (iterations, time_end - time_start)