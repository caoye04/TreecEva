from collections import defaultdict, Counter
import itertools

# Simulated system performance evaluation with distractors
def analyze_throughput(data, window_size):
    # Irrelevant analysis function (dead code path)
    smoothed = []
    for i in range(len(data) - window_size + 1):
        smoothed.append(sum(data[i:i+window_size]) / window_size)
    return [x * 0.95 for x in smoothed]

def compute_entropy(sequence):
    # Distractor: used nowhere in final computation
    freq = defaultdict(float)
    for item in sequence:
        freq[item] += 1
    total = len(sequence)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 3)

def generate_combinations(elements):
    # Dead utility - creates red herring
    combs = []
    for r in range(1, len(elements)+1):
        combs.extend(itertools.combinations(elements, r))
    return combs

def filter_outliers(values, threshold=2):
    # Looks important but unused
    mean = sum(values) / len(values)
    std = (__import__('math').sqrt(sum((x - mean)**2 for x in values) / len(values)))
    return [v for v in values if abs(v - mean) <= threshold * std]

def validate_checksum(record):
    # Misleading intermediate validation
    chk = 0
    for c in str(record):
        if c.isdigit():
            chk ^= int(c)
    return chk % 7

# Real computational chain begins
base_metrics = [89, 93, 76, 88, 95, 84, 90]
event_log = ['start', 'run', 'run', 'error', 'run', 'pause', 'run']
config_flags = {'debug': False, 'tracing': True, 'optimize': True}

# Distractor variables
buffer_cache = [base_metrics[i] % 10 for i in range(0, len(base_metrics), 2)]
trace_sequence = ''.join([e[0] for e in event_log]).upper()
active_modes = sum(1 for v in config_flags.values() if v)

# Real data structures
metrics = {
    'latency': 89,
    'accuracy': 93,
    'bandwidth': 76,
    'stability': 88,
    'response_time': 95,
    'memory_efficiency': 84,
    'cpu_utilization': 90
}

benchmark_weights = defaultdict(float, {
    'latency': 0.15,
    'accuracy': 0.20,
    'bandwidth': 0.10,
    'stability': 0.10,
    'response_time': 0.25,
    'memory_efficiency': 0.10,
    'cpu_utilization': 0.10
})

# Secondary metric transformation - relevant
adjusted_metrics = {}
for k, v in metrics.items():
    adjustment = 1.0
    if v < 85:
        adjustment = 1.05  # penalty relaxation
    elif v >= 90:
        adjustment = 1.10  # bonus scaling
    adjusted_metrics[k] = v * adjustment

# Checksum-based override flag (distractor with partial use)
total_latency_slices = [8, 9, 8, 10, 7]
override_flag = False
if validate_checksum(total_latency_slices) == 3:
    override_flag = True  # Never triggers

# Real weighting logic
weighted_sum = 0.0
max_possible = 0.0
for key in benchmark_weights:
    max_possible += 100 * benchmark_weights[key]  # Max score if all 100
    if key in adjusted_metrics:
        weighted_sum += adjusted_metrics[key] * benchmark_weights[key]

# Normalize score
normalized_base = weighted_sum / max_possible * 100

# Additional adjustment based on mode count (real dependency)
mode_multiplier = 1.0
if active_modes == 2:
    mode_multiplier = 1.05
elif active_modes == 3:
    mode_multiplier = 1.08

# Final performance score calculation
interim_result = normalized_base * mode_multiplier

# Artificial cap and floor (unused due to values)
score_capped = min(100, max(0, interim_result))

# Hidden correction factor from string pattern (real subtle use)
log_chars = ''.join(event_log)
correction_shift = Counter(log_chars)['r'] * 0.5  # Count 'r' in 'start', 'run', 'error', etc.

# Final score with correction
final_score = interim_result + correction_shift

# Decoy output lines (misleading prints)
# print(f'Debug: entropy={compute_entropy(buffer_cache)}')
# print(f'Throughput trend: {analyze_throughput(base_metrics, 3)[:2]}')
# print(f'Combination count: {len(generate_combinations([2,3,5]))}')

Result: final_score