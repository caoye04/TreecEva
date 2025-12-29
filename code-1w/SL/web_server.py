from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import subprocess
import sys
import os
from pathlib import Path
import threading
import queue
from config import DATASET_PATH, ANSWER_PATH

BASE_DIR = Path(__file__).parent
DATASET_PATH = BASE_DIR / "scripts" / "data" / "TreecEva_data.json"
ANSWER_PATH = BASE_DIR / "scripts" / "data" / "answer.json"

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 全局日志队列
log_queue = queue.Queue()

class ScriptRunner:
    """脚本运行器，支持异步执行和日志捕获"""
    
    @staticmethod
    def run_script(script_name, args=None):
        """运行指定脚本并捕获输出"""
        cmd = [sys.executable, f"scripts/{script_name}.py"]
        if args:
            cmd.extend(args)
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # 实时读取输出
            while True:
                line = process.stdout.readline()
                if not line and process.poll() is not None:
                    break
                if line:
                    log_queue.put({"type": "stdout", "message": line.strip()})
            
            # 读取错误输出
            stderr = process.stderr.read()
            if stderr:
                for line in stderr.split('\n'):
                    if line.strip():
                        log_queue.put({"type": "stderr", "message": line.strip()})
            
            return process.returncode == 0
        except Exception as e:
            log_queue.put({"type": "error", "message": f"Script error: {str(e)}"})
            return False

@app.route('/')
def home():
    """API信息"""
    return jsonify({
        "message": "Dataset Management System API",
        "endpoints": {
            "/api/dataset": "GET - 获取完整数据集",
            "/api/dataset/stats": "GET - 获取统计信息",
            "/api/task/<task_id>": "GET - 获取单个任务",
            "/api/execute": "POST - 执行操作",
            "/api/logs": "GET - 获取日志流"
        }
    })

@app.route('/api/dataset')
def get_dataset():
    """获取完整数据集"""
    try:
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        return jsonify({"success": True, "data": dataset})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/dataset/stats')
def get_stats():
    """获取数据集统计信息"""
    try:
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        
        tasks = dataset[1:] if len(dataset) > 1 else []
        
        # 统计信息
        stats = {
            "total_tasks": len(tasks),
            "difficulty_distribution": {},
            "language_distribution": {},
            "intervention_distribution": {},
            "with_cot": sum(1 for t in tasks if t.get("task", {}).get("cot", "").strip()),
            "with_answer": sum(1 for t in tasks if t.get("task", {}).get("answer") is not None)
        }
        
        for task in tasks:
            # 难度分布
            diff = task.get("metadata", {}).get("difficulty", 0)
            stats["difficulty_distribution"][str(diff)] = stats["difficulty_distribution"].get(str(diff), 0) + 1
            
            # 语言分布
            lang = task.get("metadata", {}).get("language", "unknown")
            stats["language_distribution"][lang] = stats["language_distribution"].get(lang, 0) + 1
            
            # Intervention分布
            interv = task.get("metadata", {}).get("intervention", 0)
            stats["intervention_distribution"][str(interv)] = stats["intervention_distribution"].get(str(interv), 0) + 1
        
        return jsonify({"success": True, "data": stats})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/task/<task_id>')
def get_task(task_id):
    """获取单个任务详情"""
    try:
        with open(DATASET_PATH, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        
        task = next((t for t in dataset if t.get("id") == task_id), None)
        if task:
            return jsonify({"success": True, "data": task})
        else:
            return jsonify({"success": False, "error": "Task not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/execute', methods=['POST'])
def execute_operation():
    """执行操作（execute/cot/evaluate/generate）"""
    data = request.json
    operation = data.get('operation')
    task_id = data.get('task_id')
    num_tasks = data.get('num_tasks', 1)
    
    log_queue.put({"type": "info", "message": f"Starting {operation} operation..."})
    
    def run_async():
        try:
            if operation == 'execute':
                success = ScriptRunner.run_script('execute_tasks')
                    
            elif operation == 'cot':
                success = ScriptRunner.run_script('generate_cot')
                    
            elif operation == 'evaluate':
                success = ScriptRunner.run_script('ai_evaluation')
                    
            elif operation == 'generate':
                # 生成指定数量的任务
                for i in range(num_tasks):
                    log_queue.put({"type": "info", "message": f"Generating task {i+1}/{num_tasks}..."})
                    success = ScriptRunner.run_script('generate_new_task')
                    if not success:
                        break
            else:
                log_queue.put({"type": "error", "message": f"Unknown operation: {operation}"})
                return
            
            status = "✓ Completed" if success else "✗ Failed"
            log_queue.put({"type": "status", "message": f"Operation {operation} {status}"})
            
        except Exception as e:
            log_queue.put({"type": "error", "message": f"Error: {str(e)}"})
    
    # 在后台线程运行
    thread = threading.Thread(target=run_async)
    thread.daemon = True
    thread.start()
    
    return jsonify({"success": True, "message": f"{operation} operation started"})

@app.route('/api/logs')
def get_logs():
    """获取实时日志（SSE）"""
    def generate():
        import time
        while True:
            try:
                log = log_queue.get(timeout=0.1)
                yield f"data: {json.dumps(log)}\n\n"
            except queue.Empty:
                # 发送心跳
                yield f"data: {json.dumps({'type': 'ping', 'message': ''})}\n\n"
                time.sleep(1)
    
    return app.response_class(
        generate(),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Dataset Management System API Server")
    print("="*60)
    print("\n📡 API Server: http://localhost:5000")
    print("🌐 Web Interface: Open 'web_interface.html' in your browser")
    print("\n⚠️  Make sure to open web_interface.html directly in browser")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)