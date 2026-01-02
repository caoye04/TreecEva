from itertools import compress

def analyze_growth_cycles(data):
    # Irrelevant helper function (dead code path)
    return sum(x * 2 for x in data if x > 5)

# Simulate agricultural yield prediction based on soil and plot conditions
plots = [8, 4, 7, 6, 9]
soil_quality = [0.85, 0.45, 0.70, 0.60, 0.90]
decay_factors = [0.95, 0.55, 0.75, 0.68, 0.88]  # Unused but plausible distractor

# Misleading intermediate calculations
baseline = sum(plots) / len(plots)
efficiency_flags = [sq >= 0.65 for sq in soil_quality]
filtered_plots = list(compress(plots, efficiency_flags))

# Character counting red herring (string method)
log_entry = "Plot analysis complete: Q3 metrics"
char_count = len([c for c in log_entry if c.isalpha()])
flag_summary = ''.join(['Y' if f else 'N' for f in efficiency_flags])

# Real computation begins
adjusted_yields = []
for i, p in enumerate(plots):
    adjustment = 1.0
    if soil_quality[i] < 0.6:
        adjustment = 0.6
    elif soil_quality[i] >= 0.8:
        adjustment = 1.4
    else:
        adjustment = 1.1
    adjusted_yields.append(p * adjustment * soil_quality[i])

# Secondary manipulation with slicing (relevant)
temp_buffer = adjusted_yields[1:4]
offset_correction = sum(temp_buffer) * 0.1

# Final efficiency calculation
raw_total = sum(adjusted_yields)
calibrated_total = raw_total - offset_correction

# Normalize using character count (distractor, not actually used)
normalization_factor = char_count / 100  # Plausible but unused

# Actual final result
final_yield = int(calibrated_total + 0.5)  # Round to nearest integer

# Output result as required
print(f"Result: {final_yield}")