from collections import defaultdict, Counter

# Simulated system log analyzer with decoy components and heavy interference

def analyze_events(raw_logs):
    event_count = defaultdict(int)
    priority_flags = [False] * len(raw_logs)
    temp_buffer = []
    debug_trace = {}

    for i, entry in enumerate(raw_logs):
        if 'ERROR' in entry:
            event_count['critical'] += 1
            priority_flags[i] = True
        elif 'WARN' in entry:
            event_count['warning'] += 1
        else:
            temp_buffer.append(entry)

        # Irrelevant computation - red herring
        if i % 3 == 0:
            debug_trace[f'step_{i}'] = len(temp_buffer) ** 2

    # Dead code path - never used
    def unused_validator(data):
        return sum(ord(c) for c in data) % 7 == 0

    return event_count

# Misleading auxiliary function that appears important but isn't directly used
def compute_health_score(events):
    base = sum(events.values())
    penalty = events.get('critical', 0) * 10
    return max(0, 100 - penalty - base // 5)

# Decoy data structure - looks like it's part of processing but isn't
historical_stats = {
    'peak_load': 98765,
    'last_failure_code': 0xDEADBEEF,
    'recovery_count': 42,
    'unused_diagnostic': [x**3 for x in range(15) if x % 4 != 0]
}

# Core logic buried under distractions
log_entries = [
    'INFO: system init',
    'WARN: high latency',
    'ERROR: disk failure',
    'INFO: user login',
    'WARN: retry attempt',
    'ERROR: timeout exceeded',
    'INFO: cleanup complete'
]

system_thresholds = {
    'critical_limit': 2,
    'grace_period_sec': 30,
    'mode_flag': True
}

# Heavily nested control flow with irrelevant branches
def process_metrics(logs, thresholds):
    stats = Counter()
    diagnostic_log = []
    accumulator = 0

    # Real processing mixed with noise
    for idx, log in enumerate(logs):
        words = log.split(': ')
        level = words[0]
        message = words[1] if len(words) > 1 else ''

        # Actual relevant logic
        if level == 'ERROR':
            stats['errors'] += 1
            accumulator += idx * 3
        elif level == 'WARN':
            stats['warnings'] += 1
            accumulator -= idx // 2
        else:
            stats['info'] += 1

        # Distractor: complex but unused string transformation
        transformed = ''.join(chr((ord(c) + idx) % 127) for c in message[:5]) if message else ''
        if transformed.isalpha():
            diagnostic_log.append(transformed[:3])

        # Nested conditional with misleading intermediate result
        if idx > 0 and level == 'WARN':
            if stats['errors'] > 0:
                for _ in range(2):
                    accumulator += 1  # Small incremental effect
            else:
                accumulator = abs(accumulator) ^ idx

    # Key calculation buried in multiple steps
    base_result = accumulator * (stats['errors'] + 1)
    adjustment = len(diagnostic_log) - stats['warnings']
    final_diagnostic = base_result + adjustment * 5

    # Dead branch - unreachable due to logic
    if False and len(historical_stats['unused_diagnostic']) > 10:
        final_diagnostic *= 0.5

    return final_diagnostic

# Trigger execution
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")