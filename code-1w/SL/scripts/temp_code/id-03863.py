def preprocess_readings(raw_values):
    processed = []
    for val in raw_values:
        if val < 0:
            val = abs(val)
        rounded = round(val + 0.05, 1)
        processed.append(rounded)
    return processed

# Irrelevant sensor calibration data (distractor)
calibration_offsets = [0.12, -0.08, 0.31, 0.0, 0.19]
system_gain = 1.04
temp_buffer = [x * system_gain for x in calibration_offsets]

# Real health sensor inputs
raw_vital_readings = [36.4, 37.1, 38.2, 39.5, 37.0, 36.8, 38.9]

# Misleading normalization function (dead path)
def normalize_readings(data):
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val, 3) for x in data]

# String-based symptom encoding (relevance: case conversion & string methods)
symptom_tags = ['FEVER', 'cough', 'HEADACHE', 'fatigue']
encoded_symptoms = []
for tag in symptom_tags:
    if len(tag) > 4:
        encoded_symptoms.append(tag.lower().replace('e', '3').title())
    else:
        encoded_symptoms.append(tag.upper())

# Auxiliary diagnostic thresholds (partially relevant)
thresholds = {
    'mild': (37.0, 38.0),
    'moderate': (38.0, 39.0),
    'severe': (39.0, 41.0)
}

# Decoy scoring system (irrelevant computation)
score_weights = {'FEVER': 3, 'cough': 1, 'HEADACHE': 2, 'fatigue': 1}
decoy_score = 0
for symptom, weight in score_weights.items():
    if any(symptom.lower() in t.lower() for t in symptom_tags):
        decoy_score += weight * 1.5

# Actual analysis logic
def count_in_range(data, low, high):
    return len([x for x in data if low <= x < high])

def analyze_symptoms(vitals):
    # Step 1: Preprocess raw input
    readings = preprocess_readings(vitals)
    
    # Step 2: Compute severity levels
    mild_count = count_in_range(readings, 37.0, 38.0)
    moderate_count = count_in_range(readings, 38.0, 39.0)
    severe_count = count_in_range(readings, 39.0, 41.0)
    
    # Step 3: Derive base risk from counts
    base_risk = mild_count * 10 + moderate_count * 25 + severe_count * 40
    
    # Step 4: Adjust based on string-derived flags
    has_fever = any('fever' in s.lower() for s in encoded_symptoms)
    has_severe_tag = any(len(s) > 7 for s in encoded_symptoms)
    
    # Step 5: Apply conditional modifiers
    adjustment = 0
    if has_fever and severe_count > 0:
        adjustment += 12
    if has_severe_tag:
        adjustment += 5
    
    # Step 6: Combine into diagnostic index
    diagnostic_index = base_risk + adjustment
    
    # Step 7: Apply non-linear transformation
    if diagnostic_index > 50:
        diagnostic_index = int(diagnostic_index * 1.3)
    
    # Step 8: Final clamping and offset
    final_value = diagnostic_index - 17
    
    return final_value

# Execute main logic
health_data = raw_vital_readings
final_diagnostic = analyze_symptoms(health_data)

# Output result
print(f"Result: {final_diagnostic}")