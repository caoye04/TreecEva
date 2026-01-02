from collections import defaultdict
import math

# Simulated sensor data with noise and redundant readings
def generate_noisy_data():
    raw_values = [i * 1.5 + (i % 3) for i in range(20)]
    timestamps = [t * 100 + (5 if t % 2 == 0 else -3) for t in range(20)]
    status_flags = ['OK' if i % 4 != 3 else 'NOISE' for i in range(20)]
    return list(zip(timestamps, raw_values, status_flags))

def filter_valid_readings(data):
    valid = []
    noise_count = 0
    for ts, val, flag in data:
        if flag == 'OK' and val > 0:
            valid.append((ts, val))
        else:
            noise_count += 1
    # Redundant calculation
    avg_noise_offset = sum([abs(v - 3.5) for v in range(noise_count + 1)]) if noise_count > 0 else 0
    return valid

def compute_transformed_magnitude(readings):
    # Apply non-linear transformation
    transformed = [math.log(r[1]) * (r[0] % 97) for r in readings]
    scaling_factor = len(transformed) / (sum(transformed) / 50.0) if transformed else 1.0
    adjusted = [t * scaling_factor for t in transformed]
    return adjusted

def calculate_entropy(values):
    # Unrelated helper function (dead code path)
    freq = defaultdict(int)
    for v in values:
        freq[round(v, 1)] += 1
    total = len(values)
    entropy = -sum((count/total) * math.log2(count/total) for count in freq.values() if count > 0)
    return round(entropy, 4)

def calculate_final_score(data):
    # Step 1: Filter valid sensor readings
    filtered_data = filter_valid_readings(data)
    
    # Step 2: Compute derived magnitudes
    magnitudes = compute_transformed_magnitude(filtered_data)
    
    # Step 3: Calculate baseline metrics
    base_metric = sum(magnitudes) / len(magnitudes) if magnitudes else 0
    variance_proxy = sum((m - base_metric) ** 1.8 for m in magnitudes) / len(magnitudes) if magnitudes else 0
    
    # Step 4: Apply conditional adjustment using modular arithmetic
    adjustment = 0
    for i, mag in enumerate(magnitudes):
        if i % 5 == 0:
            adjustment += (mag * 1.1) % 7.3
        elif i % 3 == 0:
            adjustment -= (mag * 0.9) % 4.1
    
    # Step 5: Combine with weighted contribution
    weight = 0.6 if len(magnitudes) > 10 else 0.4
    intermediate_score = base_metric * weight + variance_proxy * (1 - weight)
    
    # Step 6: Final nonlinear scaling
    final_score = int((intermediate_score + adjustment) * 10) / 10.0
    
    # Distractor computation: unused checksum
    checksum = sum(i * ord(str(round(v, 1))[-1]) for i, v in enumerate(magnitudes[:8])) % 997
    
    return final_score

# Generate input data
data = generate_noisy_data()

# Execute main logic
final_score = calculate_final_score(data)
print(f"Result: {final_score}")