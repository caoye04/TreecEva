def analyze_signal_strength(signal, threshold=50):
    return 'strong' if signal > threshold else 'weak'


def calculate_efficiency(ratio):
    if ratio < 0.3:
        return 0.6
    elif ratio < 0.7:
        return 0.8
    else:
        return 0.95

# System parameters
base_frequency = 2400
modulation_level = 3
signal_quality = 78
interference_level = 12

# Derived metrics
signal_ratio = signal_quality / 100
overhead = (modulation_level * 0.05) + 0.1

# Efficiency depends on signal-to-noise approximation
snr_approx = (signal_quality - interference_level) / 100
efficiency = calculate_efficiency(snr_approx)

# Red herring: power calibration (not used in final result)
power_levels = [1.0, 0.85, 0.7]
calibrated_power = sum(power_levels) / len(power_levels)
adjusted_power = calibrated_power * 0.92 if calibrated_power > 0.8 else calibrated_power * 1.1

# Simulated packet sizes for throughput estimation (distractor computation)
packet_sizes = [64, 128, 256, 512]
total_packets = 0
for size in packet_sizes:
    if size <= 256:
        total_packets += 1000 // size

# Base bandwidth influenced by frequency and modulation
base_bandwidth = base_frequency * modulation_level

# Conditional adjustment factor based on signal analysis
signal_status = analyze_signal_strength(signal_quality)
adjustment_factor = 1.1 if signal_status == 'strong' else 0.9

# Intermediate scaling (semi-relevant)
scaled_bandwidth = base_bandwidth * adjustment_factor

# Final adjustment function
def adjust_bandwidth(base, efficiency, overhead):
    raw = base * efficiency
    net = raw * (1 - overhead)
    # Apply minor boost if conditions are optimal
    boost = 1.05 if efficiency >= 0.8 and overhead < 0.25 else 1.0
    return int(net * boost)

# Critical execution point
final_bandwidth = adjust_bandwidth(base_bandwidth, efficiency, overhead)

# Output result as required
print(f"Target result: {final_bandwidth}")