@echo off
call "%~dp0build_book.bat" rag-context-rerank
exit /b %errorlevel%
