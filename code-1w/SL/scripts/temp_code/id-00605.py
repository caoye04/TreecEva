def preprocess_logs(raw):    
    # Irrelevant transformation: counts vowels in log prefixes (distractor)
    vowel_count = sum(1 for c in ''.join(raw)[:50] if c.lower() in 'aeiou')
    cleaned = [entry.strip().lower() for entry in raw if entry]
    return [c for c in cleaned if 'error' not in c]

# Misleading function that looks important but is never called
def deprecated_analysis(data):
    checksum = 0
    for item in data:
        if isinstance(item, str):
            checksum ^= len(item)
    return checksum % 7 == 0

# Auxiliary function with partial relevance
def extract_codes(entries):
    codes = []
    for e in entries:
        parts = e.split(' ')
        for p in parts:
            if p.isdigit() and len(p) == 3:
                codes.append(int(p))
    return list(set(codes))  # Remove duplicates

# Bit manipulation red herring
def obscure_transform(x):
    x = (x ^ 255) & 127
    x = (x << 2) | (x >> 6)
    return x % 100

# Decoy statistical function
def compute_entropy(arr):
    from math import log
    if not arr:
        return 0.0
    total = sum(arr)
    if total == 0:
        return 0.0
    entropy = 0.0
    for val in arr:
        prob = val / total
        if prob > 0:
            entropy -= prob * log(prob, 2)
    return round(entropy, 4)

# Core logic disguised among noise
def count_critical_sequences(events):
    count = 0
    for i in range(len(events) - 2):
        if (events[i].endswith('warn') and 
            'retry' in events[i+1] and 
            events[i+2].startswith('init')):
            count += 1
    return count

# Main analysis with multiple concepts
def analyze_pattern(logs, flags):
    # Step 1: Filter logs (relevant)
    filtered = [log for log in logs if len(log) > 10]
    
    # Step 2: Extract numeric codes (partially relevant)
    code_list = extract_codes(filtered)
    
    # Step 3: Count specific pattern (critical path)
    pattern_count = count_critical_sequences(filtered)
    
    # Step 4: Process flags with bit operations (red herring)
    flag_state = 0
    for f in flags:
        if f > 0:
            flag_state |= (1 << (f % 8))
    
    # Step 5: String-based priority scoring (distractor)
    priority_score = 0
    for log in filtered:
        words = log.split()
        for word in words:
            if word.isupper() and len(word) >= 3:
                priority_score += len(word)
    
    # Step 6: Character frequency analysis (semi-relevant)
    char_freq = {}
    for log in filtered:
        for c in log:
            if c.isalpha():
                char_freq[c] = char_freq.get(c, 0) + 1
    
    # Step 7: Find most frequent letter (used in final calculation)
    dominant_char = max(char_freq, key=char_freq.get) if char_freq else 'a'
    
    # Step 8: Compute character score using string method
    offset = ord(dominant_char.lower()) - ord('a')
    
    # Step 9: Apply modular arithmetic with combinatorics
    combinations = 1
    for i in range(pattern_count):
        combinations = (combinations * (offset + i + 1)) // (i + 1)  # C(offset+i, i+1)
    
    # Step 10: Final diagnostic computation (answer path)
    base = len(code_list) * 10
    modifier = (pattern_count ** 2) + (offset * 3)
    final_value = base + modifier - (combinations % 19)
    
    # Dead code branch: looks important but unused
    if final_value < 0:
        final_value = abs(final_value) ^ 255
        
    return final_value

# Simulated input data
raw_log_data = [
    'INIT 123 starting system',
    'WARN 456 retry connection',
    'INFO 789 normal operation',
    'ERROR 101 ignored entry',
    'WARN 456 retry timeout',
    'INIT 202 resuming',
    'DEBUG 303 verbose output',
    'WARN 456 retry init sequence',  # Match: warn -> retry -> init
    'STATUS 505 polling active'
]

system_diagnostics = [3, -1, 7, 0, 3]

# Preprocessing (irrelevant but plausible)
cleaned_logs = preprocess_logs(raw_log_data)

# Extraneous computation: character counting distraction
total_chars = sum(len(log.replace(' ', '')) for log in raw_log_data)

# Another decoy: sorting codes unnecessarily
sorted_codes = sorted([123, 456, 789, 101, 202, 303, 505])

# Key execution point
final_diagnostic = analyze_pattern(cleaned_logs, system_diagnostics)

# Output result
print(f"Result: {final_diagnostic}")