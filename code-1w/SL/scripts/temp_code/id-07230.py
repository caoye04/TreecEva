import math

# Irrelevant constants (distractors)
BASELINE_OFFSET = 3.14159
CALIBRATION_FACTOR = 0.0023
REFERENCE_VOLTAGE = 12.0
MAX_ITERATIONS = 500

# Unused auxiliary functions (dead code paths)
def deprecated_transform(x):
    return (x ** 2 + 2 * x + 1) % 7

def legacy_calibrate(signal):
    if signal < 0:
        return math.log(abs(signal) + 1)
    return signal * 0.95

# Red herring variables
transient_state = [0] * 16
accumulated_noise = 0.0
sync_threshold = None

# Core logic disguised among distractions
def frequency_modulate(signal, phase):
    # Real but indirectly used function
    return (signal * math.sin(phase)) + (phase * math.cos(signal))

def harmonic_envelope(n, base):
    total = 0.0
    for i in range(1, n + 1):
        total += math.sin(i * base / 4) / i
    return total

# Lambda with meaningful role (required feature)
adaptive_filter = lambda x, y: (x * y) / (abs(x) + abs(y) + 1e-8)

# Misleading intermediate that looks important but isn't final
diagnostic_trace = []
for t in range(10):
    diagnostic_trace.append(math.tan(t * 0.1) if t % 2 == 0 else 0)

# Primary computational chain begins here
def thermal_matrix(freq, harmonic_list):
    # Level 1: Initial setup
    magnitude = 0.0
    damping = freq ** 0.5
    
    # Level 2: Accumulation over harmonics (relevant loop)
    for h in harmonic_list:
        if h <= 0:
            continue
        # Nested conditional with early exit (SUGGESTED paradigm)
        contribution = harmonic_envelope(h, freq)
        if contribution > 1.5:
            magnitude += adaptive_filter(contribution, damping)
            break  # Early break on condition
        else:
            magnitude -= math.log(damping + 1) / (h + 1)
    
    # Level 3: Secondary adjustment using lambda and trig
    correction = sum(
        math.cos(freq / (i + 1)) * adaptive_filter(damping, i)
        for i in range(1, 5)
    )
    
    # Level 4: Final nonlinear transformation
    result = (magnitude + correction) ** 2
    
    # Dead assignment - looks like it does something
    transient_state[7] = int(result) % 16
    
    return result

# Irrelevant pre-computations
snapshot_buffer = [math.atan(i / 3) for i in range(8)]
sync_threshold = sum(snapshot_buffer) / len(snapshot_buffer)

# Input data construction with plausible noise
frequency = 6.28
harmonics = [3, 5, -2, 7, 0, 4]

# Key execution point
equilibrium = thermal_matrix(frequency, harmonics)

# Output requirement
print(f"Result: {equilibrium}")