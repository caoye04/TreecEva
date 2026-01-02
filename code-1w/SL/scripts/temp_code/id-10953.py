def evaluate_response(time_taken, word_count, accuracy):
    base_score = 100
    
    # Deduct points for exceeding optimal time (per second over 30)
    time_penalty = max(0, time_taken - 30) * 1.5
    
    # Bonus for concise responses within quality threshold
    length_bonus = 10 if 50 <= word_count <= 150 else -5
    
    # Accuracy scaling: partial credit given
    accuracy_points = accuracy * 50  # e.g., 0.85 -> 42.5
    
    intermediate_scores = [base_score, -time_penalty, length_bonus, accuracy_points]
    
    # Apply weighted adjustment using list comprehension
    adjusted_scores = [score * 0.95 for score in intermediate_scores]
    
    total = sum(adjusted_scores)
    
    # Early return if performance is exceptional
    if accuracy >= 0.9 and time_taken <= 40 and length_bonus > 0:
        return total + 20
        
    return total

# Simulated input values
response_time = 38
word_count = 120
accuracy_rate = 0.88

# Key computation step
final_score = evaluate_response(response_time, word_count, accuracy_rate)

print(f"Result: {final_score}")