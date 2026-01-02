def process_metrics(values):
    threshold = 42
    temp_result = 0
    secondary_cache = []

    for val in values:
        if val > threshold:
            temp_result += val * 0.1
            secondary_cache.append(val // 3)
        elif val == threshold:
            temp_result -= 5
        else:
            temp_result += len(str(val))

    return temp_result


def analyze_pattern(sequence):
    count_even = 0
    sum_odds = 0
    dummy_tracker = {"a": 0, "b": 0}

    for i, num in enumerate(sequence):
        if num % 2 == 0:
            count_even += 1
            dummy_tracker["a"] += i
        else:
            sum_odds += num
            dummy_tracker["b"] += 1

    # Irrelevant transformation
    transformed = [x ** 0.5 for x in sequence if x > 10]
    avg_transform = sum(transformed) / len(transformed) if transformed else 0

    return count_even > (len(sequence) // 2)

# Unused helper function (dead code path)
def unused_diagnostic(data):
    return sum(x * x for x in data if x < 0)

# Main computation chain
raw_input = [12, 45, 8, 67, 34, 23, 56]
convergence = process_metrics(raw_input)

# Simulate sensor drift compensation (mostly irrelevant)
sensor_drift = [x + 0.01 for x in raw_input]
adjusted = list(map(lambda x: x * 1.01 if x > 50 else x, sensor_drift))
data_stream = [int(x) for x in adjusted]

# Real logic hidden among distractions
is_stable = analyze_pattern(data_stream)
baseline = sum(data_stream) / len(data_stream)
offset_correction = (baseline * 0.05) if is_stable else 0

intermediate = convergence + offset_correction

# Key calculation buried in context
def calculate_rating(cvg, stream):
    rating = cvg
    penalty = 0

    # Nested conditional with early exit
    if len(stream) < 5:
        return -1
    
    for n in stream:
        if n > 50:
            penalty += 1
        if penalty > 2:  # Early break condition
            break

    # Conditional expression with string method distraction
    status_flag = "critical" if penalty >= 3 else "normal"
    adjustment = 10 if status_flag.upper().strip() == "CRITICAL" else 5
    
    rating -= adjustment

    # Red herring: complex but unused calculation
    snapshot = {i: stream[i] ** 2 for i in range(len(stream))}
    avg_snapshot = sum(snapshot.values()) / len(snapshot) if snapshot else 0

    return int(rating)

final_score = calculate_rating(convergence, data_stream)
print(f"Result: {final_score}")