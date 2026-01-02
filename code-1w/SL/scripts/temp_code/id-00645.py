def normalize_string(s):
    return s.strip().lower().replace(' ', '_')

# Simulate user input processing with noise
raw_inputs = [' Alice', 'BOB ', 'Charlie ', 'DANA', ' eve ']
valid_names = [normalize_string(name) for name in raw_inputs if len(name.strip()) > 1]

# Auxiliary computation - irrelevant to final result
length_sum = 0
for name in valid_names:
    length_sum += len(name)
average_length = length_sum / len(valid_names) if valid_names else 0

# Data transformation pipeline
encoded_values = []
for i, name in enumerate(valid_names):
    # Compute a hash-like value using position and name characteristics
    char_value = sum(ord(c) for c in name if c.isalpha())
    temp_score = (char_value + i * 10) % 100
    encoded_values.append(temp_score)

# Misleading statistical analysis (dead-end)
deviation_from_avg = []
for val in encoded_values:
    deviation_from_avg.append(abs(val - average_length))
median_deviation = sorted(deviation_from_avg)[len(deviation_from_avg)//2] if deviation_from_avg else 0

# Core logic: filter and aggregate meaningful scores
def process_scores(scores):
    filtered = [s for s in scores if s % 2 == 1]  # Keep only odd scores
    adjusted = [s + 5 for s in filtered]  # Boost each score
    return adjusted

processed_data = process_scores(encoded_values)

# Secondary distraction: analyze letter frequency (unused)
all_chars = ''.join(valid_names)
letter_freq = {}
for c in all_chars:
    if c.isalpha():
        letter_freq[c] = letter_freq.get(c, 0) + 1
max_frequency = max(letter_freq.values()) if letter_freq else 0

# Final scoring with red herring variables
redundant_factor = len(letter_freq) * median_deviation
scaling_offset = len(valid_names) > 3 and len(processed_data) < 10

# Critical statement
final_score = calculate_final_score(processed_data)

def calculate_final_score(data):
    base = sum(data)
    penalty = len([x for x in data if x > 50]) * 2
    bonus = 10 if len(data) >= 3 else 0
    return base - penalty + bonus

Result: {final_score}