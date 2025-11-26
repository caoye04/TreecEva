def process_text(text):
    words = text.lower().split()
    word_set = set(words)
    return word_set

sample_text = "the quick brown fox jumps over the lazy dog"
word_collection = process_text(sample_text)
unique_words = word_collection
final_count = len(unique_words)
print(f"Result: {final_count}")