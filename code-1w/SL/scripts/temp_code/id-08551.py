from collections import defaultdict, Counter
import math

# Simulated sensor data processing with noise filtering and scoring
raw_readings = [127, 255, 93, 150, 64, 200, 180, 30, 75, 110]
timestamps = list(range(10))

# Irrelevant auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
offset_map = {k: v for k, v in zip(dummy_labels, raw_readings)}

# Noise threshold heuristic (not actually used in final computation)
noise_floor = sum(raw_readings) / len(raw_readings) * 0.3

# Signal categorization using bit manipulation (relevant)
categories = []
for val in raw_readings:
    if val & 128:  # checks if high bit set (>= 128)
        categories.append('HIGH')
    elif val & 64:  # checks if 64 bit set
        categories.append('MEDIUM')
    else:
        categories.append('LOW')

# Decoy function: looks important but unused (dead code path)
def legacy_process(data):
    return [x ^ 0xFF for x in data if x > 100]

# Another decoy: complex but irrelevant transformation
shifted_pairs = list(zip([x >> 2 for x in raw_readings[::2]], [x << 1 for x in raw_readings[1::2]]))
combined_shifts = [a ^ b for a, b in shifted_pairs]

# Real processing begins: count category transitions
transition_count = 0
cat_enum = list(enumerate(categories))
for i in range(len(cat_enum) - 1):
    if cat_enum[i][1] != cat_enum[i + 1][1]:
        transition_count += 1

# Weight assignment using lambda map (relevant)
weights = list(map(lambda x: 0.5 if x < 100 else (1.0 if x < 200 else 1.5), raw_readings))

# Construct time-weighted signal profile (only some components are used later)
signal_profile = defaultdict(float)
for idx, (t, v, w) in enumerate(zip(timestamps, raw_readings, weights)):
    signal_profile[t] = v * w

# Unused diagnostic: misleading intermediate statistic
peak_magnitude = max(signal_profile.values()) / (sum(raw_readings) / len(raw_readings))

# Historical averages (distractor - not used)
hist_avg = Counter(categories)
baseline_deviation = abs(hist_avg['HIGH'] - hist_avg['LOW'])

# Core logic: compute aggregate score based on weighted sum, transitions, and bit patterns
bitwise_integral = 0
for val in raw_readings:
    bitwise_integral ^= val  # cumulative XOR

# Final computation chain
weighted_sum = sum(signal_profile.values())
penalty_factor = transition_count * 0.7
bonus_modifier = math.log2(bitwise_integral + 1) if bitwise_integral > 0 else 0

# Critical statement
final_score = int(weighted_sum - penalty_factor + bonus_modifier)

# Output target result
print(f"Result: {final_score}")