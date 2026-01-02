def analyze_signal(pattern, mask):
    """Irrelevant function: simulates signal filtering."""
    filtered = [p & mask for p in pattern]
    return [f ^ (f >> 1) for f in filtered if f % 3 != 0]

# Irrelevant constants
dummy_mask = 0b1101
offset_correction = 37
scale_factor = 2.5

# Distractor data structure
diagnostic_logs = {
    'errors': [101, 203, 405],
    'warnings': [],
    'debug': ['retry_count=0', 'mode=standby']
}

# Unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Core logic disguised among distractions
def transform_sequence(seq, key):
    shifted = [(x << 1) ^ key for x in seq]
    return [s % 256 for s in shifted]

# Another decoy function
calculate_hash = lambda data: sum(d * (i + 1) for i, d in enumerate(data)) % 1000

# Real computation begins here
raw_metrics = [12, 15, 22, 19, 30, 25]

# Apply non-linear transformation using bitwise and arithmetic ops
processed = []
for val in raw_metrics:
    temp = val ^ 0x1F
    temp = (temp * 3) + (temp >> 2)
    processed.append(temp)

# Misleading intermediate calculation
aggregate_diagnostic = sum(diagnostic_logs['errors']) * offset_correction // 10

# Real data path
metric_data = [x for x in processed if x > 50]

base_threshold = 64

# Conditional expression with side relevance
evaluation_mode = 'strict' if len(metric_data) > 3 else 'relaxed'

# Lambda used in actual logic
evaluate_metric = lambda m, t: (m >= t) + (m > t * 1.2)

# List comprehension with filtering and transformation
eval_results = [
    evaluate_metric(m, base_threshold) * (m // 10)
    for m in metric_data
    if m % 2 == 0 or evaluation_mode == 'strict'
]

# Key distraction: unused complex unpacking
temp_a, *rest, temp_b = sorted([10, 20, 30, 40, 50])

# Actual answer derivation
reliability_bonus = len(eval_results) if sum(eval_results) < 100 else 5

final_score = 0
for idx, score in enumerate(eval_results):
    adjustment = (score ^ idx) & 7
    final_score += score + adjustment

final_score -= reliability_bonus

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

def evaluate_performance(data, threshold):
    count_above = sum(1 for x in data if x > threshold)
    total_contribution = sum(x >> 2 for x in data if x % 4 == 0)
    penalty = count_above * (total_contribution % 5) if count_above > 0 else 0
    bonus = calculate_hash(data[:3]) // 100 if len(data) >= 3 else 0
    return (total_contribution + bonus - penalty) * (1 + (count_above >= 3))

print(f"Result: {final_score}")