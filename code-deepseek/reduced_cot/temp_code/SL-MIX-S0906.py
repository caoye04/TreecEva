import itertools

def analyze_char_distribution(text_sample):
    # Distractor: Character frequency analysis (irrelevant to final result)
    char_counts = {}
    for char in text_sample:
        char_counts[char] = char_counts.get(char, 0) + 1
    return sum(char_counts.values())  # Returns length, not used

def compute_checksum(data_values):
    # Misleading intermediate computation
    temp_sum = sum(data_values)
    bitwise_adj = temp_sum & 0xFF  # Unused bit manipulation
    return temp_sum // len(data_values) if data_values else 0

# Main processing
input_sequence = [15, 28, 42, 67, 91, 104]
base_offset = 17
redundancy_factor = 3

# Irrelevant character analysis
sample_text = "benchmark_evaluation"
char_total = analyze_char_distribution(sample_text)  # Dead result

# Primary computation chain
filtered_data = [x for x in input_sequence if x % 4 != 0]
permutations = list(itertools.islice(itertools.permutations(filtered_data[:3]), 5))

# Misleading intermediate step
checksum_value = compute_checksum(input_sequence)
intermediate_result = sum(filtered_data) - base_offset

# Distractor computation (unused)
shadow_calc = (intermediate_result * redundancy_factor) % 256

# Critical path
processed_value = intermediate_result // len(filtered_data)
correction_factor = (processed_value % 7) + 2

# Target statement
final_metric = processed_value - correction_factor

# Redundant verification (dead code path)
if final_metric > 100:
    verification_check = final_metric * 2  # Never executed
else:
    backup_calc = processed_value + correction_factor  # Never used

print(f"Target result: {final_metric}")