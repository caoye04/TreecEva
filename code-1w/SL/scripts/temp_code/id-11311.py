import itertools

# Simulated telemetry data from a distributed sensor network
def collect_telemetry(nodes):
    raw_signals = []
    for node in nodes:
        base_freq = (node * 17) % 101
        noise = (node ** 2 + 42) % 19
        signal = (base_freq ^ noise) & 63
        raw_signals.append(signal)
    return raw_signals

# Irrelevant auxiliary function – dead code path
def legacy_calibrate(x):
    return (x + 3) * 7 % 1000

# Signal normalization using sliding window – partially relevant
def normalize_signal(data):
    window_size = 3
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window_size)
        segment = data[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(round(avg))
    return smoothed

# Misleading transformation chain
def encrypt_key(material):
    key = 0
    for val in material:
        key ^= val * 13
        key %= 98765
    return key + 1000  # red herring result

# Core diagnostic processor
def derive_entropy(pattern):
    entropy = 0
    for i, p in enumerate(pattern):
        if i % 2 == 0:
            entropy += p * (i + 1)
        else:
            entropy -= p // max((i - 1), 1)
    return abs(entropy) % 50000

# Critical function: computes health signature based on frequency coherence
def compute_coherence(amplitudes):
    pairs = list(itertools.combinations(amplitudes, 2))
    matches = 0
    total = 0
    for a, b in pairs:
        if a > 0 and b > 0:
            coherence = (a & b) | ((a ^ b) >> 1)
            if coherence > 20:
                matches += 1
            total += 1
    return matches / total if total > 0 else 0.0

# Secondary load metric – used later
def calculate_system_load(timestamps):
    weighted_sum = 0
    for t in timestamps:
        weight = (t % 7) + 1
        weighted_sum += (t * weight) % 15
    return weighted_sum % 1000

# Main processing pipeline
def process_metrics(signature, load):
    temp_a = (signature * 3) % 89
    temp_b = (load * 2) % 101
    fusion = temp_a ^ temp_b
    stage_1 = (fusion + 17) * 5
    stage_2 = (stage_1 ^ (stage_1 >> 3)) % 10000
    final = stage_2 - (stage_2 // 100)
    return final

# --- Simulation Entry Point ---
if __name__ == '__main__':
    # Sensor node IDs
    node_ids = [11, 13, 17, 19, 23, 29, 31]

    # Step 1: Collect raw telemetry signals
    raw_data = collect_telemetry(node_ids)

    # Step 2: Normalize signal stream
    filtered_data = normalize_signal(raw_data)

    # Step 3: Compute frequency coherence as base signature
    raw_signature = compute_coherence(filtered_data)
    health_signature = int(raw_signature * 1000)  # Convert to integer metric

    # Irrelevant cryptographic decoy
    secret_key = encrypt_key(raw_data)  # Unused value
    audit_log = [x * 2 for x in raw_data if x % 2 == 0]  # Dead-end analysis

    # Step 4: Generate timestamp sequence for load simulation
    time_stamps = [(n * 100 + 42) for n in range(1, 9)]
    system_load = calculate_system_load(time_stamps)

    # Step 5: Apply final diagnostic fusion algorithm
    final_diagnostic = process_metrics(health_signature, system_load)

    # Additional distractions
    anomalies = list(filter(lambda x: x > 30, filtered_data))
    correction_factor = sum(anomalies) if anomalies else 0
    adjusted_diag = final_diagnostic - correction_factor  # Not used

    # Output target result
    print(f"Result: {final_diagnostic}")