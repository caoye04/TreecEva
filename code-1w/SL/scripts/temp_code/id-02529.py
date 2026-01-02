from collections import defaultdict

# Simulate sensor data with noise and valid readings
data_stream = [101, 105, -999, 108, -999, 110, 107, -999, 113, 114, -999, 115]

def process_sensor_data(stream):
    processed = []
    error_count = 0
    temp_buffer = []
    for val in stream:
        if val == -999:
            error_count += 1
            continue
        if val > 100 and val < 120:
            temp_buffer.append(val)
            processed.append(val)
    # Misleading smoothing (not used in final logic)
    smoothed = [sum(temp_buffer[i:i+2]) / 2 for i in range(len(temp_buffer)-1)] if len(temp_buffer) > 1 else temp_buffer
    return processed

def analyze_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 1
    return trend_score

def calculate_checksum(seq):
    # Unused checksum calculation (distractor)
    chk = 0
    for x in seq:
        chk ^= x  # bitwise XOR
    return chk

def calculate_final_score(data):
    base = sum(data)
    trend = analyze_trend(data)
    adjustment = 0
    
    # Nested conditional with partial relevance
    if len(data) > 5:
        if trend > 0:
            adjustment += 10
        else:
            adjustment -= 5
    else:
        adjustment += 2
    
    # Use of defaultdict as required (tracks frequency, though only length matters)
    freq = defaultdict(int)
    for d in data:
        freq[d] += 1
    
    diversity_bonus = len(freq) * 2
    
    # Red herring: complex modular arithmetic that doesn't affect outcome
    phantom_value = 0
    for k in freq:
        phantom_value = (phantom_value + k * freq[k]) % 97
    
    # Final score computation (only base, adjustment, diversity_bonus matter)
    final = base + adjustment + diversity_bonus
    
    # Dead code branch (never executed due to data constraints)
    if phantom_value < 0:
        final *= 2
        
    return final

# Main execution flow
processed_data = process_sensor_data(data_stream)
interim_diagnostic = calculate_checksum(processed_data)  # unused
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")