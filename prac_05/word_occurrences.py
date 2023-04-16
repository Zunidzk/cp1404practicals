import operator

text = input("Enter a string: ")
# Split the string into words
words = text.split()
counts_words = {}
for word in words:
    if word in counts_words:
        counts_words[word] += 1
    else:
        counts_words[word] = 1

sorted_counts_words = sorted(counts_words.items(), key=operator.itemgetter(0))

max_len_words = max(len(word) for word, count in sorted_counts_words)

print("Text: this is a collection of words of nice words this is a fun thing it is :", text)
for word, count in sorted_counts_words:
    print(f"{word:{max_len_words}} : {count}")
