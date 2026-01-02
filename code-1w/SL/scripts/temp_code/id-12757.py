import itertools

def analyze_pattern(sequence):
    trend = 0
    fluctuation = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend += 1
        elif sequence[i] < sequence[i-1]:
            fluctuation += 1
    return trend - fluctuation

def validate_stability(metric):
    if metric < 0:
        return False
    temp_buffer = [metric * 2, metric // 3, metric % 7]
    checksum = sum(temp_buffer)
    return checksum > 5

def compute_final_score(stream):
    base_values = []
    aux_log = []
    for val in stream:
        if val % 2 == 0:
            base_values.append(val ** 0.5)
        else:
            base_values.append(val * 2)
    
    # Irrelevant transformation
    transformed = [x + 1 for x in base_values if x < 10]
    aux_log.extend(transformed)

    score_accum = 0
    for idx, v in enumerate(base_values):
        if idx % 3 == 0:
            score_accum += int(v)
        elif idx % 3 == 1 and validate_stability(idx):
            score_accum += v // 2
        else:
            score_accum -= 1

    pattern_metric = analyze_pattern(base_values)
    if pattern_metric > 0:
        score_accum += pattern_metric * 2

    # Dead computation - doesn't affect result
    dummy_state = list(itertools.accumulate([1, -1, 1, -1]))
    shadow_copy = [x * 0 + score_accum for x in dummy_state]

    final_score = score_accum + len([x for x in base_values if x > 5])
    
    return final_score

data_stream = [4, 9, 2, 7, 6, 3, 8]
intermediate_stats = {"count": len(data_stream), "max": max(data_stream)}
temp_result = [x**2 for x in data_stream if x < 5]

final_score = compute_final_score(data_stream)
print(f"Target result: {final_score}")