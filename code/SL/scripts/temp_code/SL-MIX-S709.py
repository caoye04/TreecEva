from collections import defaultdict
import statistics

def encode_message(msg):
    return ''.join(chr(ord(c) + 3) for c in msg)

def decode_message(encoded_msg):
    return ''.join(chr(ord(c) - 3) for c in encoded_msg)

def tokenize(text):
    return [word.strip('.,!?') for word in text.split()]

def compute_token_weights(tokens):
    freq = defaultdict(int)
    for token in tokens:
        freq[token] += 1
    total = sum(freq.values())
    return {token: count/total for token, count in freq.items()}

def greedy_select_informative(tokens, weights, k=3):
    sorted_tokens = sorted(weights.items(), key=lambda x: x[1], reverse=True)
    selected = [token for token, _ in sorted_tokens[:k]]
    score = sum(weights[token] for token in selected if token in weights)
    return selected, score

corpus = [
    encode_message("the quick brown fox jumps over the lazy dog"),
    encode_message("a quick movement of the enemy will jeopardize five gunboats"),
    encode_message("quick thinking and brave action were essential")
]

decoded_corpus = [decode_message(msg) for msg in corpus]
token_sets = [tokenize(text) for text in decoded_corpus]
all_tokens = [token for tokens in token_sets for token in tokens]
weights = compute_token_weights(all_tokens)

# Greedy selection of top tokens
_, optimized_score = greedy_select_informative(all_tokens, weights, 4)

# Adjust score using variance of token frequencies
freq_values = list(weights.values())
variance = statistics.variance(freq_values) if len(freq_values) > 1 else 0
adjusted_score = optimized_score * (1 - variance)

# Final calculation involves sorting and selecting maximum
score_components = [optimized_score, variance, adjusted_score]
score_components.sort()
final_metric = score_components[-1] * 1000

print(f"Result: {int(final_metric)}")