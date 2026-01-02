def analyze_response_time(rt, threshold=0.5):
    return 'optimal' if rt < threshold else 'delayed'

# Simulated sensor feedback loop with calibration drift
def generate_feedback_stream(base_value, iterations):
    stream = []
    accumulator = 0
    for i in range(iterations):
        noise = (i % 7) * 0.01
        signal = base_value + noise + (0.02 * i)
        if signal > 1.0:
            signal -= 0.3
        status = analyze_response_time(signal, 0.6)
        confidence = 0.8 if status == 'optimal' else 0.3
        stream.append((signal, confidence))
    return stream

def compute_entropy(values):
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log(prob)
    return round(entropy, 6)

def filter_anomalies(data_list):
    # Irrelevant filtering logic (dead path)
    return [x for x in data_list if isinstance(x, tuple)]

def accumulate_weighted_scores(feedback_seq):
    raw_scores = []
    temp_buffer = []
    index_map = {}

    for idx, (reading, conf) in enumerate(feedback_seq):
        adjusted = reading * conf * 100
        temp_buffer.append(adjusted * 0.95)  # Distractor buffer
        if idx % 3 == 0:
            raw_scores.append(adjusted + 5)
        elif idx % 4 == 0:
            raw_scores.append(adjusted - 2)
        else:
            raw_scores.append(adjusted)
        index_map[idx] = len(temp_buffer)  # Red herring tracking

    # Unused transformation
    inverted_map = {v: k for k, v in index_map.items()}

    return raw_scores

def derive_calibration_offsets(scores):
    offsets = []n    for s in scores:
        if s > 70:
            offsets.append(s * 0.01)
        elif s > 50:
            offsets.append(s * 0.005)
        else:
            offsets.append(s * 0.001)
    return offsets  # This function is called but result not directly used

def aggregate_performance(feedback_log, scale):
    # Core relevant logic
    extracted_signals = [item[0] for item in feedback_log]
    entropy = compute_entropy(extracted_signals)
    
    # Misleading use of set operations
    unique_confidences = list(set([c for _, c in feedback_log]))
    diversity_bonus = len(unique_confidences) * 1.5 if len(unique_confidences) > 1 else 0.0
    
    score_list = accumulate_weighted_scores(feedback_log)
    total_impact = sum(score_list) * scale
    
    # Decoy accumulation
    dummy_sum = 0
    for zipped in zip(score_list, score_list[1:] + [score_list[0]]):
        dummy_sum += abs(zipped[0] - zipped[1]) * 0.1
    
    # Critical line: final_score depends on entropy, diversity, and scaled sum
    final_component = total_impact * 0.1 + entropy * 10 + diversity_bonus
    
    # Dead code block (never executed due to structure)
    if False:
        fallback = 0
        for val in extracted_signals:
            fallback += int(val * 10) ^ 5
        final_component = fallback

    return int(round(final_component))

# Irrelevant global variables
system_status = 'ACTIVE'
data_schema = {'version': '2.1', 'mode': 'diagnostic'}
baseline_readings = [0.45, 0.47, 0.53, 0.61, 0.58]

# Generate main data chain
feedback_chain = generate_feedback_stream(base_value=0.42, iterations=12)
calibration_factor = 1.05

# Perform core computation
offset_series = derive_calibration_offsets(accumulate_weighted_scores(feedback_chain))  # Computed but unused
final_score = aggregate_performance(feedback_chain, calibration_factor)

print(f"Result: {final_score}")