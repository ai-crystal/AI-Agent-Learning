@echo off
setlocal enabledelayedexpansion
chcp 936 >nul
set "PATH=%SystemRoot%\System32;%SystemRoot%;%PATH%"
cd /d "%~dp0"

echo ==========================================
echo    从语言模型到智能体 —— 一键编译
echo ==========================================
echo.

set "PYEXE="
for %%C in (
  "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe"
  "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe"
  "C:\Python312\python.exe"
  "C:\Python311\python.exe"
) do (
  if exist %%C if not defined PYEXE set "PYEXE=%%~C"
)
if not defined PYEXE (
  for /f "delims=" %%i in ('where python 2^>nul') do (
    if not defined PYEXE set "PYEXE=%%i"
  )
)
if not defined PYEXE (
  for /f "delims=" %%i in ('py -3 -c "import sys;print(sys.executable)" 2^>nul') do (
    if not defined PYEXE set "PYEXE=%%i"
  )
)
if not defined PYEXE (
  echo [错误] 没有找到 Python，请先安装 Python 3.10 以上版本。
  echo        安装时记得勾选 Add Python to PATH，装完再双击本脚本。
  echo.
  pause
  exit /b 1
)

echo [1/4] 解释器：%PYEXE%
"%PYEXE%" -c "import sys; print('      Python', sys.version.split()[0])"

echo [2/4] 检查依赖 ...
"%PYEXE%" -c "import markdown, pymdownx, pygments, playwright, fitz, matplotlib, PIL" >nul 2>nul
if errorlevel 1 (
  echo       缺依赖，正在安装，首次需要联网，可能要几分钟 ...
  "%PYEXE%" -m pip install -r requirements.txt
  if errorlevel 1 (
    echo [错误] 依赖安装失败，请检查网络后重试。
    pause
    exit /b 1
  )
)

echo [3/4] 重绘插图 ...
pushd figures
"%PYEXE%" figs_a.py
"%PYEXE%" figs_b.py
"%PYEXE%" figs_c.py
popd

if exist "从语言模型到智能体.pdf" (
  del /f /q "从语言模型到智能体.pdf" >nul 2>nul
  if exist "从语言模型到智能体.pdf" (
    echo       提示：旧的 PDF 还被占用，请先关掉阅读器窗口。
  )
)
echo [4/5] 编译 PDF ...
"%PYEXE%" build.py
if errorlevel 1 (
  echo.
  echo [错误] 编译失败，请查看上面的报错信息。
  pause
  exit /b 1
)

echo [5/5] 校验 PDF（标题与字体内嵌）...
"%PYEXE%" tools\verify_pdf_text.py
if errorlevel 1 (
  echo.
  echo [警告] 上面列出的标题没有正确进入 PDF，或字体内嵌异常。
  echo        常见原因：系统里装了变量字体（*VF.ttf）又被样式选中；
  echo        解决办法：用 style.css 里的静态字体（SimSun / Microsoft YaHei）。
  echo.
)

if exist "从语言模型到智能体.pdf" (
  echo.
  echo 完成：%~dp0从语言模型到智能体.pdf
  echo 需要阅读时双击这个文件即可。
) else (
  echo [错误] 没有生成 PDF。
)
echo.
pause
