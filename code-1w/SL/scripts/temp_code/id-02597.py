import math

# Simulated sensor data processing with embedded logic chain and distractions
def preprocess_signal(raw):    
    if len(raw) < 5:
        return [0]
    filtered = [x for x in raw if x > 0.5]  # Only positive significance
    smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]
    return smoothed[:10]

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_compatibility(data):
    temp = 0
    for x in data:
        temp += x * 0.9 + 2
    return int(temp // len(data)) if data else 0

# Core transformation with slicing and conditional mutation
def apply_envelope(signal, mode='adaptive'):
    envelope = []
    for i, val in enumerate(signal):
        if mode == 'adaptive' and i % 3 == 0:
            envelope.append(val * math.sin(i + 1))
        elif mode == 'static':
            envelope.append(val * 0.75)
        else:
            envelope.append(val * 1.1)
    # Slicing: take only middle segment if long enough
    if len(envelope) > 6:
        envelope = envelope[2:-2]
    return [round(e, 4) for e in envelope]

# Secondary processing – character counting distraction
# Counts non-whitespace characters in binary representation labels (red herring)
def count_binary_chars(values):
    total_chars = 0
    for v in values:
        bin_rep = bin(int(abs(v * 1000))) if v != 0 else '0'
        cleaned = ''.join([c for c in bin_rep if c in '01'])
        total_chars += len(cleaned)
    return total_chars  # Never actually used in main logic

# Data reshaping with decoy structure
class DataPacket:
    def __init__(self, seq, timestamp):
        self.seq = seq
        self.ts = timestamp
        self.checksum = sum(seq) * 0.1  # Unused attribute

# Misleading intermediate analysis (looks important but isn't)
def compute_robustness_index(seq):
    if not seq:
        return 0.0
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val)**2 for x in seq) / len(seq)
    return round(math.sqrt(variance), 4) if variance > 0.1 else 0.05

# Real computation path begins here — subtle activation via conditionals
def generate_baseline(length):
    base = []
    for n in range(1, length + 1):
        if n % 4 == 0:
            base.append(math.log(n))
        elif n % 3 == 0:
            base.append(math.sqrt(n))
        else:
            base.append(n ** 0.8)
    return [round(b, 4) for b in base]

# Key transformation involving slicing and comparison
def integrate_with_baseline(processed, baseline):
    result = []
    min_len = min(len(processed), len(baseline))
    for i in range(min_len):
        diff = abs(processed[i] - baseline[i])
        if diff < 1.0:
            result.append(diff * 1.5)
        else:
            result.append(1.0)
    # Critical slicing operation that affects final input size
    return result[-6:] if len(result) >= 6 else result

# Pattern analyzer — this is where the answer is determined
def analyze_pattern(pattern_vector):
    if len(pattern_vector) == 0:
        return 0
    total = 0.0
    for idx, p in enumerate(pattern_vector):
        if idx % 2 == 0:
            total += p * (idx + 1)
        else:
            total -= p * 0.5
    # Final nonlinear scaling
    if total > 5:
        return round(total ** 1.1, 4)
    elif total < 0:
        return round(abs(total) ** 0.95, 4)
    else:
        return round(total * 1.8, 4)

# --- Execution Flow with High Interference ---
raw_sensor_data = [0.3, 0.7, 1.2, 0.4, 0.9, 1.6, 2.1, 0.8, 1.3, 1.7, 0.6, 1.1]

# Step 1: Preprocess signal
filtered_data = preprocess_signal(raw_sensor_data)

# Distractor call — looks diagnostic but irrelevant
legacy_score = legacy_compatibility(filtered_data)

# Step 2: Apply envelope transformation
enveloped_signal = apply_envelope(filtered_data, mode='adaptive')

# Distractor: character counting on unused path
char_count = count_binary_chars(enveloped_signal)

# Step 3: Generate baseline for integration
baseline_reference = generate_baseline(len(enveloped_signal))

# Step 4: Integrate signals — produces critical vector
transformed_data = integrate_with_baseline(enveloped_signal, baseline_reference)

# Decoy object instantiation (misleading complexity)
packet = DataPacket(transformed_data, timestamp=1294875)

# Another red-herring metric
robustness = compute_robustness_index(transformed_data)

# --- CRITICAL EXECUTION POINT ---
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")