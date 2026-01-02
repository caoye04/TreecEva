def analyze_vital(v):
    if v < 36.0 or v > 37.5:
        return False
    return True

# Irrelevant helper (distractor)
def normalize readings(data):
    return [max(0, x) for x in data]

# Unused function (dead code path)
def deprecated_calib(seq):
    return sum(x * 0.9 for x in seq if x > 0)

# Core processing logic
def filter_anomalies(records):
    result = []
    for r in records:
        temp = r.get('temp')
        hr = r.get('heart_rate')
        if temp is None or hr is None:
            continue
        if 60 <= hr <= 100 and analyze_vital(temp):
            result.append(r)
    return result

# Set operations used idiomatically
def get_stable_ids(filtered):
    recent = {r['id'] for r in filtered if r['timestamp'] > 1000}
    historical = {r['id'] for r in filtered if r['timestamp'] <= 1000}
    return recent & historical  # Intersection: patients present in both

# Conditional expression and distractor math
def compute_baseline(metrics):
    base = sum(m['temp'] for m in metrics) / len(metrics) if metrics else 0
    adjustment = 0.3 if base < 36.5 else (-0.2 if base > 37.0 else 0)
    return base + adjustment

# Bit manipulation red herring
def scramble_key(n):
    return ((n << 3) & 0xFF) ^ 0x5A

def process_metrics(data, limits):
    cleaned = filter_anomalies(data)
    if not cleaned:
        return -999
    
    # Meaningful computation
    avg_temp = compute_baseline(cleaned)
    valid_ids = get_stable_ids(cleaned)
    
    # Distractor variables
    dummy_score = sum(scramble_key(i) for i in valid_ids) % 100
    audit_flag = len(valid_ids) > 2
    
    # Core answer computation
    threshold_temp = limits['high'] - (limits['low'] + 0.8)
    deviation = abs(avg_temp - 36.8)
    
    # Final diagnostic combines arithmetic, conditionals, and set logic
    severity = deviation * 100
    final_diagnostic = int(severity) if severity >= threshold_temp else int(threshold_temp)
    
    # Redundant print (not part of logic)
    if audit_flag:
        print(f'Audit required for {len(valid_ids)} stable patients')
    
    return final_diagnostic

# Simulated input data
health_data = [
    {'id': 101, 'temp': 36.9, 'heart_rate': 72, 'timestamp': 1005},
    {'id': 102, 'temp': 35.8, 'heart_rate': 68, 'timestamp': 1003},  # excluded by temp
    {'id': 103, 'temp': 37.1, 'heart_rate': 95, 'timestamp': 998},
    {'id': 104, 'temp': 36.7, 'heart_rate': 70, 'timestamp': 1010},
    {'id': 101, 'temp': 36.8, 'heart_rate': 74, 'timestamp': 995},
    {'id': 103, 'temp': 37.0, 'heart_rate': 98, 'timestamp': 1001}
]

# Thresholds used in final calculation
thresholds = {'low': 36.0, 'high': 38.0}

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f'Result: {final_diagnostic}')