import json
import random

# 读取数据集
with open('dataset_6000.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# 读取评估集 ID
with open('bench_id.txt', 'r', encoding='utf-8') as f:
    bench_ids = eval(f.read())  # 假设文件内容是 Python 列表格式

# 筛选符合条件的候选 ID
candidates = []

for item in dataset:
    item_id = item['id']
    
    # 提取 ID 数字部分
    id_number = int(item_id.split('-')[1])
    
    # 检查条件
    if (item_id not in bench_ids and 
        id_number > 500 and 
        item['task']['code'].count('\n') >= 70):
        candidates.append(item_id)

# 检查候选数量
print(f"找到 {len(candidates)} 个符合条件的样本")

if len(candidates) < 500:
    print(f"警告: 符合条件的样本不足 500 个!")
    train_ids = candidates
else:
    # 随机选择 500 个
    random.seed(42)  # 设置随机种子以保证可复现性
    train_ids = random.sample(candidates, 500)

# 排序以便查看
train_ids.sort()

# 保存为列表格式
with open('train_id.txt', 'w', encoding='utf-8') as f:
    f.write(str(train_ids))

print(f"已生成 train_id.txt，包含 {len(train_ids)} 个 ID")
print(f"前 10 个 ID: {train_ids[:10]}")