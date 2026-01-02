import math

# Simulated hardware diagnostic system with red herrings and complex logic

def analyze_subsystem(data, mode):
    if mode == 'A':
        return sum(x ** 2 for x in data if x > 0)
    elif mode == 'B':
        return math.prod([x for x in data if x % 2 == 1])
    else:
        return 0

# Irrelevant helper (dead code path)
def deprecated_calibrate(values):
    scaling = 1.75
    adjusted = [v * scaling for v in values]
    return adjusted[::-1]

# Unused but plausible function
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

# Core logic disguised among distractions
gate_specs = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b,
    'NAND': lambda a, b: ~(a & b) & 0b1
}

# Misleading intermediate structure (not directly used in final result)
signal_chain = [
    {'input': (1, 0), 'gate': 'AND', 'active': False},
    {'input': (1, 1), 'gate': 'OR', 'active': True},
    {'input': (0, 1), 'gate': 'XOR', 'active': True}
]

# Distractor variables
baseline_offset = 347
reference_checksum = 0
redundant_buffer = [0] * 16

# Real data sources
logic_gates = ['AND', 'XOR', 'OR', 'NAND']
raw_signals = [0b1101, 0b1010, 0b1111, 0b0001]

# Signal processing with multiple layers
processed_pairs = []
for i in range(len(raw_signals)):
    hi = (raw_signals[i] >> 4) & 0b1111
    lo = raw_signals[i] & 0b1111
    processed_pairs.append((hi, lo))

# Decoy transformation
transformed = list(map(lambda p: (p[0] ^ 0b1010, p[1] << 1), processed_pairs))

# Actual system state derived subtly
system_state = []
for idx, pair in enumerate(processed_pairs):
    a, b = pair[0] % 2, pair[1] % 2  # Extract LSBs
    result = 0
    gate = logic_gates[idx % len(logic_gates)]
    if gate in gate_specs:
        result = gate_specs[gate](a, b)
    system_state.append(result)

# Fake aggregation (unused)
temp_aggregate = analyze_subsystem(system_state, 'A')

# Critical distraction: complex-looking but irrelevant calculation
shadow_accumulator = 0
for x in system_state:
    shadow_accumulator += (x * x) + baseline_offset
    if shadow_accumulator > 1000:
        shadow_accumulator //= 2

# Another red herring: string-based checksum (unrelated)
status_flag = ''.join(str(s) for s in system_state)
flag_value = sum(ord(c) for c in status_flag) % 256

# Real computation buried in abstraction
def evaluate_resilience(bits):
    runs = 0
    for i in range(1, len(bits)):
        if bits[i] != bits[i-1]:
            runs += 1
    return runs

# Primary metric
transition_score = evaluate_resilience(system_state)

# Secondary metric
activation_density = sum(system_state) / len(system_state) if system_state else 0

# Final processing with conditional expression and dictionary lookup
metric_weights = {'transitions': 3.7, 'density': 2.4}

# Key statement containing answer
def process_metrics(gates, state):
    base = transition_score * metric_weights['transitions']
    adj = activation_density * metric_weights['density']
    correction = len(gates) if 'NAND' in gates else 0
    temp_result = base + adj + correction
    # Final adjustment using lambda and conditional expression
    finalize = lambda x: round(x, 4)
    return finalize(temp_result * (1.05 if sum(state) > 2 else 1.0))

final_diagnostic = process_metrics(logic_gates, system_state)
print(f"Target result: {final_diagnostic}")