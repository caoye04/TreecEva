from collections import defaultdict

def main():
    # Simulate user transaction behavior across multiple accounts
    transactions = [
        ('user_a', 'deposit', 250),
        ('user_b', 'withdraw', 100),
        ('user_a', 'withdraw', 50),
        ('user_c', 'deposit', 300),
        ('user_b', 'deposit', 200),
        ('user_c', 'withdraw', 75)
    ]

    # Track balance per user
    balances = defaultdict(float)
    for user, action, amount in transactions:
        if action == 'deposit':
            balances[user] += amount
        elif action == 'withdraw':
            balances[user] -= amount

    # Irrelevant tracking: count actions (not used in final score)
    action_counts = defaultdict(int)
    for user, action, _ in transactions:
        action_counts[action] += 1

    # Weight assignment based on user type (mock segmentation)
    user_risk_profile = {'user_a': 'low', 'user_b': 'medium', 'user_c': 'high'}
    risk_multiplier = {'low': 1.1, 'medium': 0.9, 'high': 0.7}
    base_weights = [1.0, 0.8, 1.2]  # Arbitrary initial weights

    # Compute dynamic weights using enumerate (semi-relevant)
    weights = []
    for i, w in enumerate(base_weights):
        adjusted = w * (i + 1)  # Artificial inflation by index
        weights.append(adjusted)

    # Normalize weights to sum to 3.0 (distraction computation)
    total_weight = sum(weights)
    normalized_weights = [w * 3.0 / total_weight for w in weights]
    scaling_factor = sum(normalized_weights) / len(normalized_weights)  # unused

    # Core logic: compute ranking score based on balance and risk-adjusted weight
    def compute_ranking(balances, weights):
        sorted_users = sorted(balances.keys())
        score = 0.0
        # Use zip to pair users with cyclic weights
        for user, w in zip(sorted_users, weights):
            base_value = balances[user]
            risk_mod = risk_multiplier[user_risk_profile[user]]
            contribution = base_value * risk_mod * w
            score += contribution

        # Additional logic: penalize if any balance exceeds threshold (not triggered)
        penalty = 0
        for b in balances.values():
            if b > 1000:
                penalty += b * 0.1
        return score - penalty

    # Misleading intermediate calculation (dead path)
    temp_analysis = {}
    for u in balances:
        temp_analysis[u] = balances[u] ** 0.5 if balances[u] > 0 else 0

    final_score = compute_ranking(balances, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()