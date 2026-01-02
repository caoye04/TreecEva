def analyze_text_patterns(text_data, keywords):
    if not text_data.strip():
        return 0
    words = text_data.lower().split()
    keyword_count = sum(1 for word in words if word in keywords)
    redundancy_factor = len(words) / (len(set(words)) + 1e-8)
    diversity_score = len(set(word[:3] for word in words))
    return (keyword_count * 2.5) / redundancy_factor + diversity_score * 0.7


def validate_stability(metric, threshold=6.0):
    return "stable" if metric > threshold else "fluctuating"


def generate_diagnostics(data):
    diagnostics = {}
    for i, item in enumerate(data):
        temp_metric = sum(ord(c) for c in item) % 100
        status = "valid" if temp_metric < 80 else "review"
        diagnostics[f"entry_{i}"] = {"metric": temp_metric, "status": status}
    return diagnostics

def filter_relevant_entries(logs, min_length=4):
    filtered = []
    for entry in logs:
        cleaned = ''.join(ch for ch in entry if ch.isalnum() or ch.isspace())
        if len(cleaned.split()) >= min_length:
            filtered.append(cleaned)
    return filtered

def compute_sentiment_bias(text_list):
    total_bias = 0
    for t in text_list:
        positive_triggers = sum(t.count(p) for p in ['good', 'excellent', 'great'])
        negative_triggers = sum(t.count(n) for n in ['bad', 'poor', 'terrible'])
        total_bias += (positive_triggers - negative_triggers) * 1.5
    return round(total_bias, 3)

def evaluate_performance(log_entries, reference_terms):
    processed_entries = [entry.upper().replace('.', '') for entry in log_entries]
    
    # Irrelevant transformation chain (distractor)
    transformed_data = []
    for entry in processed_entries:
        shifted = ''.join(chr((ord(c) - 65 + 3) % 26 + 65) if c.isalpha() else c for c in entry)
        transformed_data.append(shifted)
    
    # Decoy analysis path (dead code - never used)
    decoy_scores = []
    for item in transformed_data:
        score = 0
        for i, c in enumerate(item):
            if c in 'AEIOU':
                score += (i + 1) * 1.1
        decoy_scores.append(score)
    
    # Real processing begins here
    clean_logs = filter_relevant_entries(log_entries)
    base_analysis = sum(analyze_text_patterns(entry, reference_terms) for entry in clean_logs)
    
    # Secondary scoring (partially relevant but misleading)
    sentiment_drift = compute_sentiment_bias(log_entries)  # Used only in decoy context
    adjustment_factor = 1.0
    if sentiment_drift > 5:
        adjustment_factor = 0.9
    elif sentiment_drift < -5:
        adjustment_factor = 1.1
    
    # Key logic: combinatoric weight based on character frequency
    all_chars = ''.join(clean_logs).lower()
    consonant_weight = sum(1 for c in all_chars if c in 'bcdfghjklmnpqrstvwxyz')
    vowel_sequence_bonus = sum(1 for i in range(len(all_chars)-2) 
                                if all_chars[i:i+3] in ['eee', 'ooo', 'aaa'])
    
    # Core formula
    raw_score = base_analysis * adjustment_factor
    penalty = consonant_weight * 0.05 - vowel_sequence_bonus * 2
    final_raw = raw_score - penalty
    
    # Conditional override (never triggers due to logic, red herring)
    feedback_type = "detailed" if any('feedback' in e.lower() for e in log_entries) else "basic"
    if feedback_type == "comprehensive":  # Impossible condition
        final_raw *= 1.2
    
    # Final assignment - KEY STATEMENT
    final_score = int(round(final_raw + 17.3, 0))
    
    # Distractor variables (no impact)
    stability_check = validate_stability(final_raw / 10)
    diagnostic_report = generate_diagnostics(transformed_data)
    anomaly_count = sum(1 for v in diagnostic_report.values() if v["status"] == "review")
    
    return final_score

# Input data
feedback_log = [
    "User feedback indicates excellent responsiveness and great interface design.",
    "The system performance is good, although some features feel redundant.",
    "Poor error handling was observed during testing phase.",
    "Excellent speed, great optimization, and amazing user experience.",
    "No issues detected in this feedback entry at all."
]

target_words = {"excellent", "great", "good", "poor", "bad", "terrible"}

# Execute main function
core_metric = analyze_text_patterns(feedback_log[0], target_words)
diag_output = generate_diagnostics(feedback_log)
sentiment_index = compute_sentiment_bias(feedback_log)

# Critical execution point
final_score = evaluate_performance(feedback_log, target_words)

print(f"Result: {final_score}")