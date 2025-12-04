from collections import Counter, defaultdict

def process_frequency_bands(bands):
    # Process frequency bands data (unused in final calculation)
    band_counter = Counter(bands)
    highest_band = max(band_counter.items(), key=lambda x: x[1])
    return highest_band[0] * 2

def calculate_signal_metrics(raw_signal):
    # Signal metrics calculation (partially relevant)
    metrics = defaultdict(int)
    for val in raw_signal:
        metrics[val % 7] += 1
    
    # This appears important but isn't used in final result
    signal_quality = sum(metrics.values()) / len(metrics) if metrics else 0
    return metrics

# Initialize variables for network analysis
frequency_bands = [3, 5, 3, 7, 3, 8, 5, 3, 7]
raw_signal = [14, 22, 37, 41, 53, 60, 14, 22]
network_nodes = {"A": 5, "B": 9, "C": 12, "D": 15}

# Process frequency bands (distraction)
primary_band = process_frequency_bands(frequency_bands)

# These variables look important but aren't used in final calculation
signal_metrics = calculate_signal_metrics(raw_signal)
node_capacity = sum(network_nodes.values()) // 2

# Transmission parameters
transmission_power = 42
base_frequency = 12

# Misleading calculations that look relevant
signal_ratio = (transmission_power + primary_band) / base_frequency
network_capacity = node_capacity * signal_ratio

# These sets appear to be for network topology but are distractions
active_nodes = {"B", "D"}
all_nodes = set(network_nodes.keys())
idle_nodes = all_nodes - active_nodes

# Bandwidth calculation (distraction)
bandwidth_map = defaultdict(int)
for i, val in enumerate(raw_signal):
    if i % 2 == 0:  # Only even indices
        bandwidth_map[val % 10] += val

# Critical values (actually relevant to final answer)
signal_strength = 74
noise_factor = 15

# More distractions that appear important
modulation_factor = transmission_power % base_frequency
if modulation_factor > 5:
    transmission_mode = "high"
    overhead = 8
else:
    transmission_mode = "standard"
    overhead = 4

# This looks like it affects the calculation but doesn't
if transmission_mode == "high":
    signal_strength = signal_strength + overhead
    # The line above is misleading - this reassignment doesn't affect the answer
    # because signal_strength is used before this point in the actual calculation

# Binary representation processing (relevant)
binary_signal = bin(signal_strength)[2:]
active_bits = 0
for i, bit in enumerate(binary_signal):
    if bit == '1':
        active_bits |= (1 << i)

# This is where the actual answer is calculated
final_result = active_bits & (signal_strength - noise_factor)

# More distraction calculations after the key statement
network_efficiency = (final_result / transmission_power) * 100
if network_efficiency > 50:
    status = "optimal"
elif network_efficiency > 25:
    status = "acceptable"
else:
    status = "degraded"

# Print the result
print(f"Result: {final_result}")