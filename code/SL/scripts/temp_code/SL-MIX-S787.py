import math

genomic_sequence = [4, 1, 7, 2, 9, 3]
weighted_sum = 0
for idx, value in enumerate(genomic_sequence, start=1):
    weighted_sum += idx * value
even_count = sum(1 for x in genomic_sequence if x % 2 == 0)
half_length = len(genomic_sequence) / 2
if even_count > half_length:
    stability_score = weighted_sum ** 2
else:
    stability_score = math.sqrt(abs(weighted_sum))

final_score = int(stability_score)
print(f"Result: {final_score}")