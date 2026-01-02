def preprocess_data(raw):
    temp = [x * 1.5 for x in raw if x > 10]
    offset = sum(temp) // len(temp) if temp else 0
    adjusted = [x + offset for x in raw]
    return adjusted


def filter_outliers(data, threshold=50):
    # Irrelevant filtering path (dead logic)
    clean = [x for x in data if x < threshold]
    return clean if len(clean) > 3 else data


def calculate_efficiency(seq):
    total_ops = 0
    for i in range(len(seq)):
        if i % 2 == 0:
            total_ops += seq[i] ** 0.5
        else:
            total_ops += seq[i] // 3
    efficiency = total_ops / len(seq)
    return efficiency


def generate_baseline(size):
    # Distractor function: generates unused baseline pattern
    base = [i * 2 + 1 for i in range(size)]
    return [b ^ 7 for b in base]  # Bitwise red herring


def compute_entropy(values):
    # Complex but irrelevant computation
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = sum(-p/len(values) * log2(p/len(values)) for p in freq.values())
    return round(entropy, 4)


def analyze_performance(metrics, reference):
    # Core logic hidden among distractions
    snapshot = metrics[::2]  # slicing: every second element
    shift_key = metrics[-1] & 15  # bitwise AND as distraction

    lookup = {i: ref % 9 for i, ref in enumerate(reference)}
    bonus = 0

    for i, val in enumerate(snapshot):
        if i in lookup:
            diff = abs(val - lookup[i])
            if diff < 5:
                bonus += 2
            elif diff == 0:  # unreachable due to prior condition
                bonus += 5  # dead code branch

    aggregate = sum(snapshot)
    
    # Critical decoy: looks important but unused
    profile = {
        'peak': max(metrics),
        'stable': all(abs(metrics[i] - metrics[i+1]) < 3 for i in range(len(metrics)-1)),
        'noise_floor': compute_entropy(metrics)
    }

    # Real calculation buried here
    adjustment = len(snapshot) * (lookup.get(2, 1) % 4)
    final_score = aggregate + bonus + adjustment

    # Early return trap (never reached)
    if final_score < 0:
        return -1

    return final_score

# Main execution flow
raw_input = [8, 12, 14, 9, 16, 11, 13, 7]
data_stream = preprocess_data(raw_input)
data_stream = [x + 2 for x in data_stream]  # further obfuscation

filtered = filter_outliers(data_stream, threshold=45)

# Unused variables serving as red herrings
baseline_pattern = generate_baseline(len(filtered))
system_load = [x ^ 3 for x in filtered]  # XOR chain distraction
efficiency_ratio = calculate_efficiency(filtered)

# Dictionary used for state tracking (partial distractor)
status = {
    'init': 'complete',
    'stage': 'analysis',
    'valid': len(filtered) > 5
}

# Key data structure with slicing and indexing
metrics = [filtered[i] + (i * 2) for i in range(len(filtered))]

baseline = [18, 22, 19, 25, 30, 21, 24, 27]  # reference unrelated to generation

# Critical statement
final_score = analyze_performance(metrics, baseline)

# Output result
print(f"Result: {final_score}")