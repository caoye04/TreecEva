import math

# Simulated sensor array diagnostics with signal processing
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = [144, 25, 64, 81]
thresholds = {'S1': 100, 'S2': 30, 'S3': 60, 'S4': 75}

# Irrelevant auxiliary data (distractor)
legacy_codes = [0xABCD, 0xEF01, 0x2345]
backup_flags = {'active': False, 'version': '2.1'}

# Signal preprocessing with filtering
processed_signals = []
for i, val in enumerate(raw_readings):
    normalized = math.sqrt(val)
    if normalized > thresholds[sensor_ids[i]] ** 0.5:
        processed_signals.append(int(normalized) + 10)
    else:
        processed_signals.append(int(normalized))

# Dead code path - never executed (distractor)
if False:
    for idx in range(len(processed_signals)):
        processed_signals[idx] = max(0, processed_signals[idx] - 5)

# Decoy function that looks important but isn't used
def compute_health_score(data):
    return sum(d ** 2 for d in data) / len(data)

# Auxiliary transformation using list comprehension (relevant)
corrected_offsets = [x * 2 if x > 15 else x + 3 for x in processed_signals]

# Bit manipulation red herring (irrelevant)
def scramble(value):
    return ((value << 3) & 0xFF) ^ 0xAA

scrambled_values = [scramble(x) for x in raw_readings]  # Unused result

# Conditional adjustment based on composite logic (relevant)
adjusted_signals = []
for x in corrected_offsets:
    if x % 2 == 0 and x > 12:
        adjusted_signals.append(x // 2)
    elif x < 10:
        adjusted_signals.append(x * 3)
    else:
        adjusted_signals.append(x)

# Nested logic block with mixed operations (key relevant section)
def analyze_readings(signals):
    base = 0
    multiplier = 1
    for s in signals:
        if s > 15:
            base += s // 4
        elif 10 <= s <= 15:
            base += s % 7
        else:
            base -= s // 3
        
        # Complex conditional nesting (3 levels deep)
        if s % 4 == 0:
            if multiplier < 5:
                multiplier *= 2
            else:
                multiplier += 1
        elif s % 3 == 0:
            multiplier = max(1, multiplier - 1)
    
    return base * multiplier

# Secondary decoy function (unused)
def evaluate_stability(seq):
    running_total = 0
    for item in seq:
        running_total += item ^ 0x55
    return running_total % 100

# Key computation point
final_diagnostic = analyze_readings(processed_signals)

# Final irrelevant transformations
post_processed = [math.floor(x * 1.5) for x in processed_signals if x > 8]
checksum = sum(post_processed) & 0xFFFF  # Red herring

print(f"Result: {final_diagnostic}")