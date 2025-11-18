sentence = 'The quick brown fox jumps over the lazy dog'
words = sentence.split()
token_length_counts = {len(word): sum(1 for w in words if len(w) == len(word)) for word in words}
print(f"Result: {token_length_counts}")