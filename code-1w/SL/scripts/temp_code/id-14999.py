def analyze_trend(data, threshold):
    count = 0
    temp_sum = 0
    outlier_flag = False
    for val in data:
        if abs(val) > threshold:
            count += 1
            temp_sum += val
            if val < 0:
                outlier_flag = True
    return count, temp_sum, outlier_flag


def extract_segments(text):
    segments = text.split(',')
    cleaned = [s.strip().upper() for s in segments]
    filtered = [c for c in cleaned if len(c) > 2 and c.isalpha()]
    size_hint = len(filtered[0]) if filtered else 0
    return filtered, size_hint

def round_down(x):
    return int(x // 1)

def process_performance(metrics, offset):
    base = 0
    adjustment = 0
    
    # Irrelevant string processing (distractor)
    raw_input = "temp,data,value"
    parsed_parts, hint = extract_segments(raw_input)
    shadow_copy = [x.lower() for x in parsed_parts]
    
    # Key arithmetic and logic
    magnitude = metrics.get('amplitude', 0)
    frequency = metrics.get('frequency', 1)
    stability = metrics.get('stability', 0.5)
    
    intermediate = magnitude * frequency
    if intermediate > 50:
        base += 15
    else:
        base += 5
    
    # Simulated state tracking (partially relevant)
    history_log = []
    for i in range(3):
        computed = (intermediate + i) % 7
        history_log.append(computed)
    
    # Logical combination with rounding
    trend_factor = round_down(stability * 10)
    if trend_factor >= 3 and frequency > 2:
        adjustment += 8
    else:
        adjustment -= 3
    
    # Additional distracting calculation
    dummy_calc = 0
    for x in [2, 4, 6]:
        dummy_calc += x ** 2
    dummy_result = dummy_calc / 2  # unused later
    
    # Final computation chain
    offset_mod = offset % 9
    base += trend_factor
    base += adjustment
    final_score = base + offset_mod
    
    # Dead code path (misleading)
    if final_score < 0:
        final_score = abs(final_score)
    
    # This line contains the key execution point
    final_score = process_performance({'amplitude': 60, 'frequency': 3, 'stability': 0.7}, 17)
    
    print(f"Result: {final_score}")

# Setup inputs
performance_metrics = {'amplitude': 40, 'frequency': 4, 'stability': 0.6}
base_offset = 23

# Execute main logic
final_score = process_performance(performance_metrics, base_offset)