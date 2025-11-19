from collections import defaultdict

def calculate_adjustment(day_index, modifier_list, memo):
    if day_index < 0:
        return 1.0
    if day_index in memo:
        return memo[day_index]
    
    current_modifier = modifier_list[day_index]
    previous_value = calculate_adjustment(day_index - 1, modifier_list, memo)
    
    # Apply different operations based on modifier type
    match current_modifier:
        case x if x > 0 and x <= 1.05:
            result = previous_value * (1 + x)
        case x if x > 1.05:
            result = previous_value + (x * 0.5)
        case x if x < 0:
            result = previous_value - abs(x)**1.5
        case _:
            result = previous_value
    
    memo[day_index] = result
    return result

def process_portfolio_changes(modifiers):
    # Sort modifiers by absolute value descending, then by original index ascending
    indexed_modifiers = sorted(enumerate(modifiers), key=lambda pair: (-abs(pair[1]), pair[0]))
    sorted_modifiers = [mod for _, mod in indexed_modifiers]
    
    memoization_cache = {}
    
    for i in range(len(sorted_modifiers)):
        if sorted_modifiers[i] == 0:
            break
        # Early exit condition when cumulative effect drops below threshold
        temp_result = calculate_adjustment(i, sorted_modifiers, memoization_cache)
        if temp_result < 0.1:
            return round(temp_result * 1000)
    
    final_value = calculate_adjustment(len(sorted_modifiers)-1, sorted_modifiers, memoization_cache)
    return round(final_value * 1000)

# Portfolio modifiers representing daily changes
stock_performance_modifiers = [0.03, -0.02, 1.1, 0.95, -0.05, 1.2, 0.0, 0.8]
final_portfolio_value = process_portfolio_changes(stock_performance_modifiers)
print(f"Result: {final_portfolio_value}")