import itertools

def analyze_efficiency(logs):
    total_ops = 0
    idle_periods = 0
    for log in logs:
        entries = log.split(',')
        ops = [int(e) for e in entries if e.isdigit()]
        total_ops += sum(ops)
        if len(ops) < 3:
            idle_periods += 1
    efficiency = total_ops / (len(logs) + 1)
    return efficiency

def calculate_stress_level(hours):
    stress = 0
    for h in hours:
        if h > 8:
            stress += (h - 8) * 2
        elif h < 4:
            stress -= 1
    return max(stress, 0)

def evaluate_performance(output, risk):
    base = output * 1.5
    penalty = 0
    if risk > 0.7:
        penalty = base * 0.3
    elif risk > 0.4:
        penalty = base * 0.1
    adjusted = base - penalty
    bonus = 0
    
    # Distractor: irrelevant sequence generation
    seq = [i for i in range(1, 6)]
    combos = list(itertools.combinations(seq, 3))
    combo_count = len(combos)  # Unused variable (distractor)
    
    # Distractor: string processing with no impact
    status_msg = "System: Operational"
    padded_msg = status_msg.ljust(20, '.')
    char_sum = sum(ord(c) for c in padded_msg if c.isalpha())  # Dead computation
    
    # Real logic continues
    if adjusted > 100 and risk < 0.5:
        bonus = 20
    elif output > 80:
        bonus = 10
    
    final = adjusted + bonus
    
    # Additional distraction: unused data structure
    history = {"scores": [], "flags": set()}
    for _ in range(2):
        history["scores"].append(final * 0.1)
        # This doesn't affect anything
    
    return int(final)

# Main execution
work_logs = ["10,5,8", "7,6", "9,9,7,6", "5"]
efficiency = analyze_efficiency(work_logs)
hours_worked = [9, 7, 10, 8, 6]
stress = calculate_stress_level(hours_worked)

productivity = int(efficiency) + (40 - stress)
risk_factor = (stress / 20.0)  # Normalize to 0-1 scale

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Irrelevant post-processing
summary = f"Performance: {final_score}"
summary_bytes = summary.encode('utf-8')
byte_checksum = sum(summary_bytes) % 100  # Not used

print(f"Result: {final_score}")