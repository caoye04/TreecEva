def analyze_workload(load_data):
    base_set = {12, 18, 24, 30, 36}
    processed_data = {x * 2 for x in load_data}
    processed_data.add(42)
    processed_data.discard(24)
    return processed_data

def evaluate_metrics(primary_set, secondary_set):
    common_metrics = primary_set.intersection(secondary_set)
    unique_to_primary = primary_set - secondary_set
    temp_result = len(common_metrics) * 5
    adjusted_set = {x + temp_result for x in unique_to_primary}
    adjusted_set.update({x * 2 for x in common_metrics})
    return adjusted_set

workload_data = {6, 9, 12, 15, 18}
initial_processing = analyze_workload(workload_data)
reference_set = {20, 25, 30, 35, 40}
intermediate_calc = len(initial_processing) + len(reference_set)

adjusted_set = evaluate_metrics(initial_processing, reference_set)
extra_metrics = {55, 60, 65}
final_score = adjusted_set.union(extra_metrics)

performance_score = sum(final_score) - sum(extra_metrics)
print(f"Result: {performance_score}")