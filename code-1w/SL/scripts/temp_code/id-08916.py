def analyze_patient_data(biomarkers):
    base_score = sum(biomarkers)
    adjustment = len(biomarkers) if base_score > 20 else -len(biomarkers)
    return base_score + adjustment

biomarkers_list = [4, 7, 3, 6]
raw_score = analyze_patient_data(biomarkers_list)

age = 68
temperature = 37.1

# Determine dynamic threshold based on age and raw biomarker score
if age > 60:
    threshold_score = raw_score * 1.2 if temperature >= 37.0 else raw_score * 0.9
else:
    threshold_score = raw_score * 1.0

# Simulate early exit based on critical threshold
if threshold_score > 30:
    final_diagnosis = "High Risk"
    # Early break equivalent in function flow
else:
    threshold_score += 5
    final_diagnosis = "Moderate Risk"

final_diagnosis = determine_risk_level(age, threshold_score)

# Dummy function to prevent undefined reference (not affecting logic)
def determine_risk_level(age, score):
    return "High Risk" if score > 35 else "Low Risk"

print(f"Result: {threshold_score}")