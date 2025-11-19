import math

def transform_block(value, salt):
    return (value ^ salt) + (value << 2)

data_blocks = [12, 7, 23, 45, 89]
salt_values = [3, 5, 7, 11, 13]
hash_scores = []

for i in range(len(data_blocks)):
    block = data_blocks[i]
    salt = salt_values[i]
    transformed = transform_block(block, salt)
    scaled = int(math.log(transformed) * 100)
    
    if scaled > 200:
        adjusted = scaled ** 2
    elif scaled > 100:
        adjusted = scaled * 2
    else:
        adjusted = scaled + 10
        
    hash_scores.append(adjusted)

final_hash_score = 0
for score in hash_scores:
    final_hash_score += score & 0xFF
    
print(f"Result: {final_hash_score}")