@echo off
setlocal
setlocal enabledelayedexpansion

set "PORT=80"
set "VERBOSE=0"
set "FILENAME="
for /f "usebackq delims=" %%a in (`call cd`) do set "DIR=%%a"


:PARSE_ARGS
if "%~1" == "" goto END_PARSE

if /I "%~1" == "-verbose" (
    set "VERBOSE=1"
) else if /I "%~1" == "-v" (
	set "VERBOSE=1"
	
) else if /I "%~1" == "-port" (
    set "PORT=%~2"
    shift
) else if /I "%~1" == "-p" (
	set "PORT=%~2"
    shift

) else if /I "%~1" == "-dir" (
    set "DIR=%~2"
    shift
) else if /I "%~1" == "-d" (
    set "DIR=%~2"
    shift

) else if /I "%~1" == "-file" (
    set "FILENAME=%~2"
    shift
) else if /I "%~1" == "-f" (
	set "FILENAME=%~2"
    shift
)

shift
goto PARSE_ARGS

:END_PARSE

if "%VERBOSE%"=="1" (
	echo Port: %PORT%
    echo File: %FILENAME%
	echo Directory: !DIR!
)

call ipv4_qr -p %PORT% -r "%FILENAME%"
call python -m http.server %PORT% --bind 0.0.0.0 --directory "!DIR!"


endlocal