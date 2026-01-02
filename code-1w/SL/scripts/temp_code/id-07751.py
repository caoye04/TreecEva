def analyze_signal_strength(signal: str) -> int:
    """Misleading function - not used in final calculation."""
    if 'strong' in signal.lower():
        return 5
    elif 'moderate' in signal.lower():
        return 3
    else:
        return 1


def linear_search(arr, target):
    """Find index of target in arr, or -1 if not found."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# System configuration parameters
tower_frequency = 2.4e9
signal_quality = 'moderate'
base_rate = 128  # Mbps
packet_size = 1500  # bytes
overhead_ratio = 0.12

# Traffic load levels (simulated over time)
traffic_snapshot = [0.3, 0.5, 0.7, 0.9, 1.2, 1.5]
utilization_history = [round(100 * x) for x in traffic_snapshot]  # percentage tracking

# Determine current load index
threshold = 1.0
current_load_index = -1
for i, load in enumerate(traffic_snapshot):
    if load >= threshold:
        current_load_index = i
        break

# Unused but plausible intermediate calculations
theoretical_max = tower_frequency / (packet_size * 8) * (1 - overhead_ratio)
effective_capacity = base_rate * (1 - overhead_ratio)

# Core logic: bandwidth adjustment based on load
adjustment_factor = 1.0
if traffic_snapshot[current_load_index] > 1.4:
    adjustment_factor = 0.6
elif traffic_snapshot[current_load_index] > 1.0:
    adjustment_factor = 0.8
else:
    adjustment_factor = 1.0

# Simulate congestion control window scaling
window_scale = 1
for _ in range(current_load_index):
    window_scale += 1

# Final bandwidth computation
raw_adjusted = base_rate * adjustment_factor
scaled_adjustment = raw_adjusted // window_scale  # integer division

# Apply string-based mode modifier (using string method)
system_mode = "high-throughput-optimized"
modes = system_mode.split('-')
if 'optimized' in modes:
    scaled_adjustment = int(scaled_adjustment * 1.25)

# Distractor: irrelevant data structure manipulation
data_buffers = {f'buf_{i}': i * 10 for i in range(len(utilization_history))}
dropped_packets = sum([v for k, v in data_buffers.items() if '5' in k])

# Key assignment point
final_bandwidth = adjust_bandwidth(base_rate, traffic_snapshot[current_load_index])

# Define function after usage (plausible but requires forward understanding)
def adjust_bandwidth(rate, load):
    factor = 0.8 if load > 1.0 else 1.0
    temp = rate * factor
    # Round down using integer division by 1 after scaling
    return (int(temp * 1.1) // 1) if load < 1.4 else (int(temp * 0.9) // 1)

print(f"Result: {final_bandwidth}")