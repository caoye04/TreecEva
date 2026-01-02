from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(187):
        if i % 7 == 0:
            signals.append(f'ERR_{(i * 3) % 43}')
        elif i % 5 == 2:
            signals.append(f'WARN_{(i + 10) % 59}')
        else:
            signals.append(f'OK_{i % 13}')
    return signals

def process_signals(raw_signals):
    # Irrelevant transformation: counts per prefix (decoy)
    decoy_counter = defaultdict(int)
    for s in raw_signals:
        prefix = s.split('_')[0]
        decoy_counter[prefix] += 1

    # Actual relevant mapping: extract numeric residues
    residue_map = defaultdict(list)
    for s in raw_signals:
        try:
            val = int(s.split('_')[1])
            residue_map[s[0]].append(val)
        except (IndexError, ValueError):
            continue

    # Misleading aggregation: sum all values (not used later)
    total_sum = sum(sum(vals) for vals in residue_map.values())

    # Relevant computation: compute median residue for 'E' key
    e_residues = sorted(residue_map['E']) if 'E' in residue_map else [0]
    median_e = e_residues[len(e_residues) // 2]

    # Dead code path: never accessed
    if False:
        debug_dump = {k: len(v) for k, v in residue_map.items()}
        return {'median': 0, 'debug': debug_dump}

    return {'median': median_e, 'raw_map': residue_map, 'total': total_sum}

class DiagnosticEngine:
    def __init__(self, threshold):
        self.threshold = threshold
        self.history = []
        self.active = True

    def evaluate(self, data_chunk):
        # Complex but partially irrelevant logic
        stats = Counter()
        for key in data_chunk['raw_map']:
            stats[key] += len(data_chunk['raw_map'][key])

        # Red herring: calculate entropy-like metric (unused)
        total_entries = sum(stats.values())
        entropy = 0.0
        for count in stats.values():
            if count > 0 and total_entries > 0:
                prob = count / total_entries
                entropy -= prob * __import__('math').log2(prob) if prob > 0 else 0

        # Core logic: compare median to threshold
        flag = data_chunk['median'] > self.threshold
        score = data_chunk['median'] * (2 if flag else 1)

        # Distractor: complex tuple packing/unpacking
        result_bundle = (flag, score, {'meta': len(stats), 'ent': round(entropy, 3)})
        is_critical, _, meta_info = result_bundle

        # Early exit red herring (never triggers in this case)
        if meta_info['meta'] < 0:
            return -999

        self.history.append(flag)
        return int(score)

# Global configuration (some irrelevant)
system_config = {
    'version': '3.7.1',
    'mode': 'diagnostic',
    'buffer_size': 2048,
    'debug_mode': False,
    'baseline_offset': 17
}

# Secondary utility: unused elsewhere (dead function)
def compress_sequence(seq):
    compressed = []
    for item in seq:
        if isinstance(item, str) and '_' in item:
            a, b = item.split('_')
            compressed.append((a, int(b) % 100))
    return compressed

# Main analysis pipeline
def analyze_pattern(log_entries, flags):
    # First stage: signal processing
    processed = process_signals(log_entries)
    
    # Second stage: engine initialization
    engine = DiagnosticEngine(threshold=25 + system_config['baseline_offset'])
    
    # Third stage: evaluation
    raw_value = engine.evaluate(processed)
    
    # Fourth stage: secondary check (bit manipulation red herring)
    bit_analysis = 0
    temp_val = raw_value
    while temp_val:
        bit_analysis += temp_val & 1
        temp_val >>= 1
    
    # Fifth stage: conditional override (never triggered)
    if 'OVERRIDE_KEY' in flags and flags['OVERRIDE_KEY'] == 0xDEADBEEF:
        return flags['ALT_RESULT']
    
    # Sixth stage: final adjustment using XOR with prime
    adjustment_factor = 1999  # A large prime
    tentative_result = raw_value ^ adjustment_factor
    
    # Seventh stage: sanity bounds check
    if abs(tentative_result) > 1000000:
        return 0
    
    # Eighth stage: final diagnostic computation
    final_diagnostic = abs(tentative_result) + len(engine.history)
    
    # Spurious logging (no effect)
    log_entry = f"DIAG:{final_diagnostic}:BITS:{bit_analysis}"
    
    return final_diagnostic

# Generate input data
log_entries = generate_telemetry()
system_flags = {'INIT_PHASE': True, 'SAFETY_CHECK_PASSED': False}

# Execute main analysis
temp_placeholder = process_signals(log_entries)  # Unused intermediate
interim_test = DiagnosticEngine(42).evaluate(temp_placeholder)  # Dead execution

# Critical statement
final_diagnostic = analyze_pattern(log_entries, system_flags)

print(f"Result: {final_diagnostic}")