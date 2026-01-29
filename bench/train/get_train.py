import json

# 从文件读取 ID 列表
with open('train_id.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    # 假设文件格式是 Python 列表形式
    train_ids = eval(content)  # 或使用 ast.literal_eval(content) 更安全

# 将 ID 列表转换为集合
train_id_set = set(train_ids)

# 读取原始数据集
with open('dataset_6000.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# 筛选数据
train_dataset = [item for item in dataset if item['id'] in train_id_set]

# 导出为 JSONL 格式
with open('train_dataset_500.jsonl', 'w', encoding='utf-8') as f:
    for item in train_dataset:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"成功导出 {len(train_dataset)} 条数据到 train_dataset_500.jsonl")