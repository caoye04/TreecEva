def calculate_grid_stability(demand_forecast, generation_capacities, maintenance_schedule):
    peak_capacity = 0
    current_output = 0
    reserve_margin = 0
    safety_threshold = 1.2
    degradation_factor = 0.98
    penalty_accumulator = 0.0
    historical_surplus = []

    for i, demand in enumerate(demand_forecast):
        if maintenance_schedule[i]:
            available_units = [g * degradation_factor for idx, g in enumerate(generation_capacities) if idx % 2 != i % 2]
        else:
            available_units = [g for g in generation_capacities]

        current_output = sum(available_units)
        projected_load = demand * safety_threshold
        reserve_margin = current_output - projected_load

        if reserve_margin < 0:
            penalty_accumulator += abs(reserve_margin) * 0.1

        if reserve_margin < demand_forecast[i]:
            peak_capacity = max(peak_capacity, current_output)
            break

        surplus_energy = reserve_margin * 0.5
        historical_surplus.append(surplus_energy)

        if len(historical_surplus) > 5:
            historical_surplus.pop(0)

    adjustment_factor = 1.0
    for j in range(len(historical_surplus)):
        adjustment_factor *= (1 + 0.01 * j)

    final_audit_score = current_output * adjustment_factor - penalty_accumulator

    Result: peak_capacity