def analyze_efficiency(logs):
    durations = [entry['time'] for entry in logs if entry['active']]
    avg_duration = sum(durations) / len(durations) if durations else 0
    return avg_duration

logs_data = [
    {'time': 12, 'active': True, 'type': 'edit'},
    {'time': 5, 'active': False, 'type': 'idle'},
    {'time': 8, 'active': True, 'type': 'save'},
    {'time': 3, 'active': True, 'type': 'edit'},
    {'time': 10, 'active': False, 'type': 'pause'}
]

baseline = 7.5
measured = analyze_efficiency(logs_data)

productivity = int(100 * (1 - (measured - baseline) / baseline)) if baseline else 0

# Simulate error tracking (some distraction here)
class ErrorTracker:
    def __init__(self):
        self.errors = 0
        self.warning_count = 0

    def register(self, code):
        if code == 'E1':
            self.errors += 1
        elif code == 'W1':
            self.warning_count += 1

err_tracker = ErrorTracker()
err_tracker.register('E1')
err_tracker.register('W1')
err_tracker.register('E1')
errors = err_tracker.errors  # Only this matters

# Irrelevant stats
idle_time_estimate = sum(1 for e in logs_data if not e['active']) * 5
hypothetical_gain = idle_time_estimate * 0.3

# Core logic disguised with noise
def adjust_productivity(p, e):
    penalty = e * 3
    adjusted = p - penalty
    return max(adjusted, 10)

temp_result = adjust_productivity(productivity, errors)

# More distractions
event_types = [e['type'] for e in logs_data]
type_frequency = {t: event_types.count(t) for t in set(event_types)}
unique_actions = len(type_frequency)

# Final evaluation with red herring variables
def evaluate_performance(efficiency, fault_count):
    score = efficiency * 0.8 + (10 - fault_count * 2)
    bonus = 5 if efficiency >= 90 else 0  # unused
    debug_info = {'input_eff': efficiency, 'raw_faults': fault_count}
    final = int(score)
    return final

final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")