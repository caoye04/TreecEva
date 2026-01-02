import math

# Simulated sensor array data (irrelevant preprocessing)
def preprocess_sensor_array(raw_data):
    return [x * 1.05 for x in raw_data if x > 0]

def calculate_entropy(signal):
    entropy = 0.0
    for x in signal:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy

# Misleading diagnostic function (dead end)
def legacy_diagnostic(seq):
    threshold = 42.0
    score = 0
    for i in range(len(seq)):
        if seq[i] % 7 == 0:
            score += 3
        elif seq[i] % 3 == 0:
            score += 2
    return score * threshold

# Core transformation pipeline
baseline_readings = [8, 12, 16, 9, 4]
offset_key = sum([x ** 0.5 for x in baseline_readings])  # Irrelevant calculation

# Noise filter (unused)
noise_profile = tuple([(i * 1.1) % 1 for i in range(5)])
filtered_noise = set(noise_profile)

scaling_factor = 2.5
adjustment_matrix = [[scaling_factor * i * j for j in range(2)] for i in range(3)]

# Real processing begins here
health_signature = (18, 24, 36, 48)

# Lambda-based dynamic weight assignment (key concept)
weight_func = lambda x, y: (x + y) / (y or 1)
weights = [weight_func(health_signature[i], baseline_readings[i % 5]) for i in range(4)]

# Secondary red herring: checksum validation (never called)
def validate_checksum(data):
    return sum(data) % 11 == 0

# Bit manipulation decoy (complex but unused)
bit_flags = 0
for val in health_signature:
    bit_flags |= (val << 2)
    bit_flags ^= (val & 7)

# Actual metric processor
mask = 0b1101
intermediate = 0
for idx, w in enumerate(weights):
    temp_val = int(w * 10) ^ mask  # XOR with fixed mask
    if temp_val % 2 == 0:
        intermediate += temp_val
    else:
        intermediate -= (temp_val % 7)

# Conditional override simulation (distractor)
current_mode = 'STANDBY'
if current_mode == 'ACTIVE':
    scaling_factor *= 1.5  # Never executed

# Key comparison and logic chain
threshold_check = intermediate > 50
validity_flag = len(health_signature) == 4 and len(baseline_readings) >= 4
activation_state = threshold_check and validity_flag

# Final processing with logical dependencies
def process_metrics(sig, base):
    total = 0
    for i in range(min(len(sig), len(base))):
        if sig[i] % 2 == 0 and base[i] % 4 == 0:
            total += sig[i] // 4
        else:
            total -= base[i] // 3
    
    # Additional logic gate
    if activation_state:
        total += int(math.sqrt(intermediate))
    else:
        total -= 10
    
    # Final adjustment using modular arithmetic
    total = (total + 7) % 1000
    return total

# Execution point of interest
final_diagnostic = process_metrics(health_signature, baseline_readings)
print(f"Result: {final_diagnostic}")