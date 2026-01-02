def analyze_packet(data):
    if len(data) < 5:
        return False
    checksum = sum(ord(c) for c in data[:4]) % 256
    return checksum == ord(data[4])

# Irrelevant network monitoring variables (distractors)
current_bandwidth = 987.65
predicted_latency = 123.45
diagnostic_mode = True
packet_buffer = ['HELLO', 'WORLD', 'TEST', 'DATA']

# Unused helper function (dead code path)
def encrypt_payload(payload):
    return ''.join(chr((ord(c) + 3) % 128) for c in payload)

# Another red herring: system health monitor that's never called
def system_health_check():
    cpu_load = 78
    memory_usage = 456000
    return cpu_load < 80 and memory_usage < 500000

# Core logic disguised among distractions
network_load = [12, 15, 8, 23, 7, 19, 14, 22]
baseline_offset = 3
threshold = 15

# Distractor: unused transformation map
type_map = {'A': 1, 'B': 2, 'C': 3}

# Misleading intermediate calculation (not used in final result)
raw_aggregate = sum(x ** 0.5 for x in network_load if x > 10)
adjusted_total = raw_aggregate * 1.23  # Dead end

# Conditional expression with slicing distraction
data_slice = 'optimization_flow'[4:11]
is_active = data_slice == 'mizatio'

# Real computation hidden among noise
def calculate_efficiency(load, thresh):
    count_above = 0
    total_cycles = 0
    
    for val in load:
        if val > thresh:
            count_above += 1
            total_cycles += val
        else:
            # Bit manipulation red herring
            shifted = val << 2
            inverted = ~shifted & 0xFF

    # Linear search for first high-load index (used in logic)
    first_critical_index = -1
    for i in range(len(load)):
        if load[i] > thresh:
            first_critical_index = i
            break
    
    # Actual formula uses multiple concepts
    base_efficiency = (count_above * 100) / len(load)
    penalty_factor = total_cycles / (thresh * count_above) if count_above > 0 else 0
    
    # Final calculation incorporating conditional logic
    safety_margin = 1.0
    if first_critical_index < 3:
        safety_margin = 0.85  # Early spike reduces efficiency
    
    efficiency_score = (base_efficiency * penalty_factor) * safety_margin
    
    # One more distraction: string-based switch
    mode_flag = 'premium'.upper().lower()
    if mode_flag.startswith('pre'):
        efficiency_score *= 1.1  # Irrelevant due to override below
    
    # Override based on deterministic condition (not actually dependent on mode)
    efficiency_score = efficiency_score * 0.9  # Standard adjustment
    
    return efficiency_score

# Secondary distractor: unused list comprehension
historical_peaks = [x for x in network_load if x > threshold and x % 2 == 1]

# Key execution point
optimized_flow_rate = calculate_efficiency(network_load, threshold)

# Additional irrelevant bit operation sequence
final_diagnostic = (len(network_load) ^ 7) & 0xF

# Print required result
print(f"Target result: {optimized_flow_rate}")