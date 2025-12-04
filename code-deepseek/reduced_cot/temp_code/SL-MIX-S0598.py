from collections import Counter

product_codes = ['A101', 'B205', 'A101', 'C309', 'B205', 'A101', 'D412']
category_counts = Counter(product_codes)
most_common_code = category_counts.most_common(1)[0][0]
count_matches = sum(1 for code in product_codes if code == most_common_code)
final_count = count_matches
print(f"Result: {final_count}")