import itertools

# Simulated sensor array data from environmental monitoring station
temp_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 52, 43, 48]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 35, 30, 33, 36, 31, 34, 33]
lux_values = [12000, 11500, 12500, 11800, 12200, 11700, 12300, 12100]

# Misleading preprocessing steps
offset_correction = sum(temp_readings[:3]) / len(temp_readings[:3])
corrected_temps = [t - offset_correction + 0.5 for t in temp_readings]
duplicate_check = any(abs(a - b) < 0.1 for a, b in zip(corrected_temps, corrected_temps[1:]))

# Real processing begins: normalize readings to z-scores
mean_temp = sum(temp_readings) / len(temp_readings)
std_temp = (sum((t - mean_temp) ** 2 for t in temp_readings) / len(temp_readings)) ** 0.5
z_temps = [(t - mean_temp) / std_temp for t in temp_readings]

mean_humidity = sum(humidity_readings) / len(humidity_readings)
z_humidities = [(h - mean_humidity) / 10 for h in humidity_readings]  # Simplified scaling

# Combine metrics using weighted fusion
fused_scores = [0.7 * zt + 0.3 * zh for zt, zh in zip(z_temps, z_humidities)]

# Generate flag patterns using conditional logic and itertools
extreme_flags = [1 if abs(fs) > 0.8 else 0 for fs in fused_scores]
flag_pairs = list(itertools.combinations(extreme_flags, 2))
coincidence_count = sum(1 for a, b in flag_pairs if a == b == 1)

# Decoy analysis on pressure (irrelevant)
avg_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_anomaly = [abs(p - avg_pressure) > 3 for p in pressure_readings]
valid_pressure_windows = [i for i in range(len(pressure_anomaly)) if not pressure_anomaly[i]]

# Real control flow with nested conditions
threshold_mask = [fs > 0.5 for fs in fused_scores]
activation_chain = []
for i, (score, mask) in enumerate(zip(fused_scores, threshold_mask)):
    if mask:
        if i % 2 == 0:
            activation_chain.append(int(score * 10) | 3)  # Bitwise with red herring
        else:
            activation_chain.append(int(score * 10) & 7)
    else:
        activation_chain.append(0)

# Dead code path - never executed due to prior logic (distractor)
def analyze_lux_pattern(values):
    return [v // 1000 for v in values if v > 10000]

lux_analysis = [analyze_lux_pattern(lux_values)]  # Unused result

# Key transformation: normalization and windowing
window_size = 3
sliding_windows = [fused_scores[i:i+window_size] for i in range(len(fused_scores)-window_size+1)]
averaged_windows = [sum(window) / len(window) for window in sliding_windows]
normalized_data = [max(0, min(1, (w + 1) / 2)) for w in averaged_windows]  # Clamp to [0,1]

# Flag derivation with conditional expression
primary_flag = 1 if coincidence_count >= 5 else 0
secondary_flag = int(any(threshold_mask[:4]))
flags = (primary_flag << 1) | secondary_flag

# Critical statement
final_diagnostic = process_metrics(normalized_data, flags)

# Supporting function (should be defined before use)
def process_metrics(data, flag_config):
    base_score = sum(d * (i + 1) for i, d in enumerate(data))
    
    # Multi-layer adjustment
    if flag_config & 1:
        base_score *= 1.1
    if flag_config & 2:
        base_score += 2.5
    
    # Complex adjustment using itertools
    permutations = list(itertools.permutations([int(d * 10) for d in data[:3]], 2))
    permutation_value = sum(abs(a - b) for a, b in permutations) % 100
    
    # Final composition
    final_value = int(base_score * 100) + permutation_value
    
    # Irrelevant bit manipulation distraction
    masked_result = final_value ^ 0xAA
    shifted_back = (masked_result >> 4) | (masked_result << 4) & 0xFF
    
    return final_value  # Actual return, not the obfuscated one

# Print result for evaluation
Result: {final_diagnostic}