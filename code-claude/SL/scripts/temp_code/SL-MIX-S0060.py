def calculate_effective_power(base, mods, env):
    # Apply environmental factors
    env_factor = 1.0
    if env['weather'] == 'storm':
        env_factor = 0.8
    elif env['weather'] == 'clear':
        env_factor = 1.2
    
    # Process base power with modifiers
    adjusted_base = base
    mod_sum = sum(m['value'] for m in mods if m['active'])
    
    # Apply bitwise operations for special modifiers
    special_bits = 0
    for i, mod in enumerate(mods):
        if mod['special'] and i % 2 == 0:
            special_bits |= (1 << (i // 2))
    
    # These calculations don't affect the result
    theoretical_max = base * 2.5
    historical_avg = base * 0.75
    variance_factor = (theoretical_max - historical_avg) / base
    
    # Calculate power with different formulas for comparison
    formula_a = adjusted_base + mod_sum
    formula_b = adjusted_base * (1 + mod_sum / 100)
    
    # Select formula based on environment type
    if env['type'] == 'competitive':
        result = formula_b * env_factor
    else:
        result = formula_a * env_factor
    
    # Apply special bit modifications
    if special_bits & 3 == 3:  # If bits 0 and 1 are set
        result *= 1.1
    
    # Round to 1 decimal place
    return round(result, 1)

# Setup test data
base_power = 100
modifiers = [
    {'name': 'Boost', 'value': 25, 'active': True, 'special': True},
    {'name': 'Penalty', 'value': -10, 'active': True, 'special': False},
    {'name': 'Synergy', 'value': 15, 'active': False, 'special': True},
    {'name': 'Catalyst', 'value': 30, 'active': True, 'special': True}
]
environment = {
    'weather': 'clear',
    'type': 'competitive',
    'altitude': 1000,  # Not used in calculation
    'spectators': 250  # Not used in calculation
}

# Tracking system info (not used in calculation)
system_info = {
    'version': '2.3.1',
    'last_calibration': '2023-05-15',
    'logs': [{'timestamp': '2023-06-01', 'power_reading': 95}]
}

# Calculate alternative scenarios (not used in final result)
alternative_env = environment.copy()
alternative_env['weather'] = 'storm'
alternative_power = calculate_effective_power(base_power, modifiers, alternative_env)

# Calculate the effective power
effective_power = calculate_effective_power(base_power, modifiers, environment)
print(f"Target result: {effective_power}")