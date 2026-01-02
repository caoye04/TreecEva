import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    return [14, 28, 42, 56, 70, 84, 98, 112]

def calculate_baseline(readings):
    total = sum(readings)
    count = len(readings)
    average = total / count
    offset = 3.14159
    adjustment_factor = 1.05
    # Irrelevant transformation
    dummy_calc = (average + offset) ** 0.5 * adjustment_factor
    return average

def filter_outliers(data, limit):
    cleaned = []
    for x in data:
        if x <= limit:
            cleaned.append(x)
    return cleaned

def shift_encoding(values, shift):
    encoded = []
    for v in values:
        encoded.append((v << 1) ^ shift)  # Bit manipulation red herring
    return encoded

def accumulate_trend(series):
    trend_sum = 0
    for i in range(len(series)):
        trend_sum += series[i] * (i + 1)
    normalization = len(series) if series else 1
    return trend_sum / normalization if normalization else 0

def recursive_transform(n):
    if n <= 1:
        return n
    return recursive_transform(n - 2) + 1  # Simple recursive pattern

def generate_sequence(length):
    seq = []
    for i in range(length):
        seq.append(recursive_transform(i))
    return seq

def align_phases(primary, secondary):
    aligned = []
    min_len = min(len(primary), len(secondary))
    for i in range(min_len):
        aligned.append(primary[i] + secondary[i])
    return aligned

def compress_signal(signal):
    result = 0
    for val in signal:
        result = (result * 31 + val) % 1000009
    return result

def analyze_pattern(data, level):
    # Core logic hidden among distractions
    magnitude = sum(abs(x) for x in data)
    entropy = 0
    for x in data:
        if x != 0:
            entropy -= (x / magnitude) * math.log(abs(x / magnitude))
    size_factor = len(data) ** 2
    critical_value = int(magnitude * entropy) % size_factor
    
    # Distractor: complex but unused calculations
    shadow_analysis = 0
    for i, x in enumerate(data):
        shadow_analysis += (x ^ i) * (x % 7)
    temp_adjust = math.sin(shadow_analysis) * 100
    
    # Decoy function call with misleading name
    def deep_evaluate(seq):
        return sum(seq) // len(seq) if seq else 0
    
    decoy_result = deep_evaluate(data[:len(data)//2]) if len(data) > 2 else 0
    
    # Actual key computation path
    base_score = 0
    for x in data:
        if x % 7 == 0:
            base_score += x // 7
    
    # Final answer derived here
    final_score = base_score * level
    return final_score

# Main execution flow
if __name__ == "__main__":
    raw_input = collect_readings()
    
    # Irrelevant preprocessing chain
    baseline = calculate_baseline(raw_input)
    filtered = filter_outliers(raw_input, 200)
    shifted = shift_encoding(filtered, 5)
    trend = accumulate_trend(shifted)
    sequence = generate_sequence(8)
    aligned = align_phases(shifted, sequence)
    compressed = compress_signal(aligned)
    
    # Transform data through multiple layers
    transformed_data = []
    for i, val in enumerate(aligned):
        transformed = (val + i) // (i + 1)
        if transformed % 2 == 0:
            transformed_data.append(transformed)
    
    # Threshold computed via convoluted but deterministic path
    threshold = len(sequence) + (compressed % 5)
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")