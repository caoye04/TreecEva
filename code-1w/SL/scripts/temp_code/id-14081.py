def process_biomarkers(data, threshold=0.75):
    filtered = {k: v for k, v in data.items() if v > threshold}
    normalized = {k: round(v / sum(filtered.values()), 4) for k in filtered}
    return normalized


def compute_thermal_index(readings):
    index = 0
    for r in readings:
        index += (r ** 2) / (readings.index(r) + 1)
    return int(index % 100)

# Irrelevant sensor calibration function (dead code path)
def calibrate_sensor(signal):
    base = 1.0
    for i in range(8):
        base *= 0.98
    return base * signal

# Unused auxiliary transformation
def transform_sequence(seq):
    return [seq[i] ^ seq[(i+1)%len(seq)] for i in range(len(seq))]

# Misleading diagnostic with decoy logic
def false_diagnosis(scores):
    total = sum(scores)
    penalty = 0
    for s in scores:
        if s < 50:
            penalty += 10
    adjusted = total - penalty
    return adjusted // 3

# Core logic disguised among distractors
def evaluate_progression(state_log):
    stages = set(state_log)
    progression_score = 0
    
    # Distractor: irrelevant phase mapping
    phase_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    temp_sum = 0
    for s in phases:
        temp_sum += phase_map.get(s, 0)
    
    # Actual relevant logic
    if 'critical' in stages:
        progression_score += 40
    if 'stable' not in stages:
        progression_score += 30
    if len(stages) > 4:
        progression_score += 20
    
    return progression_score

# Main analysis with key set operations and distractions
def analyze_symptoms(active_markers, history):
    # Real input processing
    known_interactions = {'M1', 'M3', 'M7', 'M9', 'M11'}
    expressed = set(active_markers.keys())
    
    # Distractor variables
    buffer_cache = [0] * 128
    checksum = 0
    for b in buffer_cache:
        checksum ^= b
    
    # Red herring computation
    aggregate_risk = 0
    for marker, level in active_markers.items():
        if level > 0.9:
            aggregate_risk += 15
    
    # Key intersection determining outcome
    expressed_critical = expressed.intersection(known_interactions)
    severity_base = len(expressed_critical) * 17
    
    # Additional logic with decoy condition
    modifier = 1
    if 'prior_event' in history and history['prior_event'] == True:
        if 'M7' in expressed_critical:
            modifier = 1.5  # Only activates under precise condition
    
    intermediate = int(severity_base * modifier)
    
    # Another distraction: unused scoring array
    score_matrix = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            score_matrix[i][j] = (i * j) % 7
    
    # Final computation mixed with irrelevant print
    debug_flag = False
    if debug_flag:
        print(f"Debug: matrix sum = {sum(sum(row) for row in score_matrix)}")
    
    final_diagnostic = intermediate + 13
    return final_diagnostic

# Global decoy state
phases = ['A', 'B', 'C']

# Simulated patient data with misleading fields
biomarker_data = {
    'M1': 0.82,
    'M3': 0.91,
    'M5': 0.67,
    'M7': 0.93,
    'M9': 0.88,
    'M11': 0.54  # Below threshold but still counted in set
}

sensor_readings = [3.2, 4.1, 2.8, 5.5, 3.9]
patient_history = {
    'age': 67,
    'prior_event': True,
    'medications': ['A', 'B']
}

# Irrelevant preprocessing call
norm_data = process_biomarkers(biomarker_data, 0.70)

# Distraction: thermal index has no effect
thermal_index = compute_thermal_index(sensor_readings)

# Decoy function call with unused result
phantom_scores = [45, 52, 61, 48]
decoy_result = false_diagnosis(phantom_scores)

# State log for progression (partially relevant)
episode_log = ['initial', 'acute', 'critical', 'recovery', 'followup']
progression_value = evaluate_progression(episode_log)

# Critical execution point — this is where the answer is determined
final_diagnostic = analyze_symptoms(biomarker_data, patient_history)

# Output must be printed exactly once
print(f"Result: {final_diagnostic}")