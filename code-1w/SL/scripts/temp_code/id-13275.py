import itertools

def analyze_metrics(data):
    # Irrelevant analysis branch (dead path)
    if len(data) > 100:
        return sum(x ** 0.5 for x in data if x % 2 == 0)
    
    # Distractor computation
    temp_result = [x * 2 + 1 for x in data if x < 50]
    ignored_aggregate = sum(temp_result) // (len(temp_result) or 1)

    # Real processing path begins here
    filtered = [x for x in data if x > 10 and x % 3 != 1]
    mapped = list(map(lambda x: (x ** 2) % 47, filtered))
    shifted = [(val << 1) ^ 5 for i, val in enumerate(mapped)]
    return shifted


def validate_sequence(seq):
    # Unused validation function (decoy)
    checksum = 0
    for item in seq:
        checksum = (checksum * 31 + item) % 10007
    return checksum == 1234


def transform_string_key(input_str):
    # String manipulation red herring
    reversed_upper = input_str[::-1].upper()
    char_map = {chr(i): i - ord('A') for i in range(ord('A'), ord('Z')+1)}
    values = [char_map.get(c, 0) for c in reversed_upper]
    return sum(v * (i+1) for i, v in enumerate(values)) % 100


def evaluate_performance(raw_data):
    # Key logic with distractions
    
    # Irrelevant preprocessing
    normalized = [round(x * 1.05, 2) for x in raw_data]
    outlier_flag = any(abs(x - 50) < 5 for x in normalized)
    
    # Core logic disguised among noise
    processed = analyze_metrics(raw_data)
    
    # Multiple distractors
    shadow_copy = processed[:]
    adjustment_factor = 0
    for idx, val in enumerate(processed):
        if idx % 2 == 0 and val > 20:
            adjustment_factor += 1
    
    # Actual critical transformation
    accumulated = 0
    for i, num in enumerate(processed):
        if i % 3 == 0:
            accumulated += num
        elif num % 2 == 1:
            accumulated -= (num // 3)
        else:
            accumulated += (num % 7)

    # Decoy dictionary operations
    stats = {
        'count': len(processed),
        'peak': max(processed, default=0),
        'entropy': sum(p * p for p in processed) / 1000 if processed else 0
    }
    
    # Final computation chain
    base_score = accumulated * 3
    penalty = len([x for x in raw_data if x < 5]) * 2
    bonus = transform_string_key('diagnostics')  # evaluates to fixed constant: distractor
    
    # Critical assignment
    final_score = base_score - penalty + bonus

    # Dead code path
    if stats['entropy'] > 100:
        final_score = int(final_score * 0.9)
        
    return final_score

# Simulated diagnostic dataset (bit pattern influenced)
data_points = [12, 15, 18, 19, 21, 24, 25, 27, 30, 33, 36, 39]

def main():
    global final_score
    # Redundant filtering
    active_filters = ['threshold', 'outlier', 'anomaly']
    filter_status = {f: True for f in active_filters}
    
    # String decoy usage
    key_tag = "analysis_core"
    tag_upper = key_tag.upper()
    segments = tag_upper.split('_')
    segment_length_sum = sum(len(s) for s in segments)
    
    # Itertools distraction
    pairs = list(itertools.combinations([10, 20, 30], 2))
    pair_sum_avg = sum(a + b for a, b in pairs) / len(pairs) if pairs else 0
    
    # Actual execution point
    diagnostic_data = [x + (x % 4) for x in data_points]  # modifies original
    final_score = evaluate_performance(diagnostic_data)
    
    # Output requirement
    print(f"Result: {final_score}")

main()