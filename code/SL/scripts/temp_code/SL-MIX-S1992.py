file_metadata = {
    'alpha_module': {'tags': ['legacy', 'core', 'deprecated'], 'version': '2.1.3'},
    'beta_engine': {'tags': ['experimental', 'core', 'active'], 'version': '1.0.0'},
    'gamma_driver': {'tags': ['deprecated', 'driver', 'stable'], 'version': '3.2.1'}
}

version_weights = {'1.': 3, '2.': 2, '3.': 1}
tag_priority = {'core': 10, 'driver': 7, 'legacy': 5, 'deprecated': -3, 'experimental': 4, 'active': 2, 'stable': 6}

compatibility_calculator = lambda tags, version: sum(tag_priority.get(tag, 0) for tag in tags) * version_weights.get(version[:2], 1)

processed_scores = {}
for module_name, info in file_metadata.items():
    tags_set = frozenset(info['tags'])
    has_core_or_driver = 'core' in tags_set or 'driver' in tags_set
    is_not_deprecated_alone = not ('deprecated' in tags_set and len(tags_set) == 1)
    if has_core_or_driver and is_not_deprecated_alone:
        processed_scores[module_name] = compatibility_calculator(info['tags'], info['version'])
    else:
        processed_scores[module_name] = 0

final_compatibility_score = sum(processed_scores.values())
print(f'Result: {final_compatibility_score}')