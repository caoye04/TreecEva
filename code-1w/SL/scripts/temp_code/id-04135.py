def analyze_sentiment(text):
    if not text:
        return 0
    sentiment = sum(1 for c in text if c in '!?') - len([c for c in text if c.islower()])
    return sentiment + len(text.split())

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 3)

# Unused but plausible transformation
def transform_case_recursive(items, depth=0):
    if depth > 2 or not items:
        return items
    return [transform_case_recursive([x.lower() if isinstance(x, str) else x], depth+1)[0] 
            if isinstance(x, str) else x for x in items]

# Core logic disguised among distractors
def process_feedback(feedback_list):
    raw_scores = []
    adjustment_factor = 7
    
    for entry in feedback_list:
        if 'urgent' in entry.get('flags', []):
            base = len(entry['text']) * 2
        elif entry['rating'] < 3:
            base = -len(entry['comments'])
        else:
            base = analyze_sentiment(entry['text'])
        
        # Red herring computation
        temp_offset = sum(ord(c) % 5 for c in entry.get('source_id', ''))
        
        raw_scores.append(base + adjustment_factor)
    
    # Distractor: unused aggregation
    avg_raw = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    
    return raw_scores

# Another decoy function dealing with similar concepts
def compute_text_weight(texts):
    weights = [len(t) ** 0.5 for t in texts if isinstance(t, str)]
    return [w * 1.5 for w in weights]

# Key recursive evaluation chain
def evaluate_performance(log_entries):
    if not log_entries:
        return -1
    
    scores = process_feedback(log_entries)
    cumulative = 0
    
    for i, score in enumerate(scores):
        if i % 2 == 0:
            cumulative += score * (i + 1)
        else:
            cumulative -= score // max(i, 1)
    
    # Critical distraction: complex-looking but irrelevant bitwise mix
    magic_seed = 0b1010
    for s in [ord(log_entries[0]['source_id'][0]), len(log_entries)]:
        magic_seed ^= (s << 2) & 0b11111
    
    # Real answer depends only on cumulative and fixed offset
    final_modifier = 42 if any('critical' in e.get('flags', []) for e in log_entries) else 24
    
    return cumulative + final_modifier

# Simulated input data with meaningful structure
feedback_chain = [
    {
        'text': 'Poor service quality!',
        'rating': 1,
        'comments': 'Unacceptable wait times',
        'source_id': 'A7',
        'flags': ['urgent']
    },
    {
        'text': 'Good, but could improve.',
        'rating': 4,
        'comments': '',
        'source_id': 'B2',
        'flags': []
    },
    {
        'text': 'Excellent experience!!!!!',
        'rating': 5,
        'comments': 'Very satisfied',
        'source_id': 'C9',
        'flags': ['critical']
    }
]

# Dead code path - never called
legacy_data = [{'input': 'old', 'val': 100}]
def migrate_legacy(records):
    return [{'new_format': True, 'value': r['val'] * 2} for r in records]

# Trigger execution
final_score = evaluate_performance(feedback_chain)
print(f"Result: {final_score}")