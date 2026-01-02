def analyze_efficiency(data, threshold=0.75):
    """Irrelevant analysis function (dead code path)."""
    return sum(x > threshold for x in data) / len(data)


def normalize_vector(v):
    """Another decoy function with misleading relevance."""
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Irrelevant constants (distractors)
MAX_ITERATIONS = 10000
DEFAULT_TIMEOUT = 30
DEBUG_MODE = True
LOG_LEVEL = 'VERBOSE'

# Simulated sensor metrics (some are relevant, others are red herrings)
sensor_readings = {
    'temp': [23.5, 24.1, 22.9, 25.0, 23.8],
    'pressure': [101.3, 102.1, 100.7, 103.2, 101.9],
    'humidity': [45, 47, 50, 44, 46],
    'vibration': [0.01, 0.03, 0.02, 0.05, 0.04],
    'current_draw': [1.2, 1.3, 1.1, 1.4, 1.25]
}

# Misleading preprocessing (partially unused)
processed = {}
for key, values in sensor_readings.items():
    avg = sum(values) / len(values)
    processed[key] = round(avg, 2)

# Extract only relevant metrics for evaluation
metrics = [
    processed['temp'],
    processed['pressure'],
    processed['humidity']
]

# Weight vector – crucial but obscured among distractors
weights = [0.4, 0.35, 0.25]  # Allocated based on system criticality

# Decoy weight sets (distractors)
alt_weights_v1 = [0.2, 0.5, 0.3]
alt_weights_v2 = [0.6, 0.1, 0.3]
temp_bias_factor = 1.1
pressure_adjustment = 0.98

# Spurious intermediate calculations (red herrings)
baseline_deviation = (processed['temp'] - 20) * 1.8 + 32
adjusted_pressure = processed['pressure'] * 0.02953  # to psi
humidity_ratio = processed['humidity'] / 100

# Conditional adjustment that looks important but is not used
if processed['vibration'] > 0.03:
    temp_correction = 0.5
else:
    temp_correction = 0.0

# Another dead-end branch
if processed['current_draw'] > 1.2:
    power_risk = 'MODERATE'
else:
    power_risk = 'LOW'

# Real logic buried in noise
def evaluate_performance(m, w):
    """Compute weighted performance score."""
    score = 0.0
    for i, (metric, weight) in enumerate(zip(m, w)):
        # Normalize metric to a 0-1 scale using heuristic bounds
        if i == 0:  # temp: ideal 20-25°C
            normalized = max(0, min(1, (25 - abs(metric - 22.5)) / 2.5))
        elif i == 1:  # pressure: ideal around 101.3 kPa
            normalized = max(0, min(1, (103 - abs(metric - 101.3)) / 2))
        else:  # humidity: ideal 40-50%
            normalized = max(0, min(1, (50 - abs(metric - 45)) / 5))
        score += normalized * weight
    return round(score * 100, 4)  # Scale to percentage-like value

# Unused alternative scoring method (decoy)
def alt_scoring(m):
    return sum(m) / len(m)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Additional distraction: fake logging output
print(f'Debug: Baseline deviation: {baseline_deviation}')
print(f'System status: {power_risk}')

# Only this line matters
print(f'Target result: {final_score}')