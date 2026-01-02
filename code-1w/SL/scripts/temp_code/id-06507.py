def analyze_soil_composition(elements):
    # Irrelevant computation: analyzing soil elements (distractor)
    heavy_metals = {'lead', 'cadmium', 'arsenic'}
    safe_elements = {k for k in elements.keys() if k not in heavy_metals}
    contamination_score = sum(elements[el] for el in heavy_metals if el in elements)
    return contamination_score

soil_data = {'nitrogen': 45, 'phosphorus': 30, 'potassium': 25, 'lead': 5, 'zinc': 12}
contamination = analyze_soil_composition(soil_data)

# Simulate growth cycles over different plots
area_metrics = [
    {'plot_id': 'A1', 'size_acres': 10, 'irrigation_level': 85, 'fertilizer_kg': 200},
    {'plot_id': 'A2', 'size_acres': 15, 'irrigation_level': 90, 'fertilizer_kg': 220},
    {'plot_id': 'A3', 'size_acres': 12, 'irrigation_level': 78, 'fertilizer_kg': 180}
]

growth_cycles = 3
base_yield_per_acre = 120
yield_adjustment_factor = 0.01

# Tracking variables (some used, some not)
expected_loss_rate = 0.03
maintenance_effort = 0  # Dead variable - not used
historical_yields = []

# Simulate yield degradation over cycles due to soil fatigue
fatigue_accumulation = 0
for cycle in range(1, growth_cycles + 1):
    fatigue_accumulation += 0.05 * cycle  # Increases with each cycle

# Helper function to compute efficiency
def calculate_harvest_efficiency(metrics, cycles):
    total_effective_yield = 0
    total_area = 0
    
    for plot in metrics:
        base = base_yield_per_acre
        size = plot['size_acres']
        irrigation = plot['irrigation_level']
        fertilizer = plot['fertilizer_kg']
        
        # Yield formula based on multiple factors
        yield_potential = base * (1 + (irrigation - 80) * 0.005)
        yield_potential *= (1 + (fertilizer - 200) * 0.002)
        
        # Apply fatigue loss over cycles
        adjusted_yield = yield_potential * (1 - fatigue_accumulation)
        
        # Apply random-seeming but deterministic pest factor (based on plot_id hash)
        pest_factor = 1.0
        if ord(plot['plot_id'][-1]) % 3 == 0:
            pest_factor = 0.95
        
        harvested = adjusted_yield * size * pest_factor
        total_effective_yield += harvested
        total_area += size
    
    # Efficiency is average yield per acre after all losses
    efficiency = total_effective_yield / total_area
    
    # Secondary adjustment based on contamination (minimal effect)
    global contamination
    if contamination > 0:
        efficiency *= (1 - min(contamination * 0.002, 0.05))
    
    return efficiency

# Execute main calculation
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Print result as required
print(f"Target result: {final_yield}")