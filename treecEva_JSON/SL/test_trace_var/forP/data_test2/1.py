# 读取txt文件并将多行合并成一行,用\n分隔

# 输入文件路径
input_file = 'final_cot_test2.txt'
# 输出文件路径
output_file = 'output.txt'

# 读取文件
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 去除每行末尾的换行符,然后用\n连接
result = '\\n'.join(line.rstrip('\n\r') for line in lines)

# 写入输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'处理完成! 已将 {len(lines)} 行内容合并到一行')
print(f'输出文件: {output_file}')