def calculate_crop_yield():
    fields = ['wheat', 'corn', 'barley', 'oats']
    yields = [240, 325, 180, 150]
    
    # Create mapping of field to yield using enumerate
    yield_map = {}
    for idx, crop in enumerate(fields):
        yield_map[crop] = yields[idx] * (idx + 1)  # Increasing return per field index

    # Irrelevant auxiliary variable (minimal distraction)
    avg_yield = sum(yields) / len(yields)

    # Key computation step
    total_harvest = sum(yield_map.values())
    
    # Print result as required
    print(f"Target result: {total_harvest}")

calculate_crop_yield()