from collections import defaultdict

# Simulated agricultural plot data across seasons
plots = [
    {'id': 'A1', 'crop': 'wheat', 'yield_tons': 12.5, 'rainfall_cm': 45, 'fertilizer_kg': 200},
    {'id': 'A2', 'crop': 'corn', 'yield_tons': 18.3, 'rainfall_cm': 52, 'fertilizer_kg': 240},
    {'id': 'A3', 'crop': 'wheat', 'yield_tons': 14.1, 'rainfall_cm': 48, 'fertilizer_kg': 210},
    {'id': 'A4', 'crop': 'barley', 'yield_tons': 9.7, 'rainfall_cm': 40, 'fertilizer_kg': 180},
    {'id': 'A5', 'crop': 'corn', 'yield_tons': 16.8, 'rainfall_cm': 50, 'fertilizer_kg': 230}
]

# Track seasonal adjustments and baseline metrics
adjustment_log = defaultdict(float)
crop_totals = defaultdict(lambda: {'yield': 0, 'count': 0})

# Spurious tracking variables (distractors)
phantom_index = 0
dummy_checksum = 0
redundant_flag = True

for plot in plots:
    crop = plot['crop']
    yield_tons = plot['yield_tons']
    rainfall = plot['rainfall_cm']
    fertilizer = plot['fertilizer_kg']

    # Irrelevant intermediate calculation (distractor)
    dummy_checksum ^= int(fertilizer) & 7

    # Update aggregate crop stats
    crop_totals[crop]['yield'] += yield_tons
    crop_totals[crop]['count'] += 1

    # Conditional adjustment logic based on rainfall-fertilizer efficiency
    efficiency = (rainfall * 0.6 + fertilizer * 0.01) / 10
    if efficiency > 3.0:
        adjustment_log[crop] += 0.2
    elif efficiency < 2.0:
        adjustment_log[crop] -= 0.1

    # Redundant state update (dead path)
    if phantom_index > 100:
        redundant_flag = False
    phantom_index += 1

# Compute base adjusted yield per crop
crop_averages = {}
for crop, data in crop_totals.items():
    avg_yield = data['yield'] / data['count']
    adjustment = adjustment_log[crop]
    crop_averages[crop] = avg_yield + adjustment

# Secondary processing: weight by historical significance (simulated)
historical_weights = {'wheat': 1.1, 'corn': 1.2, 'barley': 0.9}
weighted_scores = []

for crop, adj_avg in crop_averages.items():
    if crop in historical_weights:
        weighted_scores.append(adj_avg * historical_weights[crop])

# Final aggregation with normalization factor
normalization_factor = len(weighted_scores) or 1
raw_aggregate = sum(weighted_scores)

# Apply bitwise mask to simulate hardware-level constraint (semi-relevant)
mask = 0xFF  # Simulate 8-bit truncation effect
masked_sum = int(raw_aggregate * 10) & mask  # Scale and truncate
final_raw = masked_sum / 10.0

# Final adjustment using conditional logic and comparison chain
correction_term = 0
if final_raw > 15:
    correction_term = 1.5
elif final_raw > 10 and redundant_flag:
    correction_term = 0.8
else:
    correction_term = 0.3

final_score = final_raw + correction_term

print(f"Result: {final_score}")