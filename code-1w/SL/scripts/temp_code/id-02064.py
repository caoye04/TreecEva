from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated system performance metrics
def generate_metrics():
    raw_data = [78, 85, None, 92, 67, 88, None, 94, 73]
    processed = []
    for val in raw_data:
        if val is not None and val >= 70:
            processed.append(val)
    return processed

# Legacy function - irrelevant but looks important
def calculate_legacy_avg(data):
    total, count = 0, 0
    for x in data:
        if x > 0:
            total += x * 1.5  # outdated weighting
            count += 1
    return total / count if count else 0

# Core transformation pipeline
def transform_sequence(seq):
    shifted = [(x >> 2) ^ 3 for x in seq]  # bit manipulation red herring
    return [x for x in shifted if x % 2 == 1]

# Frequency analysis - partially relevant
def analyze_frequency(seq):
    freq = defaultdict(int)
    for item in seq:
        freq[item] += 1
    common = Counter(freq).most_common(3)
    return dict(common)

# Main processing with decoy logic
def process_performance(base_metrics, reference):
    temp_results = {}
    
    # Irrelevant scaling
    scaled = [round(x * 1.07, 2) for x in base_metrics]
    temp_results['scaled_avg'] = sum(scaled) / len(scaled)
    
    # Bit-twiddling distraction
    encoded = [val ^ 255 for val in base_metrics if val < 90]
    temp_results['encoded_max'] = max(encoded) if encoded else 0
    
    # Real computation begins here
    filtered = [x for x in base_metrics if x in reference]
    
    # Decoy conditional with misleading comment
    # NOTE: This threshold was deprecated in v2, ignore
    if sum(base_metrics) > 400:
        adjusted = [x + 5 for x in filtered]  # this branch taken but not used
    else:
        adjusted = filtered
    
    # Actual critical path
    status_flags = [1 if x >= 85 else 0 for x in base_metrics]
    trigger_cycle = cycle([0, 1, 1])
    mask = list(islice(trigger_cycle, len(status_flags)))
    applied = [a ^ b for a, b in zip(status_flags, mask)]
    
    # Final integration - only this matters
    contribution = sum(x * y for x, y in zip(applied, base_metrics))
    penalty = analyze_frequency(base_metrics).get(73, 0) * 10
    final_score = contribution - penalty  # <-- actual answer derivation
    
    # Dead code - never accessed
    def debug_dump():
        return {'raw': base_metrics, 'temp': temp_results}
    
    return final_score

# Reference dataset
benchmark_data = {67, 73, 88, 92, 94, 95, 99}
metrics = generate_metrics()  # returns [78, 85, 92, 88, 94, 73]

# Execute main logic
final_score = process_performance(metrics, benchmark_data)
print(f"Result: {final_score}")