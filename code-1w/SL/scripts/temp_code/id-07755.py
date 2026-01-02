def calculate_yield_adjustment():
    base_yields = [320, 450, 380, 500, 410]
    quality_factors = [0.9, 1.2, 1.0, 1.3, 0.8]
    surplus_threshold = 400
    total_harvest = 0
    adjusted_yields = []

    for idx, (yield_val, qf) in enumerate(zip(base_yields, quality_factors)):
        adjusted_yield = yield_val * qf
        adjusted_yields.append(adjusted_yield)
        
        if adjusted_yield > surplus_threshold:
            total_harvest += int(adjusted_yield - surplus_threshold)

    # Irrelevant tracking variable (minor distraction)
    unused_deviation = sum(abs(base_yields[i] - (adjusted_yields[i] / quality_factors[i])) for i in range(len(base_yields)))
    
    return total_harvest

result = calculate_yield_adjustment()
print(f"Result: {result}")