import json

# 读取原始数据
with open('TreecEva_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 重新编号
counter = 1
for item in data:
    # 如果这个条目有id字段，就重新编号
    if 'id' in item:
        item['id'] = f'id-{counter:05d}'
        counter += 1

# 保存修改后的数据
with open('TreecEva_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'处理完成！共重新编号了 {counter - 1} 条数据')