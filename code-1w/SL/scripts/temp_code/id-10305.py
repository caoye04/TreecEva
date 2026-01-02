from collections import defaultdict, Counter
import math

# Simulated user interaction data for a UI prototype
touch_events = [1.2, 0.8, 1.5, 2.3, 1.1, 0.9, 1.4, 2.1]
click_latency = [150, 180, 90, 200, 170, 160, 190, 210, 140]
scroll_depths = [0.3, 0.7, 0.5, 0.9, 0.6, 0.8, 0.4, 0.7]

# Irrelevant baseline metrics (distractor)
baseline_conversion = 0.023
baseline_bounce = 0.67
projected_revenue = 0.0  # unused dead variable

# Weight configuration for multi-factor scoring (relevant)
weights = {
    'responsiveness': 0.3,
    'consistency': 0.25,
    'engagement': 0.35,
    'accessibility': 0.1
}

# Misleading intermediate calculation (red herring)
effective_throughput = sum([math.log(lat + 1) for lat in click_latency]) / len(click_latency)
event_density = len(touch_events) / sum(touch_events)  # unused

# Data transformation pipeline
smoothed_touches = [t ** 0.5 for t in touch_events]  # normalize touch duration
latency_penalties = [max(0, (lat - 100) / 100) for lat in click_latency]
avg_penalty = sum(latency_penalties) / len(latency_penalties)

# Engagement heuristics (partially relevant)
session_richness = sum(1 for sd in scroll_depths if sd > 0.5)
completion_rate = session_richness / len(scroll_depths)
dwell_adjustment = math.sqrt(completion_rate)

# Decoy function - looks important but unused
def calculate_fidelity(events):
    total = 0
    for i in range(len(events)):
        if i % 2 == 0:
            total += events[i] * 1.1
        else:
            total += events[i] * 0.9
    return total / len(events)

# Another red herring: accessibility compliance check (unused path)
compliance_flags = defaultdict(bool)
for depth in scroll_depths:
    if depth > 0.8:
        compliance_flags['deep_read'] = True
    if depth < 0.2:
        compliance_flags['skim'] = True

# Feedback metric computation (core logic)
feedback_metrics = {}
feedback_metrics['responsiveness'] = 1 / (avg_penalty + 0.1)
feedback_metrics['consistency'] = 1 - (sum(abs(smoothed_touches[i] - smoothed_touches[i-1]) 
                                          for i in range(1, len(smoothed_touches))) / len(smoothed_touches))
feedback_metrics['engagement'] = completion_rate * dwell_adjustment
feedback_metrics['accessibility'] = min(scroll_depths) * 2  # proxy for inclusiveness

# Auxiliary confusion: spurious correlation attempt (irrelevant)
spurious_links = []
for t, c in zip(touch_events, click_latency):
    if t > 1.0 and c < 180:
        spurious_links.append(t * c)
link_strength = sum(spurious_links) / len(spurious_links) if spurious_links else 0.0

# Core aggregation function with nested logic
def aggregate_performance(metrics, weight_map):
    adjusted = defaultdict(float)
    total_weight = sum(weight_map.values())
    raw_sum = 0.0
    
    for key, weight in weight_map.items():
        normalized_key = key.replace('_', '')  # dummy transform
        if key == 'consistency':
            # Special smoothing for consistency
            adjusted[key] = (metrics[key] * 0.8 + 0.2)
        elif key == 'accessibility':
            # Threshold boost
            adjusted[key] = metrics[key] + (0.1 if metrics[key] > 0.5 else 0)
        else:
            adjusted[key] = metrics[key]
        
        # Apply weight
        raw_sum += adjusted[key] * weight
    
    # Final normalization
    final = raw_sum / total_weight
    
    # Introduce subtle correction (easy to miss but deterministic)
    if metrics['engagement'] > 0.5:
        final *= 1.05  # engagement bonus
    
    return final

# Trigger point: compute final score
final_score = aggregate_performance(feedback_metrics, weights)

# Print result as required
print(f"Result: {final_score}")