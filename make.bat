@ECHO off

if "%~1" == "" goto :help
if /I %1 == help goto :help
if /I %1 == build goto :build
goto :help

:help
echo.Please use `make ^<target^>` where ^<target^> is one of
echo.  build          build slime executable
goto :eof

:build
del /f /q .\build .\dist
pyinstaller slime.py --onefile -F --windowed --icon green-slime.ico
goto :eof
