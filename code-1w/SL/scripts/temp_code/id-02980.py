from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition (distractor: some values are irrelevant)
sensor_readings = [14, 17, 23, 14, 19, 23, 29, 31, 14, 17, 23, 37, 41, 43, 47]

def preprocess_signal(raw_data):
    # Irrelevant transformation path (dead code)
    temp_buffer = [x * 1.5 for x in raw_data if x % 2 == 1]
    temp_buffer = [round(x) for x in temp_buffer]

    # Actual preprocessing begins here
    filtered = [x for x in raw_data if x > 20]  # Only values above threshold matter
    normalized = [x % 10 for x in filtered]  # Normalize to last digit
    
    # Distractor: unused frequency map
    freq_map = defaultdict(int)
    for val in raw_data:
        freq_map[val] += 1
    
    return normalized

def evaluate_health_status(metrics):
    # Misleading health model (never actually used)
    score = sum([m**2 for m in metrics]) / len(metrics) if metrics else 0
    status = 'stable' if score < 50 else 'critical'
    return status  # This function is called but result discarded

def transform_sequence(seq):
    # Unused recursive transformation (red herring)
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    return transform_sequence(seq[mid:]) + transform_sequence(seq[:mid])

def generate_checksum(values):
    # Seemingly important but ultimately irrelevant computation
    checksum = 0
    for i, v in enumerate(values):
        checksum ^= (v << (i % 3))  # Bit manipulation distraction
    return checksum % 1000  # Never used in final logic

def analyze_signal(data):
    # Core logic hidden among distractions
    if not data:
        return -1
    
    # Real computation: count occurrences of even digits
    counter = Counter(data)
    even_count = sum(counter[d] for d in counter if d % 2 == 0)
    
    # Add modular contribution based on length
    n = len(data)
    mod_factor = (n * (n + 1)) % 7
    
    # Hidden arithmetic pattern: sum of prime-positioned elements
    primes = [2, 3, 5, 7, 11, 13, 17]
    prime_sum = 0
    for p in primes:
        if p - 1 < len(data):  # Adjust for zero-indexing
            prime_sum += data[p - 1]

    # Final formula combining multiple concepts
    result = even_count * 100 + mod_factor * 10 + (prime_sum % 10)
    
    # Distractor variables (assigned but not part of result)
    avg_val = sum(data) / len(data) if data else 0
    max_run = 1
    current_run = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 1
    
    return result

# Main execution flow with misleading calls
temp_result = evaluate_health_status(sensor_readings)  # Result ignored
dummy_checksum = generate_checksum(sensor_readings)     # Unused value
shuffled = transform_sequence(sensor_readings)         # Dead-end processing

processed_data = preprocess_signal(sensor_readings)

# Key statement where answer is determined
final_diagnostic = analyze_signal(processed_data)

print(f"Target result: {final_diagnostic}")