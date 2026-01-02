from collections import defaultdict, Counter
import math

# Simulate user interaction sequences across multiple sessions
def analyze_user_engagement():
    raw_events = [
        ('session_1', ['click', 'hover', 'click', 'scroll', 'click']),
        ('session_2', ['hover', 'hover', 'click', 'click']),
        ('session_3', ['scroll', 'click', 'hover', 'hover', 'hover', 'click']),
        ('session_4', ['click', 'scroll', 'scroll'])
    ]

    # Track event counts per session
    event_counter = defaultdict(Counter)
    for session_id, events in raw_events:
        event_counter[session_id] = Counter(events)

    # Compute derived metrics (some are distractions)
    total_clicks = 0
    total_hovers = 0
    session_lengths = []
    entropy_values = []

    for session_id, counter in event_counter.items():
        total_clicks += counter['click']
        total_hovers += counter['hover']
        length = sum(counter.values())
        session_lengths.append(length)

        # Calculate Shannon entropy as a distraction
        entropy = 0.0
        for count in counter.values():
            p = count / length
            if p > 0:
                entropy -= p * math.log2(p)
        entropy_values.append(round(entropy, 4))

    # Distractor: Analyze scroll-to-click ratios
    scroll_click_ratio = 0
    total_scrolls = sum(counter['scroll'] for counter in event_counter.values())
    if total_clicks > 0:
        scroll_click_ratio = total_scrolls / total_clicks

    # Real computation path begins here
    avg_session_length = sum(session_lengths) / len(session_lengths)
    click_freq_global = total_clicks / sum(session_lengths)

    # Weighted engagement score
    base_score = 0
    for i, length in enumerate(session_lengths):
        if i % 2 == 0:
            base_score += length * 1.1
        else:
            base_score += length * 0.9

    # Apply hover bonus only if average entropy > 1.0 (distraction condition)
    avg_entropy = sum(entropy_values) / len(entropy_values)
    hover_bonus = 0
    if avg_entropy > 1.0:
        hover_bonus = total_hovers * 0.5

    # Final aggregation using bitwise manipulation for version masking (actual logic)
    version_mask = 0b101  # Simulated feature flag
    masked_base = int(base_score) & version_mask  # Only keep certain bits

    # Introduce irrelevant transformation
    inverted_mask = ~version_mask & 0b111  # Unused but computed

    # Core formula: combine masked base, click frequency, and hover bonus
    intermediate = masked_base + (click_freq_global * 10)
    final_score = int(intermediate + hover_bonus)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Call function to execute
analyze_user_engagement()