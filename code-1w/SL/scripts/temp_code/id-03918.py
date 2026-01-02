from collections import Counter
def process_performance_data(logs):
    event_counts = Counter([log['event'] for log in logs])
    total_actions = len(logs)
    unique_events = len(event_counts)
    
    # Calculate score based on frequency of 'click' and 'hover' events
    click_ratio = event_counts.get('click', 0) / total_actions if total_actions > 0 else 0
    hover_ratio = event_counts.get('hover', 0) / total_actions if total_actions > 0 else 0
    
    base_score = 50 + (click_ratio * 30)
    adjustment = (hover_ratio * 20) - (unique_events * 2.5)
    final_score = base_score + adjustment
    
    # Irrelevant metric (distractor)
    avg_length = sum(len(log['user']) for log in logs) / total_actions if total_actions > 0 else 0
    
    return int(final_score)

# Simulated user interaction data
entries = [
    {'user': 'alice', 'event': 'click'},
    {'user': 'bob', 'event': 'hover'},
    {'user': 'carol', 'event': 'click'},
    {'user': 'dave', 'event': 'scroll'},
    {'user': 'eve', 'event': 'hover'},
    {'user': 'mallory', 'event': 'click'},
    {'user': 'trudy', 'event': 'keypress'},
    {'user': 'oscar', 'event': 'hover'}
]

final_score = process_performance_data(entries)
print(f"Result: {final_score}")