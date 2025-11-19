sentence = "the quick brown fox jumps over the lazy dog and the cat"
tokens = sentence.split()
frequency = {token: tokens.count(token) for token in set(tokens)}
filtered_tokens = [token for token in tokens if frequency[token] > 1]
print(f"Result: {len(filtered_tokens)}")