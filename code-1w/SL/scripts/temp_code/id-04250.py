import math

# Simulated sensor data processing pipeline with red herrings
def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    return sum(a * b for a, b in zip(sequence, sequence[1:]))

def compute_harmonic_energy(signal):
    # Irrelevant energy computation (dead end)
    total = 0
    for x in signal:
        total += math.sin(x) * math.cos(x)
    return total

def evaluate_resonance(pattern):
    # Unused resonance detection logic
    if not pattern:
        return 0
    peak = max(pattern)
    trough = min(pattern)
    return (peak - trough) ** 1.5 if peak != trough else 0

# Core transformation chain
buffer = [x % 7 for x in range(15) if x % 2 == 1]

# Distractor: complex but unused frequency mapping
echo_map = {i: round(math.tan(i * 0.3), 4) for i in range(1, 10)}

# Decoy function that looks important but isn't called in main path
deco_filter = lambda arr: [x for x in arr if x & 1 and x > 2]

processed_chunk = []
for val in buffer:
    if val == 0:
        continue
    processed_chunk.append((val ** 2) - (val % 3))

# Secondary distraction: bit manipulation on derived values
bit_flags = 0
for num in processed_chunk:
    bit_flags ^= (num << 1) | (num >> 2)

# Tertiary red herring: character counting from numeric labels (no-op relevance)
data_tags = ['node_{}'.format(x) for x in processed_chunk]
char_count = sum(len(tag) for tag in data_tags) % 997  # Large prime mod

# Actual critical transformation
transform_buffer = lambda chunk: math.floor(
    sum(math.log(abs(x) + 1) for x in chunk) * 1.75
)

# Key assignment point
filtration_score = transform_buffer(processed_chunk)

# Final red herring: conditional override that never triggers (misleading)
if any(x > 100 for x in echo_map.values()):
    filtration_score = -1  # Dead code path

print(f"Result: {filtration_score}")