from collections import defaultdict
import math

def preprocess_data(raw):
    # Irrelevant preprocessing steps (distractors)
    temp_log = [x.lower() for x in raw if isinstance(x, str)]
    clean_data = [int(x) for x in raw if isinstance(x, int) or (isinstance(x, str) and x.isdigit())]
    
    # Semi-relevant transformation
    normalized = [math.log(x + 1) if x > 0 else 0 for x in clean_data]
    return clean_data  # Only clean_data is actually used later


def analyze_patterns(seq):
    # Distractor function: counts even/odd but not used in final logic
    counts = defaultdict(int)
    for num in seq:
        counts['even' if num % 2 == 0 else 'odd'] += 1
        counts['positive'] += 1 if num > 0 else 0
    
    # Another red herring computation
    cumulative = 0
    for i in range(len(seq)):
        if seq[i] > seq[0]:
            cumulative += i * seq[i]
    return cumulative  # Not used anywhere


def calculate_final_score(values):
    # Core logic starts here
    base_total = sum(val for val in values if val % 3 == 0)  # Only multiples of 3
    
    # Additional filtering based on position (index conditions)
    index_boost = 0
    for idx, val in enumerate(values):
        if idx > 0 and values[idx - 1] < val and val % 2 == 1:
            index_boost += 2
    
    # Conditional penalty
    penalty = 0
    if len(values) > 5:
        avg = sum(values) / len(values)
        if avg > 10:
            penalty = 7
    
    # Secondary distractor: string-like operations on numbers
    digit_sum = 0
    for val in values:
        for d in str(val):
            if d in '369':
                digit_sum += 1  # Counts occurrences of 3,6,9 digits
    
    # Final score formula
    final_score = base_total + index_boost - penalty
    
    # Dead code branch (never executed due to data)
    if False and digit_sum > 100:
        final_score *= 2
        
    return final_score

# Main execution
raw_input = [12, '45', 'test', 18, 7, 21, 9, 'ignore', 33]
data = preprocess_data(raw_input)

# Unused analysis (distractor)
analyze_patterns(data)

final_score = calculate_final_score(data)
print(f"Target result: {final_score}")