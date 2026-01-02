import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [18, 22, 15, 30, 12, 25, 14, 20, 17, 23, 16, 28]

# Irrelevant statistical measures (distractors)
mean_value = sum(data_stream) / len(data_stream)
variance = sum((x - mean_value) ** 2 for x in data_stream) / len(data_stream)
std_deviation = variance ** 0.5
median_approx = sorted(data_stream)[len(data_stream)//2]

# Redundant copy and unused transformation
backup_stream = data_stream.copy()
scaled_data = [x * 1.05 for x in data_stream]

# Decoy function that is never called
def analyze_trend(seq):
    return sum(b > a for a, b in zip(seq, seq[1:]))

# Another decoy using itertools - not part of main logic
def generate_pairs(seq):
    return list(itertools.combinations(seq, 2))

# Misleading intermediate processing (dead code path)
filtered_anomalies = []
for reading in data_stream:
    if reading < 13 or reading > 27:
        filtered_anomalies.append(reading * 0.9)

# Real preprocessing: extract every second element above threshold
primary_signals = [x for x in data_stream[::2] if x > 15]

# Distractor: complex but unused filtering
advanced_filter = list(filter(lambda x: x % 3 == 0, scaled_data))

# Transform via windowed averaging (real path)
def sliding_window_avg(seq, size=2):
    return [sum(seq[i:i+size]) / size for i in range(len(seq)-size+1)]

# Apply windowing to primary signals
windowed_signals = sliding_window_avg(primary_signals, size=2)

# Secondary transformation: amplify based on position
amplification_factors = [(i + 1) * 1.1 for i in range(len(windowed_signals))]
amplified_values = [val * amp for i, (val, amp) in enumerate(zip(windowed_signals, amplification_factors))]

# Introduce irrelevant frequency analysis (distractor)
frequency_map = {k: len(list(g)) for k, g in itertools.groupby(sorted(data_stream))}

# Create synthetic correction offset (unused)
correction_offset = sum(frequency_map[k] * k for k in frequency_map if k < 20) / 100

# Key transformation: apply conditional scaling based on magnitude
transformed_data = [
    val * 1.5 if val >= 20 else val * 0.8
    for val in amplified_values
]

# Spurious dictionary mapping - looks important but isn't used
status_flags = {
    'high': [v for v in transformed_data if v > 30],
    'medium': [v for v in transformed_data if 20 <= v <= 30],
    'low': [v for v in transformed_data if v < 20]
}

# Additional red herring: attempt to detect cycles (not used)
def has_cycle(seq):
    seen = set()
    for x in seq:
        if x in seen:
            return True
        seen.add(x)
    return False

cycle_detected = has_cycle(scaled_data)

# Real processing function with nested logic
def process_sequence(seq):
    if not seq:
        return 0
    
    # Nested conditional expression
    base = sum(x for x in seq if x > 0) // len(seq)
    adjustment = sum(
        (i * x) // 2 for i, x in enumerate(seq) if i % 2 == 0
    )
    
    # Use of itertools.chain in meaningful computation
    extended_seq = list(itertools.chain(seq, [base, adjustment]))
    
    # Multi-step reduction
    temp_result = 0
    for idx, value in enumerate(extended_seq):
        if idx % 3 == 0:
            temp_result += value * 1.1
        elif idx % 3 == 1:
            temp_result -= value * 0.9
        else:
            temp_result += (value % 7) * 2
    
    # Final nonlinear transformation
    final_modifier = int(abs(temp_result)) % 5
    return int(temp_result + (final_modifier ** 2))

# Critical execution point
final_output = process_sequence(transformed_data)

print(f"Target result: {final_output}")