import math

# Simulated hardware diagnostics with mixed signal processing
logic_gates = [True, False, True, True, False]
transmission_log = [0b101, 0b110, 0b001, 0b111]
system_state = {'voltage': 3.7, 'overclocked': False, 'phase_shift': 1.5}

temp_buffer = []
checksum = 0
redundant_flag = False
counterfeit_data = [x ** 3 for x in range(6)]  # Irrelevant computation

# Dead code path - never executed
if False:
    legacy_mode = True
    for i in range(5):
        temp_buffer.append(i * 2)

# Distractor: complex-looking but unused transformation
spectral_analysis = list(map(lambda x: (x << 2) ^ 0b1010, transmission_log))

# Misleading intermediate diagnostic with partial relevance
interim_result = sum([int(math.log2(x + 1)) for x in transmission_log if x > 0])

# Unused recursive red herring
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

# Irrelevant prime check (dead-end logic)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

prime_flags = [is_prime(x) for x in [4, 6, 8, 9, 10]]

# Real processing begins here — heavily buried
active_channels = len([gate for gate in logic_gates if gate])
baseline = system_state['voltage'] * 100

# Conditional expression with side effect avoidance
adjustment_factor = 1.2 if system_state['overclocked'] else 0.9

# Key transformation using lambda in non-trivial context
apply_correction = lambda val, adj: round(val * adj, 2)

corrected_baseline = apply_correction(baseline, adjustment_factor)

# Bit manipulation disguised as noise
shift_register = (transmission_log[0] << 1) & 0b1111

# Core logic hidden among distractions
phase_angle = int(system_state['phase_shift'] * 10)

# Conditional branches with shared variables
if active_channels > 2:
    if phase_angle > 10:
        status_code = 7
    else:
        status_code = 5
else:
    status_code = 3

# Another decoy calculation
entropy_score = -sum([p * math.log2(p) for p in [0.25, 0.25, 0.25, 0.25]])

# Data structure mix: set operations with filtering
unique_signals = set()
for log in transmission_log:
    unique_signals.add(log & 0b011)  # Extract lower bits

# Final metric assembly — depends on prior scattered state
def process_metrics(gates, state):
    core_metric = len(gates) * 100
    voltage_mod = int(state['voltage'] * 10)
    gate_influence = sum(gates) * voltage_mod
    
    # Nested conditional expression
    modifier = 1.15 if len(unique_signals) >= 2 and not state['overclocked'] else 0.85
    
    # Critical arithmetic with modular influence
    temp_result = (core_metric + gate_influence) * modifier
    
    # Final adjustment based on status code (from earlier branch)
    if status_code == 5:
        temp_result -= 50
    elif status_code == 7:
        temp_result += 25
    
    return int(temp_result) % 10000

# Execution point of interest
final_diagnostic = process_metrics(logic_gates, system_state)

# Print required result
print(f"Result: {final_diagnostic}")