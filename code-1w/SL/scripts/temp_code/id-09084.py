from itertools import combinations

def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) // len(adjusted) if adjusted else 0

def track_history(entries):
    history_log = set()
    for e in entries:
        history_log.add(e % 100)
    return sorted(history_log)

def compute_baseline(data):
    # Irrelevant computation: tracks frequency but not used later
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    unique_count = len(freq)
    temp_sum = sum([k * v for k, v in freq.items()])
    dummy_result = temp_sum // unique_count if unique_count else 0
    return dummy_result

def generate_pairs(values):
    # Creates pairs but only their count matters indirectly
    pairs = list(combinations(values, 2))
    valid_pairs = [p for p in pairs if (p[0] + p[1]) % 3 == 0]
    return len(valid_pairs)

def evaluate_risk(level, threshold=15):
    risk_factor = 0
    if level > threshold:
        risk_factor += level * 0.3
    else:
        risk_factor += level * 0.1
    # Extra logic that doesn't impact final path
    adjustment = 0
    for i in range(3):
        adjustment += (level + i) % 4
    return int(risk_factor)

def evaluate_performance(output, risk):
    base = sum(output) // len(output)
    penalty = risk * 2
    bonus = 0
    
    # Conditional bonus based on pattern in output
    mod_counts = {i: 0 for i in range(3)}
    for val in output:
        mod_counts[val % 3] += 1
    
    if mod_counts[0] > mod_counts[1] and mod_counts[0] > mod_counts[2]:
        bonus += 10
    elif mod_counts[1] >= mod_counts[2]:
        bonus += 5

    # Dummy tracking with set operations
    tracked_values = set(output)
    complements = set(range(1, max(output)+1)) - tracked_values
    gap_count = len(complements)

    # Final score influenced only by base, penalty, bonus
    score_components = {
        'base': base,
        'penalty': penalty,
        'bonus': bonus
    }
    
    result = score_components['base'] - score_components['penalty'] + score_components['bonus']
    
    # Dead code branch - never executed but adds distraction
    if False:
        fallback = compute_baseline(output)
        result = max(result, fallback)
        
    return result

# Main execution flow
raw_metrics = [8, 7, 9, 6, 10, 7, 8]
daily_logs = [101, 203, 101, 405, 506]

# Step 1: Efficiency analysis
productivity = analyze_efficiency(raw_metrics)

# Step 2: Historical tracking (set operation)
recent_events = track_history(daily_logs)

# Step 3: Risk assessment
exposure_level = generate_pairs([3, 6, 9, 12, 15])
risk_assessment = evaluate_risk(exposure_level)

# Step 4: Performance evaluation
final_score = evaluate_performance(productivity, risk_assessment)

# Print result as required
print(f"Target result: {final_score}")