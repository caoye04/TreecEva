import subprocess
import re

def validate_answer(code, target_line, expected_answer):
    """验证答案是否正确"""
    
    # 写入临时文件
    with open("temp.py", "w") as f:
        f.write(code)
    
    # Joern脚本
    script = f"""
importCode("temp.py")
val target = cpg.assignment.lineNumber({target_line}).head
val vars = target.argument(2).ast.isIdentifier.name.toList
val defs = vars.flatMap(v => 
  if (cpg.method.parameter.name(v).nonEmpty) List(0)
  else cpg.identifier.name(v).reachingDef.lineNumber.toList
).sorted.distinct
println("RESULT:" + defs.mkString(","))
"""
    
    with open("verify.sc", "w") as f:
        f.write(script)
    
    # 运行Joern
    result = subprocess.run(["joern", "--script", "verify.sc"], 
                          capture_output=True, text=True)
    
    # 解析结果
    match = re.search(r"RESULT:(.+)", result.stdout)
    if match:
        actual = [int(x) for x in match.group(1).split(",") if x.strip()]
        return sorted(actual) == sorted(expected_answer)
    return False

# 测试
code = """def calculate_score(base_score, multiplier, bonus_flag):
    total = 0                           # Line 2
    adjusted_score = base_score         # Line 3
    
    if base_score > 50:                 # Line 5
        adjusted_score = base_score * 1.2  # Line 6
        bonus_flag = True               # Line 7
    elif base_score > 20:               # Line 8
        adjusted_score = base_score * 1.1  # Line 9
    else:                               # Line 10
        adjusted_score = base_score * 0.9  # Line 11
    
    if bonus_flag:                      # Line 13
        total = adjusted_score * multiplier + 10  # Line 14
    else:                               # Line 15
        total = adjusted_score * multiplier       # Line 16
    
    return total                        # Line 18"""

print(validate_answer(code, 14, [0, 6, 9, 11]))