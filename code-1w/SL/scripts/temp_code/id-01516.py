import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings(raw_sequence):
    readings = []
    for val in raw_sequence:
        if val < 0:
            adjusted = abs(val) * 1.2
        elif val == 0:
            adjusted = 0.1
        else:
            adjusted = val * 0.9 + 0.05
        readings.append(round(adjusted, 3))
    return readings

# Irrelevant transformation: frequency domain mock-up (not used in final result)
def compute_harmonics(signal):
    harmonics = []
    for i in range(len(signal)):
        h = signal[i] * math.sin(i * 0.5) + math.cos(i)
        harmonics.append(round(h, 4))
    return harmonics

# Core processing: extract and filter meaningful segments
def extract_segments(data_stream, threshold=1.5):
    segments = []
    current_seg = []
    for x in data_stream:
        if x > threshold:
            current_seg.append(x)
        else:
            if len(current_seg) > 2:
                segments.append(current_seg[:])
            current_seg.clear()
    if len(current_seg) > 2:
        segments.append(current_seg)
    return segments

# Misleading energy calculation (unused in logic path)
def calculate_energy(segment):
    total = 0
    for val in segment:
        total += val ** 2
    return round(total, 3)

# Character-based tag generation (uses string methods but only one is relevant)
def generate_tag(segment):
    length_str = str(len(segment))
    sum_str = str(int(sum(segment)))
    # Relevant use: concatenation and digit counting
    combined = length_str + sum_str
    digit_sum = sum(int(d) for d in combined)
    label = f"SEG{digit_sum}"
    checksum = len(label.replace('S', '').replace('E', ''))  # Uses string replace
    return label, checksum

# Data refinement with early termination
def refine_segment(seg):
    if len(seg) < 3:
        return None
    filtered = [x for x in seg if x >= 1.0]
    if sum(filtered) < 5.0:
        return None  # Early exit
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Signal processor that performs key transformations
def process_signal_chunk(segment_list):
    results = []
    for seg in segment_list:
        refined = refine_segment(seg)
        if refined is None:
            continue
        avg_val = round(sum(refined) / len(refined), 3)
        results.append(avg_val)
    return results

# Diagnostic engine: determines system state based on processed input
def analyze_signal(diag_input):
    baseline = 0.75
    deviation = 0
    count = 0
    for val in diag_input:
        if val > baseline:
            deviation += (val - baseline)
            count += 1
    if count == 0:
        return 0
    avg_deviation = deviation / count
    score = int(avg_deviation * 1000)
    return score

# === MAIN EXECUTION WITH DISTRACTORS ===
raw_data = [2.1, -1.5, 3.2, 4.1, 0.8, 2.9, 3.3, 1.1, 0, 4.4, 5.0, 2.7, 1.3, 3.6]

# Step 1: Collect and adjust raw sensor readings
adjusted_readings = collect_readings(raw_data)

# Distractor: unused harmonic analysis
harmonic_components = compute_harmonics(adjusted_readings)
energy_signature = sum([x**2 for x in harmonic_components])  # Dead computation

# Step 2: Extract valid data segments above threshold
extracted_parts = extract_segments(adjusted_readings, threshold=1.4)

# Distractor: tagging each segment (only side effect is string manipulation)
tags_and_codes = []
for part in extracted_parts:
    tag_info = generate_tag(part)
    tags_and_codes.append(tag_info)

# Distractor: calculate energies for all segments (never used)
energies = []
for p in extracted_parts:
    e_val = calculate_energy(p)
    energies.append(e_val)

# Step 3: Refine and normalize segments
refined_chunks = []
for piece in extracted_parts:
    clean_piece = refine_segment(piece)
    if clean_piece:
        refined_chunks.append(clean_piece)

# Step 4: Process chunk into aggregate values
if refined_chunks:
    processed_chunk = process_signal_chunk(refined_chunks)
else:
    processed_chunk = [0.75]

# Key statement: final diagnostic score computed from processed data
final_diagnostic = analyze_signal(processed_chunk)

# Print result as required
print(f"Target result: {final_diagnostic}")