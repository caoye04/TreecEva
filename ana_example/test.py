# test_joern_simple.py
import subprocess

joern_path = r"C:\Program Files\joern\joern-cli\bin\joern-cli.bat"

# 简单测试
try:
    result = subprocess.run([joern_path, "--help"], 
                          capture_output=True, text=True, timeout=10)
    print("Return code:", result.returncode)
    print("Help output:", result.stdout[:500])  # 只显示前500字符
    if result.stderr:
        print("Errors:", result.stderr)
except Exception as e:
    print("Error:", e)