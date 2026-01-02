def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        words = text.lower().split()
        score = sum(1 for w in words if w in ['good', 'excellent', 'great'])
        score -= sum(1 for w in words if w in ['bad', 'poor', 'terrible'])
        sentiment_scores.append(max(-2, min(2, score)))
    return sentiment_scores

# Simulate system feedback logs with mixed quality indicators
def generate_diagnostic_report(health_metrics):
    diagnostics = {}
    temp_flag = 0
    for metric, value in health_metrics.items():
        if value > 85:
            temp_flag += 1
        elif value < 30:
            temp_flag -= 1
    diagnostics['stress_level'] = temp_flag
    return diagnostics

# Core evaluation logic with distractors
def evaluate_performance(feedback, base):
    # Irrelevant preprocessing (distractor)
    processed = [f.strip().rstrip('?').capitalize() for f in feedback if len(f) > 5]
    
    # Real computation begins
    raw_scores = analyze_sentiment(processed)
    adjustment_factor = 0.85
    
    # Misleading normalization path (dead code)
    normalized = []
    for s in raw_scores:
        z = s / 2.0 if s != 0 else 0
        normalized.append(round(z, 2))
    
    # Actual scoring uses unnormalized values
    total_impact = sum(abs(s) for s in raw_scores)
    positive_ratio = sum(1 for s in raw_scores if s > 0) / len(raw_scores) if raw_scores else 0
    
    # Baseline correction using dictionary lookup
    corrections = {'alpha': 1.1, 'beta': 0.95, 'gamma': 1.0}
    correction = corrections.get(base, 1.0)
    
    # Auxiliary state tracking (semi-relevant)
    audit_trail = []
    cumulative = 0
    for idx, s in enumerate(raw_scores):
        cumulative += s
        if idx % 2 == 0:
            audit_trail.append(cumulative * correction)
    
    # Final calculation
    stability_bonus = 10 if len(set(raw_scores)) < 3 else 5
    final_score = (total_impact * 5) + (positive_ratio * 100) + stability_bonus
    
    # Debug print that doesn't affect result
    debug_value = sum(audit_trail) / len(audit_trail) if audit_trail else 0
    
    return int(final_score)

# Setup inputs
feedback_entries = [
    "This is bad but recovered to great performance",
    "Poor results initially but excellent later",
    "Great improvement over time",
    "Good progress overall",
    "Excellent work done well"
]

system_health = {
    'cpu_load': 92,
    'memory_usage': 88,
    'disk_latency': 25,
    'network_jitter': 45
}

# Generate unused diagnostic (distractor call)
diag_report = generate_diagnostic_report(system_health)

baseline_version = 'gamma'

# Execute main logic
final_score = evaluate_performance(feedback_entries, baseline_version)

print(f"Result: {final_score}")