import itertools

def calculate_base_score(activities):
    return sum(hash(str(act)) % 100 for act in activities)

def process_security_logs(log_entries):
    base_scores = []
    for entry in log_entries:
        activities = entry['activities']
        is_suspicious = entry['is_suspicious']
        base_score = calculate_base_score(activities)
        adjusted_score = base_score << 1 if is_suspicious else base_score >> 1
        base_scores.append(adjusted_score)
    
    # Combine scores using combinatorial analysis
    combined_score = 0
    for combo in itertools.combinations(base_scores, 2):
        combo_sum = sum(combo)
        combined_score += combo_sum if combo_sum > 100 else combo_sum * 2
    
    return combined_score

def main():
    # Security log entries
    logs = [
        {'activities': ['login', 'file_access'], 'is_suspicious': True},
        {'activities': ['network_scan'], 'is_suspicious': False},
        {'activities': ['data_transfer', 'privilege_escalation'], 'is_suspicious': True}
    ]
    
    # Process logs to get intermediate score
    threat_level = process_security_logs(logs)
    
    # Apply final adjustments based on thresholds
    severity_threshold = 500
    final_threat_score = threat_level if threat_level > severity_threshold else threat_level + 200
    
    # Additional adjustment using set operations
    high_risk_patterns = {300, 450, 600}
    is_high_risk = threat_level in high_risk_patterns
    final_threat_score = final_threat_score * 2 if is_high_risk else final_threat_score
    
    print(f"Result: {final_threat_score}")

if __name__ == "__main__":
    main()