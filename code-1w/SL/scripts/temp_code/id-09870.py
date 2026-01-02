from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    temp_result = []
    for i in range(2, len(sequence) + 1):
        for combo in combinations(sequence, i):
            if sum(combo) % 3 == 0:
                count += 1
                temp_result.append(combo)
    # Irrelevant tracking
    pattern_log = f'Analyzed {count} patterns'
    return count

def preprocess_input(raw):
    cleaned = raw.strip().lower()
    tokens = cleaned.split(',')
    numeric_values = []
    for t in tokens:
        t = t.strip()
        if t.isdigit() or (t.startswith('-') and t[1:].isdigit()):
            numeric_values.append(int(t))
    # Distractor: unused transformation
    reversed_str = ''.join([t[::-1] for t in tokens if t.isalpha()])
    return numeric_values

def compute_final_score(data_list):
    base_total = sum(x ** 2 for x in data_list if x > 0)
    penalty = 0
    if len(data_list) > 5:
        sorted_vals = sorted(data_list)
        median_val = sorted_vals[len(sorted_vals) // 2]
        penalty = abs(median_val) * 0.5
    else:
        # Dead code branch (never executed due to input length)
        backup_flag = True
        penalty = 0
    
    # Key distraction: irrelevant string processing
    status_msg = "Processing complete".replace(' ', '_').upper()
    alert_code = len(status_msg) if 'COMPLETE' in status_msg else 0
    
    # Another red herring: unused list comprehension
    derived_metrics = [x for x in data_list if x % 2 == 0 and x > 0]
    
    final_score = int(base_total - penalty)
    return final_score

# Simulated sensor readings with noise
raw_input = "10, -3, 7, 4, 12, 5, abc, 8, 6"

# Step 1: Clean and extract numbers
extracted_numbers = preprocess_input(raw_input)

# Step 2: Analyze combinatorial patterns (unused in final score)
analysis_count = analyze_patterns(extracted_numbers)

# Step 3: Compute the actual target score
processed_data = extracted_numbers
final_score = compute_final_score(processed_data)

print(f"Result: {final_score}")