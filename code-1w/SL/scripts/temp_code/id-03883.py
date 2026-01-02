def process_entries(entries):
    processed = []
    temp_sum = 0
    debug_flag = False
    
    for entry in entries:
        if not isinstance(entry, str) or len(entry) == 0:
            continue
            
        stripped = entry.strip().lower()
        if stripped.startswith('ignore'):
            continue
            
        word_count = len(stripped.split())
        char_count = len(stripped.replace(' ', ''))
        complexity_score = (char_count * 0.3) + (word_count * 0.7)
        
        # Distractor: irrelevant transformation chain
        transformed = stripped[::-1]
        reversed_clean = transformed.replace('a', 'x').replace('e', 'y')
        dummy_metric = len(reversed_clean) % 7
        
        if word_count > 1 and 'error' not in stripped:
            processed.append(complexity_score)
        
        temp_sum += char_count
    
    average_chars = temp_sum / len(processed) if processed else 0
    return processed, average_chars


def validate_sequence(seq):
    # Irrelevant helper with dead logic path
    if not seq:
        return False
    
    valid = True
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            valid = False
    return valid


def calculate_final_score(raw_data):
    scores, avg_len = process_entries(raw_data)
    
    # Key computation variables
    base_total = sum(scores)
    penalty = 0
    
    # Nested conditional with mixed boolean and arithmetic logic
    if len(scores) >= 3:
        for i in range(len(scores)):
            if i % 2 == 0 and scores[i] > avg_len:
                penalty += 1.5
            elif scores[i] < 2.0:
                penalty += 0.5
    else:
        penalty = 5.0
    
    # Additional distractor block: unused but plausible calculation
    outlier_count = 0
    threshold = avg_len * 1.8
    for s in scores:
        if s > threshold:
            outlier_count += 1
    adjustment_factor = outlier_count * 0.9
    
    # Final score depends only on base_total and penalty
    final_score = base_total - penalty
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Input data with mixed valid/invalid entries
input_data = [
    "  Performance metrics analysis  ",
    "System status: nominal",
    "ignore this entry completely",
    "Error condition detected in module 3",
    "Data throughput optimization",
    "Concurrent user load balancing",
    "",
    "Final validation check passed"
]

# Execute main logic
final_score = calculate_final_score(input_data)