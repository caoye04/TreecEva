from collections import defaultdict, Counter

def analyze_metrics(entries):
    stats = defaultdict(float)
    temp_counts = [0] * 10
    total_entries = len(entries)
    
    for idx, entry in enumerate(entries):
        category = entry['type']
        value = entry['value']
        stats[category] += value
        
        # Distractor: irrelevant frequency tracking
        if value % 2 == 0:
            temp_counts[idx % 10] += 1

    # Meaningless transformation
    adjusted = [x * 1.5 for x in temp_counts if x > 0]
    avg_adjusted = sum(adjusted) / len(adjusted) if adjusted else 0

    # Actual logic hidden among noise
    raw_sum = sum(stats.values())
    return raw_sum, avg_adjusted

def validate_consistency(data):
    # Redundant validation with side computations
    lengths = [len(str(d['value'])) for d in data]
    mode_length = Counter(lengths).most_common(1)[0][1]
    total_chars = sum(lengths)
    
    # Irrelevant normalization
    norm_factor = total_chars / (mode_length + 1e-5)
    return norm_factor > 5

def calculate_performance(dataset):
    # Key processing step
    base_score, noise_term = analyze_metrics(dataset)
    
    # Secondary distractor: complex filtering that doesn't change outcome
    filtered = [d for d in dataset if d['value'] > 10]
    indices = [i for i, _ in enumerate(filtered)]
    zipped_data = list(zip(filtered, indices))
    
    # Fake complexity with zip and enumerate
    offset = 0
    for item, idx in zipped_data:
        if item['type'] == 'debug':
            offset += idx * 0.1
    
    # Core logic buried here
    multiplier = len(dataset) // 4
    adjustment = 1.25 if validate_consistency(dataset) else 0.75
    
    # Final computation
    final_score = int((base_score * adjustment) - offset) + multiplier
    
    # This print is required to expose the answer
    print(f"Result: {final_score}")
    return final_score

# Simulated benchmark data
benchmark_data = [
    {'type': 'compute', 'value': 25},
    {'type': 'memory', 'value': 18},
    {'type': 'compute', 'value': 30},
    {'type': 'io', 'value': 12},
    {'type': 'compute', 'value': 22},
    {'type': 'debug', 'value': 40},
    {'type': 'memory', 'value': 15},
    {'type': 'io', 'value': 8},
    {'type': 'compute', 'value': 35},
    {'type': 'debug', 'value': 50}
]

final_score = calculate_performance(benchmark_data)