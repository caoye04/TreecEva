def analyze_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

# Irrelevant helper function (dead code path)
def encrypt_shift(s, shift=3):
    result = ''
    for c in s:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

# Misleading data transformation
text_corpus = 'QuantumQuokkasQuicklyQuarantineQuirkyQueries'
char_freq = analyze_frequency(text_corpus)
sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

decoy_sum = 0
for ch, count in sorted_chars:
    decoy_sum += ord(ch) * count  # Looks important but unused later

# Bit manipulation red herring
bit_sequence = 0b110101
shifted_bits = (bit_sequence << 3) & 0b11111111
inverted = ~shifted_bits & 0b11111111

# Dummy metrics with modular arithmetic
mod_metrics = []
for i in range(1, len(sorted_chars[:5])):
    mod_metrics.append((decoy_sum * i) % 17)

# Actual relevant logic buried within distractions
def calculate_entropy(freq_dict):
    total = sum(freq_dict.values())
    entropy = 0.0
    for count in freq_dict.values():
        p = count / total
        entropy -= p * __import__('math').log2(p) if p > 0 else 0
    return round(entropy, 6)

entropy_value = calculate_entropy(char_freq)

# Conditional logic with case conversion distraction
caps_count = sum(1 for c in text_corpus if c.isupper())
if caps_count > 10:
    adjustment_factor = 0.9
else:
    adjustment_factor = 1.1  # This branch triggers

# Dictionary-based weighting system (core concept)
weight_map = {k: (1 + (ord(k) - ord('a')) % 7) for k in char_freq.keys()}
total_weight = sum(weight_map[k] * char_freq[k] for k in char_freq)

# Simulated metric normalization
norm_constant = 42.0
if norm_constant > 0:
    normalized_metric = total_weight / norm_constant
else:
    normalized_metric = total_weight

# Another decoy structure: unused list comprehension
_ = [i**2 for i in range(10) if i % 3 == 0]

# Core evaluation logic hidden among distractors
metric_data = {
    'entropy': entropy_value,
    'adjustment': adjustment_factor,
    'base_score': normalized_metric,
    'version': 'Q4-2024',
    'active': True
}

def evaluate_performance(data):
    if not data['active']:
        return -1
    
    score = data['base_score'] * data['adjustment']
    
    # Additional conditional tweak based on entropy threshold
    if data['entropy'] > 3.0:
        score += 15.0
    elif data['entropy'] > 2.0:
        score += 8.5  # This branch triggers
    else:
        score += 3.0
        
    # Final bitwise touch (actually irrelevant due to float)
    try:
        score = int(score)
        score = (score ^ 0b101010) | 0b1111
        score = float(score)
    except:
        pass
        
    return score

# Critical execution point
final_score = evaluate_performance(metric_data)
Result: {final_score}