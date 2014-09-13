@echo off
cls

If not exist Release\%1\ mkdir Release\%1
If not exist Release\%1\logs\ mkdir Release\%1\logs\
If not exist Release\%1\www\ mkdir Release\%1\www\
If not exist Release\%1\contrib\ mkdir Release\%1\contrib\

xcopy /Y /E www Release\%1\www
xcopy /Y /E contrib Release\%1\contrib
xcopy /Y /E src Release\%1

copy /Y README Release\%1\
copy /Y LICENSE Release\%1\
copy /Y CHANGES Release\%1\

Copy /Y yapw.cnf Release\%1\
Copy /Y yapw.bat Release\%1\

echo.
echo Starting build progress...
"%PROGRAMFILES%\NSIS\makensis.exe" setup.nsi
echo Build done! Setup ready.

:END
	echo.
	echo Creation finished!