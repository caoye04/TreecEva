@echo off
chcp 65001 >nul

echo ========================================
echo 自动化 GDB 变量追踪系统
echo ========================================

REM 自动检测源文件类型
set SOURCE_FILE=
if exist test.cpp (
    set SOURCE_FILE=test.cpp
    set COMPILER=g++
) else if exist test.c (
    set SOURCE_FILE=test.c
    set COMPILER=gcc
) else (
    echo 错误: 找不到 test.c 或 test.cpp
    pause
    exit /b 1
)

set EXECUTABLE=test_program.exe
set OUTPUT_FILE=output.txt

echo 找到源文件: %SOURCE_FILE%
echo 使用编译器: %COMPILER%

echo [1/3] 编译源文件...
%COMPILER% -g -O0 %SOURCE_FILE% -o %EXECUTABLE%
if errorlevel 1 (
    echo 编译失败!
    pause
    exit /b 1
)
echo √ 编译成功

echo [2/3] 生成 GDB 命令...
(
echo set pagination off
echo set confirm off
echo source gdb_trace.py
echo break main
echo run
echo trace-vars
echo quit
) > .gdb_commands

echo [3/3] 执行 GDB 追踪...
gdb -batch -x .gdb_commands %EXECUTABLE% 2>&1 > .temp_output.txt

REM 过滤：只保留以数字+空格开头，且不包含 "in " 的行
powershell -Command "Get-Content .temp_output.txt | Where-Object { $_ -match '^\d+\s+' -and $_ -notmatch '\sin\s+' } | Out-File -FilePath %OUTPUT_FILE% -Encoding UTF8"

echo.
echo ========================================
echo 追踪结果:
echo ========================================
type %OUTPUT_FILE%
echo ========================================

REM 清理临时文件
del .gdb_commands .temp_output.txt 2>nul

echo.
echo 完成!
pause