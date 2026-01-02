def analyze_pattern(seq, threshold):
    count = 0
    running_sum = 0
    for val in seq:
        if val > threshold:
            count += 1
            running_sum += val
    return count * running_sum if count > 0 else 0

# Irrelevant helper function (distractor)
def smooth_data(data):
    return [round((data[i-1] + data[i] + data[i+1]) / 3) for i in range(1, len(data)-1)]

# Another distractor: unused transformation
toggle_mask = lambda x: x ^ 15

segments = [4, 7, 2, 9, 1, 5]
weights = [0.1, 0.3, 0.15, 0.25, 0.05, 0.15]

# Misleading intermediate computation (not used later)
avg_segment = sum(segments) / len(segments)
normalized = [s / max(segments) for s in segments]

# Real logic starts here
def compute_weighted_index(data, factors):
    index = 0
    for i in range(len(data)):
        if i % 2 == 0:
            index += data[i] * factors[i]
        else:
            index -= data[i] * factors[i] * 0.5
    return round(index, 3)

base_index = compute_weighted_index(segments, weights)

# Apply pattern analysis on transformed view
transformed_seq = [x * 2 for x in segments if x < 7]
activation = analyze_pattern(transformed_seq, threshold=8)

# Core processing with lambda integration
processor = lambda segs, acts: [s + (acts % 10) for s in segs]
processed_segments = processor(segments, activation)

# Final fusion step
def process_segments(segs, wts):
    temp_sum = 0
    for j in range(len(segs)):
        contribution = segs[j] * wts[j]
        if contribution > 0.5:
            temp_sum += contribution * 1.2
        else:
            temp_sum += contribution
    # Additional adjustment based on activation level
    adjustment = activation // 10
    return int(temp_sum + adjustment)

final_score = process_segments(processed_segments, weights)

# Dead code path (distractor)
if False:
    final_score *= 2

print(f"Result: {final_score}")