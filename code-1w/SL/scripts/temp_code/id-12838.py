def normalize_readings(readings):
    normalized = []
    base = sum(readings) / len(readings)
    for val in readings:
        if val > base:
            normalized.append(val * 0.9)
        else:
            normalized.append(val * 1.1)
    return normalized

# Irrelevant data transformation (distractor)
def encrypt_signal(data):
    result = ''
    for d in data:
        result += chr((ord(d) + 3) % 256)
    return result

# Unused function - dead code path
def deprecated_calibrate(x):
    return (x + 5) ** 2

# Another decoy function with misleading intermediate output
def compute_health_index_v1(metrics):
    score = 0
    for m in metrics:
        score += m * 0.7 + 2
    return score * 1.5  # never used

# Misleading diagnostic with similar naming
temporary_diagnosis = "Stable"
previous_threshold = 85.5

# Real processing begins here
patient_data = [78, 82, 91, 88, 76]

# Bitwise manipulation on checksum (relevant but subtle)
data_checksum = 0
for val in patient_data:
    data_checksum ^= int(val)

adjusted_data = normalize_readings(patient_data)

# Simulate device calibration offset (red herring)
calibration_offset = 2.3
simulated_noise = [0.1, -0.2, 0.05, -0.15, 0.1]

# Apply noise (but not actually affecting main logic)
noisy_adjusted = [a + n for a, n in zip(adjusted_data, simulated_noise)]

# String-based status tracking (uses string method - required feature)
diagnostic_log = "Initial: PASS|Secondary: PENDING|Final: PENDING"
if sum(adjusted_data) > 400:
    diagnostic_log = diagnostic_log.replace("PENDING", "CONFIRMED")

# Extract relevant part for actual computation
status_parts = diagnostic_log.split('|')
final_status_str = status_parts[2]  # Final: CONFIRMED

# Core logic hidden among distractions
aggregate = 0
for x in adjusted_data:
    aggregate += x ** 2

# Hash map usage (suggested paradigm)
diagnostic_map = {
    'level_1': 0.8,
    'level_2': 1.2,
    'critical_factor': 0.95
}

# Modular arithmetic involved in weighting
mod_key = len(patient_data) % 3 + 1  # evaluates to 2
weighting_factor = diagnostic_map['level_1'] if mod_key == 1 else (
    diagnostic_map['level_2'] if mod_key == 2 else diagnostic_map['critical_factor']
)

interim_result = (aggregate * weighting_factor) / data_checksum

# Conditional mutation based on string content (combines string and logic)
if 'CONFIRMED' in final_status_str:
    interim_result *= 1.1

# Decoy assignment that looks important but unused
projected_outcome = round(interim_result * 1.3, 2)

# Final computation obscured by prior noise
final_diagnostic = int(interim_result + 0.5)  # round to nearest integer

# This print must be present and show the target variable
print(f"Result: {final_diagnostic}")