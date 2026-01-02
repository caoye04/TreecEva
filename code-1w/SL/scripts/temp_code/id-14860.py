import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [0.7, 1.2, -0.3, 4.5, 2.1, -1.0, 3.3, 0.0, -2.4, 1.8]

def normalize(value):
    return (value + 5) / 10

def is_significant_peak(val):
    return val > 0.75

# Irrelevant helper function (decoy)
def temperature_compensation(x):
    return x * 0.98 + 0.5

# Unused transformation path (dead code)
def legacy_filter(data):
    return [x * 0.7 for x in data if x > 1]

# Signal conditioning pipeline
def preprocess(signal_list):
    normalized = [normalize(x) for x in signal_list]
    filtered = [x for x in normalized if x > 0.1]
    smoothed = []
    for i in range(len(filtered)):
        window = filtered[max(0, i-1):min(i+2, len(filtered))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Misleading intermediate computation (red herring)
temp_analysis = [math.sin(x) * 100 for x in raw_readings]
avg_temp_score = sum(temp_analysis) / len(temp_analysis)

# Actual processing begins here
processed_samples = preprocess(raw_readings)

# Diagnostic engine with multiple logic branches
def evaluate_stability(metrics):
    if len(metrics) == 0:
        return 0
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    return variance < 0.05

def count_anomalies(data):
    count = 0
    for x in data:
        if x < 0.2 or x > 0.8:
            count += 1
    return count

# Another decoy function that's defined but not used
def frequency_domain_analysis(seq):
    magnitude = 0
    for i, val in enumerate(seq):
        magnitude += val * math.cos(i * math.pi / 4)
    return magnitude

# Critical diagnostic algorithm
def analyze_signal(cleaned_data):
    # Step 1: Check basic stability
    stable = evaluate_stability(cleaned_data)
    
    # Step 2: Count edge anomalies
    anomalies = count_anomalies(cleaned_data)
    
    # Step 3: Compute entropy-like measure
    entropy = 0
    for x in cleaned_data:
        if x > 0:
            entropy -= x * math.log(x)
    
    # Step 4: Apply modular weighting based on length
    base_score = int((entropy * 100)) % 97
    
    # Step 5: Adjust by anomaly penalty
    penalty = anomalies * 7
    adjusted = (base_score - penalty) % 53
    
    # Step 6: Stability boost if applicable
    if stable:
        adjusted = (adjusted * 2) % 101
    
    # Step 7: Final transformation using list comprehension
    history_buffer = [adjusted ^ i for i in range(3)]
    final_boost = sum([h * (i+1) for i, h in enumerate(history_buffer)])
    
    # Step 8: Apply bitwise refinement
    refined = (final_boost ^ 0x1F) & 0x7F
    
    return refined

# Execute main logic
intermediate_diagnostics = []
for sample_set in [processed_samples[:4], processed_samples[4:]]:
    score = analyze_signal(sample_set)
    intermediate_diagnostics.append(score)

# Red herring: unused aggregation
combined_diagnostic = sum(intermediate_diagnostics) // 2

# Key statement: this produces the final answer
final_diagnostic = analyze_signal(processed_samples)

print(f"Result: {final_diagnostic}")