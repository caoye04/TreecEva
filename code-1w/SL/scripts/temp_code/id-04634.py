from itertools import combinations

def preprocess_text(text):
    # Unnecessary preprocessing step (distractor)
    cleaned = text.lower().replace('.', '').strip()
    words = cleaned.split()
    return [word for word in words if len(word) > 2]

def analyze_frequency(chars):
    # Irrelevant frequency analysis (distractor)
    freq = {}
    for c in chars:
        freq[c] = freq.get(c, 0) + 1
    return freq

def validate_checksum(seq):
    # Distractor function – looks important but unused in final logic
    return sum(seq) % 7 == 0

def compute_entropy(values):
    # Seemingly advanced but irrelevant computation
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def calculate_final_score(data, weights):
    # Core logic begins
    base_values = []
    for item in data:
        if item > 0:
            base_values.append(item * 1.5)
        else:
            base_values.append(item + 5)
    
    # Apply modular arithmetic transformation
    transformed = [v % 13 for v in base_values if v > 3]
    
    # Use itertools to generate pairs (semi-relevant distraction)
    pairs = list(combinations(transformed, 2))
    pair_sum = sum(a + b for a, b in pairs[:10])  # Only first 10 used
    
    # Real contribution: weighted sum on filtered transformed values
    filtered = [v for v in transformed if v % 2 == 1]  # Keep only odd
    weighted = sum(filtered[i] * weights[i % len(weights)] for i in range(len(filtered)))
    
    # Secondary adjustment using string-based logic (bridging paradigms)
    tag = "XyZ"
    shift = sum(ord(c.lower()) - ord('a') for c in tag) % 5  # = (23+24+25) % 5 = 72%5=2
    
    final_score = weighted + pair_sum // 10 + shift
    return final_score

# Main execution
raw_input = "Data stream: alpha beta gamma completed."
chars = [c for c in raw_input if c.isalpha()]

# Irrelevant data structures
freq_map = analyze_frequency(chars)
dummy_checksum = validate_checksum([1, 3, 2, 6, 4])
text_tokens = preprocess_text(raw_input)

# Key data and weights
primary_data = [4, -2, 8, 0, 12, 7]
weights = [2, 3, 1]

# Trigger the main computation
intermediate_entropy = compute_entropy(primary_data)
final_score = calculate_final_score(primary_data, weights)

print(f"Result: {final_score}")