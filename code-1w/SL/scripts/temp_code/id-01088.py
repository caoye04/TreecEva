def preprocess_entry(entry):
    # Irrelevant transformation
    cleaned = entry.strip().lower()
    tokens = cleaned.split(' ')
    word_count = len(tokens)
    
    # Distractor: counts vowels but not used in final logic
    vowel_count = sum([1 for c in cleaned if c in 'aeiou'])
    
    # Relevant: check if contains numeric token
    has_number = any(tok.isdigit() for tok in tokens)
    return has_number, word_count


def validate_format(entry):
    # Semi-relevant validation
    if len(entry) < 3:
        return False
    if entry[0].isdigit() or entry[-1].isdigit():
        return False
    # Distractor: checking special chars but not critical
    special_chars = sum(1 for c in entry if not c.isalnum() and not c.isspace())
    return True


def calculate_risk_level(word_len, has_num):
    # Complex but mostly irrelevant scoring
    base = word_len * 2
    if has_num:
        base += 10
    # Distractor: unused adjustment
    adjustment = 5 if base > 20 else -3
    return base  # Only base matters


def evaluate_consistency(entries):
    # Counts consecutive entries with numbers
    count = 0
    max_streak = 0
    for ent in entries:
        has_num, _ = preprocess_entry(ent)
        if has_num:
            count += 1
            max_streak = max(max_streak, count)
        else:
            count = 0
    # This streak is never used in final score
    return max_streak


def calculate_final_score(entries, thresholds):
    total_weight = 0
    valid_count = 0
    debug_values = []  # Dead storage
    
    for entry in entries:
        # Validate format (semi-relevant)
        if not validate_format(entry):
            continue
        
        has_number, word_count = preprocess_entry(entry)
        
        # Key logic: only entries with numbers contribute
        if has_number:
            risk = calculate_risk_level(word_count, has_number)
            weighted_score = risk * 1.5
            total_weight += weighted_score
            valid_count += 1
            debug_values.append(weighted_score)  # Not used later
        
        # Distractor: string analysis unrelated to score
        char_freq = {c: entry.count(c) for c in set(entry) if c.isalpha()}
        palindrome_check = entry == entry[::-1]  # Unused
    
    # Final computation
    avg_weight = total_weight / valid_count if valid_count > 0 else 0
    
    # Secondary adjustment based on threshold rules
    bonus = 0
    if avg_weight > thresholds['high']:
        bonus = 25
    elif avg_weight > thresholds['medium']:
        bonus = 10
    
    # The real answer
    final_score = int(avg_weight + bonus)
    
    # Red herring: complex string metric
    all_text = ''.join(entries)
    unique_consonants = len({c for c in all_text if c.isalpha() and c not in 'aeiou'})
    
    return final_score

# Main execution
if __name__ == '__main__':
    data_entries = [
        'User input: 123',
        'Log entry abc',
        'Data stream 456',
        'Status update 789',
        'System ping',
        'Backup 0x1A',
        'Payload complete'
    ]
    
    thresholds = {
        'low': 15,
        'medium': 25,
        'high': 35
    }
    
    # Extra unused variables
    metadata_log = [len(entry) for entry in data_entries]
    timestamp_weights = [1.1, 1.2, 0.9, 1.0, 1.1, 0.8, 1.3]
    
    final_score = calculate_final_score(data_entries, thresholds)
    print(f"Result: {final_score}")