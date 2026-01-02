import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, -1.4, 5.6, 2.8, -0.9, 4.1, 6.3, -2.2]

def normalize(value):
    return (value + 10) / 20

def transform_readings(data):
    # Irrelevant transformation path (dead function)
    return [math.sin(x) for x in data if x > 0]

def filter_noise(data, threshold=0.5):
    # Applies a high-pass filter equivalent
    filtered = [x for x in data if abs(x) > threshold]
    temp_correction = sum([abs(x) for x in data]) * 0.01  # Distractor calc
    return filtered

def encode_signal(data):
    # Encodes signal into bit-like representation (bit manipulation theme)
    encoded = 0
    shift = 0
    for val in data:
        bit = int(abs(val)) & 1
        encoded |= (bit << shift)
        shift += 1
    padding = (encoded ^ 255) & 0xFF  # Red herring operation
    return encoded

def calculate_entropy(data):
    # Calculates Shannon entropy of distribution (distractor)
    total = sum(data)
    probs = [v / total for v in data]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def analyze_signal(data_packet):
    # Core logic hidden among distractions
    base_sum = sum(data_packet)
    
    # Misleading intermediate steps
    dummy_stats = {
        'max_val': max(data_packet),
        'min_val': min(data_packet),
        'range': max(data_packet) - min(data_packet)
    }
    
    # Conditional expression red herring
    adjustment = 10 if len(data_packet) > 5 else 5
    
    # Real computation path begins
    squared_total = sum([x ** 2 for x in data_packet])
    root_mean_square = math.sqrt(squared_total / len(data_packet))
    
    # Key transformation using list comprehension and arithmetic
    normalized_rms = [round(root_mean_square * normalize(x), 3) for x in data_packet[:3]]
    
    # Final diagnostic derived from RMS and length
    diagnostic_seed = int(root_mean_square * 100)
    final_value = diagnostic_seed - (len(data_packet) * 17)
    
    # Decoy logic that looks important but is unused
    def deep_evaluate(seq):
        return sum(seq) % 19
    
    return final_value

# Irrelevant auxiliary functions
def compress_sequence(seq):
    return [seq[i] for i in range(0, len(seq), 2)]

def validate_checksum(signal):
    return sum(signal) % 16 == 0

# Main execution flow
adjusted_readings = [x * 1.5 for x in raw_readings]
cleaned_data = filter_noise(adjusted_readings, threshold=1.0)
processed_data = [round(math.log(abs(x) + 1) * 2, 3) for x in cleaned_data]

# Dead code path (never called)
dummy_encoded = transform_readings(raw_readings)

# Signal encoding (irrelevant to final result)
encoded_signature = encode_signal(cleaned_data)

# Entropy calculation (red herring)
signal_entropy = calculate_entropy(processed_data)

# Actual target computation
final_diagnostic = analyze_signal(processed_data)

# Output result
print(f"Result: {final_diagnostic}")