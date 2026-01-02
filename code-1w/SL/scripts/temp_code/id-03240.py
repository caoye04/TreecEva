def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count


def extract_features(raw_text):
    words = raw_text.split()
    word_lengths = [len(w.strip(".,!?")) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    palindrome_count = sum(1 for w in words if w.lower() == w.lower()[::-1] and len(w) > 1)
    return word_lengths, avg_length, palindrome_count

raw_input = "Level radar stats nana test case"
word_data, mean_len, palindromes = extract_features(raw_input)

# Simulate data transformation pipeline
buffer = []
for val in word_data:
    if val % 2 == 0:
        buffer.append(val ** 0.5)
    else:
        buffer.append(val * 2)

processed_data = [round(x) for x in buffer if x != 0]

# Irrelevant distraction: frequency analysis with no impact
freq_map = {}
for item in processed_data:
    freq_map[item] = freq_map.get(item, 0) + 1
duplicate_check = [k for k, v in freq_map.items() if v > 1]

# Misleading intermediate calculation (not used in final result)
baseline_offset = sum(processed_data) % 7
adjustment_factor = 0
if baseline_offset > 3:
    adjustment_factor = 2
else:
    adjustment_factor = -1

# Real logic begins: detect peaks in transformed data
peak_count = analyze_pattern(processed_data)

# Secondary feature: check symmetry in first half
midpoint = len(processed_data) // 2
first_half = processed_data[:midpoint]
symmetric_match = 0
for i in range(len(first_half)):
    if i < len(first_half) - i - 1:
        if first_half[i] == first_half[-(i+1)]:
            symmetric_match += 1

# Tertiary red herring: string slicing on numeric representation
str_version = ''.join(map(str, processed_data))
overlap_segment = str_version[2:6]  # unused after this
checksum_guess = sum(int(c) for c in overlap_segment if c.isdigit()) % 9  # dead end

# Final computation using only peak_count and symmetric_match
scaling_factor = 3.5
final_score = 0
final_score = int((peak_count * scaling_factor) + symmetric_match)

# Output required format
print(f"Target result: {final_score}")