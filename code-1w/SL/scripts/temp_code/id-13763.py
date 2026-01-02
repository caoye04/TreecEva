import itertools

# Simulated sensor data preprocessing with red herrings
def fetch_raw_sensor_readings():
    return [18, 24, 57, 31, 92, 44, 10, 63]

def calculate_checksum(sequence):
    # Irrelevant checksum function (dead end)
    return sum(x * (i + 1) for i, x in enumerate(sequence)) % 1024

def apply_mask(data, mask=0b1101):
    # Bit manipulation distraction
    return [x ^ mask & 15 for x in data]

def filter_outliers(values, threshold=50):
    # Misleading filtering branch never used
    return [v for v in values if v < threshold]

def generate_pairs(seq):
    # Unused combinatorial generation (distractor)
    return list(itertools.combinations(seq, 2))

def compute_aggregate_score(items):
    # Fake scoring logic to mislead reasoning
    score = 0
    for item in items:
        if item % 3 == 0:
            score += item // 3
        elif item % 5 == 0:
            score -= item // 5
    return score * 1.5  # Never actually used

def transform_data_stream(raw_data):
    # Core transformation chain with distractions
    masked = apply_mask(raw_data, mask=0b1010)
    adjusted = [x + 5 for x in raw_data if x % 2 == 0]  # Only even numbers processed
    shifted = [(x >> 2) for x in masked]  # Right shift by 2 bits
    expanded = list(itertools.chain.from_iterable([(x, x * 2) for x in shifted]))
    truncated = [x for x in expanded if x < 100]  # Filter out large values
    return truncated  # Actual transformed data

def evaluate_stability_metric(dataset):
    # Complex but irrelevant stability analysis
    diffs = [abs(dataset[i] - dataset[i-1]) for i in range(1, len(dataset))]
    return sum(diffs) / len(diffs) if diffs else 0

def process_transformed_data(data, config):
    base = config['base_offset']
    factor = config['multiplier']
    temp_result = 0
    
    for index, value in enumerate(data):
        if index % 2 == 0:
            temp_result += value * factor
        else:
            temp_result -= value // 2
    
    # Apply base offset only if condition met
    if len(data) > 5:
        temp_result += base
    
    # Additional bit manipulation twist
    temp_result = (temp_result ^ 255) - 100  # XOR with 255 then subtract
    
    # Final adjustment based on parity of result
    if temp_result % 2 == 0:
        temp_result = int(temp_result * 1.1)
    else:
        temp_result = int(temp_result * 0.9)
    
    return temp_result

# Main execution flow
if __name__ == '__main__':
    raw_readings = fetch_raw_sensor_readings()  # [18, 24, 57, 31, 92, 44, 10, 63]
    
    # Distractor computations (no impact on final result)
    checksum = calculate_checksum(raw_readings)
    outlier_free = filter_outliers(raw_readings, threshold=40)
    all_pairs = generate_pairs(raw_readings)
    fake_score = compute_aggregate_score(raw_readings)
    stability = evaluate_stability_metric(raw_readings)
    
    # Real processing begins here
    transformed_data = transform_data_stream(raw_readings)
    
    # Configuration with meaningful parameters
    config = {
        'base_offset': 15,
        'multiplier': 3
    }
    
    # Critical statement
    final_output = process_transformed_data(transformed_data, config)
    
    # Print required result
    print(f"Target result: {final_output}")