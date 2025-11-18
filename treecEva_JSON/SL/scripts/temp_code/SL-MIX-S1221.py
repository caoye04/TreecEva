from itertools import combinations
from statistics import mean, variance

def encode_token(token):
    return sum(ord(c) << (i * 8) for i, c in enumerate(token))

def decode_token(encoded):
    chars = []
    while encoded > 0:
        chars.append(chr(encoded & 0xFF))
        encoded >>= 8
    return ''.join(chars)

class TokenAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.encoded_tokens = [encode_token(t) for t in tokens]
    
    def get_combinations(self, r):
        return list(combinations(self.encoded_tokens, r))
    
    @property
    def token_stats(self):
        lengths = [len(t) for t in self.tokens]
        return {
            'mean_length': mean(lengths),
            'variance_length': variance(lengths) if len(lengths) > 1 else 0
        }

# Process linguistic data
token_stream = ['veritas', 'aeterna', 'mors', 'vincit', 'omnia']
analyzer = TokenAnalyzer(token_stream)

# Step 1: Get pairwise combinations of encoded tokens
pairwise_encoded = analyzer.get_combinations(2)

# Step 2: Calculate XOR similarity for each pair
xor_similarities = []
for a, b in pairwise_encoded:
    xor_result = a ^ b
    # Count set bits (Hamming weight)
    bit_count = bin(xor_result).count('1')
    xor_similarities.append(bit_count)

# Step 3: Statistical analysis of similarities
similarity_mean = mean(xor_similarities)
similarity_variance = variance(xor_similarities) if len(xor_similarities) > 1 else 0

# Step 4: Apply token statistics
length_stats = analyzer.token_stats

# Step 5: Compute final semantic coherence score
semantic_coherence_score = (
    int(similarity_mean * 100) + 
    int(similarity_variance * 10) + 
    int(length_stats['mean_length'] * 1000) + 
    int(length_stats['variance_length'] * 100)
)

print(f"Result: {semantic_coherence_score}")