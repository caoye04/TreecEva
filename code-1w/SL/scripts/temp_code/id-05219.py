def analyze_sequence(data):
    count_vowels = 0
    total_pairs = 0
    temp_sum = 0
    for i, char in enumerate(data):
        if char.lower() in 'aeiou':
            count_vowels += 1
        if i > 0 and data[i-1].isalpha() and char.isalpha():
            total_pairs += 1
        temp_sum += ord(char) % 7
    return count_vowels, total_pairs


def compute_shift(seq):
    shift = 0
    for j in range(len(seq)):
        shift += (j + 1) * (ord(seq[j]) % 5)
    return shift % 9 + 1


def track_progress(items):
    progress_log = {}
    cumulative = 0
    for idx, item in enumerate(items):
        key = f"step_{idx}"
        progress_log[key] = len(item) * (idx + 1)
        cumulative += progress_log[key]
    avg_step = cumulative / len(items) if items else 0
    return avg_step


def evaluate_performance(metrics, factor):
    base = sum(metrics)
    adjustment = 1.0
    if metrics[0] > 5:
        adjustment *= 1.2
    if metrics[1] > 10:
        adjustment *= 1.15
    return int(base * factor * adjustment)

# Main execution
input_data = "DynamicAnalysisTool"
dummy_list = ["init", "parse", "resolve", "finish"]

# Irrelevant tracking (distractor)
side_counter = 0
for x in range(4):
    side_counter += len(dummy_list[x]) * (x - 1)

# Semi-relevant pre-processing
vowel_count, adjacency_pairs = analyze_sequence(input_data)

# Misleading intermediate calculation
entropy_proxy = 0
for c in input_data:
    entropy_proxy += (ord(c) * 7) % 11
entropy_proxy = entropy_proxy // len(input_data)

# Another distractor: unused helper call
_ = track_progress([input_data[:5], input_data[5:10], input_data[10:]])

# Core logic setup
shift_amount = compute_shift(input_data[:6])
scaling_factor = (shift_amount + vowel_count) / 10.0

# Build task metrics (key variables)
task_metrics = [
    vowel_count * 2 + shift_amount,
    adjacency_pairs + 5,
    len(input_data) - 3
]

# Efficiency factor influenced by multiple sources
efficiency_factor = scaling_factor
if len(input_data) % 2 == 0:
    efficiency_factor *= 1.1

# Critical statement
final_score = evaluate_performance(task_metrics, efficiency_factor)

print(f"Result: {final_score}")