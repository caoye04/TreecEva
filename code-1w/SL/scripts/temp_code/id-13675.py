import itertools

# Simulated agricultural yield dataset with noise
soil_quality = {'A': 0.9, 'B': 0.65, 'C': 0.4, 'D': 0.2}
base_yield_per_acre = 120
treatment_efficiency = {'x': 1.1, 'y': 1.3, 'z': 0.95}

# Irrelevant auxiliary data (distractor)
economic_index = {'inflation': 0.03, 'demand': 1.12, 'export_rate': 0.87}
legacy_factors = [0.98, 0.99, 1.01, 1.03]

# Field metadata with real and fake entries
crop_fields = [
    {'id': 'F1', 'soil': 'A', 'size': 15, 'treatment': 'y', 'active': True},
    {'id': 'F2', 'soil': 'B', 'size': 20, 'treatment': 'x', 'active': True},
    {'id': 'F3', 'soil': 'C', 'size': 10, 'treatment': 'z', 'active': False},  # Inactive field
    {'id': 'F4', 'soil': 'A', 'size': 12, 'treatment': 'y', 'active': True},
    {'id': 'F5', 'soil': 'D', 'size': 8, 'treatment': 'x', 'active': True}
]

# Decoy function – never called (dead code path)
def deprecated_yield_calc(area, factor):
    return area * base_yield_per_acre * factor * 0.9

# Real processing functions
def calculate_field_yield(field):
    if not field['active']:
        return 0.0
    soil_factor = soil_quality.get(field['soil'], 0.1)
    treatment_factor = treatment_efficiency.get(field['treatment'], 1.0)
    return field['size'] * base_yield_per_acre * soil_factor * treatment_factor

# Data aggregation with slicing distraction
all_combinations = list(itertools.product(['A','B','C'], [1,2,3]))
useful_combinations = all_combinations[::3]  # Slice used to mislead

harvest_data = [calculate_field_yield(f) for f in crop_fields]

# Projection map based on seasonal trends (some values irrelevant)
projection_map = {
    'Q1': 1.05,
    'Q2': 1.15,
    'Q3': 0.95,
    'Q4': 1.0,
    'dummy_key_1': 999,
    'dummy_key_2': -1
}

# Red herring: unused intermediate calculations
total_potential_fields = sum(1 for f in crop_fields)
avg_soil_score = sum(soil_quality[f['soil']] for f in crop_fields) / len(crop_fields)
unused_correction_factor = avg_soil_score * economic_index['demand']

# Real transformation: apply only Q2 projection
adjusted_yields = [y * projection_map['Q2'] for y in harvest_data]

# Complex data restructuring (distractor)
yield_summary = {f['id']: calculate_field_yield(f) for f in crop_fields}
summary_keys = list(yield_summary.keys())[1:4]  # Slicing operation (irrelevant)

# Dummy dictionary operations to increase complexity
meta_tags = {k: f"tag_{v}" for k, v in projection_map.items() if isinstance(v, float)}
meta_tags.update({'version': '2.1', 'status': 'final'})

# Core accumulation logic
yield_bins = [0] * 5
for i, y in enumerate(adjusted_yields):
    bin_idx = min(int(y // 1000), 4)
    yield_bins[bin_idx] += y

# Final aggregation using filtered projections
def aggregate_results(yields, proj_map):
    base_total = sum(yields)
    season_factor = proj_map['Q2']  # Critical use of Q2
    adjustment = base_total * (season_factor - 1)
    bonus = 0
    if base_total > 5000:
        bonus = 200
    # Extra layer: combinatorics distraction
    combos = list(itertools.combinations(yields, 2))
    combo_count = len(combos)
    # Bonus reduced by number of low-yield pairs (only for show)
    low_pairs = sum(1 for c in combos if sum(c) < 1000)
    effective_bonus = bonus - (low_pairs * 5)  # Mostly irrelevant
    return base_total + adjustment + max(effective_bonus, 0)

final_yield = aggregate_results(harvest_data, projection_map)
print(f"Result: {final_yield}")