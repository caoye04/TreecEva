def analyze_soil(ph_levels):
    adjusted = []
    for ph in ph_levels:
        if ph < 6.0:
            adjusted.append(ph + 0.5)
        elif ph > 7.5:
            adjusted.append(ph - 0.3)
        else:
            adjusted.append(ph)
    return adjusted

ph_data = [5.2, 6.8, 7.9, 6.1, 8.3, 5.7]

# Irrelevant transformation (distractor)
processed_ph = [round(p * 1.02, 2) for p in ph_data]

adjusted_ph = analyze_soil(ph_data)

# Simulate rainfall impact on growth factors (partially relevant)
def calculate_growth(rainfall_mm):
    base_growth = 1.0
    for rain in rainfall_mm:
        if 20 <= rain <= 50:
            base_growth *= 1.1
        elif rain > 50:
            base_growth *= 0.9  # Overwatering penalty
    return round(base_growth, 3)

rain_data = [45, 60, 30, 70]
growth_factor = calculate_growth(rain_data)

# Plot-level yield simulation with tuple unpacking and filtering
plots = [
    ("A1", 120, adjusted_ph[0]),
    ("B2", 95, adjusted_ph[1]),
    ("C3", 135, adjusted_ph[2]),
    ("D4", 88, adjusted_ph[3]),
    ("E5", 112, adjusted_ph[4])
]

# Dead code path - never called (distractor)
def debug_plot_status(plot_list):
    statuses = []
    for name, area, ph in plot_list:
        if area > 100 and 6.0 <= ph <= 7.0:
            statuses.append((name, "OPTIMAL"))
        else:
            statuses.append((name, "MONITOR"))
    return statuses

# Core optimization logic with list comprehension and filtering
fertility_scores = []
for _, area, ph in plots:
    score = area * (ph / 7.0)
    fertility_scores.append(score)

# Secondary adjustment using growth factor
adjusted_scores = [score * growth_factor for score in fertility_scores]

# Filtering high-potential plots
high_yield_indices = [i for i, score in enumerate(adjusted_scores) if score > 100]

# Compute weighted contribution from high-yield plots only
total_weight = sum(adjusted_scores[i] for i in high_yield_indices)
area_sum = sum(plots[i][1] for i in high_yield_indices)

# Final aggregation with normalization
if total_weight > 0:
    normalized_bias = len(high_yield_indices) * 0.25
    final_yield = int((total_weight / area_sum) + normalized_bias)
else:
    final_yield = 0

# Misleading unrelated calculation (distractor)
synthetic_index = sum(1 for x in adjusted_ph if x > 6.5) * len(rain_data)

Result: final_yield