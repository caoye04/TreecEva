from itertools import combinations

# Simulate employee performance metrics across departments
def analyze_department_metrics(base_values, threshold=0.75):
    normalized = [val / max(base_values) for val in base_values]
    filtered = [val for val in normalized if val >= threshold]
    return len(filtered)

# Calculate team synergy score based on pairwise compatibility
def compute_synergy(scores):
    pairs = list(combinations(scores, 2))
    total_compatibility = 0
    for a, b in pairs:
        total_compatibility += (a * b) / (abs(a - b) + 1)
    return round(total_compatibility, 3)

# Assess individual productivity with distraction factors
def assess_productivity(logs, noise_level=0.1):
    raw_total = sum([len(log) * (1 + noise_level) for log in logs])
    adjustment_factor = 0.9 if len(logs) > 5 else 1.1
    return int(raw_total * adjustment_factor)

# Evaluate overall performance combining multiple factors
def evaluate_performance(p, r):
    stress_index = (p * 0.01) + r
    bonus_eligibility = stress_index < 2.0
    base_score = p * (1.5 if bonus_eligibility else 0.8)
    penalty = 10 if r > 1.2 else 0
    # Additional irrelevant tracking
    audit_trail = []
    for i in range(3):
        audit_trail.append(f"check_{i}: passed")
    final_score = int(base_score - penalty)
    return final_score

# Irrelevant helper function (dead code path)
def unused_data_cleaner(data):
    cleaned = [x.strip().lower() for x in data if x]
    return sorted(set(cleaned), reverse=True)

# Main execution context
if __name__ == "__main__":
    # Real input data
    activity_logs = ["task1", "task2", "task3", "task4", "task5", "task6"]
    productivity = assess_productivity(activity_logs)
    
    # Dummy metrics for distraction
    department_data = [85, 90, 78, 92, 88, 76, 95]
    high_performers = analyze_department_metrics(department_data)
    
    # Unused structure (distractor)
    metadata_map = {
        "version": "2.1",
        "schema": "performance_v3",
        "active": False
    }
    
    # Synergy calculation (semi-relevant but not used in final score)
    skill_scores = [0.8, 0.7, 0.9, 0.6]
    synergy_score = compute_synergy(skill_scores)
    
    # Key control flow with state tracking
    risk_factor = 0.0
    if productivity > 50:
        risk_factor += 0.8
        if high_performers >= 3:
            risk_factor += 0.5
        else:
            risk_factor += 0.2
    else:
        risk_factor += 1.5
    
    # Red herring computation
    temp_result = (synergy_score * 100) // 1
    buffer_array = [0] * 5
    for idx in range(len(buffer_array)):
        buffer_array[idx] = temp_result % (idx + 1) if idx > 0 else 0
    
    # Critical statement
    final_score = evaluate_performance(productivity, risk_factor)
    
    # Output result as required
    print(f"Result: {final_score}")