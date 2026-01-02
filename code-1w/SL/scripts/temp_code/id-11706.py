import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 1.8, 4.5, 2.7, 3.6, 5.1, 2.3, 3.9]
timestamps = [163000, 163001, 163002, 163003, 163004, 163005, 163006, 163007]

# Irrelevant baseline calibration (distractor)
calibration_factor = 0.987
drift_correction = sum([abs(r - 3.0) for r in raw_readings]) / len(raw_readings)
baseline_offset = math.sin(drift_correction) * calibration_factor

# Signal transformation chain
filtered = [r for r in raw_readings if r > 2.5]  # Remove low noise
normalized = [(r - min(filtered)) / (max(filtered) - min(filtered)) for r in filtered]
scaled = [round(n * 100) for n in normalized]

# Bit manipulation red herring (irrelevant to final result)
def decoy_transform(x):
    shifted = (x << 2) & 0xFF
    toggled = shifted ^ 0b10101010
    return toggled >> 1

# Unused transformation path (dead code)
transformed_scaled = [decoy_transform(s) for s in scaled]

# Character frequency distraction (unrelated string processing)
diagnostic_code = 'ERRX209,ERRX301,ERRX209,ALRM900,ERRX301'
fault_counts = {}
for char in diagnostic_code:
    if char.isalpha():
        fault_counts[char] = fault_counts.get(char, 0) + 1

# Real processing begins: frequency of numeric patterns in scaled values
digit_frequency = {}
for val in scaled:
    for digit in str(val):
        digit_frequency[digit] = digit_frequency.get(digit, 0) + 1

# Dictionary-based state machine simulation (mixed relevance)
state_map = {
    'INIT': {'cond': lambda x: x < 50, 'next': 'LOW'},
    'LOW': {'cond': lambda x: x >= 75, 'next': 'HIGH'},
    'HIGH': {'cond': lambda x: 50 <= x <= 74, 'next': 'MID'},
    'MID': {'cond': lambda x: True, 'next': 'INIT'}
}

# State transition counter (partially relevant)
current_state = 'INIT'
transition_log = []
for val in scaled:
    next_state = state_map[current_state]['next']
    if state_map[current_state]['cond'](val):
        transition_log.append((current_state, next_state, val))
        current_state = next_state

# Accumulation logic with combinatorics distraction
pair_count = 0
for i in range(len(scaled)):
    for j in range(i + 1, len(scaled)):
        if abs(scaled[i] - scaled[j]) <= 10:
            pair_count += 1

# Case conversion red herring
event_flag = 'ALERT_LEVEL_3'.lower().replace('_', '-')
status_msg = ''.join([c.upper() if c in 'aeiou' else c for c in event_flag])

# Core calculation: weighted sum of digit frequencies at even positions
processed_data = {}
for idx, (digit, freq) in enumerate(sorted(digit_frequency.items(), key=lambda x: int(x[0]))):
    weight = 2 if (idx + 1) % 2 == 0 else 1
    processed_data[digit] = freq * weight

# Final diagnostic function
def analyze_signal(data_dict):
    # Summation with conditional multipliers
    total = 0
    for k, v in data_dict.items():
        digit_val = int(k)
        if digit_val % 2 == 0:
            total += v * digit_val
        else:
            total -= v // (digit_val + 1)
    
    # Secondary adjustment based on transition count
    adjustment = len(transition_log) * 3
    
    # Tertiary influence from pair statistics
    if pair_count > 5:
        adjustment += 7
    else:
        adjustment -= 2
    
    return total + adjustment

# Execute critical statement
final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")