from itertools import compress, count

def analyze_growth_rate(data):
    """Analyzes growth rate per plot using sensor data."""
    baseline = [10, 12, 9, 14, 13]
    adjusted = []
    temp_offsets = [0.5, -0.3, 0.8, -0.6, 0.0]
    humidity_factor = 1.02

    for i, reading in enumerate(data):
        offset = temp_offsets[i % len(temp_offsets)]
        adjusted_value = (reading + baseline[i % len(baseline)] + offset) * humidity_factor
        adjusted.append(adjusted_value)

    return adjusted

def detect_anomalies(values):
    """Detects anomalies above threshold; returns mask."""
    threshold = 25
    mask = [v < threshold for v in values]
    return mask

def calculate_optimal_harvest(plot_data, sensors):
    """Calculates final harvest yield based on filtered data."""
    # Step 1: Analyze raw sensor readings
    growth_rates = analyze_growth_rate(sensors)
    
    # Step 2: Identify valid plots by anomaly detection
    validity_mask = detect_anomalies(growth_rates)
    
    # Step 3: Use zip and enumerate to correlate plots with valid growth rates
    valid_yields = []
    debug_info = []  # Distractor: not used later
    index_counter = count(1)
    
    for idx, (plot, rate) in enumerate(zip(plot_data, growth_rates)):
        plot_id = next(index_counter)
        if validity_mask[idx]:
            # Apply soil quality factor (only some plots have enhanced soil)
            soil_enhancer = 1.1 if 'rich' in plot.get('soil', '') else 1.0
            daily_yield = rate * plot['size'] * soil_enhancer
            valid_yields.append(daily_yield)
            
            # Debug logging (distractor)
            debug_info.append(f"Plot {plot_id}: {daily_yield:.2f} units")
        else:
            continue
   
    # Step 4: Simulate 7-day growth cycle (simple loop)
    total_accumulated = 0
    for day in range(7):
        multiplier = 1 + (day * 0.05)  # Growth accelerates slightly each day
        day_total = sum(v * multiplier for v in valid_yields)
        total_accumulated += day_total

        # Redundant tracking (distractor)
        running_avg = day_total / (len(valid_yields) + 1e-8)
        _ = [x / running_avg for x in valid_yields]  # Unused computation

    # Step 5: Apply final weather adjustment (constant factor)
    wind_loss_factor = 0.93
    final_yield = int(total_accumulated * wind_loss_factor)
    
    # Irrelevant string processing (distractor)
    report_name = f"Harvest_Yield_Report_{'Q3'}"
    report_name = report_name.upper().replace('_', '-')
    title_length = len(report_name)
    _ = [c for c in report_name if c.isalpha()]  # Dead code

    return final_yield

# Main execution
plots = [
    {'id': 'A1', 'size': 5, 'soil': 'rich'},
    {'id': 'B2', 'size': 4, 'soil': 'standard'},
    {'id': 'C3', 'size': 6, 'soil': 'rich'},
    {'id': 'D4', 'size': 3, 'soil': 'standard'},
    {'id': 'E5', 'size': 7, 'soil': 'nutrient-rich'}  # Note: 'nutrient-rich' does NOT trigger soil_enhancer
]

sensors = [8.1, 9.3, 10.5, 11.2, 12.0]

final_yield = calculate_optimal_harvest(plots, sensors)
print(f"Result: {final_yield}")