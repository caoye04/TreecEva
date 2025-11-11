for ($i = 1; $i -le 10; $i++) {
    Write-Host "==========================================`n开始执行第 $i 轮...`n==========================================" -ForegroundColor Cyan
    
    Write-Host "Step 1: 生成数据..." -ForegroundColor Yellow
    python main_loop.py --generate 10
    if ($LASTEXITCODE -ne 0) { Write-Host "生成数据失败" -ForegroundColor Red; exit 1 }
    
    Write-Host "Step 2: 执行代码..." -ForegroundColor Yellow
    python main_loop.py --execute
    if ($LASTEXITCODE -ne 0) { Write-Host "执行代码失败" -ForegroundColor Red; exit 1 }
    
    Write-Host "Step 3: 生成COT..." -ForegroundColor Yellow
    python main_loop.py --cot
    if ($LASTEXITCODE -ne 0) { Write-Host "生成COT失败" -ForegroundColor Red; exit 1 }
    
    Write-Host "Step 4: 评估结果..." -ForegroundColor Yellow
    python main_loop.py --evaluate
    if ($LASTEXITCODE -ne 0) { Write-Host "评估失败" -ForegroundColor Red; exit 1 }
    
    Write-Host "第 $i 轮完成`n" -ForegroundColor Green
}

Write-Host "==========================================`n所有10轮执行完毕！`n==========================================" -ForegroundColor Green