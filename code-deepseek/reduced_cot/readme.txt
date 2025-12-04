python -m venv reduced_cot_env
.\reduced_cot_env\Scripts\activate

处理所有cases（跳过已有COT的）
python main.py --all

处理所有cases（包括已有COT的）
python main.py --all --no-skip

处理单个case
python main.py --case SL-MIX-S0001

使用不同的AI模型
python main.py --all --model qwen3_coder

调整并行数（建议4-8）
python main.py --all --workers 8
