from collections import defaultdict

# Simulate product pricing with adjustments
prices = [120, 200, 150, 90]
adjustments = [-10, 25, -5, 0]
discount_map = defaultdict(lambda: 0)
discount_map['sale'] = 5
discount_map['clearance'] = 15

# Irrelevant distraction: unused variable
unused_flag = True

# Core logic using lambda and collections
calculate_total = lambda p_list, adj_list: sum(p + a - discount_map['sale'] for p, a in zip(p_list, adj_list))

base_total = sum(prices)
final_score = calculate_total(prices, adjustments)

print(f"Result: {final_score}")