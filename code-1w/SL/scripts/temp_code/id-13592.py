def analyze_system_load(raw_data, config):
    # Irrelevant preprocessing (distractor)
    sanitized = [x for x in raw_data if isinstance(x, dict) and 'meta' in x]
    temp_flags = set()
    for entry in sanitized:
        if entry['meta'].get('version', 0) < 2:
            temp_flags.add('legacy')

    # Core logic disguised among noise
    critical_codes = {102, 204, 409}
    error_count = 0
    warning_tally = 0
    state_history = []

    # Real but obscured data extraction
    for item in raw_data:
        code = item.get('status', 0)
        if code in critical_codes:
            error_count += 1
            state_history.append(code)
        elif 100 <= code < 500:
            warning_tally += 1

    # Decoy aggregation function (never used)
    def aggregate_diagnostics(data):
        return sum(d.get('weight', 1) * d.get('severity', 0) for d in data)

    # Red herring: complex transformation with no impact
    derived_signals = []
    for i, d in enumerate(raw_data):
        signal = (i ^ d.get('status', 0)) & 0xFF
        if signal > 128:
            derived_signals.append(signal)

    # Real logic begins: filter valid logs
    log_entries = [e for e in raw_data if e.get('type') == 'LOG']
    system_thresholds = config.get('limits', {})

    # Misleading intermediate calculation
    baseline_score = len(sanitized) * config.get('multiplier', 1) - warning_tally
    adjustment_factor = 0.85 if 'adjust' in config else 1.0

    # Actual core processing hidden in lambda
    severity_weight = lambda x: 2 if x == 409 else (1 if x == 204 else 0)
    weighted_errors = sum(severity_weight(code) for code in state_history)

    # Another decoy structure
    class DiagnosticBuffer:
        def __init__(self):
            self.buffer = []
        def push(self, val):
            self.buffer.append(val)
    # Unused object instantiation
    buffer = DiagnosticBuffer()

    # Key control flow with nested conditions
    def process_metrics(logs, thresholds):
        threshold_a = thresholds.get('error_cap', 10)
        threshold_b = thresholds.get('weight_floor', 3)
        cap_exceeded = error_count > threshold_a
        floor_met = weighted_errors >= threshold_b

        # Nested logic path with distractors
        temp_result = 0
        for log in logs:
            if 'payload' in log:
                size = len(str(log['payload']))
                temp_result ^= size  # Bit manipulation red herring

        # Critical assignment buried here
        if cap_exceeded and not floor_met:
            result_code = 888
        elif not cap_exceeded and floor_met:
            result_code = 777
        else:
            result_code = 999

        # Final computation using correct path
        final_shift = (weighted_errors << 2) + (result_code % 7)
        return final_shift  # This is the real answer source

    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_thresholds)

    # Dead code path (never reached)
    if False:
        fallback = baseline_score * adjustment_factor
        final_diagnostic = int(fallback) if fallback > 0 else 0

    # Correct output
    print(f"Target result: {final_diagnostic}")

# Seeded synthetic input to ensure determinism
input_data = [
    {'type': 'LOG', 'status': 409, 'meta': {'version': 2}},
    {'type': 'LOG', 'status': 204, 'meta': {'version': 2}},
    {'type': 'LOG', 'status': 409, 'meta': {'version': 2}},
    {'type': 'EVENT', 'status': 102},
    {'type': 'LOG', 'status': 204, 'meta': {'version': 2}},
    {'type': 'LOG', 'status': 409, 'meta': {'version': 1}},  # legacy
]

config_params = {
    'limits': {
        'error_cap': 3,
        'weight_floor': 3
    },
    'multiplier': 2,
    'adjust': True
}

# Execute
analyze_system_load(input_data, config_params)