from collections import defaultdict, Counter

def analyze_sentiment(text_data):
    # Irrelevant sentiment analysis function (decoy)
    words = text_data.lower().split()
    positive = ['good', 'great', 'excellent', 'well']
    negative = ['bad', 'poor', 'terrible', 'awful']
    score = 0
    for word in words:
        if word in positive:
            score += 1
        elif word in negative:
            score -= 1
    return score

def transform_metrics(data_list):
    # Distractor: transforms data in irrelevant ways
    transformed = []
    for item in data_list:
        temp_val = (item * 1.5) % 7
        if temp_val > 4:
            transformed.append(int(temp_val ** 0.5))
        else:
            transformed.append(-1)
    return transformed

def evaluate_consistency(record):
    # Another decoy function that calculates string consistency (misleading)
    char_count = defaultdict(int)
    for c in record:
        char_count[c] += 1
    freq_counter = Counter(char_count.values())
    return max(freq_counter.keys()) - min(freq_counter.keys()) if freq_counter else 0

def compute_baseline(input_seq):
    # Dead path: computes baseline but never used in final logic
    total = 0
    count = 0
    for x in input_seq:
        if x % 2 == 0 and x > 0:
            total += x ** 0.5
            count += 1
    return total / count if count else 0

def process_feedback(entries):
    # Core relevant function embedded with noise
    feedback_tally = defaultdict(int)
    sequence_log = []  
    temp_shadow = []  # Unused list (red herring)

    for entry in entries:
        parts = entry.split(':')
        if len(parts) < 2:
            continue
        category = parts[0].strip()
        value_str = parts[1].strip()
        
        # Parse numeric value from string
        try:
            raw_value = float(''.join(filter(lambda c: c.isdigit() or c == '.', value_str)))
            if 'accuracy' in category:
                feedback_tally['precision'] += int(raw_value)
            elif 'response' in category:
                feedback_tally['speed'] += max(1, int(raw_value) // 10)
            elif 'clarity' in category:
                feedback_tally['clarity'] += len(value_str) % 5
        except ValueError:
            pass

        # Distractor block: builds unused sequence log
        seq_val = sum(ord(c) for c in value_str if c.isdigit())
        sequence_log.append(seq_val)

    # Hidden key computation buried in distractors
    key_modifier = len(sequence_log) % 3 + 1
    feedback_tally['clarity'] *= key_modifier  # Affects final result

    return feedback_tally

def aggregate_performance(summary):
    # Final aggregation with misleading operations
    base = 0
    weights = {'precision': 3, 'speed': 2, 'clarity': 4, 'redundant_metric': 0}
    
    # Fake metric added to confuse
    summary['redundant_metric'] = 999  
    
    for k, v in summary.items():
        if k in weights and weights[k] > 0:
            base += v * weights[k]
    
    # Extra manipulation based on string property of keys (real dependency)
    total_chars = sum(len(key) for key in summary.keys())
    adjustment = total_chars % 5  # 17 % 5 = 2
    final_value = base + adjustment
    
    # Critical dead code branch (never executes but looks important)
    if all(v > 0 for v in summary.values()):
        final_value = int(final_value * 0.9)
    
    return final_value

# Main execution with red herrings
raw_input_stream = [
    "accuracy: 85.5",
    "response_time: 230",
    "clarity_rating: 4.2",
    "accuracy: 92",
    "response_time: 170",
    "clarity_rating: 3.8"
]

# Irrelevant preprocessing
sentiment_shift = analyze_sentiment("performance was excellent but response time was poor")
metric_trace = transform_metrics([10, 20, 30])
consistency_flag = evaluate_consistency("aabbc")
baseline = compute_baseline([12, 14, 16, 18])

# Real data flow begins here
parsed_feedback = process_feedback(raw_input_stream)
final_score = aggregate_performance(parsed_feedback)
print(f"Result: {final_score}")