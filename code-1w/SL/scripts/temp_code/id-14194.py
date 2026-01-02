def analyze_symptoms(symptoms):
    # Irrelevant transformation (distractor)
    symptom_keys = set([s.upper() for s in symptoms])
    encoded = ''.join([str(len(s) % 3) for s in sorted(symptom_keys)])
    
    # Real logic buried within distractions
    severity_score = 0
    for s in symptoms:
        if 'fever' in s:
            severity_score += 3
        elif 'cough' in s:
            severity_score += 2
        elif 'fatigue' in s:
            severity_score += 1
    
    # Dead code path (misleading)
    if len(encoded) > 10:
        return -1
    
    return severity_score

# Unused function (red herring)
def compute_vital_index(vitals):
    return sum(vitals.values()) // len(vitals)

# Another decoy: complex but unused bitwise analysis
def assess_stability(pressure, oxygen):
    status = (pressure ^ oxygen) & 0xFF
    return format(status, '08b').count('1')

# Core data processing chain
thresholds = {
    'temp': 37.5,
    'hrv': 50,
    'resp': 20
}

health_data = {
    'vitals': {
        'temp': 38.2,
        'pulse': 98,
        'resp': 22,
        'hrv': 45
    },
    'symptoms': ['persistent fever', 'dry cough', 'muscle fatigue'],
    'readings': [0b1101, 0b1010, 0b1111],
    'history_days': 7
}

# Distractor: elaborate bit manipulation with no effect on final result
data_flags = 0
for r in health_data['readings']:
    data_flags ^= r
    data_flags = (data_flags << 1) & 0xF

# Fake risk calculation (unused but plausible)
risk_profile = list(map(lambda x: x * 1.5 if x < 30 else x * 0.8, 
                         [health_data['vitals']['temp'], health_data['vitals']['resp']]))

# String-based decoy analysis
temp_str = str(health_data['vitals']['temp'])
decimal_digits = temp_str.split('.')[1]
counter_metric = len(decimal_digits) + temp_str.count('8')

# Real signal extraction buried in noise
def extract_fever_component(temp_val):
    return int((temp_val - 37) * 10)

# Central processing function
def process_metrics(data, limits):
    # Step 1: Extract temperature deviation
    temp_excess = extract_fever_component(data['vitals']['temp'])
    
    # Step 2: Analyze symptom severity (key contributor)
    symptom_weight = analyze_symptoms(data['symptoms'])
    
    # Step 3: Check threshold crossings (only two matter)
    threshold_breaches = 0
    if data['vitals']['temp'] > limits['temp']:
        threshold_breaches += 1
    if data['vitals']['resp'] > limits['resp']:
        threshold_breaches += 1
    if data['vitals']['hrv'] < limits['hrv']:  # This one is also relevant
        threshold_breaches += 1
    
    # Step 4: Combine with irrelevant bit score (but masked out)
    bit_influence = data_flags & 0x0  # Neutralized on purpose
    
    # Step 5: Apply conditional multiplier
    multiplier = 2 if threshold_breaches >= 2 else 1
    
    # Step 6: Final composition
    base_score = temp_excess + symptom_weight + threshold_breaches
    enhanced_score = base_score * multiplier
    
    # Step 7: Offset by history (real adjustment)
    adjusted = enhanced_score - (data['history_days'] // 7)  # Only full weeks
    
    # Step 8: Final diagnostic output (this is the answer)
    final_diagnostic = max(adjusted, 5)  # Floor at 5
    
    # Misleading print statements (commented out, dead paths)
    # debug_status = assess_stability(120, 94)
    # if debug_status > 5: return -999
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")