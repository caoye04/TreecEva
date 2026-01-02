from collections import defaultdict
import math

# Simulate a system monitoring pipeline with performance metrics
def monitor_system_load(process_ids, base_frequency=2.4):
    frequency_shifts = []
    temp_logs = defaultdict(int)
    idle_cycles = 0

    for pid in process_ids:
        # Simulated frequency modulation based on process priority
        if pid % 7 == 0:
            frequency_shifts.append(base_frequency * 1.25)
        elif pid % 5 == 0:
            frequency_shifts.append(base_frequency * 0.8)
        else:
            frequency_shifts.append(base_frequency)

        # Track temperature impact (distractor logic)
        heat_contribution = (pid * 0.3) % 11
        temp_logs[pid] += int(heat_contribution)

        if pid % 3 == 0:
            idle_cycles += 1

    avg_frequency = sum(frequency_shifts) / len(frequency_shifts)
    return avg_frequency, temp_logs, idle_cycles


def analyze_operations(task_sequence):
    op_stats = defaultdict(lambda: 0)
    complexity_weights = {'A': 1.1, 'B': 2.3, 'C': 1.7, 'D': 3.0}
    total_weight = 0.0

    for idx, task in enumerate(task_sequence):
        op_stats[task] += 1
        # Weighted complexity accumulation
        if task in complexity_weights:
            total_weight += complexity_weights[task] * (idx + 1)

    # Red herring: unused transformation
    normalized_ops = [ord(t) - ord('A') for t in task_sequence]
    lambda_transform = list(map(lambda x: x ** 2 + 0.5, normalized_ops))

    average_weight = total_weight / len(task_sequence) if task_sequence else 0
    return op_stats, average_weight, lambda_transform

# Core calculation function
def calculate_efficiency(ops, overhead):
    base_efficiency = 100.0
    penalty_factor = 0.0

    # Penalty from operation distribution
    for op, count in ops.items():
        if count > 2:
            penalty_factor += count * 0.6

    # Overhead adjustment (relevant)
    adjusted_overhead = math.log(overhead + 1) if overhead > 0 else 0
    penalty_factor += adjusted_overhead * 1.1

    efficiency = base_efficiency - penalty_factor * 5
    return round(efficiency, 4)

# Main execution flow
if __name__ == "__main__":
    processes = [14, 23, 35, 42, 56, 63, 70, 84, 91, 98]
    tasks = ['A', 'B', 'C', 'B', 'A', 'D', 'C', 'B']

    # Step 1: Monitor system load (produces distractor data)
    avg_freq, temps, idle = monitor_system_load(processes)

    # Step 2: Analyze task operations (semi-relevant intermediate)
    op_distribution, avg_weight, transforms = analyze_operations(tasks)

    # Step 3: Compute auxiliary metric (mostly irrelevant)
    peak_transform = max(transforms) if transforms else 0
    transform_skew = peak_transform - sum(transforms) / len(transforms)

    # Step 4: Prepare inputs for efficiency calculation
    valid_ops = {k: v for k, v in op_distribution.items() if k in ['A', 'B', 'C', 'D']}
    overhead_value = idle + len([p for p in processes if p % 7 == 0])

    # Key statement: compute final efficiency score
    efficiency_score = calculate_efficiency(valid_ops, overhead_value)

    # Final output
    print(f"Result: {efficiency_score}")