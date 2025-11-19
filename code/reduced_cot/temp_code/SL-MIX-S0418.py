from functools import reduce

document_title = 'The Fundamental Laws of Physics'
base_hash = hash(document_title)
title_length = len(document_title)
scale_factor = reduce(lambda x, y: x + y, map(ord, document_title[:4]))
scaled_checksum = base_hash % scale_factor

print(f'Result: {scaled_checksum}')