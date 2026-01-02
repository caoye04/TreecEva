from collections import defaultdict, Counter

def analyze_sequences(data):
    # Irrelevant analysis function (dead weight)
    freq = Counter()
    for seq in data:
        for item in seq:
            freq[item] += 1
    return freq

def preprocess_records(raw_entries):
    temp_result = []
    running_sum = 0
    
    for entry in raw_entries:
        if len(entry) > 3:
            processed = [x * 2 for x in entry if x % 2 == 1]  # Only odd numbers doubled
            temp_result.append(processed)
            running_sum += sum(processed)
    
    # Misleading computation: looks important but unused later
    avg_temp = running_sum / len(temp_result) if temp_result else 0
    outlier_flag = avg_temp > 50
    
    return temp_result

def validate_structure(items):
    # Another distraction: checks balance but not used in final logic
    stack = []
    for i in items:
        if i < 0:
            if stack and stack[-1] == -i:
                stack.pop()
            else:
                stack.append(i)
    return len(stack) == 0

def calculate_final_score(dataset):
    score_map = defaultdict(int)
    total_ops = 0
    
    for group in dataset:
        group_sum = sum(group)
        shift_val = len(group) % 4
        
        # Key transformation affecting final result
        for val in group:
            if shift_val > 0:
                transformed = (val << shift_val) ^ 3  # Bitwise manipulation
                score_map[val] += transformed % 7
            else:
                score_map[val] += val % 5
        
        total_ops += len(group)
    
    # Distractor: complex-looking but irrelevant to final score
    inverted_map = {v: k for k, v in score_map.items()}
    unique_keys = set(score_map.keys())
    key_length = len(''.join(map(str, unique_keys)))
    
    # Final scoring logic
    base_score = sum(score_map.values())
    penalty = total_ops // 3
    final_score = base_score - penalty + (key_length % 9)
    
    return final_score

# Main execution flow
raw_data = [
    [1, 3, 5],
    [2, 4],
    [7, 9, 11, 13],
    [6, 8, 10]
]

# Preprocessing step with side distractions
interim_analysis = analyze_sequences(raw_data)
dispatch_flags = [len(record) for record in raw_data]
processed_data = preprocess_records(raw_data)

# Validate structure (unused result adds confusion)
structure_valid = validate_structure([len(x) for x in raw_data])

# Critical statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")