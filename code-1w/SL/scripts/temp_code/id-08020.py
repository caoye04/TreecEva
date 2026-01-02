import math

# Simulated telemetry data from a distributed sensor network
technical_logs = [
    {'sensor': 'temp_01', 'value': 98.6, 'status': 'active', 'timestamp': 1712345600},
    {'sensor': 'temp_02', 'value': 102.3, 'status': 'active', 'timestamp': 1712345601},
    {'sensor': 'pressure_a', 'value': 14.7, 'status': 'idle', 'timestamp': 1712345602},
    {'sensor': 'flow_rate', 'value': 22.5, 'status': 'active', 'timestamp': 1712345603},
    {'sensor': 'vibration_x', 'value': 0.0034, 'status': 'warning', 'timestamp': 1712345604}
]

# System configuration and thresholds
system_profile = {
    'operating_mode': 'high_throughput',
    'tolerance_band': 0.05,
    'critical_thresholds': {
        'temperature': 100.0,
        'pressure': 15.0,
        'vibration': 0.005
    },
    'sensor_weights': {
        'temp_01': 0.3,
        'temp_02': 0.3,
        'pressure_a': 0.2,
        'flow_rate': 0.1,
        'vibration_x': 0.1
    }
}

# Irrelevant utility function (decoy)
def normalize_signal(data):
    max_val = max(d['value'] for d in data if d['sensor'].startswith('temp'))
    return [d['value'] / max_val for d in data if d['sensor'].startswith('temp')]

# Unused transformation (dead code path)
legacy_mapping = {entry['sensor']: entry['value'] * 1.02 for entry in technical_logs}

# Auxiliary diagnostic functions
def assess_stability(metrics):
    if not metrics:
        return 0.0
    variance = sum((m['value'] - 100.0) ** 2 for m in metrics) / len(metrics)
    return math.exp(-variance / 100)

# Complex state tracker with red herring variables
class StateAnalyzer:
    def __init__(self, config):
        self.mode = config['operating_mode']
        self.baseline = 100.0
        self.alert_count = 0
        self._cache = {}
        self.decoy_flag = False  # Misleading internal state

    def update_cache(self, key, value):
        self._cache[key] = value * 0.95  # Distractor computation

    def compute_health_score(self, entries):
        score = 0.0
        temp_entries = [e for e in entries if 'temp' in e['sensor']]
        for entry in temp_entries:
            if entry['value'] > system_profile['critical_thresholds']['temperature']:
                score -= 10
            else:
                score += 5
        return score

    def evaluate_response_time(self, logs):
        timestamps = [log['timestamp'] for log in logs]
        if len(timestamps) < 2:
            return 0.0
        avg_interval = sum(timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)) / (len(timestamps) - 1)
        return round(avg_interval, 3)  # Seemingly important but unused

# Secondary processing with misleading intermediate output
def calculate_efficiency_factor(raw_data):
    efficiency = 1.0
    for item in raw_data:
        if item['status'] == 'active':
            efficiency *= 1.01
        elif item['status'] == 'warning':
            efficiency *= 0.95
    decoy_output = efficiency * 1000  # Looks important, never used
    return efficiency

# Core logic buried among distractions
def extract_critical_flags(log_set):
    flags = set()
    for record in log_set:
        val = record['value']
        if val > 100 and 'temp' in record['sensor']:
            flags.add('HIGH_TEMP')
        if record['status'] == 'warning':
            flags.add('SYS_WARN')
    flags.add('DIAGNOSTIC_PASS')  # Always added (subtle)
    return flags

# Data transformation pipeline with irrelevant steps
def transform_dataset(entries):
    result = []
    for e in entries:
        new_entry = {
            'node': e['sensor'].upper(),
            'reading': round(e['value'] * 1.001, 4),
            'flagged': e['status'] != 'active',
            'adjusted': False
        }
        # Complex but irrelevant adjustment logic
        if 'pressure' in e['sensor']:
            new_entry['reading'] *= 1.01
            new_entry['adjusted'] = True
        elif 'vibration' in e['sensor']:
            new_entry['reading'] = abs(new_entry['reading']) ** 0.5
        result.append(new_entry)
    # Extra filtering that doesn't affect final outcome
    return [r for r in result if r['reading'] > 0]

# Main processing function containing the actual answer derivation
def process_metrics(log_data, system_state):
    analyzer = StateAnalyzer(system_state)
    
    # Step 1: Extract relevant temperature readings
    temps = [d for d in log_data if 'temp' in d['sensor']]
    
    # Step 2: Compute weighted contribution (only weights matter, not values)
    weight_sum = sum(system_state['sensor_weights'][d['sensor']] for d in temps)
    
    # Step 3: Assess stability (returns a decimal)
    stability = assess_stability(temps)
    
    # Step 4: Calculate base health (from class method)
    health = analyzer.compute_health_score(temps)
    
    # Step 5: Determine flag count (only set size matters)
    flags = extract_critical_flags(log_data)
    flag_count = len(flags)
    
    # Step 6: Transform data (but only use length)
    transformed = transform_dataset(log_data)
    data_volume = len(transformed)
    
    # Step 7: Use dictionary operations to combine factors
    factors = {
        'stability': stability,
        'health': health,
        'flags': flag_count,
        'volume': data_volume
    }
    
    # Step 8: Actual answer computation (buried)
    intermediate = factors['health'] + factors['flags'] * 100
    final_value = int(intermediate + factors['volume'])
    
    # Irrelevant set operation (red herring)
    all_nodes = {entry['sensor'] for entry in log_data}
    critical_nodes = {'temp_01', 'temp_02', 'pressure_a'}
    overlap = len(all_nodes & critical_nodes)
    
    # Final diagnostic is based on specific calculation chain
    final_diagnostic = final_value + overlap  # This is the real answer
    
    # Dead code branch (never executed)
    if False:
        backup = sum(factors.values())
        final_diagnostic = int(backup)
    
    return final_diagnostic

# Execution flow
log_data = technical_logs
system_state = system_profile

# Irrelevant pre-processing (distractor)
sorted_logs = sorted(log_data, key=lambda x: x['timestamp'], reverse=True)
if sorted_logs[0]['status'] == 'active':
    pass  # Do nothing

# Critical execution point
final_diagnostic = process_metrics(log_data, system_state)

# Print result as required
print(f"Result: {final_diagnostic}")