import math

# Simulated sensor network diagnostic system
def collect_sensor_data():
    raw_readings = {
        'temp_01': 95.7, 'temp_02': 102.3, 'temp_03': 98.4,
        'pressure_a': 1120, 'pressure_b': 1080, 'pressure_c': 1150,
        'vibration_x': 4.2, 'vibration_y': 5.1, 'vibration_z': 3.8
    }
    return raw_readings

# Irrelevant transformation - red herring
def transform_coordinates(data):
    x, y, z = data.get('vibration_x', 0), data.get('vibration_y', 0), data.get('vibration_z', 0)
    radius = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.atan2(z, math.sqrt(x**2 + y**2))
    # This function is called but its result ignored
    return {'radius': radius, 'theta': theta, 'phi': phi}

# Unused helper - dead code path
def validate_checksum(record):
    total = 0
    for char in str(record):
        if char.isdigit():
            total += int(char)
    return total % 7 == 0

# Real processing begins here
def filter_anomalies(readings):
    critical_set = set()
    warning_set = set()
    
    for sensor, value in readings.items():
        if 'temp' in sensor and value > 100:
            critical_set.add(sensor)
        elif 'pressure' in sensor and (value < 1090 or value > 1140):
            if value < 1090:
                warning_set.add(sensor)
            else:
                critical_set.add(sensor)
        elif 'vibration' in sensor and value > 4.0:
            warning_set.add(sensor)
    
    # Key insight: only sensors in critical but not warning are selected
    exclusive_critical = critical_set - warning_set
    
    # Misleading aggregation - looks important but unused
    avg_pressure = sum(v for k, v in readings.items() if 'pressure' in k) / 3
    pressure_deviation = abs(avg_pressure - 1116.666)
    
    return list(exclusive_critical)

def generate_system_log():
    # Complex-looking log structure with irrelevant details
    log_entries = []
    for i in range(5):
        entry = {
            'timestamp': 1678840000 + i * 60,
            'event_id': f'EVT{i+1}',
            'severity': ['INFO', 'WARNING', 'CRITICAL'][i % 3],
            'component': ['network', 'power', 'io', 'sensor'][i % 4],
            'code': [200, 404, 500][i % 3]
        }
        log_entries.append(entry)
    
    # Only the count of CRITICAL entries matters
    critical_count = len([e for e in log_entries if e['severity'] == 'CRITICAL'])
    return {'entries': log_entries, 'critical_events': critical_count}

def analyze_readings(relevant_sensors, system_log):
    base_score = 100
    
    # Scoring based on number of relevant sensors
    sensor_penalty = len(relevant_sensors) * 15
    
    # Log-based bonus
    log_bonus = system_log['critical_events'] * 22
    
    # Complex-looking but irrelevant calculation
    total_chars = sum(len(k) for k in system_log['entries'][0].keys())
    key_entropy = total_chars * 0.7
    
    # Dummy state machine that does nothing
    state = 'IDLE'
    for i in range(3):
        if state == 'IDLE':
            state = 'PROCESSING'
        elif state == 'PROCESSING':
            state = 'FINALIZING'
        else:
            state = 'COMPLETE'
    
    # Actual computation
    intermediate = base_score - sensor_penalty + log_bonus
    
    # Final nonlinear transformation
    final_value = int(intermediate * 1.3)
    
    # Decoy floating point operation
    decoy_float = math.log(final_value + 1) / math.pi
    
    return final_value

# Main execution flow
data_pool = collect_sensor_data()

# Call but ignore result - distraction
spherical_coords = transform_coordinates(data_pool)

# Real filtering
filtered_sensors = filter_anomalies(data_pool)

# Build log
system_log = generate_system_log()

# Critical statement
final_diagnostic = analyze_readings(filtered_sensors, system_log)

print(f"Result: {final_diagnostic}")