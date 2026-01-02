def preprocess_logs(raw):
    lines = raw.strip().split('\n')
    tokens = []
    for line in lines:
        if line.startswith('DBG'):
            continue
        parts = line.split('|')
        tokens.extend(parts)
    return [t.strip() for t in tokens if t.strip()]

# Irrelevant helper (decoy)
def decrypt_sequence(seq):
    result = 0
    for c in seq:
        result = result * 31 + ord(c)
    return result % 10000

# Unused transformation path
def legacy_encode(s):
    return ''.join(chr((ord(c) + 5) % 95 + 32) for c in s)

# Misleading frequency counter (distractor)
def count_keywords(tokens, keywords):
    counts = {k: 0 for k in keywords}
    for t in tokens:
        if t.lower() in counts:
            counts[t.lower()] += 1
    return counts

# Heavily obscured but correct analysis
def analyze_pattern(entries):
    filtered = [e for e in entries if 'ERR' in e or 'CRIT' in e]
    lengths = [len(e.replace(' ', '')) for e in filtered]
    
    # Red herring computation
    avg_len = sum(lengths) / len(lengths) if lengths else 0
    weighted_sum = 0
    for i, ln in enumerate(lengths):
        weighted_sum += ln * (i + 1) ** 0.5
    
    # Actual signal: product of non-zero length mods
    mod_product = 1
    for ln in lengths:
        mod_val = ln % 7
        if mod_val != 0:
            mod_product *= mod_val
    
    # Decoy checksum (never used)
    checksum = 0
    for entry in entries:
        for char in entry:
            checksum += ord(char) % 11
    checksum %= 100000
    
    # Critical distraction: recursive reduction (unused)
    def reduce_entropy(data):
        if len(data) <= 1:
            return data[0] if data else 0
        return reduce_entropy([d // 2 + d % 2 for d in data[:-1]])
    
    # Real logic hidden among noise
    char_count = 0
    for entry in filtered:
        cleaned = entry.replace('CRIT', '').replace('ERR', '').strip()
        char_count += len(cleaned)
    
    # Final result combines two subtle results
    return mod_product + char_count

# Simulated log input (real data source)
raw_log_input = '''
INFO|System online|v1.2
DBG|Memory check: 98%|Threshold OK
ERR|Connection timeout|retry=3
CRIT|Auth failure|user=admin|ip=192.168.1.1
DBG|Packet trace enabled
INFO|Keep-alive sent
ERR|Database unreachable|timeout=5000ms
'''

# Execution chain with multiple distractions
token_stream = preprocess_logs(raw_log_input)
keyword_list = ['err', 'crit', 'info']

# Distractor call (no effect on final answer)
freq_analysis = count_keywords(token_stream, keyword_list)
phantom_code = decrypt_sequence('alpha7')

# Main diagnostic path
log_entries = raw_log_input.strip().split('\n')
final_diagnostic = analyze_pattern(log_entries)
print(f"Result: {final_diagnostic}")