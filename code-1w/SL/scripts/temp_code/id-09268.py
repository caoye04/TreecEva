import math

def process_metrics(raw):
    # Irrelevant transformation (dead path)
    temp_audit = [x ** 0.5 for x in raw if x > 10]
    adjusted = [x * 1.5 for x in raw]
    return adjusted

def validate_entry(record):
    # Distractor function: looks important but unused
    return sum([1 for c in record['name'] if c.isupper()]) == len(record['name'])

def transform_case(text):
    # Misleading utility with no real impact
    return ''.join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text)])

def bitwise_diagnostic(value):
    # Red herring: used to compute decoy_result
    step1 = value ^ 255
    step2 = step1 & 127
    step3 = step2 >> 3
    return step3 * 3

def calculate_entropy(values):
    # Decoy scientific computation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def calculate_adjusted_score(dataset, scaling_factors):
    # Core logic begins
    base_values = [d['value'] for d in dataset]
    
    # Apply non-uniform scaling using lambda and zip
    scaled = list(map(lambda x: x[0] * x[1], zip(base_values, scaling_factors)))n    
    # Filter anomalies (simulated)
    filtered = [v for v in scaled if 50 <= v <= 500]
    
    # Accumulate via summation with offset
    raw_sum = sum(filtered) + 17
    
    # Conditional adjustment based on length
    if len(filtered) % 2 == 1:
        raw_sum += 13
    
    # Apply logarithmic compression
    compressed = math.log(raw_sum) * 100
    
    # Introduce bit manipulation red herring
    decoy_result = bitwise_diagnostic(int(compressed))
    decoy_result = decoy_result * 0  # Neutralize (misleading)
    
    # Final adjustment using case conversion side-effect (dummy)
    flag_str = "AdJuSt" if compressed > 300 else "normal"
    adjustment = sum(1 for c in flag_str if c.isupper())  # Always 4
    
    final = compressed + adjustment
    
    return int(final)

# Main execution
if __name__ == "__main__":
    # Real data input
    data = [
        {'id': 'A', 'value': 86, 'name': 'Alpha'},
        {'id': 'B', 'value': 92, 'name': 'Beta'},
        {'id': 'C', 'value': 79, 'name': 'Gamma'},
        {'id': 'D', 'value': 98, 'name': 'Delta'},
        {'id': 'E', 'value': 83, 'name': 'Epsilon'}
    ]

    weights = [1.2, 1.1, 1.3, 0.9, 1.4]

    # Dead code path: processed but not used
    audit_log = process_metrics([item['value'] for item in data])
    entropy = calculate_entropy([len(item['name']) for item in data])

    # Key statement
    final_score = calculate_adjusted_score(data, weights)

    # Print result
    print(f"Result: {final_score}")