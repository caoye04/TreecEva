def process_entries(entries):
    processed = []
    temp_sum = 0
    redundant_counter = 0  # Distractor variable

    for entry in entries:
        if not isinstance(entry, str) or len(entry) == 0:
            continue
        stripped = entry.strip().lower()
        if 'error' in stripped:
            continue
        
        # Real logic: count vowels as signal strength
        vowel_count = sum(stripped.count(v) for v in 'aeiou')
        consonant_count = len(stripped) - vowel_count - stripped.count(' ')
        
        # Irrelevant transformation
        reversed_clean = stripped[::-1].replace(' ', '')
        mid_point = len(reversed_clean) // 2
        _ = reversed_clean[:mid_point]  # Dead computation
        
        score = vowel_count * 2 - consonant_count // 3
        processed.append(score)
        temp_sum += score  # Not used later
        
        # Fake state tracking
        redundant_counter += 1
        if redundant_counter > 100:
            break  # Never reached

    return processed


def validate_data(points):
    # Irrelevant validation with side effect-free checks
    if len(points) < 3:
        return False
    sorted_points = sorted(points)
    diff = [sorted_points[i+1] - sorted_points[i] for i in range(len(sorted_points)-1)]
    _ = sum(d > 5 for d in diff)  # Unused metric
    return True


def calculate_final_score(raw):
    parsed_data = raw.split(',')
    clean_data = [item for item in parsed_data if item.isalpha()]
    
    # Distractor: complex string manipulation that doesn't affect outcome
    transformed = []
    for item in clean_data:
        shifted = ''.join(chr((ord(c) - ord('a') + 2) % 26 + ord('a')) for c in item)
        back_to_orig = ''.join(chr((ord(c) - ord('a') - 2) % 26 + ord('a')) for c in shifted)
        transformed.append(back_to_orig)
    
    numeric_scores = process_entries(transformed)
    
    # Real aggregation
    base_total = sum(numeric_scores)
    adjustment_factor = len(numeric_scores) if len(numeric_scores) > 0 else 1
    pseudo_entropy = 0
    
    # Fake entropy-like calculation
    for x in numeric_scores:
        if x != 0:
            import math
            pseudo_entropy += x * math.log(abs(x)) if abs(x) > 1 else 0
    
    final_score = base_total * 3 // adjustment_factor
    
    # Additional distraction
    outlier_detected = any(abs(s - base_total / adjustment_factor) > 10 for s in numeric_scores)
    _ = 'Anomaly' if outlier_detected else 'Normal'  # Unused status
    
    return final_score

# Main execution
raw_input = "SignalAlpha,NoiseError,BetaTest,GammaRay,DeltaForce,error_invalid,OmegaWave"
data = raw_input + ",ExtraFiller"  # Extra that gets filtered

final_score = calculate_final_score(data)
print(f"Result: {final_score}")