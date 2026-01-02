import math

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    entropy = 0.0
    for x in data:
        if x > 0:
            entropy -= x * math.log2(x)
    return entropy

# Misleading signal processing chain
def preprocess_signal(raw_signal):
    normalized = [x / max(raw_signal) for x in raw_signal]
    filtered = list(map(lambda x: x ** 1.5, normalized))  # Non-linear boost
    inverted = [1 - x for x in filtered if x < 0.8]      # Partial inversion
    return inverted

# Distractor: unused complex transformation
def spectral_analysis(signal):
    fft_magnitude = []
    for i in range(len(signal)):
        component = 0
        for j in range(len(signal)):
            angle = 2 * math.pi * i * j / len(signal)
            component += signal[j] * math.cos(angle)
        fft_magnitude.append(abs(component))
    return fft_magnitude

# Core logic buried among noise
def evaluate_connection_stability(link_speed, latency_jitter):
    base_score = link_speed / (1 + latency_jitter)
    penalty_factor = 0.0
    if latency_jitter > 10:
        penalty_factor = 0.3
    elif latency_jitter > 5:
        penalty_factor = 0.15
    adjusted_score = base_score * (1 - penalty_factor)
    
    # Red herring: irrelevant adjustment
    temp_debug = adjusted_score * 1.07  
    if temp_debug > 100:
        temp_debug *= 0.95  # Dead code path under current inputs

    return adjusted_score

# Actual relevant computation
network_bandwidth = 850  # Mbps
target_snr = 22.5  # Signal-to-noise ratio
distance_penalty = 0.87
user_load = 47  # concurrent users

raw_transmission_data = [0.1, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
processed_data = preprocess_signal(raw_transmission_data)
data_efficiency = sum(processed_data) / len(processed_data)

# Fake diagnostic block (distractor)
diagnostic_codes = []
for val in processed_data:
    code = int(val * 100)
    if code % 2 == 0:
        diagnostic_codes.append(code + 10)
    else:
        diagnostic_codes.append(code + 5)

def compute_signal_strength(bandwidth, users):
    # Primary formula masked by surrounding noise
    base_strength = bandwidth * 0.73
    user_attenuation = 1 - (users / 100)
    environmental_factor = 0.91
    interference_offset = 12.5
    
    # Complex-looking but actually linear combination
    strength = (base_strength * user_attenuation * environmental_factor) + interference_offset
    
    # Irrelevant intermediate scaling (never used later)
    scaled_strength = strength * 1.034
    if scaled_strength < 500:
        scaled_strength += 20
    final_normalized = round(strength, 2)
    
    return final_normalized

# Secondary system metrics (distraction)
clock_skew = 0.0034
packet_loss_rate = 0.012
retransmission_count = 3
expected_throughput = network_bandwidth * (1 - packet_loss_rate) * 0.88

# Another decoy variable influenced by case conversion
system_mode = 'ACTIVE'
mode_flag = len(system_mode.lower().replace('a', ''))  # Result: 4, irrelevant

# Critical statement embedded in non-essential flow
connection_metric = evaluate_connection_stability(network_bandwidth, 6.4)
activation_threshold = compute_signal_strength(network_bandwidth, user_load)

# Final red herring: unused conditional override
if connection_metric > 600:
    activation_threshold *= 0.9
elif mode_flag == 5:
    activation_threshold += 10

print(f"Target result: {activation_threshold}")