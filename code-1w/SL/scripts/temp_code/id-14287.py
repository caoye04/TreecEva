def analyze_soil_composition(data):
    # Irrelevant helper function (dead code path)
    return sum(x ** 0.5 for x in data if x % 3 == 0)

season_factor = 7.2
soil_data = [12, 15, 18, 21, 24, 27, 30]

# Distractor: unused matrix transformation
transform_matrix = [[i * j for j in range(3)] for i in range(3)]
processed_noise = [transform_matrix[i][i] + 5 for i in range(3)]

# Real data structure: orchard layout (rows, trees per row)
orchard_layout = [
    (4, 'gala'),      # 4 rows of gala
    (6, 'fuji'),      # 6 rows of fuji
    (3, 'honeycrisp') # 3 rows of honeycrisp
]

# Misleading intermediate calculation (not used in final result)
calculated_irrigation_rate = len(soil_data) * 0.8 + sum([len(str(x)) for x in soil_data])

# Tuple unpacking and filtering with string methods
effective_rows = 0
tree_varieties = []
for count, name in orchard_layout:
    cleaned_name = name.strip().lower()
    if 'crisp' in cleaned_name or cleaned_name.startswith('f'):
        effective_rows += count
    tree_varieties.append(cleaned_name.title())

# Secondary distractor: unused combinatorics
from math import comb
possible_pairings = comb(len(tree_varieties), 2) if len(tree_varieties) >= 2 else 0

# Core logic disguised among red herrings
def calculate_harvest_capacity(layout, factor):
    total_capacity = 0
    multiplier_map = {}
    
    for count, var in layout:
        base = 100
        ext = var.strip().lower()
        
        # Bit manipulation decoy (not actually impactful)
        shift_offset = (count & 3) ^ 1
        
        if 'gala' in ext:
            bonus = base * 0.1
        elif 'fuji' in ext:
            bonus = base * 0.25
        elif 'crisp' in ext:
            bonus = base * 0.3
        else:
            bonus = 0
        
        # Actual contribution
        yield_per_row = base + bonus + (factor * 2)
        total_capacity += count * yield_per_row
        
        # Store in map (unused)
        multiplier_map[var] = yield_per_row / base
    
    # Accumulation with fake normalization
    noise_adjusted = total_capacity - sum(processed_noise)  # processed_noise defined earlier
    normalized = noise_adjusted / (1 + len(transform_matrix))  # Use outer-scope variables as distraction
    
    # Final computation uses only essential components
    return int(normalized)  # deterministic integer output

# Early termination red herring
if calculated_irrigation_rate > 100:
    final_yield = -1
else:
    final_yield = calculate_harvest_capacity(orchard_layout, season_factor)

# Critical answer printing
print(f"Result: {final_yield}")