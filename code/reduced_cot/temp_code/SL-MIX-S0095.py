import functools
import base64

def length_normalize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tokens = func(*args, **kwargs)
        return [token if len(token) <= 10 else token[:10] for token in tokens]
    return wrapper

@length_normalize
def tokenize_and_filter(text):
    stop_words = {'the', 'is', 'in', 'at', 'which', 'on', 'a', 'an'}
    tokens = text.lower().replace(',', '').replace('.', '').split()
    return [t for t in tokens if t not in stop_words]

original_text = "The quick brown fox jumps over the lazy dog in the marketplace at dawn."
vocabulary_base = {
    'quick': 'qck', 'brown': 'brwn', 'fox': 'fx', 'jumps': 'jmps', 
    'over': 'ovr', 'lazy': 'lzy', 'dog': 'dg', 'marketplace': 'mrktplc', 'dawn': 'dwn'
}
additional_vocab = {
    'quick': 'QUICK', 'jumps': 'JUMPS', 'dog': 'DOG', 'unknown': 'UNK'
}

merged_vocab = {**vocabulary_base, **additional_vocab}
filtered_tokens = tokenize_and_filter(original_text)
encoded_tokens = []
normalized_char_count = 0

for i, token in enumerate(filtered_tokens):
    if i > 5:
        break
    encoded_token = merged_vocab.get(token, base64.b64encode(token.encode()).decode()[:8])
    if len(encoded_token) == 0:
        continue
    encoded_tokens.append(encoded_token)
    normalized_char_count += len(encoded_token)
    if normalized_char_count > 20:
        break

print(f"Result: {normalized_char_count}")