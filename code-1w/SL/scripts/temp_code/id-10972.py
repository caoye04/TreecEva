import math

def analyze_signal_strength(signal):
    # Irrelevant helper function (dead code path)
    return sum([s ** 2 for s in signal if s > 0]) // len(signal)

def decode_sequence(seq):
    # Another decoy function with no actual use
    base = 0
    for i, c in enumerate(seq):
        base += ord(c) * (31 ** i)
    return base % 1000

def filter_anomalies(data_stream):
    # Unused filtering logic to distract
    anomalies = set()
    for i, val in enumerate(data_stream):
        if val < 0 or val > 999:
            anomalies.add(i)
    return anomalies

def compute_entropy(values):
    # Distractor: looks important but unused
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def integrate_phase_vectors(phases):
    # Bit manipulation red herring
    acc = 0
    for p in phases:
        acc ^= int(p * 100) & 0xFF
    return acc | 0xABC

def main_pipeline():
    # Simulated system telemetry
    raw_readings = [127, 255, 64, 192, 32, 180, 95, 105]
    checksum_seed = 7
    temp_buffer = []

    # Irrelevant transformation chain
    for x in raw_readings:
        shifted = (x << 2) ^ checksum_seed
        normalized = shifted % 256
        temp_buffer.append(normalized)

    # Decoy data structure
    metadata_log = {
        'version': '2.1.5',
        'build': 'release-stable',
        'flags': ['OPTIMIZED', 'SECURE', 'LEGACY_MODE']
    }

    # Real computation begins here — deeply nested and mixed with noise
    log_data = [
        'ERR_CRITICAL@123', 'WARN_DISK@456', 'INFO_IDLE@789',
        'DEBUG_TRACE@101', 'STATUS_OK@202', 'TASK_DONE@303'
    ]

    error_codes = {line.split('@')[0] for line in log_data}
    timestamps = [int(line.split('@')[1]) for line in log_data]
    critical_count = sum(1 for code in error_codes if 'CRIT' in code)

    # String processing used meaningfully
    status_summary = ''.join([code[0] for code in sorted(error_codes)])
    summary_hash = sum(ord(c) * (7 ** i) for i, c in enumerate(status_summary)) % 10000

    # Control flow with red herrings
    system_state = {}
    for ts in timestamps:
        if ts % 3 == 0:
            system_state[ts] = 'STANDBY'
        elif ts % 2 == 0:
            system_state[ts] = 'ACTIVE'
        else:
            system_state[ts] = 'UNKNOWN'

    # Core logic hidden among distractions
    def evaluate_stability(ts_list, state_map):
        stable_windows = 0
        for t in ts_list:
            if state_map[t] == 'ACTIVE' and t > 200:
                stable_windows += 1
        return stable_windows * len(ts_list)

    stability_score = evaluate_stability(timestamps, system_state)

    # Multiple assignments and destructuring
    baseline, offset = 100, 17
    multiplier, _ = divmod(stability_score + summary_hash, 987)

    # Real calculation buried in noise
    diagnostic_chain = []
    for i in range(3):
        val = (baseline + offset * i) ** 2
        diagnostic_chain.append(val if val % 2 == 0 else val + 1)

    avg_diag = sum(diagnostic_chain) / len(diagnostic_chain)

    # Final computation depends only on specific derived values
    def process_metrics(logs, state):
        # Only this part matters
        valid_logs = [l for l in logs if 'OK' in l or 'DONE' in l]
        codes = [l.split('@')[0] for l in valid_logs]
        numeric_part = sum(int(l.split('@')[1]) for l in valid_logs)
        flag_weight = len([c for c in codes if 'DONE' in c]) * 100
        return numeric_part + flag_weight

    final_diagnostic = process_metrics(log_data, system_state)

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused complex structure to increase interference
    class DiagnosticNode:
        def __init__(self, value):
            self.value = value
            self.children = []

        def add_child(self, val):
            self.children.append(DiagnosticNode(val))

    root = DiagnosticNode(1)
    for i in range(2, 5):
        root.add_child(i)

    return final_diagnostic

if __name__ == '__main__':
    main_pipeline()