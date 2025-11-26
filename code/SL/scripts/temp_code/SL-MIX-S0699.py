from collections import Counter

text_data = "data analysis requires careful data analysis and thorough analysis of the data"
words = text_data.split()
word_counts = Counter(words)
analysis_count = word_counts["analysis"]
data_count = word_counts["data"]
final_count = word_counts["analysis"]
print(f"Result: {final_count}")