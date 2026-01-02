from itertools import cycle

# Simulate sensor array readings with noise filtering
def collect_readings():
    raw_data = [105, 92, 110, 88, 95, 103, 87, 98]
    filtered = [x for x in raw_data if 90 <= x <= 105]
    return filtered

# Apply dynamic gain based on environment mode
def calculate_gain(mode, temp_factor=1.0):
    base_gain = 0.85
    boost_modes = {'turbulent': 1.3, 'laminar': 1.1, 'default': 1.0}
    gain = base_gain * boost_modes.get(mode, 1.0)
    
    # Irrelevant compensation (distractor)
    pressure_adj = 0.98
    flow_rate = 45.6
    density = 1.225
    dummy_comp = pressure_adj * flow_rate / (density + 1e-5)
    
    return gain

# Adjust flux using nonlinear transformation
def adjust_flux(flux, mode):
    readings = collect_readings()
    avg_reading = sum(readings) / len(readings) if readings else 0
    
    # Complex adjustment logic
    if mode == 'turbulent':
        flux *= 1.25
    elif mode == 'calibration':
        flux *= 0.9
    else:
        flux *= 1.1
    
    # Secondary adjustment based on average sensor input
    flux += avg_reading * 0.05
    
    # Dead code path (distractor)
    if False:
        backup_modes = ['safe', 'debug']
        for m in backup_modes:
            flux -= 1  # Never executed
    
    # Use lambda for dynamic correction
    correct = lambda x: x * (1 + 0.03 * (x > 100))
    flux = correct(flux)
    
    # String-based flag check (uses string method)
    flags = "error, info, warning"
    has_warning = 'warning' in flags.lower()
    if has_warning:
        flux *= 0.99
    
    return round(flux, 4)

# Main execution block
base_flux = 76.0
mode = 'laminar'

temp_sensor = 23.5
humidity = 47
sensor_cycle = cycle(['A', 'B', 'C'])
next(sensor_cycle)  # Unused but simulates system tick

# Extraneous calculation (distractor)
dark_current = 0.002
integration_time = 1.5
baseline_noise = dark_current * integration_time

# Key computation step
final_flux = adjust_flux(base_flux, mode)

# Print final result as required
print(f"Result: {final_flux}")