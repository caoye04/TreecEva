from collections import defaultdict, Counter

# Simulated quantum register state (classical simulation)
quantum_register = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]

# Irrelevant signal processing artifacts
def process_noise_signal(signal):
    filtered = [s ^ 1 for s in signal[:len(signal)//2]]
    return [x * 2 for x in filtered]

noise_data = [1, 1, 0, 0, 1, 1, 0, 0]
decoy_output = process_noise_signal(noise_data)  # Dead path

# Auxiliary monitoring system with decoy logic
class SystemMonitor:
    def __init__(self):
        self.log = defaultdict(int)
        self.alerts = set()

    def update(self, val):
        self.log[val] += 1
        if val > 5:
            self.alerts.add('OVERFLOW')

monitor = SystemMonitor()
for bit in quantum_register:
    monitor.update(bit ^ 1)  # Misleading: tracks flipped bits but unused later

# Bit transformation pipeline
def apply_correction_code(bits):
    corrected = bits.copy()
    for i in range(1, len(bits)-1):
        # Majority vote correction (only affects middle elements)
        window = bits[i-1:i+2]
        corrected[i] = max(set(window), key=window.count)
    return corrected

corrected_register = apply_correction_code(quantum_register)

# Decoy statistical analysis
mean_value = sum(corrected_register) / len(corrected_register)
variance_proxy = sum((x - mean_value) ** 2 for x in corrected_register)
entropy_approx = len(set(corrected_register))  # Useless for binary data

# Real computation begins: frequency analysis
bit_frequencies = Counter(corrected_register)
dominant_bit = bit_frequencies.most_common(1)[0][0]

# Signal phase alignment (irrelevant slicing manipulation)
phase_shifted = corrected_register[3:] + corrected_register[:3]
reversed_phase = phase_shifted[::-1]

# Core diagnostic logic (depends only on frequency and pattern matching)
def detect_anomaly_pattern(seq):
    # Look for isolated 0s between 1s: [1,0,1] pattern
    anomalies = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] == 1 and seq[i] == 0 and seq[i+1] == 1:
            anomalies += 1
    return anomalies

anomaly_count = detect_anomaly_pattern(corrected_register)

# Red herring: complex-looking but unused matrix transformation
def generate_correlation_matrix(bits):
    n = len(bits)
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = bits[i] & bits[j]
    return matrix

# Unused heavy computation
correlation_map = generate_correlation_matrix(quantum_register)

# Destructuring decoy
top_three, *rest = [bit_frequencies.get(1), anomaly_count, entropy_approx, variance_proxy]

# Actual critical computation path
def analyze_system_state(register):
    # Step 1: corrected register already computed
    freq = Counter(register)
    
    # Step 2: find dominant bit
    dom_bit = freq.most_common(1)[0][0]
    
    # Step 3: count transitions (0->1 or 1->0)
    transitions = 0
    for i in range(1, len(register)):
        if register[i] != register[i-1]:
            transitions += 1
    
    # Step 4: calculate stability score (inversely proportional to transitions)
    stability = len(register) - transitions
    
    # Step 5: detect embedded control pattern [1,1,0,1]
    pattern_found = 0
    for i in range(len(register) - 3):
        if register[i:i+4] == [1, 1, 0, 1]:
            pattern_found += 1
    
    # Step 6: apply weighting formula
    raw_score = (freq[dom_bit] * 13) + (stability * 7) - (anomaly_count * 23)
    
    # Step 7: finalize diagnostic using pattern bonus
    final_score = raw_score + (pattern_found * 19)
    
    # Step 8: sanity clamp (not triggered here)
    if final_score < 0:
        final_score = 1
    
    return final_score

# Key execution point
final_diagnostic = analyze_system_state(quantum_register)

print(f"Target result: {final_diagnostic}")