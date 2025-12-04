text_data = "programming assessment benchmark"
text_chars = list(text_data.replace(" ", ""))
char_frequencies = [text_chars.count(c) for c in text_chars]
unique_count = len(set(text_chars))
print(f"Result: {unique_count}")