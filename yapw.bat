@echo off
cls

if not exist contrib\PortablePython1.0\python.exe echo. & echo ERROR: Python not found! & goto :END

echo.
echo Starting YAPW...
contrib\PortablePython1.0\python.exe src\yapw.py
goto :END

:END
