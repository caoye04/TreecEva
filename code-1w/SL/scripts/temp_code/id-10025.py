def analyze_trend(values):
    if len(values) < 3:
        return False
    trend_up = all(values[i] < values[i+1] for i in range(len(values)-1))
    trend_down = all(values[i] > values[i+1] for i in range(len(values)-1))
    return 'increasing' if trend_up else ('decreasing' if trend_down else 'volatile')

# Simulated system health metrics over time
temperature_readings = [22.1, 22.5, 23.4, 24.6, 25.8]
load_history = [0.45, 0.56, 0.61, 0.68, 0.72]
cpu_spikes = [1.2, 1.8, 1.1, 2.3, 0.9]

# Extraneous helper function (not directly used)
def normalize(value, min_val=0, max_val=100):
    return (value - min_val) / (max_val - min_val)

# Auxiliary data processing
temp_trend = analyze_trend(temperature_readings)
load_trend = analyze_trend(load_history)

# Distractor variables
baseline_reference = sum(temperature_readings) / len(temperature_readings)
stale_metric = ''.join([str(int(x)) for x in cpu_spikes])
unused_flag = temp_trend == 'volatile' or load_trend != 'increasing'

# Threshold configuration for evaluation
thresholds = {
    'temp_limit': 30.0,
    'load_warning': 0.8,
    'spike_tolerance': 2.0,
    'duration_cycles': 5
}

# Metric aggregation
current_metrics = {
    'avg_temp': sum(temperature_readings) / len(temperature_readings),
    'peak_load': max(load_history),
    'excess_spikes': len([s for s in cpu_spikes if s > thresholds['spike_tolerance']]),
    'system_age_days': 450,
    'maintenance_window': 'Q3'
}

# String-based status encoding (uses string method)
status_flags = []
if current_metrics['avg_temp'] > 25.0:
    status_flags.append('high_temp')
if current_metrics['peak_load'] > thresholds['load_warning']:
    status_flags.append('elevated_load')

flag_summary = '; '.join(status_flags).upper() if status_flags else 'NORMAL'

# Core evaluation logic
def evaluate_performance(metrics, config):
    score = 100
    
    # Deductions based on thresholds
    if metrics['avg_temp'] > config['temp_limit']:
        score -= 25
    elif metrics['avg_temp'] > 24.0:
        score -= 10

    if metrics['peak_load'] >= config['load_warning']:
        score -= 15

    spike_penalty = metrics['excess_spikes'] * 5
    score -= spike_penalty
    
    # Arbitrary age factor (distractor logic)
    age_factor = 1 if metrics['system_age_days'] < 500 else 0.9
    adjusted_score = score * age_factor  # Not used in final path

    # Conditional override based on flag summary
    if 'ELEVATED_LOAD' in flag_summary:
        score -= 10
    
    # Final adjustment based on volatility
    volatile_spikes = any(abs(cpu_spikes[i] - cpu_spikes[i+1]) > 1.0 
                         for i in range(len(cpu_spikes)-1))
    if volatile_spikes and 'high_temp' in status_flags:
        score -= 8

    return int(score)

# Execution point of interest
final_score = evaluate_performance(current_metrics, thresholds)

# Print result as required
print(f"Result: {final_score}")