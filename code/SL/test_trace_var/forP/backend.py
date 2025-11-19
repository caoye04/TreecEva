from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os
import json
import traceback

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 配置基础路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# ==================== API: 获取所有测试用例列表 ====================
@app.route('/api/tests', methods=['GET'])
def get_tests():
    """扫描目录，返回所有测试用例"""
    try:
        test_cases = []
        
        print(f"📁 正在扫描目录: {BASE_PATH}")
        
        # 检查目录是否存在
        if not os.path.exists(BASE_PATH):
            print(f"❌ 目录不存在!")
            return jsonify({
                'success': False,
                'error': f'目录不存在: {BASE_PATH}'
            }), 404
        
        # 扫描所有文件
        files = os.listdir(BASE_PATH)
        print(f"📄 找到 {len(files)} 个文件/文件夹")
        
        for filename in files:
            # 只处理 test 开头的 .py 文件
            if filename.startswith('test') and filename.endswith('.py'):
                try:
                    print(f"\n🔍 正在处理: {filename}")
                    
                    # 解析文件名：去掉 .py 后缀
                    name_without_ext = filename[:-3]  # 例如: test1, test2
                    print(f"   ID: {name_without_ext}")
                    
                    # 尝试提取编号（从test后面开始的数字部分）
                    temp = name_without_ext[4:]  # 去掉 'test' 后的部分
                    number = ''
                    description = ''
                    
                    # 提取数字
                    i = 0
                    while i < len(temp) and temp[i].isdigit():
                        number += temp[i]
                        i += 1
                    
                    # 剩余部分作为描述
                    if i < len(temp):
                        description = temp[i:]
                    else:
                        description = f"Test {number}" if number else name_without_ext
                    
                    print(f"   编号: '{number}'")
                    print(f"   描述: '{description}'")
                    
                    # data文件夹名称
                    data_folder = f"data_{name_without_ext}"
                    data_path = os.path.join(BASE_PATH, data_folder)
                    print(f"   数据文件夹: {data_folder}")
                    print(f"   是否存在: {os.path.exists(data_path)}")
                    
                    # 检查data文件夹是否存在
                    if os.path.exists(data_path) and os.path.isdir(data_path):
                        test_case = {
                            'id': name_without_ext,
                            'filename': filename,
                            'number': number if number else name_without_ext,
                            'description': description,
                            'dataFolder': data_folder
                        }
                        test_cases.append(test_case)
                        print(f"✅ 添加测试用例成功")
                    else:
                        print(f"⚠️  跳过 - 未找到数据文件夹: {data_folder}")
                        
                except Exception as e:
                    print(f"❌ 处理文件 {filename} 时出错: {str(e)}")
                    traceback.print_exc()
                    continue
        
        # 按编号排序
        test_cases.sort(key=lambda x: (int(x['number']) if x['number'].isdigit() else 999, x['filename']))
        
        print(f"\n📊 总计找到 {len(test_cases)} 个测试用例")
        for tc in test_cases:
            print(f"   ✓ {tc['filename']}")
        
        return jsonify({
            'success': True,
            'data': test_cases,
            'count': len(test_cases)
        })
    
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        print(f"❌ get_tests 错误: {error_msg}")
        print(error_trace)
        return jsonify({
            'success': False,
            'error': error_msg,
            'trace': error_trace
        }), 500


# ==================== API: 获取测试用例的所有文件内容 ====================
@app.route('/api/test/<test_id>', methods=['GET'])
def get_test_data(test_id):
    """获取指定测试用例的所有文件内容"""
    try:
        print(f"\n📖 正在加载测试数据: {test_id}")
        
        # 读取Python源文件
        py_file = f"{test_id}.py"
        py_path = os.path.join(BASE_PATH, py_file)
        
        print(f"   查找文件: {py_path}")
        
        if not os.path.exists(py_path):
            error_msg = f'文件不存在: {py_file}'
            print(f"❌ {error_msg}")
            return jsonify({
                'success': False,
                'error': error_msg
            }), 404
        
        with open(py_path, 'r', encoding='utf-8') as f:
            py_content = f.read()
        print(f"✅ 已读取 {py_file}: {len(py_content)} 字符")
        
        # 读取data文件夹中的文件
        data_folder = f"data_{test_id}"
        data_path = os.path.join(BASE_PATH, data_folder)
        
        print(f"   数据文件夹: {data_path}")
        
        if not os.path.exists(data_path):
            error_msg = f'数据文件夹不存在: {data_folder}'
            print(f"❌ {error_msg}")
            return jsonify({
                'success': False,
                'error': error_msg
            }), 404
        
        # 文件名格式（新增 reverse_cot）
        files_to_read = {
            'trace': f'trace_{test_id}.txt',
            'trimmed': f'trimmed_trace_{test_id}.txt',
            'cot': f'final_cot_{test_id}.txt',
            'reverse_cot': f'reverse_cot_{test_id}.txt'  # ★ 新增倒序COT
        }
        
        file_contents = {
            'py': py_content
        }
        
        for key, filename in files_to_read.items():
            file_path = os.path.join(data_path, filename)
            print(f"   检查文件: {filename}")
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        file_contents[key] = content
                    print(f"   ✅ 已读取: {len(content)} 字符")
                except Exception as e:
                    error_text = f'[读取文件出错: {str(e)}]'
                    file_contents[key] = error_text
                    print(f"   ❌ 读取出错: {str(e)}")
            else:
                not_found_text = f'[文件不存在: {filename}]'
                file_contents[key] = not_found_text
                print(f"   ⚠️  文件不存在")
        
        print(f"✅ 测试数据加载完成")
        
        return jsonify({
            'success': True,
            'data': {
                'id': test_id,
                'contents': file_contents
            }
        })
    
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        print(f"❌ get_test_data 错误: {error_msg}")
        print(error_trace)
        return jsonify({
            'success': False,
            'error': error_msg,
            'trace': error_trace
        }), 500


# ==================== API: 获取单个文件内容 ====================
@app.route('/api/test/<test_id>/file/<file_type>', methods=['GET'])
def get_file_content(test_id, file_type):
    """获取指定测试用例的单个文件内容"""
    try:
        print(f"\n📄 获取文件: {test_id}/{file_type}")
        
        if file_type == 'py':
            file_path = os.path.join(BASE_PATH, f"{test_id}.py")
        else:
            data_folder = f"data_{test_id}"
            file_map = {
                'trace': f'trace_{test_id}.txt',
                'trimmed': f'trimmed_trace_{test_id}.txt',
                'cot': f'final_cot_{test_id}.txt',
                'reverse_cot': f'reverse_cot_{test_id}.txt'  # ★ 新增倒序COT
            }
            
            if file_type not in file_map:
                return jsonify({
                    'success': False,
                    'error': f'未知的文件类型: {file_type}'
                }), 400
            
            file_path = os.path.join(BASE_PATH, data_folder, file_map[file_type])
        
        print(f"   文件路径: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"   ❌ 文件不存在")
            return jsonify({
                'success': False,
                'error': f'文件不存在: {file_path}'
            }), 404
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"   ✅ 读取成功: {len(content)} 字符")
        
        return jsonify({
            'success': True,
            'data': {
                'content': content
            }
        })
    
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        print(f"❌ get_file_content 错误: {error_msg}")
        print(error_trace)
        return jsonify({
            'success': False,
            'error': error_msg,
            'trace': error_trace
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