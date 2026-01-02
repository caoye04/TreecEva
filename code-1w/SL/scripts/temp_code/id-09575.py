import math

# System diagnostics simulation with interference

def monitor_throughput(timestamps):
    intervals = []n    for i in range(1, len(timestamps)):
        intervals.append(timestamps[i] - timestamps[i-1])
    return sum(intervals) / len(intervals) if intervals else 0.0

# Irrelevant signal processing function (dead path)
def process_waveform(samples):
    magnitude = 0
    for s in samples:
        magnitude += abs(s) * 0.5
    normalized = magnitude / len(samples) if samples else 0
    return round(normalized, 3)

# Core data transformation with distractors
def decode_payload(raw_frame):
    raw_data = [x ^ 21 for x in raw_frame]  # Bitwise decoy
    shifted = [x >> 1 for x in raw_data]    # Unused transformation
    return [x for x in raw_data if x % 2 == 1]

# Misleading statistical summary (red herring)
def compute_resilience_score(metrics):
    base_score = 0
    for val in metrics:
        if val > 50:
            base_score += 1.5
        elif val > 20:
            base_score += 0.7
        else:
            base_score += 0.1
    adjustment = len(metrics) * 0.05
    return base_score + adjustment  # Not used in final result

# Key function: computes diagnostic from timing and errors
def aggregate_metrics(log_entries, error_flags):
    valid_durations = []
    penalty_factor = 0
    
    # Primary logic chain (nested 4 levels deep)
    for entry in log_entries:
        if 'status' in entry and entry['status'] == 'active':
            duration = entry.get('duration', 0)
            start_phase = entry.get('phase', 0)
            
            if duration > 0:
                adjusted = duration * (1 + start_phase * 0.1)
                filtered = True
                
                # Cross-reference with error set using set operations
                flag_key = int(duration % 10)
                if flag_key in error_flags:
                    penalty_factor += 1
                    continue  # Skip errored entries
                
                temp_check = []
                for d in str(duration):
                    if d.isdigit():
                        digit = int(d)
                        if digit > 0:
                            temp_check.append(math.log(digit + 1))
                
                if len(temp_check) >= 2:
                    smoothed = sum(temp_check) / len(temp_check)
                    valid_durations.append(smoothed * duration)

    # Distractor: unused min/max calculations on tuples
    if valid_durations:
        duration_stats = (min(valid_durations), max(valid_durations), len(valid_durations))
        avg_duration = sum(valid_durations) / len(valid_durations)
        spike_ratio = duration_stats[1] / (avg_duration + 1e-6)
        
        # Decoy string manipulation
        tag_parts = ['sys', 'diag', 'v2']
        version_tag = ''.join([part[0] for part in tag_parts]).upper()
        metadata_hash = len(version_tag) * 17
        
        # Actual answer computation buried under noise
        base_value = int(avg_duration // 1)
        modifier = penalty_factor ** 2
        final_diagnostic = base_value - modifier
        
        # Print required output
        print(f"Result: {final_diagnostic}")
        return final_diagnostic
    
    return -1

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 8192
DEFAULT_TIMEOUT = 15.5
RETRY_LIMIT = 3

# Simulation data with mixed relevance
timestamps = [100, 105, 112, 115, 123]
failure_codes = [2, 5, 7, 9]
signal_samples = [-3.2, 1.4, 5.6, -0.8, 2.9]

# Main execution context
timing_log = [
    {'status': 'active', 'duration': 84, 'phase': 1},
    {'status': 'idle', 'duration': 32, 'phase': 0},  # skipped
    {'status': 'active', 'duration': 91, 'phase': 2},
    {'status': 'active', 'duration': 77, 'phase': 1},
    {'status': 'active', 'duration': 88, 'phase': 2}
]

failure_set = set(failure_codes)  # Used in set operation
data_frame = [64, 32, 16, 8]

# Dead code path invocation (misleading)
throughput_avg = monitor_throughput(timestamps)
signal_level = process_waveform(signal_samples)
decoded_data = decode_payload(data_frame)
resilience = compute_resilience_score(decoded_data)

# Critical execution point
final_diagnostic = aggregate_metrics(timing_log, failure_set)