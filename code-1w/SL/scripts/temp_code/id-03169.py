import math

def analyze_soil_quality(plots):
    # Irrelevant function - dead code path
    return [sum(plot) / len(plot) for plot in plots]

def calculate_rainfall_deviation(rain_data, baseline=120):
    # Distractor computation - not used in final result
    deviations = []
    for i, val in enumerate(rain_data):
        dev = abs(val - baseline)
        deviations.append(dev * 0.1)
    return deviations

def filter_unstable_regions(region_mask, stability_threshold=0.75):
    # Misleading intermediate: looks important but unused
    valid_regions = []
    for i, mask in enumerate(region_mask):
        if sum(mask) / len(mask) > stability_threshold:
            valid_regions.append(i)
    return valid_regions

def simulate_growth_cycle(data, factor=1.05):
    # Dead-end simulation with decoy logic
    results = []
    for cycle in range(3):
        temp = []        
        for val in data:
            temp.append(val * (factor ** cycle))
        results.append(temp)
    return results[-1]

def optimize_harvest(regions, weather):
    # Core relevant function
    yields = []
    
    # Real processing begins here
    for i, region in enumerate(regions):
        base_yield = 0
        adjustment = 0
        
        # Meaningful use of enumerate and zip
        for j, (crop, area) in enumerate(zip(region['crops'], region['areas'])):
            if crop == 'wheat':
                base_yield += area * 2.1
                adjustment += 0.3
            elif crop == 'corn':
                base_yield += area * 1.8
                adjustment += 0.4
            elif crop == 'barley':
                base_yield += area * 1.5
                adjustment -= 0.2

        # Weather impact using actual forecast data
        trend_factor = 1.0
        for k, (temp, precip) in enumerate(zip(weather[i]['temps'], weather[i]['rain'])):
            if temp > 25:
                trend_factor *= 0.98
            if precip < 40:
                trend_factor *= 0.95
            elif precip > 100:
                trend_factor *= 0.92

        # Key calculation
        adjusted_yield = (base_yield + adjustment * 10) * trend_factor
        yields.append(round(adjusted_yield, 4))
    
    # Aggregate across regions using complex reduction
    total = 0
    weights = [0.3, 0.4, 0.3]  # Regional importance
    for idx, yld in enumerate(yields):
        total += yld * weights[idx]
    
    # Final transformation
    final_yield = int(total * 100) / 100.0  # Round to two decimals
    
    # Decoy assignments that look like they might affect result
    dummy_correction = math.log(adjustment + 2) * 1000
    final_yield += 0.0  # Neutral operation as red herring
    
    return final_yield

# Main execution context
regions = [
    {
        'name': 'northeast',
        'crops': ['wheat', 'corn', 'barley'],
        'areas': [45, 60, 30]
    },
    {
        'name': 'central',
        'crops': ['corn', 'wheat', 'corn'],
        'areas': [70, 40, 55]
    },
    {
        'name': 'southern',
        'crops': ['barley', 'wheat', 'barley'],
        'areas': [35, 50, 40]
    }
]

forecast_data = [
    {
        'week': 'wk1',
        'temps': [22, 24, 26, 28, 25],
        'rain': [50, 45, 30, 20, 35]
    },
    {
        'week': 'wk2',
        'temps': [20, 23, 27, 29, 31],
        'rain': [120, 90, 40, 30, 25]
    },
    {
        'week': 'wk3',
        'temps': [18, 21, 24, 26, 25],
        'rain': [60, 70, 80, 110, 130]
    }
]

# Irrelevant preprocessing - distractor
soil_health = [[0.8, 0.7, 0.9], [0.6, 0.8, 0.7], [0.5, 0.6, 0.55]]
analyze_soil_quality(soil_health)

# Unused simulation - misleading complexity
dummy_cycles = simulate_growth_cycle([100, 150, 90])

# Unused filtering - red herring
valid_idx = filter_unstable_regions([[True, False, True], [True, True, True], [False, False, True]])

# Actual key computation
final_yield = optimize_harvest(regions, forecast_data)

# Print result as required
print(f"Target result: {final_yield}")