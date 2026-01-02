import itertools

def analyze_pattern(sequence):
    counts = {}
    for char in sequence:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def validate_sequence(seq):
    valid = True
    for i in range(len(seq) - 1):
        if seq[i] == seq[i+1]:
            valid = False
    return valid

def compute_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * p  # simplified pseudo-entropy
    return entropy

def calculate_final_score(data, thresholds):
    # Step 1: Filter relevant entries
    filtered = [x for x in data if x > thresholds['min_val']]
    
    # Irrelevant distraction: character pattern analysis on string representation
    str_repr = ''.join([str(int(x % 10)) for x in filtered])
    pattern_analysis = analyze_pattern(str_repr)
    unused_entropy = compute_entropy(list(pattern_analysis.values()))
    
    # Step 2: Group consecutive similar magnitude numbers (distraction with real purpose)
    grouped = []
    current_group = []
    for num in sorted(filtered):
        if not current_group or abs(num - current_group[-1]) < 3:
            current_group.append(num)
        else:
            if len(current_group) >= 2:
                grouped.append(sum(current_group))
            current_group = [num]
    if len(current_group) >= 2:
        grouped.append(sum(current_group))
    
    # Step 3: Apply threshold-based scoring
    base_score = 0
    for g in grouped:
        if g > thresholds['high_group']:
            base_score += 15
        elif g > thresholds['med_group']:
            base_score += 8

    # Step 4: Adjust score using digit frequency (semi-relevant)
    digits = [int(d) for d in str(base_score) if d.isdigit()]
    freq_pairs = list(itertools.combinations(digits, 2))
    pair_sum = sum(a + b for a, b in freq_pairs if (a + b) % 2 == 0)  # only even-sum pairs
    
    # Final computation
    adjustment = len(freq_pairs) - pair_sum % 7
    final_score = base_score + adjustment
    
    # Dead code path - never executed due to logic above
    if len(digits) > 100:
        fallback = compute_entropy(digits)
        final_score = int(fallback)
        
    return final_score

# Main execution
raw_data = [4.2, 6.1, 6.3, 2.8, 9.5, 9.4, 9.6, 1.0, 5.5, 5.7, 5.6, 3.3]
config = {
    'min_val': 3.0,
    'med_group': 10.0,
    'high_group': 16.0
}

result_flag = validate_sequence('abcxyz')  # unrelated validation
misc_data = [x**2 for x in range(5) if x % 2 == 0]  # dead-end calculation

final_score = calculate_final_score(raw_data, config)
print(f"Target result: {final_score}")