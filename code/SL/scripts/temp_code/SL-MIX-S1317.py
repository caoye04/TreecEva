def calculate_rebalancing_points(history, index):
    if index >= len(history):
        return 0
    
    current_value = history[index]
    if current_value < 0:
        return calculate_rebalancing_points(history, index + 2) + abs(current_value)
    else:
        return max(current_value, calculate_rebalancing_points(history, index + 1))

portfolio_history = [3, -1, 4, -2, 5, -3, 6]
initial_matrix = [[x for x in portfolio_history if x > 0], [abs(x) for x in portfolio_history if x < 0]]
rebalancing_dict = {i: calculate_rebalancing_points(portfolio_history, i) for i in range(len(portfolio_history))}
filtered_dict = {k: v for k, v in rebalancing_dict.items() if v > 3}
combined_values = [initial_matrix[0][i] + initial_matrix[1][i] for i in range(min(len(initial_matrix[0]), len(initial_matrix[1])))]
threshold_check = [val for val in combined_values if val > sum(filtered_dict.values()) / len(filtered_dict)]
optimal_rebalance_sum = sum(threshold_check) if threshold_check else 0
print(f"Result: {optimal_rebalance_sum}")