@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"

set "PYEXE="
for %%P in ("C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe" "C:\Python312\python.exe" "C:\Python311\python.exe") do (
  if exist %%P if not defined PYEXE set "PYEXE=%%~P"
)
if not defined PYEXE (
  for /f "delims=" %%P in ('where python 2^>nul') do if not defined PYEXE set "PYEXE=%%P"
)
if not defined PYEXE (
  echo [ERROR] Python 3.10+ not found.
  pause
  exit /b 1
)

echo [1/4] Check Python dependencies
"%PYEXE%" -c "import markdown, pymdownx, pygments, playwright, fitz, matplotlib, PIL" >nul 2>nul
if errorlevel 1 (
  "%PYEXE%" -m pip install -r requirements.txt
  if errorlevel 1 (
    echo [ERROR] pip install failed.
    pause
    exit /b 1
  )
)

echo [2/4] Generate illustrations
"%PYEXE%" render_figures.py
if errorlevel 1 (
  echo [ERROR] Figure generation failed.
  pause
  exit /b 1
)

echo [3/4] Build PDF
"%PYEXE%" build.py
if errorlevel 1 (
  echo [ERROR] PDF build failed.
  pause
  exit /b 1
)

echo [4/4] Verify PDF text and site links
"%PYEXE%" checks\verify_pdf_text.py
"%PYEXE%" checks\verify_repo.py

echo.
echo Done: output\book.pdf
pause
