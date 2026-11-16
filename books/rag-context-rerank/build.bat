@echo off
call "%~dp0..\..\build\build_book.bat" rag-context-rerank
exit /b %errorlevel%
