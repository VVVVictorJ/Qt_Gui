 @echo off
 ::����Ҫ���ü��뵽path���������е�·��
 set My_PATH=%~dp0%ffmpeg\bin
 set PATH=%PATH%;%My_PATH%
 reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%" /f
 exit
