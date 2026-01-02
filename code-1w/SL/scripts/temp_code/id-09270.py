def analyze_metrics(data, threshold=5):
    filtered = [x for x in data if x > threshold]
    temp_sum = sum(filtered) * 0.8
    normalization_factor = len(data) + 1
    adjusted = temp_sum / normalization_factor
    return adjusted


def collect_insights(values):
    result = []
    for val in values:
        if val % 2 == 0:
            result.append(val ** 0.5)
    return result

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return (x ** 2 + 3 * x + 1) // 2

# Misleading accumulator with no impact
total_trace = 0
for i in range(12):
    total_trace += i * 2

# Decoy variables and operations
decoys = [3, 6, 9, 12]
offset_adjustment = sum(decoys) * 0.1
offset_adjustment *= 0  # Neutralized but looks important

# Core dataset
raw_input = [4, 7, 2, 9, 5, 8, 6]

# Bit manipulation red herring
bitmask = 0b10101
masked_values = [n & bitmask for n in raw_input]
suspicious_total = sum(masked_values) >> 1

# Set operations (required feature)
feedback_pool = {4, 7, 2, 9, 5, 8, 6, 10}
noise_set = {1, 3, 5, 7, 11}
feedback_set = feedback_pool - noise_set  # Remove interference elements

# Unused transformation chain
intermediate_log = [
    f'entry_{x}' for x in sorted(feedback_set) if x in {7, 9, 6, 4, 8}  # Complex filter
]

# String method distraction (required feature)
log_strings = ['error', 'warning', 'info', 'debug']
severity_count = len([s for s in log_strings if 'e' in s])
flagged = ''.join(log_strings).count('w')

# Conditional accumulation with nested logic
running_tally = 0
for item in feedback_set:
    if item > 5:
        running_tally += item
    else:
        running_tally -= item

# Another decoy calculation
phantom_score = len(feedback_pool.intersection(noise_set)) * 100

# Key function that uses list comprehension and set (required features)
def aggregate_performance(records):
    base_scores = [x * 2 for x in records]  # List comprehension
    bonus = len(records) // 2
    penalty = sum([x for x in base_scores if x > 10]) // 5
    return sum(base_scores) + bonus - penalty

# Secondary irrelevant transformation
snapshot = tuple(sorted(feedback_set, reverse=True)[:4])
shadow_copy = [x + 1 for x in snapshot if x % 2 == 1]

# Critical execution point
final_score = aggregate_performance(feedback_set)

# Print required output
print(f"Result: {final_score}")