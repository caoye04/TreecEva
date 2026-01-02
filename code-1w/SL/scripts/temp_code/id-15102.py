def calculate_energy_capacity():
    base_storage = [120, 200, 180, 95, 130]
    peak_output = 450
    efficiency_factor = 0.85
    
    # Simulate recent usage pattern with slicing
    recent_usage = base_storage[1:4]
    total_stored = [x * 0.9 for x in base_storage]
    
    # Available renewable sources (non-zero contributors)
    available_sources = [solar for solar in recent_usage if solar > 100]
    
    # Key computation point
    energy_capacity = total_stored[:3] and sum(available_sources) * efficiency_factor
    
    # Irrelevant logging variable (minor distraction)
    log_entry = f'Processed {len(base_storage)} units'
    
    print(f"Result: {energy_capacity}")

calculate_energy_capacity()