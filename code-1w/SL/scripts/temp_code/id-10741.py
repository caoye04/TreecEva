def preprocess_record(record):
    # Irrelevant transformation (dead code path)
    temp_score = sum([ord(c) for c in record['name']]) % 7
    adjusted_age = record['age'] + (record['flags'] & 3)
    
    # Distractor: complex but unused computation
    decoy_metric = (record['systolic'] >> 2) ^ (record['diastolic'] << 1)
    decoy_metric = decoy_metric % 13 if decoy_metric > 100 else decoy_metric * 2

    # Relevant: normalize blood pressure category
    if record['systolic'] < 90 or record['diastolic'] < 60:
        bp_category = 'hypotensive'
    elif record['systolic'] >= 140 or record['diastolic'] >= 90:
        bp_category = 'hypertensive'
    else:
        bp_category = 'normal'

    # Another distractor: unused risk scoring with red herring logic
    baseline_risk = 1
    if record['age'] > 50:
        baseline_risk += 2
    if record['flags'] & 4:
        baseline_risk *= 1.5
    if len(record['name']) % 2 == 0:
        baseline_risk -= 0.5  # This path is never actually used

    # Key relevant transformation
    severity_index = 0
    if bp_category == 'hypotensive':
        severity_index += 3
    elif bp_category == 'hypertensive':
        severity_index += 2

    if record['age'] > 65:
        severity_index += 1

    return {
        'severity': severity_index,
        'category': bp_category,
        'id': record['id'],
        'processed': True
    }

# Unused recursive function (decoy)
def calculate_entropy(data, depth=0):
    if depth > 5:
        return 0.0
    return (sum([d % 10 for d in data]) / len(data)) + calculate_entropy(data[::2], depth + 1)

# Main diagnostic logic
def analyze_patient_data(records):
    stats = {'hypotensive': 0, 'hypertensive': 0, 'normal': 0}
    total_severity = 0
    processed_count = 0

    # Real processing loop
    for r in records:
        proc = preprocess_record(r)
        stats[proc['category']] += 1
        total_severity += proc['severity']
        processed_count += 1

    # Distractor: unused statistical computations
    mean_age = sum([r['age'] for r in records]) / len(records)
    variance_proxy = sum([(r['systolic'] - 120) ** 2 for r in records]) / len(records)
    skew_flag = (records[0]['flags'] | records[-1]['flags']) & 5

    # Irrelevant string-based analysis
    name_chars = ''.join([r['name'] for r in records])
    char_freq = {}
    for c in name_chars:
        char_freq[c] = char_freq.get(c, 0) + 1
    rare_chars = [c for c, cnt in char_freq.items() if cnt == 1]

    # Another decoy metric
    phantom_index = len(rare_chars) * (skew_flag + 1)
    if phantom_index > 10:
        phantom_index = phantom_index // 2

    # Core result calculation (depends on multiple prior steps)
    base_diagnostic = total_severity * 100
    adjustment_factor = 0
    if stats['hypertensive'] > stats['normal']:
        adjustment_factor += 5
    if stats['hypotensive'] > 0:
        adjustment_factor += 10
    if processed_count >= 3:
        adjustment_factor += 2

    final_diagnostic = base_diagnostic + adjustment_factor

    # Final red herring: a print that looks important but isn't
    debug_trace = f"Final trace: {stats['hypertensive']}H-{stats['hypotensive']}L"

    return final_diagnostic

# Input data (fixed seed for determinism)
patient_records = [
    {'id': 101, 'name': 'Alice', 'age': 72, 'systolic': 88, 'diastolic': 58, 'flags': 5},
    {'id': 102, 'name': 'Bob', 'age': 45, 'systolic': 142, 'diastolic': 92, 'flags': 2},
    {'id': 103, 'name': 'Charlie', 'age': 67, 'systolic': 138, 'diastolic': 88, 'flags': 6},
    {'id': 104, 'name': 'Diana', 'age': 39, 'systolic': 118, 'diastolic': 76, 'flags': 1},
]

# Execution point
final_diagnostic = analyze_patient_data(patient_records)
print(f"Target result: {final_diagnostic}")