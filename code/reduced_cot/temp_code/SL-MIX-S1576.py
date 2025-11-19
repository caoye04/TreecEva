def calculate_efficiency(segment_length):
    if segment_length <= 1:
        return segment_length
    return (segment_length & 1) + calculate_efficiency(segment_length >> 1)

def process_message_segments(message):
    tokens = [ord(c) for c in message]
    scores = {}
    for i, token in enumerate(tokens):
        if token not in scores:
            scores[token] = []
        scores[token].append(calculate_efficiency(token))
    
    aggregated_scores = {k: sum(v) for k, v in scores.items()}
    sorted_scores = dict(sorted(aggregated_scores.items()))
    
    final_score = 0
    for key in sorted_scores:
        value = sorted_scores[key]
        final_score ^= (value << (key % 5))
    return final_score

message = "HELLO"
final_score = process_message_segments(message)
print(f"Result: {final_score}")