@echo off
set str=%path%
set "str2=%~dp0%ffmpeg\bin"
 
:STR_VISTOR
if defined  str (
for /F "delims=; tokens=1,*" %%a in ("%str%") do (
set "str=%%b"
echo %%a|findstr /i "%str2%" &&echo "����%str2%,��Ҫɾ��" &&(goto STR_VISTOR)
set "newPath=%newPath%%%a;"
goto :STR_VISTOR
))
 
setx PATH "%newPath%" -m
 
pause