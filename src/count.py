import slate

with open('../text.pdf') as file:
    doc = slate.PDF(file)

for s in doc:
    print s + "\n"