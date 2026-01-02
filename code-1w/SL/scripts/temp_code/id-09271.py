def analyze_pattern(sequence, threshold):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            count += 1
    return count > threshold

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x % 3 == 0)

# Misleading intermediate computation
temp_weights = [i * 1.5 for i in range(8)]
weight_adjustment = sum(temp_weights) / len(temp_weights)

# Real logic begins: character frequency analysis on encoded signal
signal = 'abccbaabcaaabcbbca'
char_freq = {}
for ch in signal:
    char_freq[ch] = char_freq.get(ch, 0) + 1

# Extract frequencies as list
frequencies = list(char_freq.values())
frequencies.sort()

# Slice middle portion (relevant)
middle_slice = frequencies[1:-1]

# Decoy set operations with irrelevant transformations
s1 = {x for x in frequencies if x > 2}
s2 = {x for x in temp_weights if x.is_integer()}
s3 = s1.union(s2).difference({3, 4})
set_red_herring = len(s3) * 2  # Distractor

# Simulate sensor drift correction (irrelevant but plausible)
corrected_readings = []
for i in range(5):
    val = (i + 1) * 0.9 + 0.1
    corrected_readings.append(int(val))

# Core algorithm: recursive segment scoring
def score_segment(seg):
    if len(seg) <= 1:
        return seg[0] if seg else 0
    mid = len(seg) // 2
    left = score_segment(seg[:mid])
    right = score_segment(seg[mid:])
    return left + right * (mid % 3 + 1)

# Apply scoring to sliced frequencies
segment_score = score_segment(middle_slice)

# Bit manipulation decoy
bit_fiddling = 0
for x in frequencies:
    bit_fiddling ^= (x << 2) | (x >> 1)

# Baseline adjustment using slicing and offset
baseline = sum(frequencies[::2]) / 2.0

# Metrics derived from multiple sources (only some relevant)
metrics = {
    'peak': max(frequencies),
    'spread': frequencies[-1] - frequencies[0],
    'density': len(signal) / (len(char_freq) or 1),
    'entropy_proxy': sum(x * x for x in middle_slice),
    'artificial_offset': weight_adjustment,  # Red herring
    'ghost_metric': set_red_herring  # More distraction
}

# Actual evaluation logic hidden among noise
def evaluate_performance(mets, base):
    raw = mets['entropy_proxy'] - mets['spread']
    adj = raw / (base or 1)
    bonus = 10 if analyze_pattern(frequencies, 2) else 0
    penalty = 5 if len(s2) > 6 else 0  # Depends on dead code values
    return int(adj + bonus - penalty)

# Critical execution point
final_score = evaluate_performance(metrics, baseline)

# Output result
print(f"Result: {final_score}")