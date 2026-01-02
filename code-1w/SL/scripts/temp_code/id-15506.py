from collections import defaultdict, Counter
import math

# Simulated sensor array processing with diagnostic analysis
def preprocess_readings(raw_data):
    processed = []
    for val in raw_data:
        if val < 0:
            val = abs(val) * 1.5
        if val > 100:
            val = 99.9
        processed.append(round(val, 2))
    return processed

# Irrelevant helper: used to mislead about data importance
def calculate_entropy(sequence):
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Decoy function: appears important but unused in critical path
def validate_checksum(arr):
    chk = 0
    for i, v in enumerate(arr):
        chk ^= (v * (i + 1)) % 256
    return chk == 42

# Core transformation: builds logic grid from thresholds
def generate_logic_grid(values):
    grid = []
    for v in values:
        row = [
            int(v % 7 == 0),
            int(v > 50),
            int(v < 25),
            int((v * 1.6) % 1 < 0.3)
        ]
        grid.append(row)
    return grid

# Flag generation based on pattern rules
def extract_flags(grid):
    flag_state = defaultdict(int)
    temp_hist = []

    for i, row in enumerate(grid):
        flag_state['A'] += row[0]
        flag_state['B'] += row[1] and not row[2]
        flag_state['C'] += int(row[3] or (i % 4 == 0))

        # Dead computation branch - distractor
        if i > 10:
            running_avg = sum(temp_hist[-5:]) / 5 if temp_hist else 0
            flag_state['D'] = int(running_avg > 40)

        temp_hist.append(sum(row))

    # Unused flag update
    flag_state['X'] = 999  # red herring
    return dict(flag_state)

# Real-time anomaly scoring (irrelevant to final result)
def compute_anomaly_score(data):
    score = 0
    for x in data:
        if 10 < x < 30:
            score += 0.3
        elif x > 80:
            score += 0.7
    return round(score * 100, 1)

# Critical analysis function: computes final diagnostic
def analyze_pattern(grid, metadata):
    base = 0
    adjustment = 0

    for idx, row in enumerate(grid):
        # Complex conditional accumulation
        if row[1] and not row[2]:
            base += idx * (row[0] + 1)
        if row[3]:
            base += int(math.sin(idx * 0.5) * 10) % 3

        # Interdependent flag logic
        if metadata.get('A', 0) > 3:
            adjustment += 2
        if metadata.get('C', 0) % 2 == 0:
            adjustment -= 1

    # Final non-linear transformation
    result = (base ** 2) // (adjustment if adjustment != 0 else 1)
    return result + 5

# --- Main Execution ---
if __name__ == "__main__":
    # Raw sensor input (simulated)
    readings = [14, 63, 88, 7, 52, 19, 91, 4, 33, 76, 82, 11, 67, 2, 58]

    # Step 1: Preprocess sensor data
    calibrated = preprocess_readings(readings)

    # Step 2: Compute irrelevant metrics (distraction)
    entropy = calculate_entropy(calibrated)
    anomaly_score = compute_anomaly_score(calibrated)

    # Step 3: Generate core logic grid
    logic_grid = generate_logic_grid(calibrated)  # Key variable

    # Step 4: Extract control flags
    flags = extract_flags(logic_grid)  # Another key variable

    # Dead code block: looks like validation but not connected
    checksum_ok = validate_checksum([int(x) for x in calibrated])

    # Diagnostic accumulator (misleading intermediate)
    diag_trace = []
    for v in calibrated:
        if v % 10 == 0:
            diag_trace.append(v * 0.1)

    # CRITICAL STATEMENT
    final_diagnostic = analyze_pattern(logic_grid, flags)

    # Output target result
    print(f"Result: {final_diagnostic}")