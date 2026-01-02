def preprocess_sequence(seq):
    return [x for x in seq if x % 3 == 0]

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return sum([len(str(x)) for x in data])

# Another decoy function with misleading intermediate output
def compute_shadow_metric(arr):
    shadow_value = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            shadow_value += arr[i] * 2
        else:
            shadow_value -= arr[i]
    return shadow_value  # never used

# Character counting function (suggested paradigm)
def count_chars(text_list):
    total = 0
    for t in text_list:
        total += len(t)
    return total

# Linear search implementation (suggested paradigm)
def find_first_exceeding(arr, threshold):
    for i, val in enumerate(arr):
        if val > threshold:
            return i
    return -1

# Main logic chain
sequence_pool = [12, 15, 18, 22, 24, 27, 30, 33, 36, 40]
filtered_batch = preprocess_sequence(sequence_pool)

# Decoy variables with plausible but irrelevant computations
aggregation_key = sum(filtered_batch) * 2 - 100
baseline_offset = len(sequence_pool) + len(filtered_batch)
shadow_diagnostic = compute_shadow_metric(filtered_batch)

# Real work begins: construct logic core
logic_core = []
for num in filtered_batch:
    bin_rep = bin(num)[2:]
    ones_count = bin_rep.count('1')
    if ones_count % 2 == 1:
        logic_core.append(num // 3)
    else:
        logic_core.append(-(num // 3))

# Diagnostic map creation using conditional expressions (required feature)
diagnostic_map = {
    x: ('high' if x > 10 else 'low' if x < 0 else 'medium') for x in logic_core
}

# Simulate character counting on fake labels
label_set = [f"node_{i}_{v}" for i, v in enumerate(diagnostic_map.values())]
char_count_total = count_chars(label_set)

# Red herring: linear search for something irrelevant
trigger_index = find_first_exceeding(logic_core, 15)

# Critical operation hidden among distractions
temp_result = 0
for k, v in diagnostic_map.items():
    if v == 'high':
        temp_result += k * 2
    elif v == 'medium':
        temp_result += k
    else:
        temp_result -= 1

# Key statement embedded in post-processing
adjustment_factor = char_count_total // (trigger_index + 1) if trigger_index != -1 else 0
final_diagnostic = temp_result + adjustment_factor - baseline_offset

# Print final result as required
print(f"Result: {final_diagnostic}")