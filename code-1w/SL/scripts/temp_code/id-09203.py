from itertools import combinations

def analyze_segments(data):
    segments = []
    temp_sum = 0
    for val in data:
        if val > 0:
            temp_sum += val
        else:
            if temp_sum > 0:
                segments.append(temp_sum)
            temp_sum = 0
    if temp_sum > 0:
        segments.append(temp_sum)
    return segments

def extract_features(segments):
    features = set()
    total_energy = sum(segments)
    avg_energy = total_energy / len(segments) if segments else 0
    
    # Distractor: irrelevant feature computation
    peak_count = 0
    for s in segments:
        if s > avg_energy * 1.5:
            peak_count += 1
    
    # Real computation path
    mod_values = [s % 7 for s in segments if s % 3 != 0]
    adjusted_mods = [m * 1.5 for m in mod_values]
    
    # More distraction
    _ = [x ** 2 for x in adjusted_mods if x < 5]  # unused list comprehension
    
    return sum(adjusted_mods), peak_count  # peak_count is irrelevant

def validate_sequence(seq):
    # Uses string method as per requirement
    seq_str = ''.join(map(str, seq))
    if '00' in seq_str or '11' in seq_str:
        return False
    return True

def calculate_final_score(processed_data):
    base_score = 0
    for item in processed_data:
        if isinstance(item, tuple) and len(item) == 2:
            a, b = item
            if b != 0:
                base_score += a // b  # integer division
            else:
                base_score += a
    return int(base_score * 1.75)

# Main execution
raw_signal = [3, 5, -1, 2, 4, 6, -2, 1, 8, 0, 7, 3]

# Step 1: Segment analysis
segmented = analyze_segments(raw_signal)

# Step 2: Feature extraction (one output used, one ignored)
distraction_feature, _ = extract_features(segmented)

# Step 3: Generate candidate patterns using itertools
pattern_pool = list(combinations([1, 2, 3, 4], 3))
valid_patterns = []
for p in pattern_pool:
    if validate_sequence(p):
        valid_patterns.append(p)

# Step 4: Process data with distractors
accumulated = 0
processing_logs = []  # dead variable
for i, pat in enumerate(valid_patterns):
    accumulated += sum(pat) + i
    processing_logs.append(f"Processed {i}")  # logged but not used

# Step 5: Prepare input for final score
intermediate_values = [len(valid_patterns), accumulated, int(distraction_feature)]
processed_data = [(intermediate_values[i], i+1) for i in range(len(intermediate_values))]

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")