def evaluate_performance(output_rate, defect_count, minimum_threshold):
    base_score = output_rate * 10
    penalty = defect_count * 5
    
    # Irrelevant distraction: historical data analysis (not used)
    historical_avg = 87.3
    fluctuation_index = abs(historical_avg - base_score) / historical_avg
    adjusted_fluctuation = fluctuation_index * 100 if fluctuation_index > 0.1 else 0
    
    # Real logic begins
    efficiency_ratio = output_rate / (defect_count + 1)
    bonus = 20 if efficiency_ratio >= 8 else 10 if efficiency_ratio >= 5 else 0
    
    # Conditional expression for quality tier
    quality_tier = 'High' if defect_count < 3 else 'Medium' if defect_count < 7 else 'Low'
    
    # String-based flag encoding (distraction)
    status_flag = f"PROD:{output_rate}-ERR:{defect_count}"
    encoded_diagnostic = status_flag.replace(':', '_').upper()
    diagnostic_length = len(encoded_diagnostic)
    
    # Core scoring logic
    raw_score = base_score - penalty + bonus
    
    # Threshold adjustment using comparison and logical operations
    meets_threshold = raw_score >= minimum_threshold
    final_score = raw_score + 15 if meets_threshold and quality_tier == 'High' else raw_score
    
    # Dead code path - never executed due to fixed condition
    if len(status_flag) < 0:  # Impossible condition
        final_score *= 1.1
    
    return final_score

# Main execution
productivity = 12
errors = 2
threshold = 95

interim_diagnosis = "Stable operation with minor defects"
diag_words = interim_diagnosis.split(' ')
word_count = len([w for w in diag_words if len(w) > 4])

# Additional irrelevant computation
checksum = sum(ord(c) for c in interim_diagnosis[:10]) % 7

final_score = evaluate_performance(productivity, errors, threshold)
print(f"Result: {final_score}")