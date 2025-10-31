from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 配置基础路径
BASE_PATH = r"C:\Users\caoye\Desktop\TreecEva\treecEva_JSON\SL\test_trace_var\forP"

# ==================== API: 获取所有测试用例列表 ====================
@app.route('/api/tests', methods=['GET'])
def get_tests():
    """扫描目录，返回所有测试用例"""
    try:
        test_cases = []
        
        # 扫描所有test_*.py文件
        for filename in os.listdir(BASE_PATH):
            if filename.startswith('test') and filename.endswith('.py'):
                # 解析文件名
                name_without_ext = filename[:-3]  # 去掉.py
                parts = name_without_ext.split('_', 2)  # test_01_basic_noise
                
                if len(parts) >= 3:
                    number = parts[1]
                    description = parts[2].replace('_', ' ')
                else:
                    number = ''
                    description = name_without_ext
                
                data_folder = f"data_{name_without_ext}"
                data_path = os.path.join(BASE_PATH, data_folder)
                
                # 检查data文件夹是否存在
                if os.path.exists(data_path):
                    test_cases.append({
                        'id': name_without_ext,
                        'filename': filename,
                        'number': number,
                        'description': description,
                        'dataFolder': data_folder
                    })
        
        # 按编号排序
        test_cases.sort(key=lambda x: x['number'])
        
        return jsonify({
            'success': True,
            'data': test_cases
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ==================== API: 获取测试用例的所有文件内容 ====================
@app.route('/api/test/<test_id>', methods=['GET'])
def get_test_data(test_id):
    """获取指定测试用例的所有文件内容"""
    try:
        # 读取Python源文件
        py_file = f"{test_id}.py"
        py_path = os.path.join(BASE_PATH, py_file)
        
        if not os.path.exists(py_path):
            return jsonify({
                'success': False,
                'error': f'文件不存在: {py_file}'
            }), 404
        
        with open(py_path, 'r', encoding='utf-8') as f:
            py_content = f.read()
        
        # 读取data文件夹中的文件
        data_folder = f"data_{test_id}"
        data_path = os.path.join(BASE_PATH, data_folder)
        
        if not os.path.exists(data_path):
            return jsonify({
                'success': False,
                'error': f'数据文件夹不存在: {data_folder}'
            }), 404
        
        # 修正：文件名格式为 final_cot_test_01_basic_noise.txt
        files_to_read = {
            'trace': f'trace_{test_id}.txt',
            'trimmed': f'trimmed_trace_{test_id}.txt',
            'cot': f'final_cot_{test_id}.txt'
        }
        
        file_contents = {
            'py': py_content
        }
        
        for key, filename in files_to_read.items():
            file_path = os.path.join(data_path, filename)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_contents[key] = f.read()
            else:
                file_contents[key] = f'[文件不存在: {filename}]'
        
        return jsonify({
            'success': True,
            'data': {
                'id': test_id,
                'contents': file_contents
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ==================== API: 获取单个文件内容 ====================
@app.route('/api/test/<test_id>/file/<file_type>', methods=['GET'])
def get_file_content(test_id, file_type):
    """获取指定测试用例的单个文件内容"""
    try:
        if file_type == 'py':
            file_path = os.path.join(BASE_PATH, f"{test_id}.py")
        else:
            data_folder = f"data_{test_id}"
            # 修正：文件名格式
            file_map = {
                'trace': f'trace_{test_id}.txt',
                'trimmed': f'trimmed_trace_{test_id}.txt',
                'cot': f'final_cot_{test_id}.txt'
            }
            
            if file_type not in file_map:
                return jsonify({
                    'success': False,
                    'error': f'未知的文件类型: {file_type}'
                }), 400
            
            file_path = os.path.join(BASE_PATH, data_folder, file_map[file_type])
        
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'error': f'文件不存在: {file_path}'
            }), 404
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return jsonify({
            'success': True,
            'data': {
                'content': content
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# ==================== 静态文件服务 ====================
@app.route('/')
def index():
    """返回前端HTML页面"""
    return send_file('cot.html')


if __name__ == '__main__':
    print("=" * 60)
    print("🚀 COT生成框架 - 测试用例浏览器服务器")
    print("=" * 60)
    print(f"📁 基础路径: {BASE_PATH}")
    print(f"🌐 访问地址: http://localhost:5000")
    print("=" * 60)
    print("\n按 Ctrl+C 停止服务器\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)