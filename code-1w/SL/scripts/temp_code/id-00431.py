def analyze_pattern(sequence):
    # Irrelevant analysis function (dead code path)
    return sum(ord(c) for c in sequence if c.isupper())


def preprocess_data(raw):
    # Distractor: complex but unused transformation
    cleaned = raw.strip().replace(' ', '').lower()
    frequency = {char: cleaned.count(char) for char in set(cleaned)}
    sorted_chars = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))
    return ''.join(sorted_chars)

# Unused helper that looks important
def validate_checksum(data):
    total = 0
    for i, c in enumerate(data):
        total += (i + 1) * ord(c)
    return total % 17 == 0

# Main logic begins
raw_input = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

# Step 1: Extract every second character
step_one = raw_input[::2]  # Takes uppercase letters

# Step 2: Count vowels in extracted string
vowel_count = sum(1 for c in step_one if c.lower() in 'aeiou')

# Step 3: Compute ASCII sum of non-vowels
non_vowel_ascii = sum(ord(c) for c in step_one if c.lower() not in 'aeiou')

# Step 4: Apply modular arithmetic to constrain growth
mod_base = 19
intermediate = (non_vowel_ascii * vowel_count) % mod_base

# Step 5: Simulate data shift with string manipulation
shifted = ''.join(chr((ord(c) - ord('A') + intermediate) % 26 + ord('A')) for c in step_one)

# Step 6: Count character frequency and extract most common
freq_map = {}
for c in shifted:
    freq_map[c] = freq_map.get(c, 0) + 1
most_frequent = max(freq_map.keys(), key=lambda x: freq_map[x])

# Step 7: Compute secondary metric — average position in alphabet
avg_position = sum(ord(c) - ord('A') + 1 for c in shifted) / len(shifted)

# Step 8: Use integer division and rounding to derive adjustment factor
adjustment = round(avg_position // 2) * 3

# Step 9: Final aggregation using multiple inputs
final_score = (intermediate + ord(most_frequent) + adjustment) * len(set(shifted))

# Misleading decoy variables
checksum_valid = (sum(ord(c) for c in shifted) + final_score) % 13 == 0
placeholder_result = analyze_pattern(raw_input)
data_preview = preprocess_data(raw_input)

# Target result output
print(f"Result: {final_score}")