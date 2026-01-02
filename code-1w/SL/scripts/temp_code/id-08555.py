def analyze_text(text):
    char_freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Irrelevant computation: letter pair frequency (not used later)
    pair_freq = {}
    for i in range(len(text) - 1):
        pair = text[i:i+2].lower()
        if pair.isalpha():
            pair_freq[pair] = pair_freq.get(pair, 0) + 1

    # Distractor: unused transformation
    reversed_freq = {k: v for k, v in sorted(char_freq.items(), key=lambda x: -ord(x[0]))}
    
    return char_freq

# Misleading data preprocessing path (dead end)
def legacy_normalize(data):
    return [x.strip('!?') for x in data if len(x) > 0]  # never called

# Recursive digit sum — irrelevant but looks important
def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(int(d) for d in str(n)))

# Bit manipulation red herring
def obscure_key(value):
    result = 0
    for i in range(8):
        result ^= (value >> i) & 1
    return result << 4

# Real processing chain
def extract_vowel_count(freq_dict):
    vowels = 'aeiou'
    return sum(freq_dict.get(v, 0) for v in vowels)

def extract_consonant_count(freq_dict):
    consonants = ''.join([chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in 'aeiou'])
    return sum(freq_dict.get(c, 0) for c in consonants)

# Simulate weighting model with decoy parameters
def apply_weighting(vowels, consonants, bias_mode=False, scale_factor=1.0):
    if bias_mode:  # never triggered
        return (vowels * 0.3 + consonants * 0.7) * scale_factor
    return vowels * 1.5 + consonants * 0.8

# Core logic hidden among distractions
def transform_sequence(data_list):
    # Unused sorting variant
    sorted_by_len = sorted(data_list, key=len, reverse=True)
    # Actual relevant operation
    joined = ''.join(data_list).lower()
    intermediate = ''.join([c for c in joined if c in 'aeioubcdfg'])
    return intermediate * 2  # double it for no clear reason (but affects output)

# Another decoy function that looks like scoring
def heuristic_rank(items):
    scores = []
    for item in items:
        score = 0
        for ch in item:
            score += ord(ch) % 7
        scores.append(score)
    return sum(scores) // len(scores) if scores else 0

# Main pipeline
raw_input = ['Hello', 'World', 'Code', 'AI', 'Test']

# Dead code branch
if len(raw_input) > 10:
    normalized = [s.upper() for s in raw_input]
elif len(raw_input) == 3:
    normalized = [s[::-1] for s in raw_input]
else:
    normalized = [s for s in raw_input if 'x' not in s]  # actually used, filters nothing

processed_chars = transform_sequence(normalized)
character_map = analyze_text(processed_chars)

vowel_total = extract_vowel_count(character_map)
consonant_total = extract_consonant_count(character_map)

# Decoy normalization
norm_sum = vowel_total + consonant_total
if norm_sum > 0:
    v_ratio = round(vowel_total / norm_sum, 6)
    c_ratio = round(consonant_total / norm_sum, 6)
    entropy_proxy = -sum(r * __import__('math').log(r) for r in [v_ratio, c_ratio] if r > 0)

weighted_value = apply_weighting(vowel_total, consonant_total)

# Multi-step accumulation with red herring variables
accum = 0
for i, c in enumerate(processed_chars[:10]):
    if c in 'aeiou':
        accum += ord(c) % 7
    elif i % 2 == 0:
        accum += 1

# Fake checksum using bitwise ops
checksum = 0
for val in [vowel_total, consonant_total, len(processed_chars)]:
    checksum ^= (val * 3) & 0xF

# Final scoring with fake complexity
aux_data = {'mode': 'A', 'level': 7, 'flags': [True, False, True]}

# The real answer depends only on weighted_value and fixed transforms
intermediate_result = int(weighted_value) + (checksum * 2)

# Critical statement
final_score = intermediate_result - 5

# Print result as required
print(f"Target result: {final_score}")