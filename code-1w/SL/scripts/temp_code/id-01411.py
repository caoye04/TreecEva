def calculate_peak_load():
    base_load = 17
    growth_rate = 1.08
    daily_totals = [int(base_load * (growth_rate ** i)) for i in range(7)]
    
    # Apply weekly maintenance reduction on day 4
    daily_totals[3] = int(daily_totals[3] * 0.6)
    
    # Extract and sort top capacities for peak analysis
    capacities_filtered = [val for val in daily_totals if val > 20]
    capacities_sorted = sorted(capacities_filtered)
    
    # Determine peak operational capacity from top three days
    peak_capacity = max(capacities_sorted[-3:])
    
    # Irrelevant auxiliary variable (minor distraction)
    avg_capacity = sum(daily_totals) / len(daily_totals)
    
    print(f"Result: {peak_capacity}")

calculate_peak_load()