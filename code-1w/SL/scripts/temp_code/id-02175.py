from itertools import combinations

def analyze_sequence(data):
    temp_results = []
    cumulative_shift = 0
    for i, val in enumerate(data):
        shifted = val + (i % 4)
        temp_results.append(shifted)
        
    # Misleading intermediate: used in distractor path
    avg_temp = sum(temp_results) / len(temp_results) if temp_results else 0
    
    filtered_pairs = []
    for a, b in combinations(temp_results, 2):
        if (a + b) % 3 == 0:
            filtered_pairs.append(a * b)
    
    # Distractor: complex but unused computation
    pair_sums = [p % 17 for p in filtered_pairs]
    aggregate_noise = sum(pair_sums) * 0.1
    
    return temp_results

def validate_pattern(seq):
    validation_marks = []    
    for idx in range(len(seq)):
        if idx % 2 == 0:
            validation_marks.append(seq[idx] ** 0.5)
        else:
            validation_marks.append(seq[idx] // 3)
    
    # Dead code branch (never executed due to prior logic)
    if False and len(validation_marks) > 100:
        correction_factor = max(validation_marks) / min(validation_marks)
        validation_marks = [v * correction_factor for v in validation_marks]
    
    return validation_marks

def calculate_rating(log_data):
    base = sum(log_data) // len(log_data)
    deviation = 0
    for x in log_data:
        deviation += abs(x - base)
    
    # Semi-relevant transformation
    adjusted_base = base + (deviation // 10)
    
    # Final score influenced only by adjusted_base and fixed offset
    final_rating = adjusted_base * 3 - 15
    
    # Red herring variables
    peak = max(log_data)
    entropy_approx = len([x for x in log_data if x % 2]) * 0.7
    
    return final_rating

# Main execution
raw_input = [12, 7, 9, 14, 6, 11, 8]

# Step 1: Analyze sequence with enumeration and combinatorial side calculations
interim_findings = analyze_sequence(raw_input)

# Step 2: Validate pattern (output not used, but adds cognitive load)
consistency_checks = validate_pattern(interim_findings)

# Step 3: Calculate final score from analysis log
final_score = calculate_rating(interim_findings)

print(f"Result: {final_score}")