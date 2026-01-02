from collections import defaultdict, Counter

# Simulate multi-stage employee review with distractions
def generate_feedback_vector(traits):
    feedback = defaultdict(float)
    for trait in traits:
        if len(trait) > 6:
            feedback[trait] += 0.3
        elif trait.startswith('c'):
            feedback[trait] += 0.5
        else:
            feedback[trait] += 0.2
    return feedback

def apply_weighting(raw_feedback, weights):
    weighted = {}
    total = 0.0
    for k, v in raw_feedback.items():
        weighted[k] = v * weights.get(k, 1.0)
        total += weighted[k]
    return total

def analyze_trait_distribution(traits):
    # Distractor function: computes frequency but not used in final path
    freq = Counter(traits)
    rare_traits = [t for t, c in freq.items() if c == 1]
    trait_summary = { 'count': len(traits), 'unique': len(freq), 'rare_count': len(rare_traits) }
    return trait_summary

def build_evaluation_trace(log_entries):
    # Irrelevant trace builder - dead code path
    trace = []
    level = 0
    for entry in log_entries:
        level += 1
        trace.append(f"[L{level}] Processing {entry[:10]}")
    return trace

def recursive_threshold_check(value, depth=0):
    # Misleading recursive function that appears important but is unused
    if depth >= 5 or value < 0.1:
        return depth
    return recursive_threshold_check(value / 1.5, depth + 1)

def process_comments(comments):
    # Another distractor: processes text but result ignored
    word_count = 0
    uppercase_ratio = 0.0
    all_words = []
    for comment in comments:
        words = comment.split()
        word_count += len(words)
        all_words.extend(words)
    if word_count > 0:
        uppercase_count = sum(1 for w in all_words if w.isupper())
        uppercase_ratio = uppercase_count / word_count
    return {'total_words': word_count, 'shouting_ratio': uppercase_ratio, 'keywords': [w for w in all_words if w.lower() in ['excellent', 'poor']]}  

def evaluate_performance(feedback_log):
    base_weights = {
        'communication': 1.2,
        'creativity': 1.4,
        'consistency': 1.3,
        'collaboration': 1.1,
        'competence': 1.5
    }
    
    # Key logic hidden among noise
    temp_results = []
    for entry in feedback_log:
        vector = generate_feedback_vector(entry['traits'])
        score = apply_weighting(vector, base_weights)
        temp_results.append(score)
    
    # Real computation buried here
    avg = sum(temp_results) / len(temp_results)
    bonus = 0.0
    if avg > 0.6:
        bonus = 0.15
    elif avg > 0.4:
        bonus = 0.05
    
    adjustment_factor = 1.0
    size_metric = len(feedback_log) * 2
    if size_metric > 5:
        adjustment_factor *= 1.05
    
    # Actual answer determined here
    final_raw = avg + bonus
    adjusted_final = final_raw * adjustment_factor * 100
    
    # Red herring: complex rounding that isn't used
    precise_value = round(adjusted_final, 4)
    floor_val = int(precise_value // 1)
    
    # Final assignment
    final_score = int(round(adjusted_final))  # This is the real target
    
    # Dead code below
    debug_info = defaultdict(list)
    for i, r in enumerate(temp_results):
        debug_info['values'].append(f"Step{i}={r:.3f}")
    
    return final_score

# Main execution
if __name__ == "__main__":
    # Input data with meaningful structure
    employee_data = [
        {'id': 101, 'traits': ['communication', 'creativity'], 'notes': 'Solid performer'},
        {'id': 102, 'traits': ['consistency', 'communication', 'collaboration'], 'notes': 'Team player'},
        {'id': 103, 'traits': ['competence', 'creativity', 'communication'], 'notes': 'Innovative'}
    ]

    # Extract traits for processing
    trait_sequence = [entry['traits'] for entry in employee_data]

    # Run distractor functions to increase interference
    _ = analyze_trait_distribution([t for traits in trait_sequence for t in traits])
    _ = build_evaluation_trace([str(entry['id']) for entry in employee_data])
    _ = process_comments([entry['notes'] for entry in employee_data])
    _ = [recursive_threshold_check(0.8, i) for i in range(3)]

    # Critical statement - point of interest
    final_score = evaluate_performance(trait_sequence)
    
    # Output result as required
    print(f"Target result: {final_score}")