import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

# Another decoy: unused transformation
def mirror_sequence(seq):
    return [seq[-i-1] for i in range(len(seq))]

# Core logic disguised among distractions
def generate_phases(base, count):
    phases = []
    temp = base
    for i in range(count):
        if i % 3 == 0:
            temp = (temp * 2) ^ 5
        elif i % 3 == 1:
            temp = (temp + 7) | 3
        else:
            temp = int(math.sqrt(temp ** 2 + 1))
        phases.append(temp)
    return phases

# Distractor: complex but unused data generation
def build_lattice(dim):
    lattice = [[(i*j + 1) % 17 for j in range(dim)] for i in range(dim)]
    trace = sum(lattice[i][i] for i in range(dim))
    return trace  # Never used

# Real transformation path
def transform_signal(raw):
    shifted = [(x << 1) ^ 3 for x in raw if x % 2 == 1]  # Bit manipulation + filtering
    amplified = [val * 1.5 for val in shifted]
    return amplified

# Key analysis function
def analyze_pattern(series, limit):
    cumulative = 0
    adjustment = 0
    for idx, value in enumerate(series):
        if value > limit:
            adjustment += 0.5
        # Conditional accumulation with nested logic
        if idx % 2 == 0 and value > 0:
            cumulative += math.floor(value - adjustment)
        else:
            cumulative -= int(adjustment)
    return int(cumulative)

# Irrelevant global constants (red herrings)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 8.75
ACTIVE_MODES = ['debug', 'trace', 'profile']

# Unused recursive function (dead code path)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Primary data initialization
base_input = [4, 7, 2, 9, 5, 12, 3]

# Distractor computations
entropy_value = compute_entropy([0.2, 0.3, 0.5])
lattice_trace = build_lattice(6)
phase_sequence = generate_phases(4, 5)

# Actual signal processing chain
filtered_amplitude = [x for x in base_input if x > 4]  # List comprehension
transformed_data = transform_signal(filtered_amplitude)

# Misleading intermediate
shadow_copy = [x for x in transformed_data]
for i in range(len(shadow_copy)):
    shadow_copy[i] = (shadow_copy[i] + 10) * 0.9  # Dead-end transformation

threshold = 8.5

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")