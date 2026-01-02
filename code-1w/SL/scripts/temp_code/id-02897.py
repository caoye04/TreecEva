import itertools

# Simulated user engagement metrics from a content platform
def analyze_engagement(raw_views, click_data):
    normalized = [v * 0.85 for v in raw_views if v > 10]
    filtered_clicks = list(filter(lambda x: x[1] > 2, click_data))
    
    # Irrelevant transformation (distractor)
    dummy_aggr = sum([c[0] * c[1] for c in filtered_clicks]) // len(filtered_clicks) if filtered_clicks else 0
    
    # Real signal: average session depth
    depth_scores = [c[1] for c in filtered_clicks]
    avg_depth = sum(depth_scores) / len(depth_scores) if depth_scores else 0
    return max(normalized) * avg_depth if normalized else 0

# Legacy function – unused but looks important (dead code path)
def calculate_reach_factor(followers, impressions):
    if followers == 0:
        return 0
    base_factor = (impressions / followers) * 1.7
    adjustment = 0
    for i in range(3):
        adjustment += base_factor / (i + 2)
    return adjustment

# Core processing with red herrings and multiple concepts
def transform_sequence(seq):
    shifted = [(x << 1) & 255 for x in seq]
    xor_key = 42
    encrypted = [s ^ xor_key for s in shifted]
    
    # Decoy checksum (never used in final logic)
    checksum = 0
    for val in encrypted:
        checksum = (checksum + val) % 97
    
    # Actual relevant result: count of values > 100
    return len([v for v in encrypted if v > 100])

# Complex control flow with distractors
def evaluate_content_quality(metrics, thresholds):
    quality_flags = []
    decoy_accumulator = 0
    
    for idx, m in enumerate(metrics):
        # Distractor logic
        if idx % 3 == 0:
            decoy_accumulator += m ** 0.5
            continue  # skips actual evaluation occasionally
        
        # Relevant logic mixed in
        pass_threshold = any(m > t for t in thresholds)
        flag = 'high' if m > 75 else 'low'
        quality_flags.append(flag)
    
    # Only this line matters
    high_count = quality_flags.count('high')
    return high_count * 13

# Main data processing chain
def process_metrics(data_packet):
    # Extract components
    views = data_packet.get('views', [])
    clicks = data_packet.get('clicks', [])
    tags = data_packet.get('tags', [])
    
    # Distraction: complex string manipulation that leads nowhere
    tag_combinations = list(itertools.combinations(tags, 2))
    tag_scores = {}
    for pair in tag_combinations:
        joined = ''.join(pair).lower()
        score = sum(ord(c) for c in joined) % 50
        tag_scores[pair] = score
    
    # Fake aggregation (red herring)
    total_tag_weight = sum(tag_scores.values()) // max(len(tag_scores), 1) if tag_scores else 0
    
    # Real work begins here
    base_engagement = analyze_engagement(views, clicks)
    sequence_signal = transform_sequence([len(clicks), len(views), len(tags), 42, 64])
    quality_bonus = evaluate_content_quality(views, [80, 90])
    
    # Critical computation path
    intermediate = base_engagement + sequence_signal
    adjustment = 1.0
    if intermediate > 100:
        adjustment = 0.9
    elif intermediate < 50:
        adjustment = 1.1
    
    # Final calculation
    final_value = (intermediate * adjustment) + quality_bonus
    
    # Decoy assignment
    final_value = final_value * 0.98  # almost looks like it's being refined
    
    # This is actually printed
    final_score = int(round(final_value))
    return final_score

# Input data with realistic structure
engagement_data = {
    "views": [120, 45, 89, 156, 201, 67, 94],
    "clicks": [(1, 3), (2, 1), (3, 4), (4, 2), (5, 5)],
    "tags": ["Tech", "AI", "Cloud", "Security"]
}

# Execute main logic
final_score = process_metrics(engagement_data)
print(f"Target result: {final_score}")