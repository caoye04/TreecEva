import itertools

def analyze_readings(readings):
    # Irrelevant transformation: frequency analysis (dead-end)
    freq = {k: len(list(g)) for k, g in itertools.groupby(sorted(readings))}
    normalized = [x / max(readings) for x in readings if x > 0]
    return [x * 100 for x in normalized]

def compute_entropy(data):
    # Misleading function: looks important but unused in final path
    from math import log
    total = sum(data)
    probs = [v / total for v in data]
    return -sum(p * log(p) for p in probs if p > 0)

def filter_outliers(seq, factor=1.5):
    # Distractor: used on irrelevant data
    if len(seq) < 3:
        return seq
    sorted_seq = sorted(seq)
    q1, q3 = sorted_seq[len(seq)//4], sorted_seq[3*len(seq)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in seq if lower <= x <= upper]

def derive_significance(values, weights):
    # Red herring: complex logic that doesn't affect final result
    weighted = [v * w for v, w in zip(values, weights)]
    base_score = sum(weighted) / len(weighted)
    adjustment = 0
    for i, w in enumerate(weights):
        if w > 0.7:
            adjustment += 0.1
    return base_score * (1 + adjustment)

def process_metrics(indicators, thresholds):
    # Core relevant logic starts here
    primary_keys = ['temp', 'pulse', 'resp']
    temp_val = indicators['temp']
    pulse_val = indicators['pulse']
    resp_val = indicators['resp']
    
    # Intermediate diagnostic flags (some used, some not)
    fever = temp_val > thresholds['temp_high']
    bradycardia = pulse_val < thresholds['pulse_low']  
    tachypnea = resp_val > thresholds['resp_high']
    
    # Real computation path
    score_components = []
    if fever:
        score_components.append(30)
    if bradycardia:
        score_components.append(25)
    if tachypnea:
        score_components.append(20)
    
    # Additional condition based on combined state
    if fever and bradycardia:
        score_components.append(15)
    
    base_score = sum(score_components)
    
    # Modifier based on secondary indicator (unused in distractors)
    o2_sat = indicators.get('o2', 98)  # Default high
    hypoxia = o2_sat < thresholds['o2_low']
    if hypoxia:
        base_score += 10
    
    # Final nonlinear transformation
    modifier = 1.0
    if base_score >= 50:
        modifier = 1.4
    elif base_score >= 30:
        modifier = 1.2
    
    adjusted_score = base_score * modifier
    
    # This is the actual answer variable
    final_diagnostic = int(round(adjusted_score))
    
    return final_diagnostic

# --- Main execution block ---

# Irrelevant dataset initialization (distractor)
raw_readings = [36.8, 37.2, 37.0, 38.1, 37.8, 39.5, 36.9]
analyzed = analyze_readings(raw_readings)
entropy = compute_entropy([50, 30, 20])

# Another red herring list
vital_weights = {'temp': 0.9, 'pulse': 0.75, 'resp': 0.8}
sig_values = [0.4, 0.6, 0.55]

# Outlier filtering on fake data
noisy_data = [10, 12, 11, 15, 100, 13, 14]
cleaned = filter_outliers(noisy_data)

# Used significance derivation (but on irrelevant inputs)
dummy_sig = derive_significance(sig_values, list(vital_weights.values()))

# Core data structures involved in real computation
health_indicators = {
    'temp': 38.3,
    'pulse': 54,
    'resp': 22,
    'o2': 94  # Slightly low, but not critical
}

threshold_map = {
    'temp_high': 38.0,
    'pulse_low': 60,
    'resp_high': 20,
    'o2_low': 92
}

# Key statement: this determines the answer
final_diagnostic = process_metrics(health_indicators, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")