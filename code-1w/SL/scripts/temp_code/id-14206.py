from collections import defaultdict, Counter

# Simulated system log analyzer with decoy logic and multiple distractions
def load_config():
    return {'threshold': 5, 'debug': False, 'version': '3.7'}

def deprecated_util(val):
    # Unused function - red herring
    return val ** 2 + 1

def generate_sequence(n):
    # Distractor: generates Fibonacci-like sequence but not used in final result
    seq = [1, 1]
    for i in range(2, n + 5):
        seq.append(seq[-1] + seq[-2])
    return seq

def validate_checksum(data):
    # Seemingly important but unused validation
    checksum = 0
    for d in data:
        checksum ^= d * 3
    return checksum == 0

# Irrelevant data structures
temp_cache = defaultdict(int)
for i in range(10):
    temp_cache[f'key_{i}'] = i * 11

device_states = ['active', 'idle', 'standby', 'active', 'fault', 'active', 'idle']
state_count = Counter(device_states)

# Core simulation data
log_entries = [
    {'level': 'ERROR', 'code': 500, 'ts': 1623456789},
    {'level': 'WARN', 'code': 404, 'ts': 1623456790},
    {'level': 'ERROR', 'code': 500, 'ts': 1623456791},
    {'level': 'INFO', 'code': 200, 'ts': 1623456792},
    {'level': 'ERROR', 'code': 503, 'ts': 1623456793},
    {'level': 'WARN', 'code': 403, 'ts': 1623456794},
    {'level': 'ERROR', 'code': 500, 'ts': 1623456795}
]

system_flags = {
    'panic_mode': False,
    'overload': True,
    'maintenance_window': None,
    'retry_count': 3
}

# Decoy transformation using list comprehension and lambda (not directly affecting result)
transformed = [lambda x: x['code'] * 2 for _ in log_entries]
squared_codes = [entry['code'] ** 2 for entry in log_entries if entry['level'] == 'WARN']

# Real processing begins here — heavily buried among distractions
def extract_errors(logs):
    errors = []
    error_count = 0
    for entry in logs:
        if entry['level'] == 'ERROR':
            error_count += 1
            # Only codes divisible by 100 are critical
            if entry['code'] % 100 == 0:
                errors.append(entry['code'])
    # Return only critical error codes
    return errors

# Another layer of processing with distractors
def filter_by_timestamp(logs, base_ts):
    recent = []
    for entry in logs:
        if entry['ts'] > base_ts - 10:
            recent.append(entry)
    return recent  # Not actually used in final logic

# Key analysis function with mixed concepts
def analyze_pattern(entries, flags):
    # Step 1: Extract all ERROR entries
    error_codes = [e['code'] for e in entries if e['level'] == 'ERROR']
    
    # Step 2: Count frequency of each error code
    freq = defaultdict(int)
    for code in error_codes:
        freq[code] += 1
    
    # Step 3: Find most frequent error code
    primary_cause = max(freq, key=lambda k: freq[k])
    
    # Step 4: Apply bitmask analysis on the code (bitwise distraction)
    masked_value = primary_cause & 0xFF  # Lower 8 bits
    shifted = (primary_cause >> 4) & 0xFFFF  # Shift and mask
    
    # Step 5: Check if overload flag affects outcome (distractor logic)
    overload_factor = 1
    if flags['overload']:
        overload_factor = 2  # Misleading multiplier
    
    # Step 6: Compute diagnostic score based on frequency and code
    base_score = 0
    for code, count in freq.items():
        if count > 1:
            base_score += code // 100  # Normalize to class (5xx → 5)
    
    # Step 7: Add bonus for repeated critical errors (500-class)
    if 500 in freq and freq[500] >= 3:
        base_score += 10
    
    # Step 8: Final adjustment using bitwise XOR with retry count (actual dependency)
    final_adjustment = base_score ^ flags['retry_count']
    
    # Step 9: Dead calculation — looks important but unused
    theoretical_max = len(entries) * 500
    efficiency_ratio = (base_score / theoretical_max) if theoretical_max else 0
    
    # Step 10: The real answer
    final_diagnostic = final_adjustment * 1000 + masked_value
    
    return final_diagnostic

# Call the main analysis
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")