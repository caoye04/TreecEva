def process_vital_signs(readings):
    filtered = [x for x in readings if x > 0]
    base_score = sum(filtered) // len(filtered) if filtered else 0
    
    # Irrelevant transformation (distractor)
    normalized = [round(x * 1.07 + 2.3, 1) for x in filtered]
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0

    # Unused function (dead code path)
    def adjust_for_age(value, age):
        return value * (0.95 if age > 60 else 1.05)

    # Misleading intermediate score
    temporal_index = (base_score * 0.3) + (avg_normalized * 0.7)

    return base_score


def evaluate_risk_level(biomarkers):
    risk_map = {'glucose': 0, 'creatinine': 0, 'bilirubin': 0}
    level_code = 0
    
    for marker, value in biomarkers.items():
        if marker == 'glucose' and value > 140:
            risk_map[marker] = 2
            level_code += 2
        elif marker == 'creatinine' and value > 1.5:
            risk_map[marker] = 3
            level_code += 3
        elif marker == 'bilirubin' and value > 2.0:
            risk_map[marker] = 1
            level_code += 1

    # Red herring: complex but unused scoring
    composite_risk = 0
    weights = {'glucose': 0.4, 'creatinine': 0.5, 'bilirubin': 0.3}
    for k, v in risk_map.items():
        composite_risk += v * weights[k]
    
    # This function actually just returns a simple sum (but not obvious)
    return level_code

# Simulate lab data ingestion (mostly irrelevant)
def ingest_lab_data(sample_ids):
    results = {}
    for sid in sample_ids:
        results[sid] = {
            'timestamp': '2023-12-01',
            'status': 'processed',
            'metrics': {'validity': 0.98, 'noise_floor': 0.02}
        }
    return results

# Core analysis logic with key set operations
def analyze_symptoms(active_set, log_history):
    baseline_patterns = {1, 2, 4, 8, 16}
    emergent_markers = {3, 5, 7, 9, 11}
    
    # Key computation
    overlapping_signals = active_set & emergent_markers
    novel_components = active_set - baseline_patterns
    
    # Distractor: unused signal propagation model
    propagated = set()
    for sig in overlapping_signals:
        for i in range(1, 4):
            propagated.add(sig * i)
    
    # Another red herring: time-based decay simulation
    decay_factor = 1.0
    for entry in log_history:
        if entry['time'] < 1000:
            decay_factor *= 0.9
    
    # Actual relevant logic (well hidden)
    severity_index = len(novel_components) * 5
    instability_score = len(overlapping_signals) * 3
    
    # Final result built from two key components
    final_score = severity_index + instability_score
    
    # Critical side calculation using modular arithmetic
    adjustment = (final_score * 7) % 13
    
    # The real answer comes from this combination
    final_diagnostic = final_score + adjustment
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Input vital signs (partially relevant)
    vitals = [-1, 88, 92, 0, 105, 110]
    score_1 = process_vital_signs(vitals)
    
    # Lab data ingestion (mostly distraction)
    samples = ['S001', 'S002']
    lab_data = ingest_lab_data(samples)
    
    # Biomarker evaluation (creates misleading intermediate)
    markers = {'glucose': 150, 'creatinine': 1.2, 'bilirubin': 3.1}
    risk_level = evaluate_risk_level(markers)
    
    # Build history log (used in actual logic)
    history_log = [
        {'event': 'onset', 'time': 500},
        {'event': 'treatment', 'time': 800},
        {'event': 'followup', 'time': 1200}
    ]
    
    # Critical set construction (key input)
    symptom_flare = {3, 4, 5, 10, 11, 13}
    
    # Execute target statement
    final_diagnostic = analyze_symptoms(symptom_flare, history_log)
    
    print(f"Target result: {final_diagnostic}")