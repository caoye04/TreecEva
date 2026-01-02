from collections import defaultdict, Counter
import itertools

# Simulated health monitoring system with noise filtering and state tracking
def analyze_vital(vital, history, mode='standard'):
    if len(history) < 3:
        return False
    avg = sum(history[-3:]) / 3
    trend = history[-1] - avg
    if mode == 'strict' and abs(trend) > 15:
        return True
    return abs(trend) > 10


def apply_correction(value, factor=1.0):
    # Outdated compensation logic (dead code path - never used in main flow)
    corrected = value * factor
    if corrected > 100:
        return 95
    return corrected

# Irrelevant signal processing helper (distractor)
def smooth_signal(signal_list):
    smoothed = []
    for i in range(len(signal_list)):
        window = signal_list[max(0, i-1):min(i+2, len(signal_list))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Unused error counter (red herring)
error_count = 0
device_status = {'calibrated': False, 'last_sync': None}

# Core data structures
vital_signs = [
    [72, 75, 73, 78, 85, 90],  # Heart rate samples
    [120, 118, 125, 130, 140, 155],  # Systolic pressure
    [80, 82, 85, 88, 95, 105]   # Respiratory rate
]

# Misleading auxiliary map (partially used, partially irrelevant)
threshold_map = defaultdict(lambda: 0.5)
threshold_map.update({
    'hr': 1.2, 'bp': 1.5, 'rr': 1.1,
    'temp': 0.8, 'o2': 1.3  # Unused keys act as distractors
})

# Noise injection simulation (distractor computation)
noise_profile = []
for i in range(6):
    noise = (i ** 2) % 7
    if noise > 4:
        noise_profile.append(noise * 0.1)

# Data alignment using itertools (relevant)
cyclic_offsets = list(itertools.islice(itertools.cycle([1, -1]), 6))
adjusted_signs = []
for series in vital_signs:
    adjusted = [series[i] + cyclic_offsets[i] for i in range(6)]
    adjusted_signs.append(adjusted)

# Historical buffer setup (relevant)
history_log = defaultdict(list)
for idx, label in enumerate(['hr', 'bp', 'rr']):
    history_log[label] = adjusted_signs[idx][:4]

# Spurious data transformation (irrelevant)
duplicate_data = []
for row in adjusted_signs:
    rev = [row[i] for i in range(len(row)-1, -1, -1)]
    duplicate_data.append(rev)

# Main diagnostic processor (key function)
def process_metrics(data, thresholds):
    flags = []
    
    # Bitwise-encoded status register (mixed paradigm)
    status_register = 0
    
    for i, seq in enumerate(data):
        # Apply offset-based modulation
        mod_seq = [seq[j] + (j & 1) * 2 for j in range(len(seq))]
        
        # Trend analysis with conditional expression
        base_trend = mod_seq[-1] - mod_seq[0]
        severity = base_trend * thresholds['hr' if i == 0 else ('bp' if i == 1 else 'rr')]
        
        # Logical flag with short-circuit behavior
        critical = (severity > 60) or (len(mod_seq) > 5 and mod_seq[-1] > 100)
        
        # Update status via bitwise OR
        if critical:
            status_register |= (1 << i)
        
        flags.append(critical)
    
    # Auxiliary calculation: entropy approximation (distractor but looks important)
    entropy_approx = 0.0
    flag_counts = Counter(flags)
    for k, cnt in flag_counts.items():
        p = cnt / len(flags)
        if p > 0:
            entropy_approx -= p * __import__('math').log(p)
    
    # Real computation: accumulated deviation
    total_drift = 0
    for series in data:
        drift = max(series) - min(series)
        total_drift += drift
    
    # Final decision logic (depends only on status_register and total_drift)
    if status_register & 0b111:  # All three critical
        score = total_drift * 3
    elif status_register & 0b101:  # First and third
        score = total_drift * 2 + 5
    else:
        score = total_drift + 10
    
    # Final adjustment based on modular arithmetic
    final_score = (score * 7) % 97
    
    # Secondary transformation (looks complex but deterministic)
    transform_key = (final_score ^ 42) & 0xFF
    intermediate = (transform_key * 3 + 1) // 2
    
    # Final result built from multiple layers
    result = intermediate + (status_register << 2)
    
    # This variable is the true answer
    final_diagnostic = result + len([x for x in flags if x])
    
    return final_diagnostic

# Execution point of interest
health_data = adjusted_signs
final_diagnostic = process_metrics(health_data, threshold_map)

# Output requirement
print(f"Result: {final_diagnostic}")