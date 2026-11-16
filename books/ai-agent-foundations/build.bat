@echo off
call "%~dp0..\..\build\build_book.bat" ai-agent-foundations
exit /b %errorlevel%
