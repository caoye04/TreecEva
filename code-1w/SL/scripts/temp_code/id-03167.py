def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper (distractor)
def smooth_data(arr):
    if not arr:
        return []
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        smoothed.append((arr[i-1] + arr[i] + arr[i+1]) / 3)
    smoothed.append(arr[-1])
    return smoothed

# Unused transformation function (dead code path)
def transform_scale(val, factor=1.5):
    return val * factor if val > 0 else abs(val)

# Decoy metric calculation
def compute_entropy(data):
    from math import log
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for v in freq.values():
        p = v / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Real logic starts here
def extract_segments(text_block):
    segments = text_block.split(',')
    cleaned = [seg.strip().lower() for seg in segments]
    filtered = [s for s in cleaned if 'error' not in s and 'fail' not in s]
    return filtered

def build_index(items):
    index_map = {}
    for idx, item in enumerate(items):
        key = item[:3] if len(item) >= 3 else item
        index_map[key] = index_map.get(key, 0) + (idx + 1)
    return index_map

def generate_metrics(log_entries):
    raw_lengths = [len(entry) for entry in log_entries]
    peaks = analyze_pattern(raw_lengths)
    base_metric = sum(raw_lengths) / len(raw_lengths) if raw_lengths else 0
    # Red herring: complex but unused bitwise shift
    shifted_peaks = peaks << 3 | 7
    adjustment = 2.5 if peaks > 2 else 1.2
    return {
        'avg_length': base_metric,
        'peak_count': peaks,
        'adjusted_metric': base_metric * adjustment,
        'bitwise_trace': shifted_peaks  # Not used later
    }

def evaluate_performance(metrics):
    score = 0
    metric_set = set(metrics.keys())
    # Use of set operations (required feature)
    essential = {'avg_length', 'peak_count', 'adjusted_metric'}
    if essential.issubset(metric_set):
        base = metrics['avg_length']
        bonus = metrics['peak_count'] * 10
        penalty = 0
        # String slicing distraction
        trace_str = f"trace_{metrics['bitwise_trace']}"
        suffix_val = int(trace_str[-2:]) if trace_str[-2:].isdigit() else 0
        # Meaningless string operation chain
        temp_str = trace_str.upper()[::-1].replace('E', '').lower()
        if 'z' in temp_str:
            penalty += 15
        # Actual scoring logic
        score = base + bonus - penalty
        # Early return red herring (never reached due to condition above)
        if base > 1000:
            return 999
    else:
        return -1
    # Critical statement
    final_score = evaluate_performance(metric_dict)
    return int(round(score))

# Simulated input data
log_input = "SystemInit, ProcessFlow error, DataStream, NetworkPing fail, TimerTick, UserInput, CacheFlush"

# Processing pipeline
segments = extract_segments(log_input)
index_lookup = build_index(segments)
processed_logs = [s.replace(' ', '_').title() for s in segments]

# Generate actual metrics
metric_dict = generate_metrics(processed_logs)

# Introduce irrelevant list transformation
buffer_data = [ord(w[0]) for w in processed_logs if len(w) > 4]
binary_flags = [(x & 1, x >> 2) for x in buffer_data]

# Another decoy structure
status_tree = {i: chr(97 + (i % 26)) for i in range(len(segments))}

# Final evaluation
final_score = evaluate_performance(metric_dict)
print(f"Result: {final_score}")