from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental monitoring
def preprocess_raw(data_stream):
    scaled = [x * 0.7 for x in data_stream if x > -50]
    filtered = [y for y in scaled if y < 1000]
    return filtered

# Irrelevant audio processing decoy
def enhance_audio(signal):
    return [int(s ** 1.1) for s in signal if s > 0]  # Dead-end path

# Signal conditioning with distractor logic
def clean_noise(readings):
    temp_store = []
    buffer_map = defaultdict(int)
    for i, val in enumerate(readings):
        buffer_map[i] = val % 7
        if i % 3 == 0:
            temp_store.append(val + 2)
        else:
            temp_store.append(val - 1)
    # Misleading transformation (not used later)
    normalized = [abs(t) ** 0.5 for t in temp_store if t != 0]
    return temp_store  # Only this matters

# Red herring: network latency simulation (unused)
def simulate_hop(latency_base, packets):
    results = []
    for p in range(packets):
        jitter = (p * 1.03) % 0.7
        results.append(latency_base + jitter)
    return sum(results)

# Core analysis function with critical branching
def analyze_readings(signals):
    stats = defaultdict(float)
    magnitude_count = Counter()

    for s in signals:
        category = 'high' if s > 15 else 'low' if s < 5 else 'medium'
        magnitude_count[category] += 1

    # Distractor accumulation
    phantom_total = 0
    for i in range(len(signals)):
        if i % 4 == 0:
            phantom_total += math.sin(i) * 100

    # Real logic chain starts here
    base_score = 0
    for val in signals:
        if val > 10:
            base_score += int(val // 2)
        elif val < 0:
            base_score -= int(abs(val) // 3)

    adjustment = 0
    if magnitude_count['high'] > magnitude_count['low']:
        adjustment = len(signals) * 2
    else:
        adjustment = -len(signals)

    intermediate = base_score + adjustment

    # Conditional expression with bitwise interference
    secondary_flag = (intermediate & 1) == 1
    multiplier = 1.5 if secondary_flag else 2.0

    # Critical combinatorics distractor (unused)
    combo_sum = 0
    for r in range(1, 4):
        combo_sum += math.comb(8, r)  # Irrelevant to final result

    # Final computation
    final_value = int(intermediate * multiplier)

    # Decoy assignment
    diagnostic_code = 999  
    diagnostic_code = 404  # Misdirection

    # Actual target variable
    final_diagnostic = final_value + 50
    return final_diagnostic

# Unused image sampling function (dead code)
def sample_pixels(resolution):
    pixels = resolution[0] * resolution[1]
    samples = [i for i in range(0, pixels, 100)]
    return len(samples)

# Main execution flow
raw_sensor_data = [23, -15, 8, 42, 67, -30, 5, 12, 18, 9, 55]

# Step 1: Preprocess
stream_output = preprocess_raw(raw_sensor_data)

# Step 2: Clean noise (actual usage)
processed_signals = clean_noise(stream_output)

# Step 3: Analyze (contains key statement)
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")