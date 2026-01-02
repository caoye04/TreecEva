from collections import defaultdict, Counter
import math

# Irrelevant sensor simulation data (distractor)
baseline_noise = [0.01, -0.02, 0.005, 0.013, -0.008]
noise_accumulator = sum([abs(x) for x in baseline_noise if x != 0.005])

def deprecated_calibrate(x):  # Dead function - never called
    return x * 0.98 + 0.05

def generate_frequencies(n):
    return [i ** 1.5 for i in range(1, n+1)]

# Unused frequency map (red herring)
frequency_map = generate_frequencies(10)

# Core health monitoring variables
readings = [88, 92, 95, 87, 91, 96, 89, 94]
signal_power = [r ** 2 for r in readings]
validity_flags = [r % 2 == 0 for r in readings]

# Bit manipulation decoy
decoy_key = 0b110101
mask = 0b11110000
scrambled = (decoy_key << 3) ^ mask  # Unused result

# Logical aggregation with distractors
critical_count = 0
event_log = defaultdict(int)
for idx, val in enumerate(readings):
    event_log[f'sample_{idx}'] = val
    if val > 90:
        critical_count += 1
    elif val < 90:
        event_log['low_count'] += 1

# Distractor: complex but unused statistical calculation
mean_reading = sum(readings) / len(readings)
variance = sum((x - mean_reading) ** 2 for x in readings) / len(readings)
std_deviation = math.sqrt(variance)
adjusted_scores = [math.log(x) * math.cos(math.pi / 6) for x in readings]

# Fake diagnostic path (never taken due to condition)
temporary_state = None
if len(readings) < 5:
    temporary_state = 'QUARANTINE'
else:
    temporary_state = 'STABLE'  # This runs but isn't final

# Decoy data structure transformation
tuple_chain = [(r, validity_flags[i]) for i, r in enumerate(readings)]
filtered_chain = [t for t in tuple_chain if t[1]]
decoherence_score = sum(t[0] for t in filtered_chain)  # Looks important, unused

# Health signature built from multiple sources
health_signature = []
for r in readings:
    if r % 5 == 0:
        health_signature.append(r * 1.1)
    elif r % 4 == 0:
        health_signature.append(r * 0.95)
    else:
        health_signature.append(r * 1.02)

# Another red herring: set operations with no downstream effect
unique_readings = set(readings)
expected_range = set(range(85, 100))
overlap = unique_readings & expected_range  # 7 elements, but unused
anomalies = expected_range - unique_readings  # Distractor set

# Primary processing function with nested logic
def process_metrics(signature, raw):
    # Nested helper - looks complex
    def smooth(data):
        return [d * 0.99 for d in data]
    
    smoothed = smooth(signature)
    
    # Multiple layers of conditional accumulation
    total = 0
    multiplier = 1
    for i, s in enumerate(smoothed):
        if i % 3 == 0:
            total += s * 1.1
        elif i % 3 == 1 and raw[i] > 90:
            total -= s * 0.05
        else:
            total += math.sqrt(s)  # Nonlinear contribution
    
    # Bitwise distraction inside function
    key_token = 0b1010
    if len(raw) & 1:
        key_token ^= 0b0101
    
    # Final adjustment using list comprehension and counting
    flag_counter = Counter(validity_flags)
    true_flags = flag_counter[True]
    
    # The actual answer depends on this final computation
    final_adjustment = total * (1 + (true_flags / len(raw)))
    
    # Decoy return branch (never reached)
    if False and key_token == 0:
        return int(sum(smoothed))
    
    return final_adjustment

# Critical execution point
final_diagnostic = process_metrics(health_signature, readings)

# Output the target result
print(f"Target result: {final_diagnostic}")