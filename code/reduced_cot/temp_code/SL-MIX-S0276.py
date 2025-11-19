from functools import reduce

def calculate_portfolio_index():
    # Transaction records: [timestamp, amount, type]
    transactions = [
        [1001, 5000, 'DEPOSIT'],
        [1002, -1200, 'WITHDRAWAL'],
        [1003, 800, 'DEPOSIT'],
        [1004, -300, 'FEE'],
        [1005, 1500, 'DEPOSIT']
    ]
    
    # Step 1: Categorize transactions using switch-like dictionary
    category_map = {
        'DEPOSIT': lambda x: x * 1.02,  # 2% bonus on deposits
        'WITHDRAWAL': lambda x: x * 1.01,  # 1% processing fee
        'FEE': lambda x: x * 1.05  # 5% fee surcharge
    }
    
    # Step 2: Apply category adjustments
    adjusted_amounts = list(map(lambda t: category_map[t[2]](t[1]), transactions))
    
    # Step 3: Create hash table for cumulative tracking
    cumulative_tracker = {}
    running_sum = 0
    for i, amount in enumerate(adjusted_amounts):
        running_sum += amount
        cumulative_tracker[i] = running_sum
    
    # Step 4: Apply divide and conquer to find median adjustment
    def find_median(lst):
        n = len(lst)
        if n <= 1:
            return lst[0] if lst else 0
        mid = n // 2
        if n % 2 == 1:
            return sorted(lst)[mid]
        else:
            return (sorted(lst)[mid-1] + sorted(lst)[mid]) / 2
    
    median_adjustment = find_median(adjusted_amounts)
    
    # Step 5: Calculate performance weights using functional reduction
    weights = list(map(lambda x: x / median_adjustment if median_adjustment != 0 else 0, adjusted_amounts))
    weight_product = reduce(lambda a, b: a * b, weights, 1)
    
    # Step 6: Compute final index
    final_index = int(sum(cumulative_tracker.values()) * weight_product)
    
    return final_index

final_index = calculate_portfolio_index()
print(f"Result: {final_index}")