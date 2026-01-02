def preprocess_integrity_check(data, config):
    checksum = 0
    for item in data:
        if isinstance(item, int) and item % 2 == 0:
            checksum += item ^ config.get('mask', 7)
    return checksum

# Irrelevant system health monitoring (dead path)
def evaluate_health_status(health_log):
    if len(health_log) > 100:
        return sum(h * 0.5 for h in health_log if h > 50) // len(health_log)
    return -1

# Decoy transformation function
def transform_legacy_format(raw_data):
    return [val << 2 for val in raw_data if val < 500]  # Unused

# Auxiliary filtering logic with misleading intermediate
threshold_map = {k: (k ** 2 + 3) // 2 for k in range(8)}
resource_pool = list(range(45, 88))

# Simulate sensor noise injection (irrelevant)
sensor_noise = [abs((i * 7) % 11 - 5) for i in range(len(resource_pool))]
noisy_pool = [r + n for r, n in zip(resource_pool, sensor_noise)]

# Dummy cache initialization (distraction)
cache_slots = [[0 for _ in range(4)] for _ in range(10)]
for i in range(10):
    cache_slots[i][i % 4] = (i * 17) % 19

# Core analysis engine
def normalize_weights(values, factor=1.75):
    total = sum(abs(v) ** 0.5 for v in values)
    return [round(v / total * factor, 6) for v in values]

def detect_peaks(series):
    peaks = []
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            peaks.append(i)
    return peaks[:3]  # Limit to top 3

def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    length = len(data)
    for count in freq.values():
        p = count / length
        entropy -= p * log2(p)
    return round(entropy, 4)

# Secondary validation chain (partially relevant but not final)
baseline_shift = sum(resource_pool[i] for i in range(0, len(resource_pool), 7)) // 6
adjusted_pool = [x - baseline_shift for x in resource_pool]

# Hidden signal extraction (red herring)
signal_pattern = [x for x in adjusted_pool if x in threshold_map]

# Main state analyzer with multiple internal steps
def analyze_system_state(resources, limits):
    # Step 1: Filter valid resources
    valid_set = [r for r in resources if r > limits.get(min(limits.keys()), 0)]
    
    # Step 2: Apply dynamic scaling
    scale_factor = len(valid_set) / (sum(valid_set) / 100) if valid_set else 1
    scaled = [s * scale_factor for s in valid_set]
    
    # Step 3: Normalize for cross-system comparison
    normalized = normalize_weights(scaled, factor=2.1)
    
    # Step 4: Detect instability windows
    critical_windows = 0
    for i in range(len(normalized) - 1):
        if abs(normalized[i] - normalized[i+1]) > 0.35:
            critical_windows += 1
    
    # Step 5: Compute stability entropy
    stability_entropy = compute_entropy([int(n * 1000) for n in normalized])
    
    # Step 6: Calculate harmonic balance
    harmonic_balance = 0
    for i in range(1, len(normalized)):
        if normalized[i] != 0:
            harmonic_balance += normalized[i-1] / normalized[i]
    
    # Step 7: Aggregate multi-metric score
    raw_score = (stability_entropy * 100) + (len(valid_set) * 12) - (critical_windows * 8)
    
    # Step 8: Final adjustment using peak consistency
    peaks = detect_peaks(scaled)
    peak_consistency = sum(scaled[p] for p in peaks) if peaks else 0
    
    # Final result calculation
    final_score = int(raw_score + peak_consistency - harmonic_balance)
    
    return final_score

# Execution point of interest
equilibrium_score = analyze_system_state(resource_pool, threshold_map)

# Additional irrelevant logging
log_entry = f"System equilibrium: {equilibrium_score}, Noise level: {sum(sensor_noise)}"

# Print required output
print(f"Result: {equilibrium_score}")