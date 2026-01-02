def analyze_pattern(data):
    peak = max(data)
    trough = min(data)
    spread = peak - trough
    # Distractor: irrelevant statistical moment
    moment2 = sum(x**2 for x in data) / len(data)
    return spread

# Simulated sensor readings over time
sensor_log = [14, 18, 22, 19, 25, 30, 28, 24, 20, 17, 23, 27, 33]

# Irrelevant transformation (dead path)
def transform_signal(signal):
    return [x * 0.95 + 2 for x in signal if x > 20]

transformed = transform_signal(sensor_log)  # Unused downstream

baseline = 20
offsets = [x - baseline for x in sensor_log]  # Centered deviations

# Extract active window using slicing
active_window = offsets[4:9]  # Critical slice: indices 4 to 8

# Auxiliary calculation with misleading intermediate
noise_floor = sum(abs(x) for x in offsets if x < 0) // len(offsets)  # Unused

# Bitwise flag simulation (distractor)
status_flag = 0b101010
mask = 0b111100
filtered_flag = status_flag & mask  # Not used later

# Energy accumulation with conditional gating
def accumulate_energy(segment, limit):
    total = 0
    for val in segment:
        if abs(val) > limit:
            total += val ** 2
        else:
            total -= val  # Small penalty
    return total

energy_pool = accumulate_energy(active_window, 3)

# Secondary helper: computes directional bias
def compute_bias(sequence):
    positive_count = sum(1 for x in sequence if x > 0)
    negative_count = sum(1 for x in sequence if x < 0)
    return positive_count - negative_count

bias_score = compute_bias(active_window)  # Used only in red herring branch

# Main flow calculator
def calculate_net_flow(readings, thresh):
    # Re-slice with offset for confusion
    subset = readings[1:-1]  # Remove first and last
    filtered = [x for x in subset if abs(x) >= thresh]
    
    # Real computation path
    magnitude = sum(abs(x) for x in filtered)
    sign_factor = 1 if sum(filtered) >= 0 else -1
    
    # Distractor: complex but unused expression
    entropy = 0.0
    if len(filtered) > 1:
        from math import log
        probs = [abs(x)/magnitude for x in filtered]
        entropy = -sum(p * log(p) for p in probs if p > 0)
    
    # Actual result
    net_flow = sign_factor * magnitude
    
    # Additional red herring variables
    avg_noise = magnitude / (len(filtered) + 1)
    correction_term = bias_score * 0.5  # Nowhere used
    
    return net_flow

threshold = 4
ergy_sequence = sensor_log

# Key assignment
final_flux = calculate_net_flow(energy_sequence, threshold)

# Output target
print(f"Result: {final_flux}")