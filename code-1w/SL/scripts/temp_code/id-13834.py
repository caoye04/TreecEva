def preprocess_vitals(vital_signs):
    # Irrelevant transformation: converts temperature from C to F (not used in final logic)
    temp_f = [v[0] * 9/5 + 32 for v in vital_signs]
    heart_rate_zones = ["low" if hr[1] < 60 else "high" for hr in vital_signs]
    return temp_f  # Dead end: this return value is never used meaningfully


def calculate_bmi(height_cm, weight_kg):
    # Distractor function: BMI is calculated but not used in diagnosis
    bmi_values = []
    for h, w in zip(height_cm, weight_kg):
        meters = h / 100
        bmi = w / (meters ** 2)
        bmi_values.append(round(bmi, 2))
    return bmi_values


def evaluate_stress_index(readings):
    # Complex but irrelevant computation: simulates stress analysis
    stress_scores = []
    for r in readings:
        score = 0
        for i, val in enumerate(r):
            if i % 2 == 0:
                score += val ** 0.5
            else:
                score -= val // 3
        stress_scores.append(abs(score))
    return stress_scores  # Never used in main flow


def filter_abnormal_entries(data, limit=75):
    # Misleading filtering: looks important but doesn't affect outcome
    filtered = []
    for record in data:
        if sum(record) / len(record) > limit:
            filtered.append(record)
    return filtered  # Unused in actual diagnostic path


def count_alphanumeric_chars(text_blocks):
    # Character counting distractor
    counts = {}
    for block in text_blocks:
        alpha = sum(1 for c in block if c.isalpha())
        num = sum(1 for c in block if c.isdigit())
        counts[block] = (alpha, num)
    return counts


def analyze_symptoms(vital_data, thresholds):
    # Core logic buried in distractions
    
    # Step 1: Extract respiratory rate (index 2) and oxygen saturation (index 3)
    resp_rates = [entry[2] for entry in vital_data]
    o2_levels = [entry[3] for entry in vital_data]
    
    # Step 2: Compute average respiratory rate
    avg_resp = sum(resp_rates) / len(resp_rates)
    
    # Step 3: Count how many times O2 < threshold
    o2_threshold = thresholds['oxygen']
    low_o2_count = sum(1 for level in o2_levels if level < o2_threshold)
    
    # Step 4: Determine severity based on combination
    if avg_resp > 20 and low_o2_count >= 2:
        severity_code = 3
    elif avg_resp > 18 or low_o2_count >= 1:
        severity_code = 2
    else:
        severity_code = 1
    
    # Step 5: Apply bitmask simulation for 'diagnostic confidence'
    confidence = (severity_code << 2) | low_o2_count
    
    # Step 6: Use logical operations to adjust for age factor (embedded in data index 4)
    ages = [entry[4] for entry in vital_data]
    elderly_present = any(age >= 65 for age in ages)
    comorbidity_flag = thresholds['comorbidity']
    
    # Step 7: Final adjustment using boolean logic and bit check
    if elderly_present and comorbidity_flag:
        adjusted_confidence = confidence | 8
    else:
        adjusted_confidence = confidence & ~8  # Clear bit if not met
    
    # Step 8: Final diagnostic code computed via mixed arithmetic and logic
    base_score = adjusted_confidence * 100
    penalty = 0
    if avg_resp > 22:
        penalty += 25
    if low_o2_count >= 3:
        penalty += 50
    
    final_diagnostic = base_score - penalty
    
    return final_diagnostic

# Main execution context
if __name__ == "__main__":
    
    # Simulated patient data: each row = [temp_c, hr, resp_rate, o2_sat, age]
    patient_data = [
        [36.8, 72, 18, 96, 45],
        [37.1, 76, 21, 92, 68],
        [37.5, 80, 23, 89, 70],
        [36.9, 74, 19, 95, 50]
    ]
    
    # Threshold configuration (only 'oxygen' and 'comorbidity' are actually used)
    thresholds = {
        'oxygen': 93,
        'heart_rate': 100,           # Unused
        'fever': 38.0,              # Unused
        'comorbidity': True
    }
    
    # Irrelevant preprocessing steps (distractors)
    _ = preprocess_vitals(patient_data)
    _ = calculate_bmi([170, 165, 172, 160], [70, 75, 80, 68])
    _ = evaluate_stress_index([[50, 60], [70, 80], [55, 65], [72, 88]])
    _ = filter_abnormal_entries(patient_data)
    _ = count_alphanumeric_chars(["vitals_001", "vitals_002"])
    
    # Key execution point
    final_diagnostic = analyze_symptoms(patient_data, thresholds)
    
    # Output result
    print(f"Target result: {final_diagnostic}")