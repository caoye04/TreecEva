import math

# Irrelevant astronomical constants (distractors)
gravitational_constant = 6.67430e-11
light_year_in_km = 9.4607e12
cosmic_variance_factor = 0.987

# Simulated quantum energy states (relevant data structure)
energy_states = [(-3, 1.2), (-1, 0.8), (0, 1.0), (2, 1.5), (4, 0.9)]

# Irrelevant signal processing function (dead code path)
def analyze_frequency(signal):
    return sum([x * math.sin(i) for i, x in enumerate(signal)]) if signal else 0

# Misleading entropy calculation with unused result (red herring)
entropy_proxy = sum([w * math.log(w) for _, w in energy_states if w > 0])
entropy_proxy += cosmic_variance_factor  # Further distraction

# Unused recursive decoy function (irrelevant)
def fibonacci_entropy(n):
    if n <= 1:
        return n
    return fibonacci_entropy(n-1) + fibonacci_entropy(n-2)

# Auxiliary physics-inspired transformation (partially relevant)
def apply_thermal_bias(level, weight):
    bias = math.exp(-abs(level) / 10)
    adjusted = weight * (1 + bias)
    normalization_shift = 0.1 * level  # Never used outside this function
    return adjusted

# Core combinatorial filter (relevant logic)
valid_transitions = list(filter(lambda x: x[0] >= 0, energy_states))

# Distractor: complex-looking but unused tensor operation
baseline_tensor = [[i*j*0.01 for j in range(3)] for i in range(3)]
tensor_trace = sum(baseline_tensor[i][i] for i in range(3))

# Fake state collapse simulation (irrelevant)
collapsed_state = None
for idx, (lvl, w) in enumerate(energy_states):
    if lvl == 0:
        collapsed_state = w * 2
        break
if collapsed_state is None:
    collapsed_state = -999  # Red herring value

collapsed_state *= gravitational_constant  # Further misdirection

# Real computation begins: weighted transformation using list comprehension
transformed_weights = [
    apply_thermal_bias(level, weight) for level, weight in valid_transitions
]

# Secondary filtering based on transformed magnitude (relevant)
significant_contributions = [
    tw for tw in transformed_weights if tw > 1.1
]

# Dummy combinatorics (distractor)
def count_combinations(n, r):
    if r > n or r < 0:
        return 0
    num = math.factorial(n)
    den = math.factorial(r) * math.factorial(n - r)
    return num // den

# Unused combination count (misleading intermediate)
possible_pairs = count_combinations(len(energy_states), 2)

# Critical aggregation step (key logic)
aggregated_energy = sum(significant_contributions) * len(valid_transitions)

# Final nonlinear scaling via logarithmic correction (relevant)
log_correction = math.log(aggregated_energy) if aggregated_energy > 0 else 0

class PhaseTransitionProcessor:
    def __init__(self, base_factor):
        self.base_factor = base_factor
        self.history = []

    def integrate(self, x):
        result = x * self.base_factor + 0.5
        self.history.append(result)
        return result

# Processor instantiation (relevant)
processor = PhaseTransitionProcessor(base_factor=1.75)

# Key statement in description
final_output = processor.integrate(log_correction)

# Thermodynamic potential derived from final output (answer variable)
thermodynamic_potential = int(final_output * 1000)  # Final deterministic scalar

print(f"Result: {thermodynamic_potential}")