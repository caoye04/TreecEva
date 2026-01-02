import itertools

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 58, 52]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1009, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 35, 40, 45, 50, 42, 38]  # Not used in final calculation
light_intensity = list(range(100, 700, 100))  # Dead code path filler

# Preprocessing: normalize readings to baseline
baseline_temp = sum(temperature_readings) / len(temperature_readings)
normalized_temps = list(map(lambda x: round(x - baseline_temp, 2), temperature_readings))

# Misleading transformation chain (partly unused)
doubled_humidity = [h * 2 for h in humidity_readings if h > 45]  # Partial use, distracts from main flow
filtered_pressure = [p for p in pressure_readings if p < 1012]

# Core diagnostic signal extraction
valid_windows = []
for i in range(len(normalized_temps) - 2):
    window = normalized_temps[i:i+3]
    if sum(window) > 0:
        valid_windows.append(window)

# Decoy statistical analysis (never invoked)
def compute_turbulence_index(data_stream):
    """Unused function - red herring"""
    return sum((x - sum(data_stream)/len(data_stream))**2 for x in data_stream)

# Real-time drift correction using sliding window
sliding_correction = []
for w in valid_windows:
    correction_factor = abs(sum(w)) / len(w)
    sliding_correction.append(round(correction_factor, 3))

# Data fusion engine
fusion_kernel = lambda temps, humids: [t * (h / 100) for t, h in zip(temps, humids[:len(temps)])]
fused_signal = fusion_kernel([sum(w) for w in valid_windows], humidity_readings)

# Diagnostic accumulator with bit flags (mixed paradigm)
class DiagnosticEngine:
    def __init__(self):
        self.flags = 0b0
        self.metrics = []
    
    def set_flag(self, bit):
        self.flags |= (1 << bit)
    
    def accumulate(self, value):
        self.metrics.append(round(value, 4))

engine = DiagnosticEngine()
engine.set_flag(2)
engine.set_flag(4)

for val in fused_signal:
    if val > 0.5:
        engine.accumulate(val * 1.2)
    else:
        engine.accumulate(val * 0.8)

# Secondary processing chain (distractor - looks important but isn't primary)
rolling_avg = []
for i in range(len(fused_signal) - 1):
    avg = (fused_signal[i] + fused_signal[i+1]) / 2
    rolling_avg.append(avg)

# Unused symbolic transformation
symbolic_codes = [''.join(c.lower() if i % 2 == 0 else c.upper() for c in 'diagnostic') for i in range(3)]

# Critical processing chain
processing_chain = [
    sum(engine.metrics),
    sum(sliding_correction),
    len(valid_windows) * 10
]

def aggregate_metrics(chain, mode='strict'):
    """Main aggregation logic"""
    base_score = chain[0] * 1.5
    adjustment = chain[1] if chain[1] > 2 else 0
    bonus = chain[2] // 5 if mode == 'strict' else 0
    return int(round(base_score + adjustment + bonus))

diagnostics = {'version': '2.1', 'calibrated': True}

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Additional decoy logic
if any(x > 100 for x in pressure_readings):
    final_diagnostic -= 10

# Output the target result
print(f"Target result: {final_diagnostic}")