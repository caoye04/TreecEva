import math

# System health monitoring simulation with diagnostic reasoning

def generate_trace_sequence(base_signal, noise_level):
    return [base_signal * (i % 7) + ((i ** 2) % 11) * noise_level for i in range(15)]

def compute_entropy(values):
    hist = {}
    for v in values:
        hist[v] = hist.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in hist.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def evaluate_redundancy(pattern):
    # Irrelevant redundancy check (distractor)
    duplicates = 0
    seen = set()
    for x in pattern:
        if x in seen:
            duplicates += 1
        seen.add(x)
    return duplicates

def filter_anomalies(trace, threshold=10):
    # Unused function - dead code path (distractor)
    return [x for x in trace if abs(x) < threshold]

def shift_cipher(text, offset):
    # String manipulation distractor
    result = ''
    for c in text:
        if c.isalpha():
            shifted = ord(c.lower()) - ord('a')
            shifted = (shifted + offset) % 26
            result += chr(shifted + ord('a'))
        else:
            result += c
    return result

def recursive_sum(n):
    # Misleading recursive function (red herring)
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)

def extract_diagnostic_code(signal, flags):
    # Complex but partially irrelevant transformation
    temp = 0
    for bit in flags:
        temp = (temp << 1) | bit
    masked = signal & 0xFF
    return (masked ^ temp) % 89

def analyze_pattern(logic_traces, system_flags):
    # Core analysis logic
    key_metric = 0
    for i, trace in enumerate(logic_traces):
        ent = compute_entropy(trace)
        if ent > 3.0:
            key_metric += int(ent * 10)
        elif ent > 2.0:
            key_metric += 5
        else:
            key_metric += 1
    
    # Secondary influence from flags
    flag_value = 0
    for f in system_flags:
        flag_value = (flag_value << 1) | (1 if f else 0)
    
    # Real computation path
    intermediate = key_metric * 17 + (flag_value ^ 0b1010)
    
    # Distractor: unused complex dictionary structure
    diagnostics_log = {
        'trace_count': len(logic_traces),
        'entropy_profile': [round(compute_entropy(t), 4) for t in logic_traces],
        'redundancy_score': evaluate_redundancy([item for sublist in logic_traces for item in sublist]),
        'cipher_tag': shift_cipher('diagnostics_active', key_metric % 26),
        'recursive_check': recursive_sum(len(logic_traces))
    }
    
    # Actual answer derivation
    adjustment = 0
    if flag_value & 0b1100:
        adjustment += 23
    if len(logic_traces) >= 5:
        adjustment -= 7
    
    final_diagnostic = intermediate + adjustment
    
    # Red herring print (never executed)
    # print(f'Debug: {diagnostics_log}')
    
    return final_diagnostic

# Simulated input data
base_input = 3
noise = 2
raw_sequences = [
    generate_trace_sequence(base_input, noise),
    generate_trace_sequence(base_input + 1, noise - 1),
    generate_trace_sequence(base_input - 1, noise),
    generate_trace_sequence(base_input, noise + 1),
    generate_trace_sequence(base_input + 2, noise - 1),
    generate_trace_sequence(base_input - 2, noise + 2),
    generate_trace_sequence(base_input, noise)
]

# System state flags (bit vector)
system_flags = [True, False, True, False, True]

# Extraneous string processing (distractor)
token_pool = ['ERR', 'OK', 'DBG', 'SYS']
status_map = {token: (ord(token[0]) * (i+1)) % 97 for i, token in enumerate(token_pool)}

# Key execution point
final_diagnostic = analyze_pattern(raw_sequences, system_flags)

# Output result as required
print(f"Result: {final_diagnostic}")