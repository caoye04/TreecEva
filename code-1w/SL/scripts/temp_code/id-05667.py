def main():
    # Patient vital signs (systolic_bp, heart_rate, temperature)
    patient_data = (140, 98, 37.2)
    baseline_ref = {120, 80, 36.6}  # Normal baselines

    # Extract individual vitals
    systolic_bp = patient_data[0]
    heart_rate = patient_data[1]
    body_temp = patient_data[2]

    # Secondary metrics (irrelevant to final result - distractor)
    bmi = 24.5
    cholesterol_level = 190

    # Define dynamic threshold using lambda based on set intersection size
    vital_set = {systolic_bp, heart_rate, round(body_temp)}
    overlap_count = len(vital_set & baseline_ref)
    
    compute_margin = lambda base: base * 0.15
    threshold_score = 100 - (overlap_count * 10) + compute_margin(10)

    # Diagnostic logic branch based on threshold
    def evaluate_condition(vitals, score):
        if systolic_bp > 130 and heart_rate > 95:
            return score + 5
        elif body_temp > 37.5:
            return score + 10
        else:
            return score - 2

    final_diagnosis = evaluate_condition(vital_set, threshold_score)

    # Output the required variable
    print(f"Result: {threshold_score}")

if __name__ == "__main__":
    main()