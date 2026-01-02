import json

# 读取错误日志
with open('attention.json', 'r', encoding='utf-8') as f:
    error_log = json.load(f)

# 收集所有需要删除的id
ids_to_delete = set()
ids_to_delete.update(error_log.get('regex_failed', []))
ids_to_delete.update(error_log.get('ai_failed', []))

print(f'需要删除的id总数: {len(ids_to_delete)}')

# 读取数据集
with open('TreecEva_data_reduced_formated_cot.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'原始数据条数: {len(data)}')

# 过滤掉需要删除的数据项
filtered_data = [item for item in data if item.get('id') not in ids_to_delete]

print(f'删除后数据条数: {len(filtered_data)}')
print(f'实际删除了: {len(data) - len(filtered_data)} 条数据')

# 保存过滤后的数据
with open('TreecEva_data_reduced_formated_cot.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print('处理完成!')