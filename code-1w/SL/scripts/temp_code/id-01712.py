import itertools

def analyze_response_time(raw_logs):
    # Irrelevant preprocessing function (dead end)
    cleaned = [x for x in raw_logs if x > 0]
    return sum(cleaned) // len(cleaned)

def compute_entropy(data):
    # Misleading mathematical distraction
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 3)

def validate_checksum(sequence):
    # Distractor: looks important but unused in critical path
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) % 256
    return checksum == 0

def extract_key_metrics(log_entries):
    # Extract relevant metrics with red herrings
    durations = []
    timeouts = 0
    peak_memory = 0
    memory_readings = []

    for entry in log_entries:
        if 'duration' in entry:
            durations.append(entry['duration'])
        if entry.get('status') == 'timeout':
            timeouts += 1
        if 'memory' in entry:
            memory_readings.append(entry['memory'])

    avg_duration = sum(durations) / len(durations) if durations else 0
    timeout_rate = timeouts / len(log_entries)

    # Decoy computation
    if memory_readings:
        peak_memory = max(memory_readings)
        avg_memory = sum(memory_readings) / len(memory_readings)

    # Real metric used later
    efficiency_ratio = (1000 / (avg_duration + 1)) if avg_duration < 50 else 0.5

    # Dead-end variables
    compression_factor = 1.0
    redundancy_count = 0

    return {
        'efficiency': efficiency_ratio,
        'stability': 1 - timeout_rate,
        'complexity': compute_entropy([len(str(d)) for d in durations])
    }

def normalize_vector(v):
    # Unused helper - misleading abstraction
    mag = sum(x ** 2 for x in v) ** 0.5
    return [round(x / mag, 4) for x in v] if mag else v

def aggregate_performance(metrics, weights):
    # Core logic buried in noise
    score = 0.0
    components = []

    # Key calculation - depends only on efficiency and stability
    for key, weight in weights.items():
        if key in metrics:
            if key == 'complexity':
                # This branch is never taken due to weight configuration
                adjusted = 1 - metrics[key] / 10
                score += weight * adjusted
            else:
                score += weight * metrics[key]
            components.append(f'{key}: {metrics[key]}*{weight}')

    # Red herring: post-processing that doesn't affect result
    final_components = list(itertools.chain.from_iterable(
        [c.split(':')] for c in components
    ))
    
    # Actual answer computed here
    return round(score, 6)

# Simulated system log data - realistic input
log_data = [
    {'duration': 12, 'status': 'success', 'memory': 45},
    {'duration': 15, 'status': 'success', 'memory': 52},
    {'duration': 8,  'status': 'success', 'memory': 41},
    {'duration': 55, 'status': 'timeout', 'memory': 98},
    {'duration': 10, 'status': 'success', 'memory': 44},
    {'duration': 14, 'status': 'success', 'memory': 50},
    {'duration': 9,  'status': 'success', 'memory': 42},
    {'duration': 11, 'status': 'success', 'memory': 48}
]

# Extract meaningful performance metrics
extracted_metrics = extract_key_metrics(log_data)

# Irrelevant transformation chain
raw_durations = [entry['duration'] for entry in log_data]
sorted_pairs = list(zip(raw_durations, enumerate(raw_durations)))
decorated = [(d, idx) for d, (i, idx) in sorted_pairs if d < 50]
flat_indices = list(itertools.chain.from_iterable(
    [(idx,) * (1 if i % 2 == 0 else 0) for d, idx in decorated]
))  # Always empty second element

# Weight schema - only two keys matter
weight_scheme = {
    'efficiency': 0.6,
    'stability': 0.4,
    'complexity': 0.0  # Weight zero makes this irrelevant despite being computed
}

# Critical execution point
final_score = aggregate_performance(extracted_metrics, weight_scheme)

# Print result as required
print(f"Result: {final_score}")