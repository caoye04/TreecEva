def analyze_system_load(raw_data, threshold_config):
    # Irrelevant preprocessing (distractor)
    normalized_data = [x * 1.05 for x in raw_data if x > 0]
    filtered_data = list(filter(lambda x: x < threshold_config['max_limit'], normalized_data))

    # Unused function - red herring
    def deprecated_analysis(seq):
        return sum([i * seq[i] for i in range(len(seq))])

    # Simulated log weights (not used in final calculation)
    weights = [0.8, 1.2, 0.9, 1.1]
    weighted_logs = [raw_data[i % len(raw_data)] * weights[i % len(weights)] for i in range(8)]

    # Core logic disguised among distractions
    active_segments = []
    for i, val in enumerate(raw_data):
        if val > threshold_config['critical']:
            active_segments.append(i)

    # Decoy aggregation (never used)
    avg_weighted = sum(weighted_logs) / len(weighted_logs) if weighted_logs else 0
    peak_load = max(raw_data) * 1.0  # Misleading intermediate

    # Real processing begins here
    def generate_diagnostics(entries, crit):
        diagnostics = []
        for idx, entry in enumerate(entries):
            if entry > crit:
                # Bit manipulation as part of real logic
                encoded = (idx << 2) ^ int(entry / 10)
                diagnostics.append(encoded)
        return diagnostics

    # Another decoy structure
    class LoadSimulator:
        def __init__(self, data):
            self.data = data
            self.sim_result = None

        def run(self):
            self.sim_result = sum(x ** 0.5 for x in self.data)  # Dead code path

    simulator = LoadSimulator(raw_data)
    simulator.run()  # Execution has no effect on result

    # Actual critical path
    log_entries = [x for x in raw_data if x > 40]  # Filter meaningful entries
    system_threshold = threshold_config['critical']

    temp_results = []
    for i, val in enumerate(log_entries):
        # Using enumerate and zip meaningfully but with distraction
        shift_factor = i % 3 + 1
        adjusted = (val >> shift_factor) + (i & 3)
        temp_results.append(adjusted)

    # Real transformation using lambda
    transform = lambda x: x * 2 + 1
    processed_values = [transform(x) for x in temp_results]

    # Key computation hidden in middle
    checksum = 0
    for i, v in enumerate(processed_values):
        checksum += v ^ (i + 1)

    # Final diagnostic derived from core logic
    final_diagnostic = checksum & 0xFFFF  # Ensure within bounds

    # Unrelated string operations (distractor)
    status_msg = "System OK"
    if 'urgent' in status_msg.lower():
        status_msg = status_msg.replace("OK", "ALERT")

    # Unused tuple unpacking
    try:
        a, b = (100, 200)
        c, d = b, a  # Dead assignment
    except:
        pass

    return final_diagnostic

# Main execution
config = {
    'max_limit': 150,
    'critical': 65
}

data_stream = [30, 45, 70, 55, 80, 90, 40, 60, 75]

# Entry point
final_diagnostic = analyze_system_load(data_stream, config)
print(f"Result: {final_diagnostic}")