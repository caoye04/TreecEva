import math

# Irrelevant utility function (dead code path)
def normalize_values(data):
    return [x / sum(data) for x in data]

# Misleading intermediate transformation
def transform_sequence(seq):
    return [int(math.sqrt(x)) * 2 for x in seq if x > 10]

# Distractor: unused performance model
class LegacyScorer:
    def __init__(self, weight):
        self.weight = weight

    def score(self, val):
        return val * self.weight

# Core logic disguised among red herrings
def analyze_metric(met):
    base = met.get('value', 0)
    if base <= 0:
        return 0
    adjusted = math.log(base) * 1.5
    if met.get('active'):
        adjusted += 10
    return round(adjusted, 3)

# Recursive processing with slicing distraction
def recursive_amplify(arr, depth=0):
    if depth >= 3 or len(arr) < 2:
        return arr[0] if arr else 0
    mid = len(arr) // 2
    left = recursive_amplify(arr[:mid], depth + 1)
    right = recursive_amplify(arr[mid:], depth + 1)
    return left + right + depth

# Bit manipulation decoy
decoy_mask = 0b101010
hidden_flags = (decoy_mask << 3) & 0b1111000

# Unused dictionary structures (cross-reference distractors)
baseline_profiles = {
    'p1': {'threshold': 85, 'weight': 0.5},
    'p2': {'threshold': 90, 'weight': 0.7},
    'p3': {'threshold': 75, 'weight': 0.3}
}

benchmark_data = [
    {'value': 25, 'active': True},
    {'value': 16, 'active': False},
    {'value': 81, 'active': True}
]

# String processing red herring
status_log = "System OK: Ready for execution sequence"
status_parts = status_log.upper().replace("SYSTEM", "CORE").split(':')
log_flag = len(status_parts[0]) > 5

# Lambda-based filter (partially relevant)
valid_entry = lambda x: isinstance(x, dict) and 'value' in x

# Main evaluation chain
metrics = list(filter(valid_entry, ["dummy", {}, benchmark_data[0], 123, benchmark_data[2]]))

# Complex aggregation with multiple concepts
total_raw = sum(entry['value'] for entry in metrics)
score_components = []

for metric in metrics:
    analyzed = analyze_metric(metric)
    score_components.append(analyzed)

# Data transformation with slicing distraction
shifted = score_components[1:] + score_components[:1]

# Irrelevant set operation (distractor)
available_keys = {k for d in benchmark_data for k in d.keys()}
required_keys = {'value', 'active'}
compliance = len(required_keys - available_keys)

# Key computation buried in logic
composite_input = [int(c * 2) for c in shifted]

# Recursive function call with non-obvious contribution
bonus = recursive_amplify(composite_input)

# Final scoring logic
base_final = sum(score_components)
penalty = len([m for m in metrics if not m.get('active')]) * 5

# Critical statement
final_score = evaluate_performance(metrics, benchmark_data)

# Actual implementation defined after usage (obfuscation)
def evaluate_performance(data_list, ref_data):
    raw_sum = sum(item['value'] for item in data_list)
    log_contrib = sum(math.log(item['value']) for item in data_list)
    activity_bonus = sum(7 for item in data_list if item.get('active'))
    base_score = raw_sum * 0.1 + log_contrib + activity_bonus
    # Incorporate recursive result indirectly
    ripple = recursive_amplify([int(math.log(d['value'])) for d in ref_data if d['value'] > 1])
    return int(base_score + ripple - 15)

print(f"Target result: {final_score}")