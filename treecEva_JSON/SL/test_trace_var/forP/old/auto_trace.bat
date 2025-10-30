@echo off
chcp 65001 >nul

echo ==================================================
echo Python 自动变量追踪系统
echo ==================================================

REM 检测源文件
set SOURCE_FILE=
if exist test.py (
    set SOURCE_FILE=test.py
) else (
    echo 错误: 找不到 test.py
    pause
    exit /b 1
)

echo.
echo 找到源文件: %SOURCE_FILE%

set OUTPUT_FILE=output.txt

echo.
echo [1/2] 执行追踪...
python trace_python.py %SOURCE_FILE%
if errorlevel 1 (
    echo 追踪失败!
    pause
    exit /b 1
)
echo √ 追踪成功

echo.
echo [2/2] 追踪结果:
echo ==================================================
type %OUTPUT_FILE%
echo ==================================================

echo.
echo 完成! 结果已保存到: %OUTPUT_FILE%
pause