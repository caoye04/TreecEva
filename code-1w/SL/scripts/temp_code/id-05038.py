from collections import defaultdict

# Simulate sensor bit patterns and diagnostic thresholds
def analyze_sensor_pattern(raw_readings):
    base_value = 17
    shift_factor = 3
    mask = 0b11010100
    adjustment = 0b00111110
    
    # Preprocess raw data using frequency analysis
    freq_count = defaultdict(int)
    for reading in raw_readings:
        freq_count[reading] += 1
    
    # Extract dominant pattern (most frequent value)
    dominant_reading = max(freq_count, key=freq_count.get)
    
    # Derive bit pattern from dominant reading with shift transformation
    bit_pattern = (dominant_reading << shift_factor) & 0xFF
    
    # Critical computation: detect anomalous bit deviations
    threshold_check = (bit_pattern ^ mask) & adjustment > base_value
    
    # Irrelevant secondary metric (distractor)
    normalized_score = sum(freq_count.values()) / (len(freq_count) or 1)
    
    return threshold_check

# Input data sequence
data_stream = [21, 22, 21, 23, 21, 22, 21]

result = analyze_sensor_pattern(data_stream)
print(f"Result: {result}")