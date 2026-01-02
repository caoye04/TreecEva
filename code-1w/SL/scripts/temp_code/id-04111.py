def analyze_pattern(sequence):
    if not sequence.strip():
        return 0
    words = sequence.lower().split()
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    avg_length = char_count / word_count if word_count else 0
    
    # Distractor: irrelevant linguistic analysis
    vowel_ratio = sum(1 for c in ''.join(words) if c in 'aeiou') / char_count if char_count else 0
    repeated_words = len([w for w in set(words) if words.count(w) > 1])
    
    return word_count * 2 + int(avg_length)


def validate_entry(record):
    # Semi-relevant validation with side computations
    if 'status' not in record or record['status'] != 'active':
        return False
    
    name = record.get('name', '')
    if not name or not name.replace(' ', '').isalpha():
        return False
    
    # Distractor: extra formatting checks
    title_case_check = name == name.title()
    has_middle_name = len(name.split()) > 2
    
    score = record.get('score', -1)
    return 50 <= score <= 100


def calculate_final_score(data, thresholds):
    base_points = 0
    bonus_tally = []
    penalty_log = []
    
    # Main logic begins
    for entry in data:
        if validate_entry(entry):
            raw_score = entry['score']
            base_points += raw_score
            
            # Compute normalized performance
            max_threshold = max(thresholds.values())
            normalized = raw_score / max_threshold * 100
            
            # String-based category mapping (uses string method)
            category = entry.get('category', 'general').strip().lower()
            multiplier = 1.0
            if 'advanced' in category:
                multiplier = 1.2
            elif 'intermediate' in category:
                multiplier = 1.1
            
            adjusted = raw_score * multiplier
            bonus_tally.append(adjusted - raw_score)
            
            # Hidden conditional that affects final result
            if len(bonus_tally) % 2 == 0 and adjusted > 85:
                base_points += 5  # hidden bonus
        else:
            # Dead code path (rarely reached due to filtering above)
            penalty_log.append(entry['score'])
    
    # Irrelevant aggregation
    total_bonus = sum(bonus_tally)
    average_penalty = sum(penalty_log) / len(penalty_log) if penalty_log else 0
    
    # Key computational step: min/max/average used meaningfully
    if bonus_tally:
        spread = max(bonus_tally) - min(bonus_tally)
        base_points += int(spread)
    
    # Final adjustment using string-derived metadata
    metadata_tag = 'X1A9'.replace('X', 'T')  # dummy transformation
    tag_digit = int(metadata_tag[-1])
    base_points -= tag_digit
    
    # Core answer computation
    final_score = base_points + len(data) // 3
    return final_score

# Simulated dataset
entries = [
    {'name': 'Alice Johnson', 'score': 88, 'status': 'active', 'category': 'advanced_track'},
    {'name': 'Bob Smith', 'score': 76, 'status': 'inactive', 'category': 'intermediate level'},
    {'name': 'Charlie Lee', 'score': 92, 'status': 'active', 'category': 'advanced_research'},
    {'name': 'Diana King', 'score': 81, 'status': 'active', 'category': 'basic'},
    {'name': 'Evan Wong', 'score': 95, 'status': 'active', 'category': 'advanced'}
]

thresholds_config = {
    'min_pass': 50,
    'recommended': 75,
    'excellence': 90
}

# Auxiliary distractor function
def debug_summary(seq_list):
    lengths = [len(s) for s in seq_list]
    return {
        'total': sum(lengths),
        'max_len': max(lengths),
        'sorted': sorted(lengths)
    }

phrases = ["Clean Code", "Design Patterns", "Refactoring", "Working Software"]
dbg = debug_summary(phrases)

# Trigger point: critical assignment
final_score = calculate_final_score(entries, thresholds_config)
print(f"Result: {final_score}")