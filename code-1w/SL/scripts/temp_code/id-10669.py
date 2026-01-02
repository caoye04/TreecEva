def calculate_soil_health(index):
    if index < 3:
        return 0.5
    elif index == 3:
        return 0.7
    else:
        return 0.9

# Simulate crop yield prediction across multiple plots
def calculate_harvest_efficiency(plots):
    base_multiplier = 2.5
    penalty_factor = 0.8
    bonus_applied = False
    total_yield = 0.0
    temp_buffer = []  # Unused buffer (distractor)

    for plot in plots:
        size = plot['size']
        health_index = plot['health']
        irrigation_status = plot['irrigated']
        
        # Irrelevant string processing (distractor)
        status_msg = f"Plot size: {size}".replace('Plot', 'Field').upper()
        if len(status_msg) > 10:
            _ = status_msg.split(' ')

        health_score = calculate_soil_health(health_index)
        
        # Primary yield calculation
        raw_yield = size * base_multiplier * health_score
        
        # Conditional bonus logic with early break possibility
        if raw_yield > 40 and not bonus_applied:
            raw_yield *= 1.15
            bonus_applied = True

        # Simulated data logging (dead code path - distractor)
        debug_data = {}
        if raw_yield < 0:
            debug_data['error'] = 'Negative yield'

        # Bitwise flag check for pest resistance (semi-relevant)
        pest_resistant = plot.get('resistant', False)
        if pest_resistant:
            # XOR-based resilience adjustment (minor effect)
            adjustment = raw_yield ^ int(raw_yield) % 3
            raw_yield += adjustment * 0.1

        total_yield += raw_yield
        
        # Early exit condition based on cumulative threshold
        if total_yield > 150:
            break

    # Final adjustment using modular arithmetic
    final_adjustment = int(total_yield) % 7
    final_yield = round(total_yield - final_adjustment, 2)
    
    return final_yield

# Input data setup
plots_data = [
    {'size': 10, 'health': 2, 'irrigated': True, 'resistant': True},
    {'size': 15, 'health': 4, 'irrigated': False, 'resistant': False},
    {'size': 12, 'health': 5, 'irrigated': True, 'resistant': True},
    {'size': 8, 'health': 3, 'irrigated': True, 'resistant': False}
]

# Execution point of interest
final_yield = calculate_harvest_efficiency(plots_data)
print(f"Result: {final_yield}")