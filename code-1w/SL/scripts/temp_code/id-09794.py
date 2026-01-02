import math

def analyze_sequence(seq):
    return sum(x ** 2 for x in seq if x % 2 == 1)

# Irrelevant helper function (dead code path)
def deprecated_checksum(data):
    return sum(data) % 256

# Unused transformation table
cipher_map = {chr(i): i - 97 for i in range(97, 123)}
offset_key = 42
buffer_size = 512  # Unused constant

log_data = [
    {'timestamp': 1001, 'event': 'start', 'payload': [1, 3, 5, 7]},
    {'timestamp': 1005, 'event': 'compute', 'payload': [2, 4, 6, 8]},
    {'timestamp': 1010, 'event': 'sample', 'payload': [9, 11, 13]}
]

system_state = {
    'mode': 'diagnostic',
    'version': '3.8.1',
    'flags': 0b1010,
    'cache_hit': False,
    'debug_level': 3
}

# Misleading intermediate computation (red herring)
temp_analysis = 0
for entry in log_data:
    if 'payload' in entry:
        temp_analysis += len(entry['payload']) * 2

temp_analysis = (temp_analysis >> 1) ^ 15  # Bit manipulation distraction

# Auxiliary function with string processing (distractor)
def extract_labels(logs):
    labels = []
    for log in logs:
        event = log.get('event', '')
        if event.islower():
            labels.append(event[::-1])  # Reverse string
    return labels

# Another decoy function using dictionary operations
def build_index(logs):
    index = {}
    for i, log in enumerate(logs):
        index[f"entry_{i}"] = log.get('timestamp')
    return index

# Real processing begins here
def compute_baseline(payloads):
    total = 0
    for p in payloads:
        if len(p) > 2:
            total += max(p) - min(p)
    return total

def evaluate_entropy(payloads):
    entropy = 0.0
    for p in payloads:
        if p:
            avg = sum(p) / len(p)
            variance = sum((x - avg) ** 2 for x in p) / len(p)
            entropy += math.log(variance + 1)
    return entropy

def process_metrics(logs, state):
    payloads = [entry['payload'] for entry in logs if 'payload' in entry]
    
    # Key metric 1: baseline spread
    baseline = compute_baseline(payloads)
    
    # Key metric 2: entropy measure
    entropy_score = evaluate_entropy(payloads)
    
    # Conditional logic with bit flag check
    adjustment = 0
    if state['flags'] & 0b1000:  # Check specific bit
        adjustment += 5
    if not state['cache_hit']:
        adjustment -= 2
    
    # Core calculation chain
    raw_value = baseline * 3 + int(entropy_score * 4)
    interim = (raw_value ^ 0xAB) + offset_key  # XOR with hex constant
    interim = abs(interim) % 10000
    
    # Final adjustment based on debug level
    if state['debug_level'] > 2:
        interim += 7
    
    # Real answer derived here
    final_diagnostic = interim + adjustment
    
    # Dead branch (never executed)
    if False:
        final_diagnostic = deprecated_checksum([final_diagnostic])
    
    return final_diagnostic

# Extracted labels (unused result)
labels = extract_labels(log_data)

# Index map (irrelevant data structure)
index_map = build_index(log_data)

# Critical execution point
final_diagnostic = process_metrics(log_data, system_state)

# Output result as required
print(f"Target result: {final_diagnostic}")