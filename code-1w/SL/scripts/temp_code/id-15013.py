import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_readings(raw):    normalized = [(x - min(raw)) / (max(raw) - min(raw) + 1e-9) for x in raw]    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]    return smoothed[:len(raw)]

def compute_entropy(arr):    """Irrelevant function - looks useful but not used in main logic"""
    total = sum(arr)
    if total == 0:        return 0.0
    probabilities = [x / total for x in arr if x > 0]
    return -sum(p * math.log(p) for p in probabilities)

def shift_cipher(data, key):    """Decoy transformation - never called"""
    return [chr((ord(chr(x)) - 97 + key) % 26 + 97) if 0 <= x <= 25 else x for x in data]

def generate_fibonacci(n):    """Unused helper - distracts from core logic"""
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def analyze_component_stability(readings, tolerance):    """Main analysis pipeline with embedded distractions"""
    # Irrelevant intermediate calculation
    baseline = sum(readings) / len(readings)
    deviations = [abs(x - baseline) for x in readings]
    variance_proxy = sum(d ** 2 for d in deviations) / len(deviations)

    # Real processing begins here
    filtered = [x for x in readings if x > baseline - tolerance]

    # Distracting control flow
    if len(filtered) < len(readings) // 2:
        adjustment_factor = 0.8
        adjusted = [x * adjustment_factor for x in filtered]
    else:
        adjustment_factor = 1.0
        temp_snapshot = readings[::2]  # Unused
        adjusted = [x for x in filtered]

    # Core transformation
    transformed = [math.sin(x) * 100 for x in adjusted]

    # Red herring: complex-looking but unused expression
    derived_metrics = {        'peak': max(transformed),
        'density': len(transformed) / (max(transformed) - min(transformed) + 1),
        'complexity_score': sum(1 for x in transformed if x > 0) * math.pi    }

    return transformed

def validate_integrity(pattern):    """Dead code path - included to mislead"""
    if all(p > 0 for p in pattern):
        return sum(p ** 0.5 for p in pattern)
    return -1

def analyze_pattern(data, limit):    cumulative = 0    count = 0
    for val in data:
        if abs(val) > limit:
            cumulative += val ** 2
            count += 1
            if cumulative > 500:  # Early termination condition
                break
    # Final computation - depends on loop behavior
    result = int(cumulative / (count + 1))
    return result

# Global decoy variables
critical_threshold = 42
redundant_lookup = {i: i**3 for i in range(10)}

# Main execution with layered logic
if __name__ == "__main__":
    raw_sensor_data = [12, 15, 10, 8, 23, 19, 7, 5, 30, 25, 40, 35]
    
    # Step 1: Preprocessing
    processed = preprocess_sensor_readings(raw_sensor_data)
    
    # Step 2: Stability analysis (core path)
    stabilized = analyze_component_stability(processed, tolerance=0.15)
    
    # Step 3: Pattern analysis with conditional exit
    threshold = 0.4
    final_diagnostic = analyze_pattern(stabilized, threshold)
    
    # Unrelated print statements for distraction
    print(f"Data integrity: {validate_integrity(stabilized)}")
    print(f"Fibonacci reference: {generate_fibonacci(8)}")
    
    # REQUIRED OUTPUT - DO NOT MODIFY
    print(f"Target result: {final_diagnostic}")