import math

# System integrity parameters
def compute_integrity_threshold(base, modifier):
    return (base ** 0.5) + (modifier / 4)

# Irrelevant helper - dead path
def deprecated_hash(seq):
    return sum([ord(c) * (i + 1) for i, c in enumerate(seq)]) % 100

# Core analysis function with multiple concepts
base_signal = [32, 64, 97, 120, 101, 112]
offset_key = 97
signal_chars = [chr(c - offset_key) for c in base_signal if c > 90]

# Distractor: unused transformation
encoded_map = {c: ord(c) % 13 for c in signal_chars}

# Critical data set
raw_sequence = ''.join(signal_chars)  # 'safeex'

# Misleading checksum (not used in final result)
checksum = 0
for i, c in enumerate(raw_sequence):
    checksum += ord(c) * (i + 1)
checksum = checksum % 97

# Character frequency analysis (relevant)
frequency_map = {}
for c in raw_sequence:
    frequency_map[c] = frequency_map.get(c, 0) + 1

# Determine rare characters (appearing only once)
rare_characters = {k for k, v in frequency_map.items() if v == 1}  # {'s', 'f', 'x'}

# Set operations on character groups
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {c for c in raw_sequence if c not in vowels}

# Secure segments: consonants that are rare
secure_segments = consonants & rare_characters  # {'s', 'f', 'x'}

# Compute entropy factor from character distribution
unique_count = len(set(raw_sequence))
total_count = len(raw_sequence)
probabilities = [frequency_map[c] / total_count for c in frequency_map]
entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)

# Secondary distractor: unused entropy variant
local_entropy = 0
for c in raw_sequence[:3]:
    p = frequency_map[c] / total_count
    local_entropy -= p * math.log2(p) if p > 0 else 0

# Decoy normalization (never applied)
normalization_factor = 1.0
if len(secure_segments) > 5:
    normalization_factor = 0.8
elif 'z' in secure_segments:
    normalization_factor = 0.9

# Key computation step
entropy_factor = round(entropy * 10, 4)  # ~15.2877 → 15.2877

# Target statement
filtration_score = len(secure_segments) * entropy_factor

# Final red herring: unused conditional adjustment
if total_count > 10 and checksum < 50:
    filtration_score += 100
elif len(vowels & set(raw_sequence)) >= 2:
    filtration_score *= 0.9  # Not triggered

print(f"Target result: {filtration_score}")