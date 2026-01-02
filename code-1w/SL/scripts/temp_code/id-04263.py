from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_sensor_data = [1024, 2048, 1536, 3072, 2560]
error_flags = [False, True, False, False, True]

# Irrelevant auxiliary mappings (distractor)
legacy_code_mapping = {
    'A': 'alpha',
    'B': 'beta',
    'C': 'gamma',
    'D': 'delta'
}

# System state with mixed types (red herring)
system_state = {
    'version': '3.7.1',
    'active': True,
    'resources': {'cpu': 75, 'memory': 82, 'disk': 45},
    'mode': 'diagnostic',
    'cache_hits': 1203,
    'cache_misses': 198,
    'last_reset': 1623450000
}

# Log entries with noise and extra fields
log_entries = [
    {'ts': 1623456780, 'level': 'INFO', 'msg': 'Startup sequence initiated', 'src': 'SYS', 'extra': {}},
    {'ts': 1623456785, 'level': 'WARN', 'msg': 'High memory pressure', 'src': 'MEM', 'extra': {'temp': 72}},
    {'ts': 1623456790, 'level': 'INFO', 'msg': 'Checkpoint saved', 'src': 'STORAGE', 'extra': {}},
    {'ts': 1623456795, 'level': 'ERROR', 'msg': 'I/O timeout', 'src': 'DISK', 'extra': {'retry': 3}},
    {'ts': 1623456800, 'level': 'INFO', 'msg': 'Recovery complete', 'src': 'NET', 'extra': {}}
]

# Decoy function that looks important but is unused
def analyze_legacy_flow(data):
    accumulator = 0
    for item in data:
        if isinstance(item, dict) and 'legacy' in item:
            accumulator += len(item.keys())
    return accumulator

# Auxiliary transformation (partially relevant, partially distracting)
def extract_signal_strength(raw_values, threshold=1024):
    filtered = [x for x in raw_values if x > threshold]
    normalized = [math.log(x, 2) for x in filtered]  # Convert to power-of-2 exponents
    return sum(normalized) / len(normalized) if normalized else 0.0

# Misleading diagnostic calculator (dead path)
class DiagnosticEngine:
    def __init__(self, config):
        self.config = config
        self.history = []

    def compute_health(self, data):
        return sum(data) % 100

# Real processing begins here
def collect_diagnostic_stats(entries, state):
    stats = defaultdict(int)
    level_weights = {'INFO': 1, 'WARN': 5, 'ERROR': 10, 'CRITICAL': 25}
    
    # Meaningful aggregation
    for entry in entries:
        level = entry['level']
        stats['event_count'] += 1
        stats['severity_score'] += level_weights.get(level, 0)
        
        # Conditional logic with red herring
        if level == 'ERROR' and entry['src'] == 'DISK':
            stats['disk_errors'] += 1
            # This looks important but isn't used later
            stats['penalty'] += 15

    # Add irrelevant derived metrics (distractors)
    stats['apparent_stress'] = (stats['severity_score'] * stats['event_count']) / (state['resources']['cpu'] + 1)
    stats['fake_index'] = int(math.sqrt(state['cache_hits']))

    return stats

# Core logic with actual answer dependency
def calculate_base_metric(sensor_data):
    total_bits = 0
    for val in sensor_data:
        # Bit manipulation: count set bits in each reading
        bit_count = bin(val).count('1')
        total_bits += bit_count * (val & 7)  # Weight by lower 3 bits
    return total_bits

# Main processor combining multiple concepts
def process_metrics(logs, state):
    # Step 1: Extract real signal
    base_metric = calculate_base_metric(raw_sensor_data)
    
    # Step 2: Gather log statistics (only event_count and severity_score are used)
    log_stats = collect_diagnostic_stats(logs, state)
    
    # Step 3: Simulate conditional override (never triggers due to mode)
    override_mode = state['mode'] == 'emergency' and log_stats['disk_errors'] > 5
    if override_mode:
        return -999  # Dead code path
    
    # Step 4: Use only specific parts of log stats
    meaningful_contribution = log_stats['event_count'] * log_stats['severity_score']
    
    # Step 5: Incorporate system resources conditionally
    resource_factor = 1
    if state['resources']['memory'] > 80:
        resource_factor += 0.25
    if state['resources']['disk'] < 50:
        resource_factor += 0.15  # This applies
    
    # Step 6: Apply signal strength (actually constant)
    signal_strength = extract_signal_strength(raw_sensor_data)
    adjusted_signal = round(signal_strength * 100)  # becomes 110
    
    # Step 7: Combine components (only some are relevant)
    intermediate = base_metric + meaningful_contribution
    intermediate *= resource_factor
    
    # Step 8: Final computation chain
    final_diagnostic = intermediate + adjusted_signal
    
    # Red herring: enumerate and zip used meaninglessly
    indices = list(enumerate(zip(timestamps, error_flags)))
    decoy_sum = sum(idx * ts for idx, (ts, flag) in indices if flag)  # Computed but unused
    
    # Another decoy: counter on log sources
    src_counter = Counter(entry['src'] for entry in logs)
    diversity_bonus = len(src_counter) if src_counter['SYS'] > 0 else 0  # Unused
    
    return int(final_diagnostic)

# Key execution point
final_diagnostic = process_metrics(log_entries, system_state)
print(f"Target result: {final_diagnostic}")