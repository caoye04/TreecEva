def analyze_metrics(data):
    # Irrelevant helper function (dead code path)
    temp_vals = [len(x) for x in data if 'err' not in x]
    return sum(temp_vals) // len(temp_vals) if temp_vals else 0

# Misleading intermediate variables
dummy_counter = 0
buffer_cache = [0] * 10
temp_result = None

# Simulated system log entries with mixed content
log_entries = [
    'INFO: task_started id=45',
    'DEBUG: retry_attempt count=2',
    'INFO: task_completed duration=127',
    'WARN: threshold_exceeded limit=85 value=92',
    'INFO: task_completed duration=68',
    'INFO: task_completed duration=203',
    'DEBUG: heartbeat interval=30',
    'INFO: task_completed duration=91'
]

# Baseline configuration (partially relevant)
baseline = {
    'threshold': 100,
    'penalty_rate': 0.15,
    'bonus_credit': 7,
    'debug_mode': False
}

# Decoy data structures
event_map = {i: f'evt_{i}' for i in range(len(log_entries))}
flag_register = {'active': True, 'level': 3, 'mode': 'passive'}

# Auxiliary function that appears important but is only partially used
def extract_durations(logs):
    durations = []
    total_debug = 0
    for entry in logs:
        if 'duration=' in entry:
            parts = entry.split(' ')
            for part in parts:
                if part.startswith('duration='):
                    try:
                        durations.append(int(part.split('=')[1]))
                    except ValueError:
                        continue
        if 'retry_attempt' in entry:
            total_debug += 1  # Red herring accumulation
    return durations, total_debug

# Another decoy transformation
formatted_data = [line.upper().replace(':', ';') for line in log_entries]
size_metric = sum(len(item) for item in formatted_data) % 50  # Distractor

# Key function containing relevant logic among noise
def evaluate_performance(entries, config):
    # Extract meaningful information amidst noise
    raw_durations, debug_count = extract_durations(entries)
    
    # Irrelevant normalization step (looks important but unused later)
    normalized = [d / max(raw_durations) * 100 for d in raw_durations] if raw_durations else []
    
    # Real logic begins here — scoring based on baseline threshold
    above_threshold = 0
    below_threshold = 0
    for dur in raw_durations:
        if dur > config['threshold']:
            above_threshold += 1
        else:
            below_threshold += 1
    
    # Accumulate base score from performance distribution
    distribution_score = below_threshold * 10 - above_threshold * 5
    
    # Hidden rule: bonus applied only if exactly three tasks completed under threshold
    bonus_trigger = 1 if below_threshold == 3 else 0
    bonus_award = bonus_trigger * config['bonus_credit']
    
    # Penalty for long average duration (only if over threshold)
    avg_duration = sum(raw_durations) / len(raw_durations) if raw_durations else 0
    penalty = 0
    if avg_duration > config['threshold']:
        penalty = int(avg_duration * config['penalty_rate'])
    
    # Final score calculation (this is what matters)
    final_computation = distribution_score + bonus_award - penalty
    
    # Dead assignment — misleading because named "critical" but unused
    critical_intermediate = (above_threshold + below_threshold) * 17
    
    return final_computation

# Spurious preprocessing steps
filtered_logs = [x for x in log_entries if 'INFO' in x or 'WARN' in x]
correlation_id = hash(tuple(filtered_logs)) % 1000

# Key execution point
final_score = evaluate_performance(log_entries, baseline)

# Output result as required
print(f"Target result: {final_score}")