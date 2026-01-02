def preprocess_logs(raw):
    cleaned = []
    for entry in raw:
        if 'ERROR' in entry or 'CRITICAL' in entry:
            cleaned.append(entry.strip().lower())
    return cleaned

# Irrelevant utility function (distractor)
def encrypt_sequence(seq):
    return [pow(s, 3, 19) for s in seq]

def count_severity(lines):
    counts = {'error': 0, 'critical': 0, 'warning': 0}
    for line in lines:
        if 'error' in line:
            counts['error'] += 1
        if 'critical' in line:
            counts['critical'] += 1
        if 'warning' in line:
            counts['warning'] += 1
    temp_result = sum(counts.values()) * 0.5  # Misleading intermediate
    return counts

def generate_checksum(data_list):
    # Complex but irrelevant checksum (dead path)
    chk = 0
    for d in data_list:
        chk ^= hash(d) % 1000
    return chk + 113

def filter_anomalies(records):
    anomalies = []
    for r in records:
        words = r.split()
        if len(words) > 5 and 'failed' in r:
            anomalies.append(len(words))
    return anomalies if anomalies else [0]

def decode_shift(pattern_str):
    decoded = ''
    for c in pattern_str:
        if c.isalpha():
            shifted = chr(((ord(c.lower()) - ord('a') - 7) % 26) + ord('a'))
            decoded += shifted
        else:
            decoded += c
    return decoded  # Used only in decoy logic

def analyze_pattern(logs, flags):
    severity_map = count_severity(logs)
    total_alerts = sum(severity_map.values())
    
    # Key distraction: complex bit manipulation with partial relevance
    flag_state = 0
    for f in flags:
        flag_state ^= f << 2
        flag_state &= 0xFFFF
    
    # Extract key signal from logs
    error_count = severity_map['error']
    critical_count = severity_map['critical']
    
    # Core logic buried in distractions
    base_score = (critical_count * 3) + (error_count * 1)
    
    # Conditional expression with string method red herring
    adjustment = len(decode_shift('olssv')[:3]) if base_score > 5 else 0  # 'hello' shifted back
    
    # Real computation hidden among noise
    diagnostic_weight = base_score + adjustment
    
    # Decoy dictionary operation
    stats = {
        'entries': len(logs),
        'flags_active': len([f for f in flags if f > 0]),
        'checksum': generate_checksum(logs)
    }
    stats['derived'] = diagnostic_weight * 2  # Unused field (distractor)
    
    final_diagnostic = diagnostic_weight * 17
    return final_diagnostic

# Simulated input data
raw_log_data = [
    '  CRITICAL: System failed to initialize memory block ',
    'ERROR: Failed authentication attempt detected       ',
    'WARNING: High CPU usage observed in subsystem 4',
    'CRITICAL: Database connection timeout exceeded',
    'ERROR: Invalid pointer access in module X',
    'ERROR: Configuration file not found'
]

system_diagnostics = [5, 3, 0, 7, 2]  # Sensor flags

# Preprocessing chain with irrelevant steps
cleaned_logs = preprocess_logs(raw_log_data)
anomaly_lengths = filter_anomalies(cleaned_logs)
encrypted_diags = encrypt_sequence(system_diagnostics)  # Dead computation

# Key execution point
final_diagnostic = analyze_pattern(cleaned_logs, system_diagnostics)

print(f"Result: {final_diagnostic}")