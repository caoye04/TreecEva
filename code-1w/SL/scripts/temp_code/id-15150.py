from collections import defaultdict

# Simulate a ranking system for participants in a multi-event competition
def main():
    events = ['math', 'coding', 'design', 'presentation']
    participants = ['Alice', 'Bob', 'Charlie', 'Diana']

    # Raw scores from each event (real data)
    raw_scores = {
        'Alice': [88, 92, 75, 80],
        'Bob': [76, 85, 90, 88],
        'Charlie': [90, 78, 82, 73],
        'Diana': [85, 95, 80, 92]
    }

    # Normalize scores per event using min-max scaling
    normalized = defaultdict(list)
    for i, event in enumerate(events):
        col_scores = [raw_scores[p][i] for p in participants]
        min_val, max_val = min(col_scores), max(col_scores)
        for p in participants:
            norm_score = (raw_scores[p][i] - min_val) / (max_val - min_val) if max_val != min_val else 0
            normalized[p].append(norm_score)

    # Compute average normalized performance
    avg_normalized = {p: sum(scores)/len(scores) for p, scores in normalized.items()}

    # Assign preliminary rankings based on average (lower index = better)
    sorted_by_avg = sorted(avg_normalized.keys(), key=lambda x: avg_normalized[x], reverse=True)
    rankings = {p: idx + 1 for idx, p in enumerate(sorted_by_avg)}

    # Dummy transformation: mirror rankings (distraction)
    mirrored_rankings = {p: 5 - rank for p, rank in rankings.items()}  # irrelevant

    # Weight vector for final calculation (based on event importance)
    weights = {'math': 0.25, 'coding': 0.35, 'design': 0.15, 'presentation': 0.25}

    # Irrelevant computation: count how many times a participant ranked in top 2 across events (misleading)
    top2_counts = defaultdict(int)
    for event_idx, event in enumerate(events):
        event_scores = [(p, raw_scores[p][event_idx]) for p in participants]
        sorted_event = sorted(event_scores, key=lambda x: x[1], reverse=True)
        for p, _ in sorted_event[:2]:
            top2_counts[p] += 1

    # More distractions: unused helper function
    def unused_helper(data):
        return sum(x * 2 for x in data if x > 0.5)

    # Another red herring: transform normalized into z-scores (not used)
    z_scores = {}
    for p in participants:
        mean_norm = sum(normalized[p]) / len(normalized[p])
        variance = sum((x - mean_norm)**2 for x in normalized[p]) / len(normalized[p])
        std_dev = variance ** 0.5
        z_scores[p] = [(x - mean_norm) / std_dev if std_dev != 0 else 0 for x in normalized[p]]

    # Core logic: compute final score using ranking and weights
    def calculate_final_score(ranks, w):
        base_score = 0
        # Use original rankings and weight by inverse rank (higher rank = lower numerical rank = better)
        for p, rank in ranks.items():
            contribution = (1 / rank) * sum(w.values()) * 100
            base_score += contribution
        # Apply adjustment factor based on number of participants
        adjustment = len(participants) * 0.5
        final = base_score + adjustment
        return int(final)  # deterministic integer result

    # Critical execution point
    final_score = calculate_final_score(rankings, weights)

    # Print result as required
    print(f"Result: {final_score}")

    # Unused conditional branch (dead code path)
    if False:
        fallback = sum(top2_counts.values()) * 10
        print(f"Fallback: {fallback}")

if __name__ == "__main__":
    main()