from collections import defaultdict, Counter

# Simulate log data parsing for user activity on a platform
def parse_user_logs(raw_logs):
    user_activity = defaultdict(list)
    action_counter = Counter()
    temp_accumulator = 0

    for entry in raw_logs:
        parts = entry.split('|')
        user_id = parts[0]
        action = parts[1]
        timestamp = int(parts[2])

        user_activity[user_id].append((action, timestamp))
        action_counter[action] += 1

        # Distractor: accumulate but not used later
        temp_accumulator += len(action)

    return user_activity, action_counter


def filter_active_sessions(user_activity, min_actions=3):
    filtered_sessions = {}
    session_lengths = []

    for user, actions in user_activity.items():
        sorted_actions = sorted(actions, key=lambda x: x[1])
        if len(sorted_actions) >= min_actions:
            filtered_sessions[user] = sorted_actions
            session_lengths.append(len(sorted_actions))

    # Distractor: statistical computation with no impact
    avg_length = sum(session_lengths) / len(session_lengths) if session_lengths else 0
    length_variance = sum((x - avg_length) ** 2 for x in session_lengths) / len(session_lengths) if session_lengths else 0

    return filtered_sessions


def extract_action_sequences(filtered_sessions):
    sequences = []
    action_duration_map = defaultdict(list)\n
    for user, actions in filtered_sessions.items():
        seq = [act[0] for act in actions]
        sequences.append(seq)

        # Compute time gaps between consecutive actions (distractor logic)
        for i in range(1, len(actions)):
            gap = actions[i][1] - actions[i-1][1]
            action_duration_map[seq[i]].append(gap)

    # Distractor: derived structure not used in final result
    avg_durations = {k: sum(v)/len(v) for k, v in action_duration_map.items()}

    return sequences


def compute_sequence_complexity(sequences):
    complexity_scores = []
    for seq in sequences:
        unique_actions = len(set(seq))
        total_actions = len(seq)
        repetition_factor = total_actions - unique_actions

        # Real logic contribution
        entropy_like = 0
        count_map = {}
        for action in seq:
            count_map[action] = count_map.get(action, 0) + 1
        for count in count_map.values():
            prob = count / total_actions
            entropy_like -= prob * __import__('math').log(prob) if prob > 0 else 0

        score = (unique_actions * 1.5) + (entropy_like * 2.0) - (repetition_factor * 0.5)
        complexity_scores.append(score)

    return complexity_scores


def calculate_final_score(complexity_scores):
    base = sum(complexity_scores)
    penalty = 0
    for score in complexity_scores:
        if score < 5.0:
            penalty += 2.5
    return int(base - penalty)

# Main execution
if __name__ == '__main__':
    raw_log_data = [
        'U1|login|100', 'U1|edit|150', 'U1|save|200', 'U1|logout|250',
        'U2|login|110', 'U2|view|160', 'U2|view|170', 'U2|edit|300', 'U2|save|350', 'U2|logout|400',
        'U3|login|120', 'U3|settings|180', 'U3|logout|220',
        'U4|login|130', 'U4|edit|200', 'U4|edit|210', 'U4|edit|220', 'U4|save|230', 'U4|share|240', 'U4|logout|300'
    ]

    # Step 1: Parse logs
    user_activity, action_counter = parse_user_logs(raw_log_data)

    # Step 2: Filter sessions
    active_sessions = filter_active_sessions(user_activity)

    # Step 3: Extract sequences
    action_sequences = extract_action_sequences(active_sessions)

    # Step 4: Compute complexity
    processed_data = compute_sequence_complexity(action_sequences)

    # Key statement
    final_score = calculate_final_score(processed_data)
    print(f"Target result: {final_score}")