import math

# Simulated system performance metrics over time
def generate_metrics():
    raw_data = [127, 83, 156, 92, 201, 77, 144]
    processed = {}
    for i, val in enumerate(raw_data):
        processed[f'step_{i}'] = {
            'raw': val,
            'squared': val ** 2,
            'binary': bin(val),
            'log_val': round(math.log(val + 1), 4) if val > 0 else 0,
            'flagged': val > 100
        }
    return processed

# Irrelevant helper: converts numbers to roman numerals (unused path)
def to_roman(n):
    if n <= 0: return ''
    vals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), 
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    res = ''
    for v, r in vals:
        while n >= v:
            n -= v
            res += r
    return res

# Decoy function that looks important but isn't called
def analyze_security_risk(data_map):
    risk_score = 0
    for k, v in data_map.items():
        if isinstance(v, dict) and v.get('flagged'):
            risk_score += hash(k) % 17
    return risk_score % 11

# Bit manipulation red herring
def obfuscate_key(base_num):
    temp = base_num << 3
    temp ^= 0xFF
    temp = (temp & 0xFFFF) >> 4
    return temp * 1.5  # never used directly

# Real processing begins here
def filter_critical_steps(log_data):
    critical = []
    for step_key, entry in log_data.items():
        if entry['raw'] > 100 and entry['log_val'] > 4.0:
            critical.append(entry['raw'])
    return critical

def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 4)

def transform_sequence(nums):
    # Double odd numbers, halve even ones using integer division
    transformed = []
    for num in nums:
        if num % 2 == 0:
            transformed.append(num // 2)
        else:
            transformed.append(num * 2)
    return transformed

def count_combinations(n, r):
    # Simple combinatorics: C(n,r) = n! / (r!(n-r)!)
    if r > n or r < 0:
        return 0
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result  # unused distractor

def aggregate_features(filtered):
    # Apply transformations and extract features
    doubled = [x * 2 for x in filtered]
    shifted = [x >> 2 for x in doubled]  # bit shift
    summed = sum(shifted)
    avg = summed / len(shifted) if shifted else 0
    return int(avg)

def evaluate_performance(metrics_log):
    # Extract steps meeting criteria
    critical_raw = filter_critical_steps(metrics_log)
    
    # Transform the sequence
    transformed_vals = transform_sequence(critical_raw)
    
    # Compute derived statistics
    entropy = compute_entropy(transformed_vals)
    
    # Aggregate into feature score
    feature_score = aggregate_features(transformed_vals)
    
    # Dummy dictionary operations for distraction
    aux_info = {f'item_{i}': {'val': v, 'meta': hex(v ^ 0xAB)} for i, v in enumerate(transformed_vals)}
    aux_info['stats'] = {'count': len(transformed_vals), 'entropy': entropy}
    aux_info['version'] = '2.1-alpha'
    del aux_info['item_0']  # meaningless deletion
    
    # Secondary processing chain
    baseline = 50
    adjustment_factor = 0.8
    if len(transformed_vals) >= 3:
        adjustment_factor += 0.15
    elif len(transformed_vals) == 2:
        adjustment_factor += 0.05
    
    # Main computation
    raw_total = sum(critical_raw)
    adjusted_base = baseline * adjustment_factor
    
    # Final composition
    complexity_bonus = len([v for v in transformed_vals if v > 150])
    stability_penalty = sum(1 for v in transformed_vals if v < 50)
    
    final_score = int(
        adjusted_base + 
        (raw_total / 10) + 
        (complexity_bonus * 7) - 
        (stability_penalty * 3) +
        int(entropy * 2)
    )
    
    # Dead code branch - looks like it affects result but doesn't
    if final_score > 200:
        scaling = math.sqrt(final_score) / 10
        final_score = int(final_score / scaling)  # not actually executed
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Generate full metrics log
    metrics_log = generate_metrics()
    
    # Irrelevant pre-processing (distractor)
    temp_array = [len(v['binary']) for v in metrics_log.values() if v['flagged']]
    weighted_sum = sum(i * temp_array[i] for i in range(len(temp_array)))
    
    # Actual target computation
    final_score = evaluate_performance(metrics_log)
    
    # Print result as required
    print(f"Result: {final_score}")