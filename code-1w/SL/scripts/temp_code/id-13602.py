def analyze_data(samples):
    # Irrelevant preprocessing
    normalized = [x * 0.95 for x in samples if x > 0]
    outliers = [x for x in normalized if x > 100]
    filtered = [x for x in normalized if x <= 100]
    return filtered

# Simulated sensor readings (distraction)
sensor_log = [105, 88, 92, 150, 77, 96, 110]
processed_data = analyze_data(sensor_log)

# Core logic disguised among distractions
def compute_baseline(values):
    base = sum(values) / len(values)
    adjustment = 0.0
    for v in values:
        if v < base:
            adjustment += 0.5
    return base - adjustment

baseline = compute_baseline([80, 90, 75, 85])

# Bit manipulation decoy
flag_register = 0b1101
flag_register = flag_register ^ 0b1010  # Toggle bits
flag_register = flag_register | 0b0100
unused_flag = flag_register & 0b1001  # Dead computation

# Set operations (required feature)
expected_metrics = {"latency", "throughput", "error_rate", "jitter"}
reported_metrics = {"latency", "power", "throughput", "memory", "error_rate"}
metric_intersection = expected_metrics & reported_metrics
extraneous_metrics = reported_metrics - expected_metrics

# Linear search in validation (suggested paradigm)
def find_missing(req, provided):
    missing = []
    for r in req:
        found = False
        for p in provided:
            if r == p:
                found = True
                break
        if not found:
            missing.append(r)
    return missing

missing = find_missing(expected_metrics, reported_metrics)

# Distractor: Unused performance model
class PerformanceModel:
    def __init__(self):
        self.alpha = 0.7
        self.beta = 1.3

    def predict(self, x):
        return x * self.alpha + 2

model = PerformanceModel()
phantom_prediction = model.predict(50)  # Not used

# Real logic buried here
def validate_entry(code):
    if len(code) != 4:
        return False
    checksum = 0
    for c in code:
        checksum ^= ord(c)  # XOR each character (bitwise)
    return checksum == 0x42

access_codes = ["ABCD", "EFGH", "XYZW", "KLMN"]
total_valid = 0
for code in access_codes:
    if validate_entry(code):
        total_valid += 1

# Key computation path
base_value = 420
if total_valid > 0:
    base_value -= 15 * total_valid
else:
    base_value += 100

scaling_factor = len(metric_intersection)  # 3 metrics in common
adjusted_base = base_value * scaling_factor

penalty = 0
for m in extraneous_metrics:
    if 'power' in m or 'memory' in m:
        penalty += 12

final_base = adjusted_base - penalty

# Decoy function with no side effects
def calculate_thermal_load(data):
    temp = 0
    for d in data:
        temp += d ** 0.5
    return temp * 1.5

thermal = calculate_thermal_load(processed_data)  # Misleading energy metric

# Actual final calculation
metric_set = [baseline, final_base, len(missing), thermal]

def evaluate_performance(metrics):
    score = metrics[1]  # final_base is key
    score += int(metrics[0])  # add integer part of baseline
    score -= metrics[2] * 10  # penalize missing metrics
    if metrics[3] > 200:
        score -= 50
    return int(score)

final_score = evaluate_performance(metric_set)
print(f"Target result: {final_score}")