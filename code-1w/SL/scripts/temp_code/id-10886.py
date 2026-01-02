def preprocess_signal(raw_data, threshold=0.5):
    filtered = [x for x in raw_data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

# Irrelevant sensor data (distraction)
sensor_readings_a = [0.1, 0.4, 0.6, 0.9, 1.2]
sensor_readings_b = [-0.3, 0.0, 0.7, -1.1]
dummy_stats = {'mean': 0.42, 'variance': 0.18}

# Unused transformation function (dead code path)
def transform_coordinates(coords):
    return [(x * 2 + 1, y * 2 - 1) for x, y in coords]

# Core quantum register simulation
class QuantumRegister:
    def __init__(self, size):
        self.size = size
        self.state_vector = [1 << i for i in range(size)]
        self.coherence = True

    def apply_phase_shift(self):
        for i in range(len(self.state_vector)):
            if self.state_vector[i] & 3:  # bitwise check
                self.state_vector[i] ^= 5  # XOR flip

    def measure(self):
        return sum(self.state_vector) >> 1

# Initialize registers
quantum_registers = [QuantumRegister(4), QuantumRegister(3), QuantumRegister(5)]

# Simulate decoherence on even-indexed registers
for idx, reg in enumerate(quantum_registers):
    if idx % 2 == 0:
        reg.coherence = False
        reg.apply_phase_shift()

# Bitmask analysis (relevant but indirect)
bitmask_summary = 0
for reg in quantum_registers:
    for val in reg.state_vector:
        bitmask_summary ^= val  # accumulate XOR

# Distractor: unused string processing with zip and enumerate
log_entries = ['ERR_CRITICAL', 'WARN_DISK', 'INFO_READY', 'DEBUG_TRACE']
timestamps = [1001, 1005, 1012, 1020]
error_flags = set()
for i, (ts, entry) in enumerate(zip(timestamps, log_entries)):
    if 'ERR' in entry:
        error_flags.add(f'{ts}:{i}')

# Another distraction: character counting in system codes
system_codes = ['QX4', 'QX8', 'QX12']
char_count = sum(len(code) for code in system_codes)  # unused

# Real computation begins here — data transformation chain
working_values = []
for reg in quantum_registers:
    measured = reg.measure()
    adjusted = measured * 2 if not reg.coherence else measured // 2
    working_values.append(adjusted)

# Combine using bitwise and arithmetic logic
aggregated = 0
for i, val in enumerate(working_values):
    if i % 2 == 0:
        aggregated += val ^ (3 << i)  # XOR with shifted constant
    else:
        aggregated -= val & (0xFF)   # mask lower byte

# Secondary processing with set operations
temp_set_a = {x for x in working_values}
temp_set_b = {x * 2 for x in working_values}
intersection_size = len(temp_set_a & temp_set_b)

# Final diagnostic depends on aggregated and intersection
baseline = 100
scaling_factor = 1.5

# Critical execution point
final_diagnostic = int((aggregated + intersection_size) * scaling_factor + baseline)

# Print result as required
print(f"Result: {final_diagnostic}")