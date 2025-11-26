task_categories = ['urgent', 'high', 'medium', 'low', 'urgent', 'high', 'urgent', 'medium']
category_counts = {}
for category in task_categories:
    category_counts[category] = category_counts.get(category, 0) + 1
priority_category = 'urgent'
final_count = category_counts.get(priority_category, 0)
print(f"Result: {final_count}")