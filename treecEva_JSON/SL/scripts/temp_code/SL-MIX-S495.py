def transform_tracker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

data_segments = [15, 22, 8, 37, 45]
segment_weights = [2, 3, 1, 4, 5]
adjusted_values = []

@transform_tracker
def process_segment(value, weight):
    adjusted = (value * weight) % 17 if value > 20 else (value + weight) % 13
    return adjusted

for i in range(len(data_segments)):
    val = data_segments[i]
    wt = segment_weights[i]
    adjusted_val = process_segment(val, wt)
    adjusted_values.append(adjusted_val)

valid_adjustments = [x for x in adjusted_values if x > 3 and x < 12]
transformation_count = process_segment.call_count
aggregate_sum = sum(valid_adjustments)
final_metric = aggregate_sum if transformation_count >= 3 else 0

print(f'Result: {final_metric}')