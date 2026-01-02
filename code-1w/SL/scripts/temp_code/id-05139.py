def analyze_text_patterns(text):
    # Distractor: irrelevant text analysis
    char_freq = {}
    for c in text:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    # Dead code path (never used)
    if 'xyz' in text:
        return sum(ord(c) for c in text if c.isupper())

    # Another red herring
    temp_result = len(text.split()) * 2 - len(char_freq)
    return None

# Misleading global variable
system_flag = True

# Unused helper function (decoy)
def decrypt_sequence(seq):
    return [x ^ 7 for x in seq if x % 3 != 0]

# Real logic starts here — performance metrics evaluation
def compute_efficiency(tasks_completed, time_spent):
    if time_spent <= 0:
        return 0.0
    base_efficiency = (tasks_completed ** 1.5) / time_spent
    bonus = 1.0 if tasks_completed > 10 else 0.5
    return round(base_efficiency * bonus, 4)

def validate_stability(error_count, threshold=5):
    # Logical distraction with short-circuiting
    return not (error_count >= threshold and system_flag is True)

def aggregate_metrics(raw_values):
    total = 0
    multiplier = 1
    for val in raw_values:
        if val < 0:
            continue
        if val % 7 == 0:
            multiplier = 1.2  # boost on multiples of 7
        total += val * multiplier
        multiplier = 1  # reset unless condition hits again
    return int(total)

def evaluate_performance(metrics, reference):
    # Key computation branch
    efficiency = compute_efficiency(metrics['completed'], metrics['time'])
    stable = validate_stability(metrics['errors'])
    
    # String-based distractor: uses string method but irrelevant
    key_token = reference['version'].upper().replace("V", "")
    version_num = int(key_token) if key_token.isdigit() else 1
    
    # Critical data transformation
    raw_scores = reference['base_scores']
    adjusted_sum = aggregate_metrics(raw_scores)
    
    # Irrelevant list manipulation
    temp_list = [x for x in raw_scores if x > 5]
    temp_list.reverse()
    offset = sum(temp_list[:2]) if len(temp_list) >= 2 else 0
    
    # More distractions
    hypothetical = []
    for i in range(3):
        hypothetical.append(offset * (i + version_num))
    
    # Real signal: final score depends only on efficiency, stability, and adjusted_sum
    stability_bonus = 50 if stable else -20
    final_value = int(efficiency * 10 + adjusted_sum + stability_bonus)
    
    # DEAD CODE: would affect result but unreachable
    if False:
        final_value -= offset  # never executed

    return final_value

# Simulated input data
metrics = {
    'completed': 12,
    'time': 4.0,
    'errors': 3
}

benchmark_data = {
    'version': 'v3',
    'base_scores': [6, 7, 14, -5, 8, 21],  # includes multiples of 7
    'timestamp': '2024-05-17'
}

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark_data)

# Print required output
print(f"Result: {final_score}")