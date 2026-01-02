def analyze_pattern(sequence):
    count_a = sum(1 for c in sequence if c == 'A')
    count_t = sum(1 for c in sequence if c == 'T')
    count_g = sum(1 for c in sequence if c == 'G')
    count_c = sum(1 for c in sequence if c == 'C')
    total = len(sequence)
    
    # Distractor: GC content not used later
    gc_content = (count_g + count_c) / total if total else 0
    
    # Distractor: Reverse complement computed but unused
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse_complement = ''.join(complement_map.get(base, '') for base in sequence[::-1])
    
    # Key metric: A-T richness
    at_richness = (count_a + count_t) / total if total else 0
    return at_richness


def calculate_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0
    n = len(values)
    for count in freq_map.values():
        p = count / n
        entropy -= p * log2(p)
    return entropy

# Misleading helper function that's never called
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

# Main processing
thresholds = {'low': 0.3, 'high': 0.7}
data = 'AAATTGCGATAGCTTTACGGGATACCGTTT'

# Simulate sensor readings – irrelevant to final result
readings = [len(data), sum(ord(c) for c in data) % 100, len(data) // 3]
sorted_readings = sorted(readings)
filtered_readings = list(filter(lambda x: x > 10, sorted_readings))

# Extract substring patterns – distractor computation
subsequences = [data[i:i+5] for i in range(0, len(data), 5)]
long_subseq = [s for s in subsequences if len(s) == 5]

# Compute pattern metrics – some used, some not
pattern_metrics = {}
for i, seq in enumerate(long_subseq):
    score = analyze_pattern(seq)
    pattern_metrics[f'segment_{i}'] = round(score, 3)

# Distractor: entropy of metric values (not used)
metric_values = list(pattern_metrics.values())
entropy = calculate_entropy([int(v * 100) for v in metric_values]) if metric_values else 0

# Core logic disguised among distractions
base_value = len([c for c in data if c in 'AT'])
modifier = 0
if pattern_metrics['segment_0'] > thresholds['low']:
    modifier += 2
if pattern_metrics['segment_1'] > thresholds['high']:
    modifier += 3
if len(filtered_readings) == 2:
    modifier *= 1  # Neutral effect

# Critical execution point
final_score = base_value + modifier * 5
print(f"Result: {final_score}")