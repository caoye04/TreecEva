from itertools import groupby

def calculate_performance(records):
    # Filter valid assessments with passing status
    passed = [r for r in records if r['passed']]
    
    # Group by category (assume sorted by category)
    grouped = {k: list(g) for k, g in groupby(passed, key=lambda x: x['category'])}
    
    # Compute average duration per category
    avg_times = {}
    for cat, entries in grouped.items():
        total = sum(e['duration'] for e in entries)
        avg_times[cat] = total / len(entries)
    
    # Baseline metric
    baseline_duration = 120.0
    adjustment_factor = 0.85
    
    # Calculate composite score based on efficiency
    efficiency_scores = []
    for avg in avg_times.values():
        if avg < baseline_duration:
            bonus = (baseline_duration - avg) * adjustment_factor
        else:
            bonus = 0
        efficiency_scores.append(10 + bonus)
    
    # Irrelevant distraction: unused variable
    max_possible = max(efficiency_scores) if efficiency_scores else 0
    
    # Final aggregation
    final_raw = sum(efficiency_scores)
    scaling_constant = 1.2
    final_score = int(final_raw * scaling_constant)
    
    return final_score

# Input data
assessments = [
    {'category': 'math',     'passed': True,  'duration': 95},
    {'category': 'math',     'passed': True,  'duration': 110},
    {'category': 'logic',    'passed': False, 'duration': 130},
    {'category': 'logic',    'passed': True,  'duration': 105},
    {'category': 'coding',   'passed': True,  'duration': 150},
    {'category': 'coding',   'passed': True,  'duration': 135},
    {'category': 'coding',   'passed': True,  'duration': 120}
]

# Execution point
final_score = calculate_performance(assessments)
print(f"Result: {final_score}")