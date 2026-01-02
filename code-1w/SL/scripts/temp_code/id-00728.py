def preprocess_text(text_list):
    # Irrelevant text preprocessing with distractors
    cleaned = []
    for item in text_list:
        item = item.strip().lower()
        item = ''.join(ch for ch in item if ch.isalnum())
        cleaned.append(item)
    return cleaned

# Misleading data transformation
raw_strings = ['  Data@Point1 ', 'Meta$Value2', 'Entry#Three']
tokenized = [s.split('@') for s in raw_strings]
flattened_tokens = [item for sublist in tokenized for item in sublist]
processed_text = preprocess_text(flattened_tokens)

# Decoy statistical function (never used)
def compute_zscore(val, mean_val, std_dev):
    if std_dev == 0:
        return 0
    return (val - mean_val) / std_dev

# Real computation begins here — complex weighting logic disguised among noise
base_values = [3, 7, 12, 18, 25]
index_offsets = [i**2 % 7 for i in range(len(base_values))]
adjusted_vals = [base_values[i] + index_offsets[i] for i in range(len(base_values))]

# Weight matrix – only one row is actually used
weights = [
    [0.1, 0.2, 0.3, 0.4, 0.5],
    [0.5, 0.4, 0.3, 0.2, 0.1],  # This row is irrelevant
    [0.2, 0.3, 0.4, 0.5, 0.6]   # This row is also unused
]

# Conditional selection based on dummy criterion
threshold_metric = sum(adjusted_vals) / len(adjusted_vals)
use_weight_row = 0
if threshold_metric > 15:
    use_weight_row = 1
else:
    use_weight_row = 0  # Actual path taken

# Another red herring: bit manipulation that computes but isn't used
bit_encoded = 0
for v in adjusted_vals:
    bit_encoded ^= (v << 2) | (v >> 1)

# Distractor: unused dictionary mapping
status_map = {i: ('high' if i > 10 else 'low') for i in adjusted_vals}

# Core logic hidden among distractions
scaling_factor = 1.5
data_set = [val * scaling_factor for val in adjusted_vals]

# Use of enumerate and zip — required Python feature
weighted_sum = 0
for idx, (val, weight) in enumerate(zip(data_set, weights[use_weight_row])):
    weighted_sum += val * weight

# Secondary adjustment using string-based key (distractor)
key_sequence = 'abcde'
length_penalty = len(key_sequence) * 0.05

# Final scoring logic depends on conditional expression and prior weighted sum
interim_score = weighted_sum - length_penalty

def calculate_final_score(data, w):
    temp = 0
    for x in data:
        if x > 10:
            temp += x * 0.9
        else:
            temp += x * 1.1
    return int(temp + 0.5)  # Round to nearest integer

final_score = calculate_final_score(data_set, weights)

# Output result as required
print(f"Result: {final_score}")