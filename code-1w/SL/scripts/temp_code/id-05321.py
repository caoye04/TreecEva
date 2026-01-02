import math

# Network optimization simulation with interference and red herrings
def analyze_signal_strength(frequencies):
    # Irrelevant analysis function (dead code path)
    return sum([abs(f * math.sin(f)) for f in frequencies])


def calculate_jitter(timestamps):
    # Misleading computation - not used in final result
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    jitter = sum(d ** 2 for d in diffs) / len(diffs) if diffs else 0
    normalization_factor = 1.85  # Decoy constant
    return jitter * normalization_factor

# Critical function involved in actual computation
def evaluate_channel_capacity(channels, load_factor=1.0):
    capacity = 0
    for ch in channels:
        if ch['active']:
            # Apply Shannon-Hartley inspired calculation
            snr = ch['signal'] / ch['noise']
            bandwidth = ch['bandwidth']
            capacity += bandwidth * math.log2(1 + snr) * load_factor
    return int(capacity)

# Distractor: Energy efficiency calculator (unused)
def compute_energy_efficiency(powers, durations):
    total_energy = sum(p * d for p, d in zip(powers, durations))
    avg_power = sum(powers) / len(powers) if powers else 0
    efficiency_score = total_energy / (avg_power + 0.1)
    return round(efficiency_score, 4)

# Core logic with conditional expressions and set operations
latency_profile = {'high': 0.12, 'medium': 0.065, 'low': 0.02}
traffic_peaks = {10, 14, 18, 22}  # Hours of peak traffic (red herring)
off_peak = {t for t in range(24) if t not in traffic_peaks}

# Simulated channel data
channels = [
    {'bandwidth': 40, 'signal': 8.5, 'noise': 1.7, 'active': True},
    {'bandwidth': 30, 'signal': 6.0, 'noise': 2.0, 'active': True},
    {'bandwidth': 50, 'signal': 3.0, 'noise': 3.0, 'active': False},  # Inactive channel
    {'bandwidth': 20, 'signal': 9.0, 'noise': 1.5, 'active': True},
]

timestamp_log = [0.0, 0.04, 0.09, 0.13, 0.18]  # Used to trigger decoy call
power_levels = [12.5, 14.0, 13.2, 15.1]
duration_intervals = [30, 45, 60, 40]

# Conditional expression determining optimization mode
optimization_mode = 'aggressive' if len(channels) > 3 else 'conservative'

# Red herring: unused transformation
transformed_signals = [
    ch['signal'] ** 1.5 if ch['bandwidth'] > 35 else ch['signal'] ** 0.8
    for ch in channels if ch['active']
]

# Key intermediate variable (misleading)
current_throughput = evaluate_channel_capacity(channels, load_factor=0.85)

# Decoy function calls (irrelevant computations)
jitter_metric = calculate_jitter(timestamp_log)
efficiency = compute_energy_efficiency(power_levels, duration_intervals)
signal_analysis = analyze_signal_strength([ch['signal'] for ch in channels])

# Set-based filtering with conditional expression
valid_bandwidths = {
    ch['bandwidth'] for ch in channels 
    if ch['active'] and (ch['signal'] / ch['noise']) > 1.5
}

# Core optimization logic with nested conditions and distractors
scaling_factor = 1.25 if 'aggressive' in {optimization_mode} else 1.0
penalty = 0.1 if len(valid_bandwidths & {30, 40}) == 2 else 0  # Use of set intersection

# Final transmission optimization
def optimize_transmission(channels, profile):
    base_capacity = evaluate_channel_capacity(channels)
    load_adjustment = profile['medium'] * 100  # Convert to scalar
    adjusted = base_capacity * (1 + load_adjustment)
    
    # Multiple layers of logic
    if len(channels) >= 3:
        if any(ch['signal'] > 8.0 for ch in channels if ch['active']):
            bonus = sum(ch['bandwidth'] for ch in channels if ch['signal'] > 8.0 and ch['active'])
            adjusted += bonus * scaling_factor
        else:
            adjusted -= 50
    
    # Final conditional adjustment using ternary-like pattern
    final_value = adjusted * 0.95 if penalty > 0 else adjusted * 1.05
    
    # Introduce minor bit manipulation as distraction (neutral effect)
    flag = 0b1010
    mask = 0b1111
    masked = flag & mask
    
    # Return transformed result
    return int(final_value) + masked - 10  # Remove artificial addition

# Execution point of interest
final_bandwidth = optimize_transmission(channels, latency_profile)

# Output result as required
print(f"Result: {final_bandwidth}")