from collections import defaultdict

# Simulate system benchmark data with multiple test phases
def generate_benchmark_data():
    data = defaultdict(list)
    data['phase1'].extend([85, 90, 78])
    data['phase2'].extend([92, 88])
    data['phase3'].extend([76, 81, 89, 94])
    return data

def calculate_phase_average(scores):
    return sum(scores) / len(scores)

def round_up(value):
    return int(value + 0.5)

def calculate_performance(raw_data):
    averages = {phase: round_up(calculate_phase_average(scores)) 
                for phase, scores in raw_data.items()}
    total = sum(averages.values())
    adjustment = len(averages) * 2  # Bonus for number of completed phases
    total += adjustment
    return total

# Irrelevant utility (mild distraction, intervention level 5)
def format_report(data):
    return {k: f'{v}%' for k, v in data.items()}

# Main execution
benchmark_data = generate_benchmark_data()
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")