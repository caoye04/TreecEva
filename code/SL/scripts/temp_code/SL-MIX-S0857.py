from collections import Counter

inventory_items = ['hammer', 'wrench', 'screwdriver', 'hammer', 'wrench', 'wrench', 'bolt']
tool_counts = Counter(inventory_items)

counter_a = tool_counts['hammer']
counter_b = tool_counts['wrench']
final_tally = counter_a + counter_b

print(f"Result: {final_tally}")