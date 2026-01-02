from collections import defaultdict, Counter

# Simulated user interaction logs with redundant and irrelevant fields
timestamps = [1678886400, 1678886460, 1678886520, 1678886600, 1678886680]
user_actions = ['click', 'scroll', 'click', 'hover', 'click']
duration_ms = [500, 1200, 300, 800, 450]
irrelevant_flags = [0x1A, 0x2C, 0x0F, 0x3D, 0x1B]  # Bitwise red herring

# Preprocessing: extract action counts and session features
action_counter = Counter(user_actions)
click_count = action_counter['click']
hover_count = action_counter['hover']
scroll_count = action_counter['scroll']

def process_durations(durations):
    avg_duration = sum(durations) / len(durations)
    max_duration = max(durations)
    min_duration = min(durations)
    normalized = [d / avg_duration for d in durations]  # Unused distraction
    return int(avg_duration)

avg_duration_ms = process_durations(duration_ms)

# Simulate feature matrix with decoy computations
decoy_matrix = [[i * j for j in range(3)] for i in range(5)]
misleading_sum = sum(sum(row) for row in decoy_matrix)  # Dead-end calculation

# Build processed data with relevant and irrelevant components
processed_data = defaultdict(int)
processed_data['base_clicks'] = click_count
processed_data['temporal_factor'] = len(timestamps) // 2
processed_data['duration_metric'] = avg_duration_ms // 100
processed_data['phantom_flag'] = irrelevant_flags[0] ^ 0xFF  # XOR distraction

# Secondary fake transformation
fake_weights = [0.5, 0.3, 0.2]
weighted_fake = sum(processed_data[f'phantom_flag'] * w for w in fake_weights)  # Not used

# Core scoring logic (depends only on select inputs)
def calculate_final_score(data):
    base = data['base_clicks'] * 10
    temporal_bonus = data['temporal_factor'] * 3
    duration_penalty = data['duration_metric']
    
    # Irrelevant condition (always true, but looks meaningful)
    if data['temporal_factor'] >= 0:
        base += 5
    
    # Another distraction: unused internal calculation
    hypothetical_score = (base + temporal_bonus) * 0.9
    
    final = base + temporal_bonus - duration_penalty
    return final

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")