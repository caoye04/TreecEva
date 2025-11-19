def polynomial_hash(chunk, base=31, mod=1000000007):
    hash_value = 0
    for char in chunk:
        hash_value = (hash_value * base + ord(char)) % mod
    return hash_value

documents = [
    "CONFIDENTIAL_REPORT_Q3",
    "FINANCIAL_STATEMENTS_2023",
    "EMPLOYEE_DATABASE_BACKUP"
]

weights = [2, 3, 5]
verification_code = 0

for i, doc in enumerate(documents):
    chunk_hashes = [
        polynomial_hash(doc[j:j+5]) 
        for j in range(0, len(doc), 5) 
        if j+5 <= len(doc)
    ]
    weighted_sum = sum(hash_val * weights[i] for hash_val in chunk_hashes)
    verification_code = (verification_code + weighted_sum) % 1000000007

print(f"Result: {verification_code}")