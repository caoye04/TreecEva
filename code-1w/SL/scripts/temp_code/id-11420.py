def process_sensor_array(raw_readings):
    # Irrelevant signal filtering (dead code path)
    filtered = [x * 0.98 for x in raw_readings if x > 0]
    normalized = [min(max(val, 0), 100) for val in raw_readings]

    # Distractor: complex-looking but unused transformation
    transformed = []
    for i, v in enumerate(normalized):
        if i % 3 == 0:
            transformed.append(v ** 0.5 + 2.5)
        elif i % 3 == 1:
            transformed.append(v / 2.1 - 1.7)
        else:
            transformed.append(v * 1.1 % 10)

    # Real computation begins: categorize levels
    categories = {'stable': [], 'elevated': [], 'critical': []}
    for val in normalized:
        if val < 40:
            categories['stable'].append(val)
        elif val < 75:
            categories['elevated'].append(val)
        else:
            categories['critical'].append(val)

    stats = {
        'stable_count': len(categories['stable']),
        'elevated_count': len(categories['elevated']),
        'critical_count': len(categories['critical'])
    }

    # Red herring: unused statistical moment calculation
    mean_val = sum(normalized) / len(normalized)
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized)
    skewness = sum((x - mean_val) ** 3 for x in normalized) / (len(normalized) * (variance ** 1.5)) if variance > 0 else 0

    # Decoy function definition (never called)
    def adjust_for_drift(data, factor=1.02):
        return [d * factor for d in data]

    # Actual relevant logic: generate summary hash based on counts
    count_tuple = (stats['stable_count'], stats['elevated_count'], stats['critical_count'])
    hash_seed = count_tuple[0] * 17 + count_tuple[1] * 31 + count_tuple[2] * 7
    summary_hash = (hash_seed ^ 0xABCDEF) % 10000

    return summary_hash


def evaluate_risk_level(diag_code):
    # Misleading risk table with unused mappings
    risk_map = {
        'A1': 0.1, 'A2': 0.3, 'B1': 0.6, 'B2': 0.8,
        'C1': 1.2, 'C2': 1.5, 'X9': 2.0, 'Z0': 5.0
    }
    
    # Another decoy structure
    priority_queue = []
    for k, v in risk_map.items():
        if v > 1.0:
            priority_queue.append((v, k))
    
    # Real logic: simple mapping based on prefix
    prefix = diag_code[:2]
    if prefix in ['A1', 'A2']:
        return 1
    elif prefix in ['B1', 'B2']:
        return 2
    elif prefix in ['C1', 'C2']:
        return 3
    else:
        return 0

# Unused recursive helper (red herring)
def calculate_entropy(data, base=2):
    from math import log
    if len(data) <= 1:
        return 0
    p = sum(1 for x in data if x > 50) / len(data)
    if p == 0 or p == 1:
        return 0
    return -p*log(p, base) - (1-p)*log(1-p, base)

# Core analysis function that combines multiple concepts
def analyze_metrics(data_entries, thresholds):
    # Initialize result accumulator
    diagnostic_score = 0

    # Irrelevant preprocessing chain
    cleaned = []
    for entry in data_entries:
        clean_entry = {}
        for k, v in entry.items():
            if isinstance(v, float):
                clean_entry[k] = round(v, 2)
            elif isinstance(v, str):
                clean_entry[k] = v.strip().upper()
            else:
                clean_entry[k] = v
        cleaned.append(clean_entry)
    
    # Distractor: string pattern matching with no effect
    flags = []
    for entry in cleaned:
        status_str = entry.get('status', '')
        if status_str.startswith('CRIT'):
            flags.append(3)
        elif 'WARN' in status_str:
            flags.append(2)
        elif status_str.endswith('OK'):
            flags.append(1)
    
    # Real work: extract numeric values and compare to thresholds
    values = [entry['value'] for entry in data_entries]
    avg_value = sum(values) / len(values)
    
    # Use dictionary for dynamic threshold lookup
    category = 'default'
    if avg_value < 30:
        category = 'low'
    elif avg_value < 70:
        category = 'medium'
    else:
        category = 'high'
    
    applied_threshold = thresholds.get(category, thresholds['default'])
    
    # Critical branching logic
    if avg_value > applied_threshold * 1.1:
        severity = 3
    elif avg_value > applied_threshold * 0.9:
        severity = 2
    else:
        severity = 1
    
    # Tuple unpacking with meaningful computation
    base_codes = [process_sensor_array(values)]
    meta_code = base_codes[0] + (severity * 1000)
    
    # Final composition using string method as required (but only one affects outcome)
    code_str = f"DX{meta_code:06d}"
    checksum = sum(int(d) for d in code_str[2:] if d.isdigit())  # Uses string slicing
    final_code = meta_code + (checksum % 10)
    
    # Dead code: alternate checksum method (never used)
    temp = 0
    for i, c in enumerate(code_str):
        if c.isdigit():
            temp += (i+1) * int(c)
    
    # The actual answer contribution
    diagnostic_score += final_code

    return diagnostic_score

# Global constants (some irrelevant)
DEFAULT_THRESHOLDS = {
    'low': 20,
    'medium': 50,
    'high': 80,
    'default': 40
}

SECURITY_CODES = [
    'A1', 'B2', 'C1', 'X9', 'Z0'
]

# Simulated input data
health_data = [
    {'value': 25, 'status': 'STABLE'},
    {'value': 35, 'status': 'warn_trend'},
    {'value': 45, 'status': 'ok_status'},
    {'value': 65, 'status': 'CRITICAL_MONITOR'},
    {'value': 85, 'status': 'CRIT_EMERG'}
]

# Trigger decoy function calls to mislead
_ = evaluate_risk_level('B1')

# Key assignment statement
final_diagnostic = analyze_metrics(health_data, DEFAULT_THRESHOLDS)

# Print result as required
print(f"Target result: {final_diagnostic}")