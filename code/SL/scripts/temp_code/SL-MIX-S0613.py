master_registry = frozenset(range(100, 200))
manuscripts = {101, 103, 105, 107, 109, 111, 113, 115}
chronicles = {102, 104, 106, 108, 110, 112, 114, 116}
codexes = {120, 125, 130, 135, 140, 145, 150, 155}

preserved_lore = manuscripts.union(chronicles)
filtered_finds = master_registry.difference(codexes)
archived_tomes = preserved_lore.intersection(filtered_finds)

print(f'Result: {len(archived_tomes)}')