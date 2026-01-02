def analyze_pattern(sequence):
    """Irrelevant analysis function - distractor"""
    count = 0
    for char in sequence:
        if char.isupper():
            count += 1
    return count * 2

# Unused but misleading data structures
baseline_metrics = {"alpha": 12, "beta": 19, "gamma": 7}
dummy_sequence = "AbCdEfGhIjK"
useless_count = analyze_pattern(dummy_sequence)

# Core logic disguised among red herrings
threshold_set = {3, 5, 7, 11, 13}
scaling_factor = 1.75
correction_offset = -4

user_data = [
    (15, 'PASS', 4),
    (6, 'FAIL', 3),
    (21, 'PASS', 5),
    (9, 'PASS', 7),
    (4, 'FAIL', 2)
]

# Decoy transformation - looks important but unused
transformed = []
for val, status, level in user_data:
    if status == 'PASS':
        transformed.append((val // level) * 2)

# Real processing buried in noise
def filter_by_prime(value, primes):
    for p in primes:
        if value % p == 0:
            return True
    return False

def compute_weighted_sum(records, weights=(0.5, 0.3, 0.2)):
    total = 0.0
    for record in records:
        base_val, verdict, tier = record
        if tier >= 3 and verdict == 'PASS':
            adjustment = len(str(base_val))  # uses string method
            total += base_val * weights[0] + adjustment * weights[1]
    return total

def validate_entry(item):
    """Another decoy validator"""
    text_repr = str(item[0])
    return text_repr.startswith('1') or text_repr.endswith('9')

# Multiple layers of processing with distractions
intermediate_values = set()
for entry in user_data:
    raw_val = entry[0]
    if raw_val > 5:
        intermediate_values.add(raw_val // 2)  # integer division

# This function appears complex but only one path matters
def process_results(data, required_filters):
    score = 0
    active_flags = [False, True, False]
    
    for item in data:
        value, outcome, rank = item
        
        # Meaningful condition mixed with irrelevant checks
        passes_filter = filter_by_prime(value, required_filters)
        has_length_bonus = len(str(value)) == 2  # string method used meaningfully
        
        temp_modifier = 0
        if outcome == 'PASS':
            if passes_filter and has_length_bonus:
                temp_modifier = 11
            elif outcome == 'PASS' and rank > 2:
                temp_modifier = 7
        else:
            temp_modifier = -5
            
        # Critical accumulation
        if 'PASS' in outcome:  # redundant but obscures logic
            score += value // rank  # integer division and tuple unpacking
        
        # Dead branch - distractor
        if value < 0:
            fallback = scaling_factor * correction_offset
            score -= int(fallback)
            
    # Final transformation that actually determines result
    aggregate = compute_weighted_sum(data)
    final_component = score + int(aggregate)  # combines two independent computations
    
    # Red herring: modifying unused variables
    debug_info = {
        'entries': len(data),
        'flags': sum([1 for x in active_flags if x]),
        'offset': correction_offset
    }
    
    return final_component

# Key execution point
final_score = process_results(user_data, threshold_set)

# Irrelevant post-processing
summary_tag = f'SCORE_{str(final_score)[-3:]}'
archive_label = summary_tag.lower().replace('_', '-')

print(f"Result: {final_score}")