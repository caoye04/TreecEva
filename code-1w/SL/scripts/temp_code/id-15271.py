def simulate_blood_pressure(age, stress_factor):
    if age < 30:
        return 110 + stress_factor * 5
    elif age < 60:
        return 120 + stress_factor * 7
    else:
        return 130 + stress_factor * 9

# Irrelevant sensor simulation (distraction)
temperature_log = [36.1, 36.3, 36.8, 37.0, 37.2]
avg_temp = sum(temperature_log) / len(temperature_log)

def compute_oxygen_saturation(level, altitude):
    # Distractor function with misleading relevance
    base_sat = 98 - (altitude / 1000) * 2
    return max(85, base_sat - level * 1.5)

# Simulated lab values with decoy computations
wbc_count = 8.6  # Normal range
rbc_count = 4.9  # Normal
platelets = 220  # Normal

# Dummy transformation chain (dead path)
data_buffer = [wbc_count, rbc_count, platelets]
normalized = [x / 10 for x in data_buffer]
scaled = [int(x * 100) for x in normalized]
filtered = list(filter(lambda x: x > 20, scaled))

# Actual relevant physiological parameters
heart_rate_baseline = 72
activity_level = 3
hrv_index = 65  # Heart rate variability

# Conditional expression influencing autonomic state
autonomic_tone = 'parasympathetic' if hrv_index > 60 else 'sympathetic'

# Neurological response model (partially relevant)
def reflex_response(stimulus_intensity):
    if stimulus_intensity > 8:
        return 1.8
    elif stimulus_intensity > 5:
        return 1.4
    else:
        return 1.0

# Misleading metabolic pathway simulation
metabolic_rate = 1.0
for i in range(3):
    metabolic_rate *= 1.05  # Minor increases

# Unused recursive red herring
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

unused_sequence = [fibonacci(x) for x in range(6)]

# Key patient state variables
age = 45
stress_marker = 6
oxygen_level = 96

# Compute vital signs using actual logic chain
bp = simulate_blood_pressure(age, stress_marker)
o2_sat = compute_oxygen_saturation(2, 500)

# Determine cardiac load index with nested conditionals and distractors
cardiac_load = 0
if bp > 140 or o2_sat < 90:
    cardiac_load += 40
elif bp > 130:
    cardiac_load += 25
else:
    cardiac_load += 15

cardiac_load += heart_rate_baseline // 10

efficiency_ratio = (o2_sat / bp) * 100

# Complex conditional expression combining multiple factors
decision_metric = efficiency_ratio if autonomic_tone == 'parasympathetic' else (efficiency_ratio * 0.85)

def analyze_patient_state():
    # Core diagnostic logic buried among distractions
    score = 100
    score -= cardiac_load
    score += stress_marker * 2
    
    # Red herring: irrelevant neural readiness check
    neural_readiness = 80
    for i in range(2):
        neural_readiness -= i * 3
    
    # Real adjustment based on oxygen and pressure
    if bp >= 130 and o2_sat < 95:
        score -= 10
    
    # Final nonlinear adjustment
    if decision_metric < 60:
        score -= 15
    else:
        score -= 5
    
    # Decoy mutation (never used)
    score_alternate = score * 1.1
    
    return int(score)

# Execution point of interest
final_diagnostic = analyze_patient_state()

# Print result as required
print(f"Result: {final_diagnostic}")