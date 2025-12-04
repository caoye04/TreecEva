text_data = "python programming language python code python algorithm data structure"
words = text_data.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
max_count = max(word_freq.values())
max_word = max(word_freq, key=word_freq.get)
final_count = word_freq.get(max_word, 0)
print(f"Result: {final_count}")