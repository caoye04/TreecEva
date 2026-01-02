import math

# Simulated sensor data from a thermal imaging system
temperature_readings = [23.5, 24.1, 25.0, 26.7, 27.3, 28.0, 29.1, 30.5]

def calculate_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return entropy

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    return filtered

def transform_coordinates(x, y):
    # Irrelevant geometric transformation (distractor)
    r = (x**2 + y**2) ** 0.5
    theta = math.atan2(y, x)
    return (r * math.cos(theta + 0.1), r * math.sin(theta + 0.1))

def generate_frequency_map(text):
    # String-based frequency analysis (partial red herring)
    freq_map = {}
    for char in text.lower():
        if char.isalpha():
            freq_map[char] = freq_map.get(char, 0) + 1
    sorted_chars = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_chars)

def extract_vowel_pattern(sentence):
    # Additional string processing with no impact on final result
    vowels = ''.join([c for c in sentence.lower() if c in 'aeiou'])
    return vowels[::-1]  # reversed vowel sequence

def normalize_signal(signal):
    min_val = min(signal)
    max_val = max(signal)
    normalized = [(x - min_val) / (max_val - min_val) * 100 for x in signal]
    return normalized

def compute_checksum(data_list):
    # Bit manipulation distractor
    checksum = 0
    for val in data_list:
        shifted = int(val * 10) << 2
        checksum ^= shifted % 257
    return checksum

def analyze_signal(data_packet):
    # Core logic hidden among distractions
    base_metric = sum(math.sqrt(x) for x in data_packet if x > 25)
    adjustment_factor = len([x for x in data_packet if x < 26])
    entropy_score = calculate_entropy(data_packet)
    
    # Critical calculation path
    intermediate = base_metric * (adjustment_factor + 1)
    noise_compensated = intermediate - (entropy_score * 10)
    
    # Red herring: unused complex structure
    diagnostics_log = {
        'raw_length': len(temperature_readings),
        'filtered_count': len(filter_outliers(temperature_readings)),
        'checksum': compute_checksum(temperature_readings),
        'coordinate_transform': transform_coordinates(5, 12),
        'text_analysis': generate_frequency_map('thermal imaging diagnostic'),
        'vowel_pattern': extract_vowel_pattern('imaging system active')
    }
    
    # Final relevant computation
    final_diagnostic = int(noise_compensated + 0.5)  # rounded to nearest integer
    return final_diagnostic

# Main execution flow
processed_data = normalize_signal(temperature_readings)

# Dead code path - never called but looks important
def legacy_diagnostic_routine():
    historical_data = [22.1, 23.0, 24.5]
    return sum(historical_data) / len(historical_data)

# Unused variable assignment (distractor)
dummy_snapshot = {
    'timestamp': '2023-11-05',
    'sensor_id': 'THM-7X',
    'status': 'calibrating',
    'readings_count': len(temperature_readings)
}

# Key statement
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")