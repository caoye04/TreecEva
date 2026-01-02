from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulate agricultural yield prediction with noise and red herrings
def generate_base_signals(years):
    signal_map = defaultdict(float)
    for y in years:
        signal_map[y] = (y % 13) * 0.7 + ((y * 2) % 11)
    return signal_map

def apply_seasonal_filter(data, mode='strict'):
    filtered = {}
    decoy_accum = 0
    temp_shift = [0.1, -0.2, 0.15, -0.05]
    
    for year, val in data.items():
        if year % 4 == 0 and mode == 'strict':
            # Leap year adjustment (irrelevant to final result)
            adjusted = val * 0.95
            decoy_accum += adjusted % 1
        else:
            adjusted = val * 1.05
        
        # Real transformation path
        if year > 1990:
            filtered[year] = round(adjusted + temp_shift[(year - 1991) % 4], 2)
        else:
            filtered[year] = adjusted
    
    # Dead code path — never used
    if decoy_accum > 100:
        fallback = {k: v * 0.8 for k, v in data.items()}
        return fallback

    return filtered

def compute_anomaly_score(data):
    # Complex but irrelevant scoring
    scores = []
    for a, b in combinations(data.values(), 2):
        diff = abs(a - b)
        if diff > 2.0:
            scores.append(diff * 0.3)
    return sum(scores) / len(scores) if scores else 0.0

def extract_growth_cycles(data):
    # Uses itertools.cycle for windowing (distractor)
    growth_trend = []    
    keys = sorted(data.keys())
    c = cycle([1, -1, 0])
    
    for i, k in enumerate(keys):
        trend_val = data[k] * next(c)
        growth_trend.append(abs(trend_val))  # Some obfuscation
    
    # This function returns unused list
    return growth_trend

def process_chlorophyll(readings):
    # Fake sensor processing
    processed = []
    for r in readings:
        if r < 0:
            continue
        processed.append(r ** 0.5 if r > 1 else r)
    return processed

def aggregate_by_decade(data):
    decade_bin = defaultdict(list)
    for year, val in data.items():
        decade = (year // 10) * 10
        decade_bin[decade].append(val)
    
    avg_by_decade = {d: sum(vals)/len(vals) for d, vals in decade_bin.items()}
    return avg_by_decade

def finalize_projection(values):
    proj = 0
    multiplier = 1.0
    for i, v in enumerate(sorted(values, reverse=True)):
        if i % 3 == 0:
            multiplier *= 1.1
        proj += v * multiplier
    return int(proj)  # deterministic scalar

def harvest_results(dataset):
    # Core calculation hidden among distractions
    base_sum = sum(v for v in dataset.values() if v > 2.5)
    count_eligible = len([v for v in dataset.values() if 1.5 <= v <= 4.0])
    penalty = 0
    
    # Irrelevant anomaly check
    anomaly = compute_anomaly_score(dataset)
    if anomaly > 0.5:
        penalty += 10
    
    # Actual formula
    raw_yield = base_sum * count_eligible
    adjusted_yield = raw_yield - penalty
    
    # Final manipulation
    final_modifier = len(extract_growth_cycles(dataset)) % 7  # always 5 due to input size
    return adjusted_yield + final_modifier

# --- Main Execution with Distractors ---
if __name__ == '__main__':
    # Real input data
    survey_years = list(range(1985, 2001))  # 16 years
    
    # Generate core signals
    base_signals = generate_base_signals(survey_years)
    
    # Apply real filter
    refined_readings = apply_seasonal_filter(base_signals, mode='strict')
    
    # Multiple irrelevant transformations
    anomalies = compute_anomaly_score(refined_readings)
    cycles = extract_growth_cycles(refined_readings)
    chloro_test = process_chlorophyll(list(refined_readings.values()))
    decades = aggregate_by_decade(refined_readings)
    
    # Critical statement
    final_yield = harvest_results(refined_readings)
    
    # Red herring: complex projection that isn't used
    fake_projection = finalize_projection(decades.values())
    
    # Print required result
    print(f"Result: {final_yield}")