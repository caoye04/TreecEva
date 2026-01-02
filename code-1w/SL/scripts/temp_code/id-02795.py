from collections import defaultdict

# Simulate employee performance analytics with noise and distractors
def analyze_productivity(log_entries):
    counts = defaultdict(int)
    for entry in log_entries:
        action = entry.split('_')[0]
        counts[action] += 1

    # Distractor: irrelevant aggregation
    total_chars = sum(len(e) for e in log_entries)
    avg_len = total_chars / len(log_entries) if log_entries else 0

    high_value_tasks = counts.get('complete', 0) + counts.get('approve', 0)
    low_value_tasks = counts.get('view', 0) + counts.get('edit', 0)

    # Real signal: productivity score
    productivity = high_value_tasks - 0.3 * low_value_tasks

    # Distractor: unused helper calculation
    def compute_entropy(data):
        from math import log
        if not data:
            return 0
        total = sum(data.values())
        entropy = 0
        for v in data.values():
            p = v / total
            if p > 0:
                entropy -= p * log(p, 2)
        return round(entropy, 3)
    
    entropy_score = compute_entropy(counts)  # Not used later

    return productivity

# Risk assessment module (some parts are relevant)
def assess_risk(access_logs, threshold=5):
    suspicious_count = 0
    temporal_gaps = []
    last_time = 0

    for log in access_logs:
        if 'admin' in log:
            current_time = int(log[-6:-4])  # Simulated timestamp
            if current_time - last_time < 2:
                suspicious_count += 1
            temporal_gaps.append(current_time - last_time)
            last_time = current_time

    # Distractor: complex but unused stats
    if temporal_gaps:
        mean_gap = sum(temporal_gaps) / len(temporal_gaps)
        variance = sum((x - mean_gap) ** 2 for x in temporal_gaps) / len(temporal_gaps)
        std_dev = variance ** 0.5
    else:
        mean_gap = 0
        std_dev = 0

    # Relevant logic: risk increases with suspicion
    base_risk = suspicious_count * 1.7
    adjusted_risk = base_risk + (std_dev * 0.1)  # Minor influence

    # Dead code path (never executed due to structure)
    if False:
        adjusted_risk *= 1.5  # Red herring

    return adjusted_risk

# Final evaluation combining multiple factors
def evaluate_performance(prod, risk):
    # Normalize inputs
    normalized_prod = max(0, prod)  # Floor at 0

    # Core formula: performance degrades with risk
    score = normalized_prod * (10 - min(8, risk))

    # Distractor: string-based weight adjustment (not actually affecting result)
    weights = {'low': 1.0, 'med': 0.7, 'high': 0.3}
    risk_label = 'high' if risk > 6 else 'med' if risk > 3 else 'low'
    temp_adjustment = str(weights[risk_label]).count('.')  # Always 1, irrelevant

    # Final nonlinear boost (only applies if score > 5)
    if score > 5:
        score = score * 0.9 + 3  # Diminishing returns + bump

    return int(round(score))

# Simulated input data
log_data = [
    'complete_task_01', 'view_report', 'approve_submission', 'edit_draft',
    'complete_task_02', 'view_dashboard', 'complete_task_03', 'approve_final'
]

access_events = [
    'user_login_0500', 'admin_access_0502', 'admin_access_0503',
    'user_logout_0505', 'admin_access_0510', 'admin_access_0511'
]

# Execute core logic chain
productivity = analyze_productivity(log_data)
risk_factor = assess_risk(access_events)
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Target result: {final_score}")