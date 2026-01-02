from collections import defaultdict, Counter
import itertools

# Simulated sensor fusion system for environmental monitoring

def collect_raw_data():
    return [14, 28, 14, 42, 56, 70, 56, 84, 98, 84, 112]

def apply_filter(raw, threshold=20):
    filtered = []
    for x in raw:
        if x > threshold:
            filtered.append(x * 0.7)  # attenuation
    return filtered

def compute_entropy(values):
    count = Counter(values)
    total = len(values)
    entropy = 0
    for freq in count.values():
        p = freq / total
        entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 6)

def generate_combinations(data):
    # Distractor: generates pairs but not used in final path
    return list(itertools.combinations(data, 2))

def extract_peaks(signal_list):
    peaks = []
    for i in range(1, len(signal_list)-1):
        if signal_list[i] > signal_list[i-1] and signal_list[i] > signal_list[i+1]:
            peaks.append(signal_list[i])
    return peaks if peaks else [0]

def merge_signals(primary, secondary):
    # Misleading function: appears important but unused
    merged = []
    for a, b in zip(primary, secondary):
        merged.append((a + b) // 2)
    return merged

def normalize_readings(data):
    if not data:
        return [0]
    max_val = max(data)
    return [round(x / max_val * 100, 2) for x in data]

def group_by_similarity(values):
    groups = defaultdict(list)
    for v in values:
        key = int(v // 10)  # bucket by tens
        groups[key].append(v)
    return groups

def calculate_coherence(groups):
    # Another distractor calculation
    coherence_score = 0
    for k, g in groups.items():
        if len(g) > 1:
            coherence_score += (max(g) - min(g)) / len(g)
    return coherence_score

def analyze_readings(cleaned):
    # Core logic hidden among red herrings
    avg = sum(cleaned) / len(cleaned)
    peak_vals = extract_peaks(cleaned)
    base_metric = avg * len(peak_vals)
    
    # Real computation path
    temp_result = 0
    for i, val in enumerate(cleaned):
        if val > avg:
            temp_result += (val - avg) * (i + 1)
    
    # Final transformation
    final_score = int(round(temp_result / base_metric))
    
    # Irrelevant transformations below
    mirror_vals = [abs(x - 50) for x in cleaned if x < 75]
    shadow_sum = sum(mirror_vals) % 13
    
    # This looks critical but is actually decoy
    dummy_frame = [{'idx': n, 'flag': False} for n in range(shadow_sum)]
    for item in dummy_frame:
        item['flag'] = True if item['idx'] % 3 == 0 else False
    
    # ACTUAL answer computed earlier
    return final_score

# --- Main Execution with Heavy Interference ---
raw_sensor_data = collect_raw_data()

# Distractor block 1: Unused signal generation
synthetic_noise = [x % 17 for x in range(100, 110)]
dummy_pairs = generate_combinations(synthetic_noise)

# Processing pipeline
filtered_data = apply_filter(raw_sensor_data)
processed_signals = normalize_readings(filtered_data)

# Distractor block 2: Side analysis with no impact
readings_groups = group_by_similarity(processed_signals)
consistency_metric = calculate_coherence(readings_groups)
entropy_measure = compute_entropy(processed_signals)

# Critical assignment embedded in noise
baseline_reference = [x for x in processed_signals if x > 30]
shadow_copy = baseline_reference[:]  # irrelevant deep copy

# Apply transformations that seem important but aren't
for _ in range(2):
    shadow_copy = [y * 0.95 for y in shadow_copy]

# Key statement - target of question
final_diagnostic = analyze_readings(processed_signals)

# Print required result
print(f"Result: {final_diagnostic}")