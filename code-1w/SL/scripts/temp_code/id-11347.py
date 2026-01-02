def analyze_sentiment(texts):
    sentiment_scores = {'positive': 0, 'negative': 0, 'neutral': 0}
    keyword_map = {
        'excellent': 3, 'good': 2, 'okay': 1,
        'bad': -2, 'terrible': -3, 'poor': -2,
        'average': 0, 'fine': 1
    }
    
    # Irrelevant preprocessing
    cleaned_texts = [t.lower().strip() for t in texts]
    word_count = {}
    for text in cleaned_texts:
        for word in text.split():
            word_count[word] = word_count.get(word, 0) + 1
    
    total_score = 0
    for text in cleaned_texts:
        words = text.split()
        for word in words:
            if word in keyword_map:
                sentiment_scores['positive' if keyword_map[word] > 0 else 'negative' if keyword_map[word] < 0 else 'neutral'] += 1
                total_score += keyword_map[word]
    
    # Dead computation path (never used)
    def unused_aggregator(scores):
        return sum(v * (i+1) for i, v in enumerate(sorted(scores.values())))
    
    return total_score

# Unused helper
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Distractor variables
baseline_threshold = 42
scaling_factor = 1.75
offset_adjustment = -3
placeholder_data = [1, 1, 2, 3, 5, 8, 13]

# Real logic buried among distractions
def transform_sequence(seq, mode='strict'):
    if mode == 'strict':
        processed = [x for x in seq if x % 2 == 1]  # keep odds
        return [x * 2 for x in processed][::-1]  # double and reverse
    return seq

# Another red herring
status_flags = {"active": True, "verified": False, "premium": None}
cached_results = set()

# Core function with hidden dependencies
def evaluate_criteria(values, limit):
    cumulative = 0
    seen = set()
    for v in values:
        if v in seen:
            continue
        if v > limit:
            temp_result = (v // 3) * 2
            if temp_result % 2 == 0:
                cumulative += temp_result
        else:
            cumulative -= v % 4
        seen.add(v)
    return abs(cumulative)

def build_feedback_index(responses):
    feedback_index = {}
    for i, r in enumerate(responses):
        feedback_index[f'entry_{i}'] = len(r.split())
    
    # Useless nested dict operation
    metadata = {
        'counts': {k: len(v.split()) for k, v in feedback_index.items()},
        'flags': set(feedback_index.keys())
    }
    
    return feedback_index

def evaluate_performance(logs, threshold):
    # Real input
    raw_texts = [
        'excellent service very good staff',
        'poor connection and bad experience',
        'average performance okay conditions',
        'terrible support no help'
    ]
    
    # Distractor initialization
    audit_trail = []
    validation_steps = 0
    intermediate_cache = []
    
    score_a = analyze_sentiment(raw_texts)
    
    sequence_data = [1, 2, 3, 4, 5, 6, 7]
    transformed = transform_sequence(sequence_data, 'strict')  # [14, 10, 6, 2]
    
    # Multi-step distraction
    temp_vals = []
    for t in transformed:
        if t > 5:
            temp_vals.append(t - 4)
        else:
            temp_vals.append(t + 1)
    
    # This is actually used
    criteria_input = [score_a] + temp_vals  # score_a = (3+2) + (-2-3-2) + (1+0) + (-3) = 5 -7 +1 -3 = -4
    
    # More noise
    config_settings = {
        'debug': False,
        'version': '2.1.0',
        'features': ['logging', 'metrics', 'tracing']
    }
    
    # Critical call
    score_b = evaluate_criteria(criteria_input, threshold)  # [-4, 10, 6, 2, 6] -> unique: [-4,10,6,2], limit=7
    
    # Dead code block
    if config_settings['debug']:
        print('Debug mode active')
        audit_trail.append('debug_skip')
    
    feedback_map = build_feedback_index(raw_texts)
    
    # Final computation
    base_multiplier = len(feedback_map)  # 4 entries
    adjustment = sum(1 for v in criteria_input if v < 0)  # only -4 → 1
    
    final_score = (score_b * base_multiplier) - adjustment  # score_b = evaluate_criteria([-4,10,6,2], 7)
    
    # Step-by-step for evaluate_criteria:
    # v=-4: not seen → <=7 → cumulative -= (-4 % 4)=0 → still 0
    # v=10: >7 → temp=10//3*2=6 → even → add 6 → cum=6
    # v=6:  <=7 → -= (6%4=2) → 6-2=4
    # v=2:  <=7 → -= (2%4=2) → 4-2=2
    # abs(2) = 2 → score_b = 2
    # final_score = (2 * 4) - 1 = 8 - 1 = 7
    
    # Print required at end
    print(f"Result: {final_score}")
    
    return final_score

# Trigger execution
def main():
    dummy_logs = ['log1', 'log2']
    feedback_map = {}
    result = evaluate_performance(feedback_map, 7)

main()