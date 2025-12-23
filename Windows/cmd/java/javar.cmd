@echo off
setlocal
setlocal enabledelayedexpansion

@REM java file to compile and run
set "FILE=%~1"
@REM verbose or not
set "VERBOSE=0"

:PARSE_ARGS
if "%~1" == "" goto END_PARSE

if /I "%~1" == "-verbose" (
    set "VERBOSE=1"
) else if /I "%~1" == "-v" (
	set "VERBOSE=1"	
)

shift
goto PARSE_ARGS

:END_PARSE

if "%VERBOSE%"=="1" (echo compiling %FILE%...)

javac %FILE%

if "%VERBOSE%"=="1" (
    echo running %FILE%...
    echo.
)

java %FILE%

endlocal