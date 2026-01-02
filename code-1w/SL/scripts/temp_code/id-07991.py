import itertools

# Simulated sensor data processing for a biomedical diagnostic system
def analyze_readings(readings):
    baseline = sum(readings[:5]) / 5
    deviations = [(x - baseline) ** 2 for x in readings]
    variance = sum(deviations) / len(deviations)
    adjusted_scores = [max(0, 100 - abs(x * 2)) for x in deviations]
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)) * 100) for x in readings] if len(readings) > 1 else [0]
    noise_floor = sum(normalized) % 7

    # Red herring: unused calculation path
    def compute_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        return -sum((count / len(data)) * log(count / len(data)) for count in freq.values())

    # This function is never called but looks important
    def calibrate_signal(signal):
        return [s * 0.98 + 0.5 for s in signal]

    # Core logic disguised among distractions
    risk_indicators = []
    for i, val in enumerate(readings):
        if i > 0 and abs(val - readings[i-1]) > 15:
            risk_indicators.append(1)
    fluctuation_index = sum(risk_indicators)

    score = 0
    if variance < 25:
        score += 40
    if fluctuation_index == 0:
        score += 30
    if adjusted_scores and sum(adjusted_scores) / len(adjusted_scores) > 70:
        score += 30

    return max(0, min(100, score))


def aggregate_diagnosis(patients):
    # Unused complexity: patient correlation graph (dead code path)
    correlations = []
    for p1, p2 in itertools.combinations(patients, 2):
        corr = sum(a * b for a, b in zip(p1['vitals'], p2['vitals'])) % 13
        correlations.append(corr)

    # Real aggregation logic
    valid_scores = []
    for p in patients:
        raw_score = analyze_readings(p['readings'])
        if p['weight'] > 50 and p['age'] < 80:
            adjustment = 10 if p['medication'] else 0
            valid_scores.append(raw_score + adjustment)
    return sum(valid_scores) / len(valid_scores) if valid_scores else 50

# Data preprocessing decoy
def preprocess_labels(labels):
    return [label.upper().replace('_', ' ').strip() for label in labels]

# Main pipeline with key computation buried in context
def process_metrics(data, limit):
    filtered_data = [d for d in data if d['status'] != 'inactive']
    
    # Distractor: string manipulation that looks relevant
    codes = ['A1', 'B2', 'C3', 'D4']
    encoded = ''.join(itertools.chain.from_iterable(zip(codes, map(str, sorted(set(d['id'] % 10 for d in filtered_data))))))
    checksum = sum(ord(c) for c in encoded if c.isdigit()) % 11

    # Conditional expression red herring
    classification = 'critical' if checksum > 7 else 'moderate' if checksum > 3 else 'stable'

    # Actual metric computation
    ages = [d['age'] for d in filtered_data]
    avg_age = sum(ages) / len(ages)
    
    age_penalty = 0
    if avg_age > 65:
        age_penalty = (avg_age - 65) * 0.8
    
    base_diagnostics = aggregate_diagnosis(filtered_data)
    
    # Final adjustment using case conversion distraction
    flags = [f"FLAG_{i}" for i in range(len(filtered_data))]
    upper_flags = [f.lower().replace('flag', 'tag') for f in flags]
    tag_value = len(''.join(upper_flags)) % 9

    # Key statement
    final_diagnostic = base_diagnostics - age_penalty + (tag_value if tag_value < 5 else 0)
    
    # Dead code: post-processing that isn't used
    def finalize_report(diag):
        return f"Result: {round(diag, 1)}% stability"
    
    return final_diagnostic

# Input data with realistic structure
health_data = [
    {
        'id': 101, 'age': 45, 'weight': 68, 'status': 'active',
        'readings': [95, 97, 96, 94, 98, 97, 96],
        'vitals': [70, 120, 80, 22], 'medication': False
    },
    {
        'id': 205, 'age': 72, 'weight': 75, 'status': 'active',
        'readings': [96, 95, 97, 98, 96, 95, 94],
        'vitals': [72, 125, 82, 20], 'medication': True
    },
    {
        'id': 303, 'age': 68, 'weight': 45, 'status': 'inactive',  # excluded due to status
        'readings': [90, 88, 92, 95, 93, 91, 89],
        'vitals': [68, 118, 78, 18], 'medication': False
    },
    {
        'id': 407, 'age': 78, 'weight': 82, 'status': 'active',
        'readings': [97, 96, 98, 99, 97, 96, 98],
        'vitals': [76, 130, 85, 24], 'medication': False
    }
]

threshold = 0.75

# Execute key statement
final_diagnostic = process_metrics(health_data, threshold)
print(f"Target result: {final_diagnostic}")