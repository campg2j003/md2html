@echo off
setlocal
set AUTOITDIR=%PROGRAMFILES(X86)%\AutoIt3
REM assumes Python is on PATH.
python setupexe.py py2exe
if exist "%AUTOITDIR%\aut2exe\aut2exe.exe" goto autoitFound
@echo *** AutoIt package not found, executable not created
goto :EOF
:autoitFound
"%AUTOITDIR%\aut2exe\aut2exe" /in md2html.au3 /comp 4 /console
@echo Build finished

