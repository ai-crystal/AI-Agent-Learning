@echo off
call "%~dp0..\..\books\build\build_book.bat" ai-agent-foundations
exit /b %errorlevel%
