@echo off
call "%~dp0..\..\books\build\build_book.bat" rag-context-rerank
exit /b %errorlevel%
