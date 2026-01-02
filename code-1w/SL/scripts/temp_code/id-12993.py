from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation and anomaly scoring system
def collect_diagnostics(data_stream):
    diagnostics = defaultdict(int)
    temp_log = []
    cumulative = 0

    for val in data_stream:
        if val > 100:
            diagnostics['overload'] += 1
            temp_log.append(val)
        elif val < 0:
            diagnostics['negative_spikes'] += 1
        else:
            cumulative += val % 7

    # Irrelevant transformation
    shifted = [((x * 3) + 5) % 256 for x in temp_log]
    return diagnostics, cumulative, shifted

def compute_entropy(sequence):
    if not sequence:
        return 0.0
    counter = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def apply_filter(signal):
    # Decoy filter operation with dead-end logic
    filtered = [s for s in signal if s % 2 == 1]
    smoothed = []
    for i in range(1, len(filtered)-1):
        smoothed.append((filtered[i-1] + filtered[i] + filtered[i+1]) // 3)
    return smoothed or [0]

def generate_baseline_profile(samples):
    profile = {}
    extremes = []
    for s in samples:
        if abs(s) > 50:
            extremes.append(s)
    profile['extreme_count'] = len(extremes)
    profile['peak'] = max(extremes) if extremes else 0
    profile['adjusted_mean'] = sum(samples) / (len(samples) or 1)
    return profile

def evaluate_segment_quality(data_chunk, config):
    size = len(data_chunk)
    if size == 0:
        return 0

    # Real calculation path
    valid_range = [x for x in data_chunk if config['min_thresh'] <= x <= config['max_thresh']]
    ratio = len(valid_range) / size
    
    # Red herring: complex but unused bitwise cascade
    magic = 0
    for x in data_chunk[:5]:
        magic ^= (x << 2) | (x >> 1)
        magic = (magic * 7) % 101

    # Another irrelevant stat
    jumps = sum(1 for i in range(1, len(data_chunk)) if abs(data_chunk[i] - data_chunk[i-1]) > 20)

    return int(ratio * 100)

def main_pipeline(input_trace):
    # Primary data processing stages
    stage_one = [x * 2 + 1 for x in input_trace if x % 3 != 0]
    stage_two = [y for y in stage_one if y < 150]

    # Dead code branch - never called
    def debug_dump():
        return {'raw': input_trace, 'processed': stage_two}

    stats, base_sum, noise_seq = collect_diagnostics(stage_two)
    entropy_val = compute_entropy(noise_seq)

    # Unused advanced transform
    fft_approx = [int(10 * math.sin(i * 0.1)) for i in range(len(noise_seq))]

    profile_ref = generate_baseline_profile(stage_two)
    config_settings = {
        'min_thresh': 10,
        'max_thresh': 120,
        'mode': 'strict'
    }

    quality_score = evaluate_segment_quality(stage_two, config_settings)

    # Key distraction: multiple similar variables
    final_score = quality_score * 1.5
    net_balance = final_score - base_sum % 100
    aggregate_rating = int(net_balance + entropy_val)

    segment_data = stage_two
    baseline_ref = profile_ref

    # --- Critical Statement ---
    threshold_score = evaluate_threshold(segment_data, baseline_ref)
    return threshold_score

def evaluate_threshold(data, baseline):
    # Core logic hidden among distractions
    if not data:
        return -1

    # Real computation begins
    count_high = sum(1 for x in data if x > 90)
    count_low = sum(1 for x in data if x < 10)
    mid_range = [x for x in data if 30 <= x <= 70]

    # Distractor: unused nested structure
    summary_grid = [[0]*5 for _ in range(5)]
    for i in range(min(len(data), 25)):
        r, c = i // 5, i % 5
        summary_grid[r][c] = (data[i] ^ (r + c)) % 42

    # Meaningful calculation
    avg_mid = sum(mid_range) / len(mid_range) if mid_range else 0
    peak_ref = baseline.get('peak', 1)

    # Complex conditional blending
    modifier = 1.0
    if count_high > count_low and avg_mid > 50:
        modifier = 1.8
    elif count_low > 5:
        modifier = 0.7
    else:
        modifier = 1.2

    # Decoy bit manipulation chain
    accumulator = 0
    for i, val in enumerate(data[:8]):
        accumulator += ((val << i) ^ (i * 3)) & 255
    hashed = (accumulator * 17) % 997

    # Actual answer computation (non-obvious)
    raw_measure = len(data) + int(avg_mid)
    adjusted = int(raw_measure * modifier)
    penalty = abs(count_high - count_low) * 2
    result = adjusted - penalty

    # Secondary red herring: unused tuple unpacking
    scores_list = [result, hashed, int(modifier * 100), len(summary_grid)]
    primary, _, _, _ = scores_list  # Only primary matters

    # Final decoy transformation
    final_array = [result ^ i for i in range(3)]
    out = final_array[0]  # Deterministic

    return out

# Simulated input trace - deterministic seed
input_sequence = [24, 63, 7, 91, 45, 103, 18, 67, 3, 88, 15, 72, 5, 9, 121, 33, 77, 2, 60, 41]

# Execute pipeline
temp_result = main_pipeline(input_sequence)

# Extract target variable as per critical statement
threshold_score = evaluate_threshold(
    [x * 2 + 1 for x in input_sequence if x % 3 != 0 and x < 150], 
    generate_baseline_profile([x * 2 + 1 for x in input_sequence if x % 3 != 0])
)

print(f"Target result: {threshold_score}")