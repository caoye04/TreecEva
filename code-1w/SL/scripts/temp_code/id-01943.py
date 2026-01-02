import math

# Simulated geothermal grid analysis with irrelevant distractors
def analyze_seismic_risk(zones):
    risk_score = 0
    for zone in zones:
        if len(zone) > 3:
            risk_score += sum([ord(c) for c in zone]) % 7
    return risk_score * 0.3

# Irrelevant function: calculates atmospheric pressure index (unused)
def compute_atmospheric_index(timestamps):
    base = 1013.25
    for t in timestamps:
        base *= (1 + math.sin(t % 360))
    return round(base, 2)

# Core calculation: thermal output from subsurface grid
def calculate_thermal_output(grid):
    rows, cols = len(grid), len(grid[0])
    total_energy = 0
    adjustment_factor = 1.75
    
    # Complex nested logic with red herrings
    decoy_sum = 0
    for i in range(rows):
        row_peaks = []
        for j in range(cols):
            cell_value = grid[i][j]
            
            # Bit manipulation distraction
            bit_transform = (cell_value << 2) ^ 5
            decoy_sum += bit_transform % 19
            
            if i % 2 == 0:
                if cell_value > 50:
                    total_energy += cell_value * 0.8
                else:
                    total_energy += cell_value * 0.4
            else:
                if j % 3 == 0:
                    total_energy += math.log(cell_value + 1) * 2
                else:
                    total_energy += cell_value ** 0.5
            
            # Store peak per row (partially used)
            row_peaks.append(cell_value)
        
        # Real impact: harmonic adjustment based on row max
        if row_peaks:
            max_peak = max(row_peaks)
            total_energy += 100 / (max_peak / 10 + 1)
    
    # Final transformation (key step)
    final_grid_score = sum(sum(row) for row in grid) // 10
    total_energy += final_grid_score * 0.6
    
    # Decoy normalization (irrelevant)
    normalized_decoy = decoy_sum / (rows * cols + 1)
    _ = round(normalized_decoy, 3)  # unused
    
    return total_energy * adjustment_factor

# Misleading data structures
seismic_zones = ['A7X', 'B9Y', 'C12Z', 'D4W']
timestamp_sequence = [120, 240, 360, 480]

# Actual input data (obscured among distractors)
grid_state = [
    [65, 45, 80, 30],
    [55, 72, 68, 41],
    [90, 33, 77, 50],
    [44, 85, 63, 39]
]

# Spurious calculations to increase interference
avg_temp = sum(sum(row) for row in grid_state) / (len(grid_state) * len(grid_state[0]))
fluctuation_index = max(max(row) for row in grid_state) - min(min(row) for row in grid_state)
entropy_metric = len(seismic_zones) * (fluctuation_index / 10)

# Key execution point
thermal_capacity = calculate_thermal_output(grid_state)

# Secondary irrelevant transformation
atm_index = compute_atmospheric_index(timestamp_sequence)
seismic_risk = analyze_seismic_risk(seismic_zones)

# Output the target result only
print(f"Result: {thermal_capacity}")