text_data = "The quick brown fox jumps over the lazy dog and runs through the forest"
word_list = text_data.split()
filtered_words = [word for word in word_list if len(word) > 3]
processed_words = len(filtered_words)
final_count = processed_words
print(f"Result: {final_count}")