def all_variants(text):
    for i in range(len(text)):
        for l in range(len(text)-i):
            yield text[l:l+i+1]


word = all_variants("abc")
for i in word:
    print(i)
