def process_item(x, y):
    temp = (x + y) * 2
    offset = x ^ y  # bitwise XOR for noise
    return temp + 1

# Irrelevant helper that isn't used
def unused_helper(n):
    return n ** 3 if n > 5 else n // 2

# Lambda for conditional scoring
score_transform = lambda s: s * 1.5 if s < 10 else s * 0.9

# Simulate sensor readings with some redundant processing
def analyze_readings(readings):
    total = 0
    peak = 0
    baseline = 10
    adjustment = 0
    
    for val in readings:
        if val > peak:
            peak = val
        total += val
    
    average = total / len(readings) if readings else 0
    
    # Distractor computation
    deviation_sum = sum((x - average) ** 2 for x in readings)
    variance = deviation_sum / len(readings) if readings else 0
    
    # Actual relevant logic buried here
    if average > baseline:
        adjustment = 5
    else:
        adjustment = -2
        
    return average, adjustment, peak

# Main calculation with mixed concepts
def calculate_final_score(raw_data):
    # Preprocess using irrelevant and relevant steps
    processed = [process_item(x, 3) for x in raw_data]
    
    # Additional distraction
    squared_chain = [p**2 for p in processed[:3]]
    checksum = sum(squared_chain) % 100
    
    # Analyze part of the data
    subset = processed[::2]  # Every other element
    avg, adj, max_val = analyze_readings(subset)
    
    # Core logic embedded with distractors
    base_score = sum(processed) / 10.0
    transformed = score_transform(base_score)
    
    # Multiple assignments and distractor variables
    multiplier, bonus, dummy_flag = 1.1, 0, False
    if max_val > 20:
        bonus = 7
        dummy_flag = True  # never used
    
    # Final score influenced by several factors
    final_score = (transformed + adj) * multiplier + bonus
    
    # Dead code path (never executed due to fixed condition)
    if len(raw_data) > 1000:
        final_score -= 100  # unreachable in practice
    
    return int(final_score)

# Input data
input_data = [4, 6, 5, 7, 3]

# Execute
final_score = calculate_final_score(input_data)
print(f"Result: {final_score}")