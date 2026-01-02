from collections import defaultdict, Counter
import math

# Simulated medical diagnostic system with noise and red herrings
def load_patient_metadata():
    return {
        'patient_id': 'P7890',
        'ward': 'ICU-East',
        'admission_year': 2023,
        'risk_score': 0.68
    }

def compute_thermal_index(readings):
    # Irrelevant function - not used in main logic
    return sum(r ** 1.1 for r in readings if r > 36.0) / len(readings)

def generate_placebo_mask(shape):
    # Dead code path - distractor
    mask = [[False] * shape[1] for _ in range(shape[0])]
    for i in range(shape[0]):
        for j in range(shape[1]):
            mask[i][j] = (i * j) % 3 == 0
    return mask

def filter_abnormal_values(data, limit):
    # Misleading intermediate: looks important but only used in decoy branch
    return [x for x in data if abs(x - 50) > limit]

def calculate_entropy(sequence):
    # Unused sophisticated computation - red herring
    freq = Counter(sequence)
    total = len(sequence)
    return -sum((count/total) * math.log2(count/total) for count in freq.values())

def validate_consistency(records):
    # Distractor function with complex logic but no impact
    seen = set()
    for r in records:
        if r['code'] in seen:
            return False
        if r['timestamp'] % 7 == 0:
            seen.add(r['code'])
    return True

def accumulate_baseline_shift(vitals, factor=1.07):
    # Seemingly relevant transformation, never called
    shifted = []
    for v in vitals:
        adjusted = v * factor
n        if adjusted > 100:
            adjusted = 100 + math.log(adjusted - 100 + 1)
        shifted.append(round(adjusted, 3))
    return shifted

def extract_critical_flags(logs):
    # Another unused complex analysis
    flags = defaultdict(int)
    for entry in logs:
        if 'CRITICAL' in entry.get('level', ''):
            flags[entry['node']] += 1
    return dict(flags)

def preprocess_diagnostics(raw):
    # Legitimate preprocessing step
    cleaned = [x for x in raw if isinstance(x, (int, float)) and x != 999]
    return [x for x in cleaned if 20 <= x <= 120]

def apply_calibration(signal, offset=2.1):
    # Relevant but indirectly used via reference
    return [s + offset for s in signal]

def assess_trend_pattern(values):
    # Real logic component: detects monotonic segments
    if len(values) < 3:
        return 0
    trends = []
    for i in range(1, len(values)):
        trends.append(1 if values[i] > values[i-1] else (-1 if values[i] < values[i-1] else 0))
    
    stable_periods = 0
    for i in range(len(trends)-1):
        if trends[i] == trends[i+1]:
            stable_periods += 1
    
    return stable_periods

def compute_diagnostic_weight(scores, method='quadratic'):
    # Used in final calculation
    if method == 'quadratic':
        return sum(s**2 for s in scores) / len(scores)
    return sum(abs(s) for s in scores)

def analyze_patient_data(diagnostics, thresholds):
    # Core function with key logic buried in noise
    
    # Step 1: Preprocess raw diagnostics
    processed = preprocess_diagnostics(diagnostics)
    
    # Step 2: Apply sensor calibration (relevant)
    calibrated = apply_calibration(processed, offset=1.8)
    
    # Step 3: Filter based on dynamic threshold (uses input)
    dynamic_limit = thresholds.get('upper_bound', 95) - 12
    filtered = [c for c in calibrated if c <= dynamic_limit]
    
    # Step 4: Detect trend stability (real contribution)
    stability_score = assess_trend_pattern(filtered)
    
    # Step 5: Compute weighted metric
    weight_method = 'quadratic'
    base_weight = compute_diagnostic_weight(filtered, weight_method)
    
    # Step 6: Adjust using stability
    adjusted_metric = base_weight * (1 + stability_score * 0.03)
    
    # Step 7: Final nonlinear transformation
    if adjusted_metric > 70:
        final_score = math.log(adjusted_metric) * 8.5
    else:
        final_score = adjusted_metric * 1.2
    
    # IRRELEVANT POST-PROCESSING BLOCK (distractor)
    summary_stats = {}
    summary_stats['max_raw'] = max(diagnostics) if diagnostics else 0
    summary_stats['unique_count'] = len(set(diagnostics))
    summary_stats['mode'] = Counter(diagnostics).most_common(1)[0][0]
    summary_stats['range'] = max(diagnostics) - min(diagnostics)
    
    # UNUSED BRANCH BASED ON MEDICAL CODES (red herring)
    icd_codes = ['E11.9', 'I10', 'J44.9', 'Z79.02']
    chronic_burden = 0
    for code in icd_codes:
        if code.startswith('E') or code.startswith('I'):
            chronic_burden += 1
    
    # CRITICAL ASSIGNMENT - THE ANSWER VARIABLE
    final_diagnostic = int(round(final_score + chronic_burden * 0.5))
    
    # More noise: fake validation chain
    metadata = load_patient_metadata()
    if metadata['risk_score'] > 0.5:
        final_diagnostic += 1  # This would matter, but risk_score is 0.68 → triggers!
    
    # BUT WAIT: override based on hidden rule
    admission_tag = metadata['ward'][4:]  # 'East'
    if 't' in admission_tag:
        final_diagnostic -= 1  # cancels the previous +1
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data
    diagnostics = [88, 92, 76, 81, 85, 79, 83, 91, 999, 'N/A', 87, 89, 80, 78, 84]
    thresholds = {
        'lower_bound': 30,
        'upper_bound': 107,
        'criticality': 'moderate'
    }
    
    # Call target function
    final_diagnostic = analyze_patient_data(diagnostics, thresholds)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")