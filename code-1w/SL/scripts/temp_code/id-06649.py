from itertools import compress

def analyze_efficiency(logs):
    durations = [entry['time'] for entry in logs]
    statuses = [entry['success'] for entry in logs]
    avg_duration = sum(durations) / len(durations)
    success_rate = sum(statuses) / len(statuses)
    
    # Distractor: irrelevant filtering
    filtered_logs = [d for d in durations if d > avg_duration]
    penalty = len(filtered_logs) * 0.05

    efficiency = (success_rate * 100) - (avg_duration * 0.1) - penalty
    return efficiency

def calculate_stress_level(workload, breaks):
    base_stress = workload * 1.2
    recovery = len(breaks) * 5
    stress_index = base_stress - recovery
    stress_index = max(1, stress_index)
    
    # Dead computation: not used later
    normalized = (stress_index - 1) / 9 * 100 if stress_index <= 10 else 100
    
    return stress_index

def evaluate_performance(output, risk):
    base = output * 10
    adjustment = 0
    if risk > 7:
        adjustment -= 15
    elif risk < 4:
        adjustment += 10
    else:
        adjustment += 5
    
    # Complex but relevant logic
    multiplier = 1.5 if output > 80 else (1.2 if output > 60 else 0.8)
    score = (base + adjustment) * multiplier
    
    # Red herring: unused transformation
    transformed = round(score ** 0.5, 3) * 10
    
    return int(score)

# Simulated dataset
work_sessions = [
    {'time': 120, 'success': True},
    {'time': 150, 'success': True},
    {'time': 90, 'success': False},
    {'time': 180, 'success': True},
    {'time': 200, 'success': False}
]

break_intervals = [10, 15, 5]  # minutes

# Irrelevant preprocessing
session_times = [s['time'] for s in work_sessions]
long_tasks = list(filter(lambda x: x > 140, session_times))
completion_flags = [1 if s['success'] else 0 for s in work_sessions]
flag_summary = ''.join(str(f) for f in completion_flags)
split_flags = flag_summary.split('0')

# Key variables
productivity = analyze_efficiency(work_sessions)
risk_factor = calculate_stress_level(sum(session_times), break_intervals)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

# Extra distraction
buffer = [0]*5
for i in range(len(buffer)):
    buffer[i] = i * 2

# Output result
print(f"Result: {final_score}")