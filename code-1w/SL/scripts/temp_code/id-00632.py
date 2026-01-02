from collections import defaultdict, Counter
import math

# Simulated sensor data processing with integrity checks
def analyze_readings(raw_data):
    readings = [x for x in raw_data if isinstance(x, (int, float)) and x >= 0]
    filtered = list(map(lambda x: x * 0.9 + 0.1, readings))
    
    # Irrelevant transformation chain (distractor)
    temp_offset = sum(filtered) / len(filtered) if filtered else 0
    adjusted = [math.sin(x / 10) for x in filtered]
    normalized = [abs(y) ** 0.5 for y in adjusted]

    # Actual relevant computation begins
    histogram = defaultdict(int)
    for val in readings:
        bucket = int(math.log(val + 1, 2)) if val > 0 else 0
        histogram[bucket] += 1

    mode_bucket = max(histogram.items(), key=lambda x: x[1])[0]
    
    # Decoy scoring function (never called)
    def evaluate_coherence(data):
        return sum([bin(int(x))[2:].count('1') for x in data if x > 0])

    # Secondary irrelevant analysis
    binary_pattern = ''.join([str(len(bin(int(x)))-2) % 2) for x in readings[:5]])
    parity_check = binary_pattern.count('1') % 3

    # Core logic disguised among distractions
    def assess_stability(seq):
        if not seq:
            return 0
        diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
        variance = sum(d**2 for d in diffs) / len(diffs) if diffs else 0
        return round(math.sqrt(variance), 4)

    stability_metric = assess_stability(readings)

    # Red herring: complex but unused structure
    class DiagnosticFrame:
        def __init__(self, values):
            self.data = values
            self.checksum = sum(v * (i+1) for i, v in enumerate(values))

        def validate(self):
            return self.checksum % 7 == 0

    frame = DiagnosticFrame(readings)

    # Real pathway: counting digit frequencies in string representation
    digit_string = ''.join([str(int(x)) for x in readings if x > 0])
    digit_freq = Counter(digit_string)
    
    # Misleading intermediate score (not final)
    pseudo_entropy = -sum((freq/len(digit_string)) * math.log(freq/len(digit_string)) 
                          for freq in digit_freq.values())

    consistency_log = []
    for digit, count in sorted(digit_freq.items()):
        if int(digit) % 2 == 0:
            consistency_log.append(count * int(digit))
        else:
            consistency_log.append(count - int(digit))

    # Final computation buried in abstraction
    def compute_integrity_score(log_entries):
        base = sum(log_entries)
        correction = len([x for x in log_entries if x > 5])
        penalty = bin(base).count('1')  # Bit manipulation red herring
        return base + correction - penalty

    final_diagnostic = compute_integrity_score(consistency_log)

    # Dead code paths (unused functions)
    def calculate_robustness_index(seq):
        return math.prod([x % 5 + 1 for x in seq]) % 1000
    
    def generate_audit_trace():
        return ''.join(chr(97 + i % 26) for i in range(20))

    # Output the required result
    print(f"Result: {final_diagnostic}")