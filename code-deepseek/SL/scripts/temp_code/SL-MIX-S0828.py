text_data = "DataAnalysis2024:Processing-Results_Compiled"
count_digits = 0
count_letters = 0
count_other = 0

for char in text_data:
    if char.isdigit():
        count_digits += 1
    elif char.isalpha():
        count_letters += 1
    else:
        count_other += 1

processing_overhead = 5
data_quality_score = 8
final_count = count_digits * processing_overhead + count_letters - count_other

print(f"Result: {final_count}")