from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(187):
        if i % 7 == 0:
            signals.append(('ERROR', i * 3 % 11))
        elif i % 5 == 0:
            signals.append(('WARNING', i // 4))
        else:
            signals.append(('INFO', i % 13))
    return signals

def filter_relevant_logs(raw_logs):
    # Irrelevant preprocessing: transforms data but not used in final path
    temp_map = defaultdict(list)
    for level, code in raw_logs:
        temp_map[level].append(code)
    
    # Distractor transformation chain
    aggregated = {}
    for k, v in temp_map.items():
        aggregated[k] = sum(v) // len(v) if v else 0
    
    # Another red herring: complex but unused structure
    histogram = Counter([code for _, code in raw_logs if code % 2 == 1])
    rare_codes = [c for c, cnt in histogram.items() if cnt < 3]

    # ACTUAL relevant subset (buried in distractions)
    critical_codes = [code for level, code in raw_logs if level == 'ERROR' and code % 3 == 2]
    return critical_codes

def compute_diagnostic_score(seq):
    # Complex but partially irrelevant scoring
    if not seq:
        return -1
    
    # Meaningful intermediate: modular accumulation
    acc = 0
    for i, val in enumerate(seq):
        acc += (val * (i + 1)) % 97
    
    # Redundant branching - distracts from core logic
    if acc > 1000:
        acc = acc // 2
    elif acc > 500:
        acc = acc - 100
    
    # Secondary transformation on bit pattern
    bit_analysis = 0
    for shift in [2, 4, 6]:
        bit_analysis ^= (acc >> shift) & 0xF
    
    return (acc * 3) ^ bit_analysis  # Final obfuscation

def validate_sequence(s):
    # Unused validation function (dead code path)
    return all(x >= 0 for x in s) and len(set(s)) > 1

def decode_signature(values):
    # Another decoy function that looks important
    if len(values) < 5:
        return None
    sig = 0
    for v in values[:5]:
        sig = (sig * 31 + v) % 65536
    return hex(sig)

def analyze_pattern(logs, flags):
    # Core logic hidden among multiple inputs
    base_values = filter_relevant_logs(logs)
    
    # Flags contain misleading info
    mode_flag = flags.get('ENHANCED', False)
    debug_level = flags.get('DEBUG_DEPTH', 0)
    
    # Real computation
    score = compute_diagnostic_score(base_values)
    
    # Final adjustment using set operations (meaningful but subtle)
    seen_mods = {v % 7 for v in base_values}
    modifier = len(seen_mods.intersection({2, 3, 5}))
    
    # Critical deterministic assignment
    final_diagnostic = (score * 2) + modifier
    
    # Dead code to obscure flow
    if mode_flag:
        dummy = [x * debug_level for x in base_values if x > 50]
        final_diagnostic += sum(dummy) % 100  # Never reached due to flag
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Generate real input
    log_entries = generate_telemetry()
    
    # Configuration with red herring parameters
    system_flags = {
        'ENHANCED': False,           # Misleading - looks like it enables something
        'DEBUG_DEPTH': 7,            # Unused in active path
        'AUDIT_MODE': 'FULL',        # Completely irrelevant
        'TIMEOUT_MS': 1500          # Distractor constant
    }
    
    # Key statement
    final_diagnostic = analyze_pattern(log_entries, system_flags)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")