import math

# Simulated biomedical signal processing pipeline
# Contains multiple layers of data transformation with distractors

def analyze_waveform(signal):
    if not signal:
        return 0
    peak = max(signal)
    baseline = sum(signal) / len(signal)
    noise_floor = math.sqrt(sum([x**2 for x in signal])) / len(signal)
    # Distractor: irrelevant spectral estimate
    spectral_estimate = [math.sin(x / 3) for x in signal]
    # Real computation: signal quality index
    sqi = (peak - baseline) / (noise_floor + 1e-6)
    return round(sqi, 3)

# Irrelevant auxiliary function (dead code path)
def compute_harmonic_series(n):
    return [1/i for i in range(1, n+1)]

# Data normalization utility (used later)
def normalize_vector(vec):
    norm = math.sqrt(sum([v**2 for v in vec]))
    return [v/norm for v in vec] if norm > 0 else vec

# Core metric processor
process_metrics = lambda data, config: sum([
    analyze_waveform(data.get('lead_i', [])) * config['weight_a'],
    analyze_waveform(data.get('lead_ii', [])) * config['weight_b'],
    len([x for x in data.get('timestamps', []) if x % 2 == 0]) * 0.1  # minor time-based factor
])

# Decoy function that looks important but isn't called
def generate_fourier_components(signal, harmonics=5):
    components = {}
    for h in range(1, harmonics+1):
        components[f'h{h}'] = sum([math.cos(h * x / 2) for x in signal[:10]])
    return components

# Large dataset with red herrings
health_data = {
    'patient_id': 'P7890',
    'timestamp': 1685432100,
    'lead_i': [12, 15, 8, 20, 17, 5, 23, 19, 14],
    'lead_ii': [18, 22, 14, 27, 25, 10, 30, 24, 19],
    'spo2': 97,
    'respiration_rate': 16,
    'auxiliary': {'v5': [9, 13, 7, 18, 16, 8, 21], 'v6': [11, 14, 9, 19, 17, 7, 22]},
    'timestamps': [1685432100, 1685432102, 1685432104, 1685432106, 1685432108],
    'metadata': {
        'device': 'ECG-Pro 3000',
        'firmware': '2.1.7',
        'calibration': [0.98, 1.02, 0.99, 1.01]
    }
}

# Unused complex structure (distractor)
class DiagnosticEngine:
    def __init__(self):
        self.thresholds = {}
        self.filters = []
        self.version = '1.5'
    
    def apply_filter(self, signal):
        return [x * 0.95 for x in signal]

# Another decoy list comprehension with string methods
log_entries = [
    f"ERROR: Sensor {chr(65+i)} offline" if i % 5 == 0 else f"OK: Sensor {chr(65+i)} active"
    for i in range(20)
]
error_count = len([entry for entry in log_entries if entry.startswith('ERROR')])

# Actual threshold configuration used in processing
thresholds = {
    'weight_a': 1.2,
    'weight_b': 0.8,
    'critical_level': 25.0
}

# Complex data transformation chain (some steps are distractions)
filtered_signals = {}
for lead_name, signal in [(k, v) for k, v in health_data.items() if 'lead' in k]:
    cleaned = [x for x in v if 5 <= x <= 35]
    normalized = normalize_vector(cleaned)
    filtered_signals[lead_name] = [round(x * 1.05, 2) for x in normalized]

# Update health_data with processed signals (not used in final result - red herring)
health_data['processed'] = filtered_signals

# Critical statement
final_diagnostic = process_metrics(health_data, thresholds)

# Additional distraction: set operations on string characters
diagnostic_codes = set('DXA12') | set('DXB34') | set('DXC56')
comorbidities = set('DXA12') & set('DXA78') | set('DXC56')
risk_score = len(diagnostic_codes.symmetric_difference(comorbidities)) * 1.5

# Print required target result
print(f"Target result: {final_diagnostic}")