def sensor_calibrate(raw):    
    # Irrelevant calibration routine (dead code path)
    if len(raw) == 0:
        return [0]
    scale = 1.0 if sum(raw) > 50 else 0.8
    return [x * scale + 2 for x in raw[:3]]

# Unused helper function (decoy)
def compress_signal(data):
    return [data[i] + data[-i-1] for i in range(len(data)//2)]

# Misleading preprocessing chain
def filter_noise(seq):
    temp_result = []
    for x in seq:
        if x > 10 and x < 90:
            temp_result.append(x * 0.95)
    return [round(x, 1) for x in temp_result]

# Another decoy transformation
def enhance_resolution(arr):
    enhanced = []
    for val in arr:
        enhanced.append(val * 1.1 if val < 75 else val * 0.9)
    return enhanced

# Core logic buried in distractions
def normalize_readings(values):
    total = sum(values)
    factor = 100.0 / total if total != 0 else 1
    return [round(v * factor, 2) for v in values]

# Data reconstruction red herring
def reconstruct_sequence(nums):
    rev = nums[::-1]
    paired = [nums[i] + rev[i] for i in range(len(nums))]
    return [p/2 for p in paired]

# Primary processing with string-based validation
def validate_and_extract(log_entry):
    # Uses string method (required feature)
    if not log_entry.strip().startswith("LOG"):\n        return []
    parts = log_entry.split(',')
    readings = []
    for part in parts[1:]:
        # More string processing
        cleaned = part.strip().replace('R:', '').replace('X', '')
        if cleaned.isdigit():
            readings.append(int(cleaned))
    return readings

# Critical data transformation
def process_readings_set(raw_logs):
    extracted = []
    for log in raw_logs:
        parsed = validate_and_extract(log)
        extracted.extend(parsed)
    filtered = filter_noise(extracted)
    # Only this line matters for final result
    normalized = normalize_readings(filtered)
    return normalized

# Final analysis function
def analyze_readings(data):
    baseline = sum(data) / len(data)
    variance = sum((x - baseline) ** 2 for x in data) / len(data)
    score = baseline * 0.7 + (1 / (1 + variance)) * 30
    return round(score, 4)

# Simulated sensor log input (string inputs with embedded numbers)
logs = [
    "LOG,SYS,X78,R:85,X,R:73",
    "LOG,INIT,R:60,R:95,X,R:88",
    "LOG,CAL,R:70,X,R:90,R:80"
]

# Dead variable assignments (distractors)
dummy_weights = [0.1, 0.2, 0.3, 0.4]
signal_matrix = [[1,2],[3,4]]
compression_ratio = 0.0

# Irrelevant data structure manipulation
temp_aggregate = {}
for i, log in enumerate(logs):
    temp_aggregate[f'entry_{i}'] = len(log.split(','))

# Unused intermediate arrays
raw_dump = []
for log in logs:
    raw_dump.extend([c for c in log if c.isdigit()])

# Actual execution begins here
parsed_readings = []
for log_entry in logs:
    reading_set = validate_and_extract(log_entry)
    parsed_readings.extend(reading_set)

# Apply correct processing pipeline
processed_data = process_readings_set(logs)

# This is the key statement
final_diagnostic = analyze_readings(processed_data)

# Print required output
print(f"Result: {final_diagnostic}")