text_corpus = "apple banana cherry apple date banana elderberry"
word_list = text_corpus.split()
word_frequency = {}
for word in word_list:
    word_frequency[word] = word_frequency.get(word, 0) + 1
unique_words = set(word_frequency.keys())
unique_words_counter = len(unique_words)
final_count = unique_words_counter
print(f"Result: {final_count}")