@echo off
setlocal
if exist "%SystemRoot%\System32\chcp.com" "%SystemRoot%\System32\chcp.com" 65001 >nul
set "SLUG=%~1"
if not defined SLUG (
  echo Usage: build_book.bat ^<book-slug^>
  exit /b 2
)

pushd "%~dp0.."
set "PYEXE="
for %%P in (
  "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe"
  "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe"
  "C:\Python312\python.exe"
  "C:\Python311\python.exe"
) do (
  if exist %%P if not defined PYEXE set "PYEXE=%%~P"
)
if not defined PYEXE (
  for /f "delims=" %%P in ('where python 2^>nul') do if not defined PYEXE set "PYEXE=%%P"
)
if not defined PYEXE (
  echo [ERROR] Python 3.10+ not found.
  popd
  pause
  exit /b 1
)

echo [1/4] Check dependencies
"%PYEXE%" -c "import markdown, pymdownx, pygments, playwright, fitz, matplotlib, PIL" >nul 2>nul
if errorlevel 1 (
  "%PYEXE%" -m pip install -r build\requirements.txt
  if errorlevel 1 (
    echo [ERROR] pip install failed.
    popd
    pause
    exit /b 1
  )
)

echo [2/4] Generate illustrations for %SLUG%
"%PYEXE%" build\render_figures.py --book %SLUG%
if errorlevel 1 (
  echo [ERROR] Figure generation failed.
  popd
  pause
  exit /b 1
)

echo [3/4] Build %SLUG% PDF
"%PYEXE%" build\build.py --book %SLUG%
if errorlevel 1 (
  echo [ERROR] PDF build failed.
  popd
  pause
  exit /b 1
)

echo [4/4] Verify %SLUG% text
"%PYEXE%" build\checks\verify_pdf_text.py --book %SLUG%

echo.
echo Done: books\%SLUG%\output\
popd
pause
