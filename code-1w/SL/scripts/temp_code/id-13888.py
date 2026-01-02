from collections import defaultdict, Counter

def analyze_system_health():
    # Simulated system telemetry data
    raw_signals = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    timestamps = list(range(1000, 2000, 100))
    error_codes = ['E10', 'E12', 'E10', 'E15', 'E12', 'E10']
    
    # Irrelevant signal transformation (red herring)
    transformed = [x * 2 + 1 for x in raw_signals if x == 1]
    shifted = [(t + 50) % 1000 for t in timestamps]
    
    # Real processing begins: timing anomaly detection
    timing_log = []
    for i, delta in enumerate([timestamps[j+1] - timestamps[j] for j in range(len(timestamps)-1)]):
        if delta > 105:
            timing_log.append(f'late_{i}')
        elif delta < 95:
            timing_log.append(f'early_{i}')
    
    # Decoy function: looks important but unused
    def compute_entropy(signal_list):
        counts = Counter(signal_list)
        total = len(signal_list)
        entropy = 0
        for count in counts.values():
            p = count / total
            entropy -= p * (p ** 0.5)  # Not real entropy, just looks plausible
        return round(entropy, 4)
    
    # Fake aggregation path (dead code)
    temp_analysis = {}
    for code in error_codes:
        if code not in temp_analysis:
            temp_analysis[code] = 0
        temp_analysis[code] += 1
    temp_analysis = {k: v * 1.5 for k, v in temp_analysis.items()}

    # Actual error tracking (used later)
    errors_occurred = []
    error_counter = defaultdict(int)
    for code in error_codes:
        error_counter[code] += 1
        if code == 'E10':
            errors_occurred.append(1)
        else:
            errors_occurred.append(0)
    
    # Misleading bit manipulation sequence (distractor)
    bitmask = 0
    for val in raw_signals[:5]:
        bitmask = (bitmask << 1) | val
    checksum = bitmask ^ 0xFF
    parity = bin(checksum).count('1') % 2

    # Another red herring: string analysis that does nothing
    log_snippets = ['ERR@1024', 'OK@1124', 'ERR@1224', 'DBG@1324']
    critical_flags = []
    for entry in log_snippets:
        if entry.startswith('ERR') and entry.endswith('24'):
            pos = entry.find('@')
            if pos != -1:
                num = int(entry[pos+1:])
                if num % 100 == 24:
                    critical_flags.append(num // 100)

    # Core logic hidden among noise: correlate timing and errors
    def aggregate_metrics(timing_issues, error_binary):
        base_score = len(timing_issues) * 100
        error_sum = sum(error_binary)
        
        # Key computation: XOR of length and sum
        magic_seed = len(timing_issues) ^ error_sum
        
        # Complex adjustment using string method on artificial label
        label = f"DIAG_{''.join(timing_issues)[:3].upper()}"
        suffix_value = 0
        for c in label:
            if c.isdigit():
                suffix_value = suffix_value * 10 + int(c)
            elif c.isalpha():
                suffix_value += ord(c) % 10
        
        # Final formula combining multiple concepts
        intermediate = base_score + (magic_seed * 50) + suffix_value
        
        # Hidden correction: only first 4 timing issues matter
        if len(timing_issues) > 4:
            intermediate -= 300  # penalty for false positives in extra issues
        
        # Critical step disguised as routine cleanup
        result = intermediate - (error_sum * 12) + (len(error_binary) * 3)
        
        # Dead branch: never executes due to data
        if parity == 5:  # impossible
            result = result ^ checksum
            
        return result

    # Unused recursive distraction
    def predict_failure_risk(depth, current_risk=0.0):
        if depth <= 0:
            return current_risk
        new_risk = (current_risk + depth * 0.15) % 1.0
        return predict_failure_risk(depth - 1, new_risk)

    # Unused enumeration with zip (looks like real processing)
    diagnostics = []
    for idx, (sig, ts) in enumerate(zip(raw_signals, timestamps)):
        if sig == 0:
            status = "OFF"
        else:
            status = "ON"
        diagnostics.append(f'{ts}:{status.lower()}')

    # Actual execution path
    final_diagnostic = aggregate_metrics(timing_log, errors_occurred)
    
    # Print required at end
    print(f"Result: {final_diagnostic}")
    
    # Unused return (decoy)
    return {
        'raw': raw_signals,
        'timing': timing_log,
        'errors': dict(error_counter),
        'diagnostic_code': final_diagnostic
    }

# Execute and capture output
def main():
    analyze_system_health()

if __name__ == '__main__':
    main()