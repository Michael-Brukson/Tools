@echo off
setlocal
setlocal enabledelayedexpansion

rem "secure" parameter- dictates whether http or https should be used. http default.
set "SEC=0"
rem "protocol" parameter- string representation of SEC parameter. Allows waving of headache-y if statements.
set "PROT=http"
rem "port" parameter- what port to send to qrenco.de. 80 default
set "PORT=80"
rem "verbose" parameter- whether to log parameters. default false.
set "VERBOSE=0"
rem "route" parameter- name of additional string at end of route. Defaults to empty.
set "ROUTE="

:PARSE_ARGS
if "%~1" == "" goto END_PARSE

if /I "%~1" == "-sec" (
    set "SEC=1"
	set "PROT=https"
) else if /I "%~1" == "-s" (
	set "SEC=1"
	set "PROT=https"
	
) else if /I "%~1" == "-verbose" (
    set "VERBOSE=1"
) else if /I "%~1" == "-v" (
	set "VERBOSE=1"
	
) else if /I "%~1" == "-port" (
    set "PORT=%~2"
    shift
) else if /I "%~1" == "-p" (
	set "PORT=%~2"
    shift

) else if /I "%~1" == "-route" (
    set "ROUTE=%~2"
    shift
) else if /I "%~1" == "-r" (
	set "ROUTE=%~2"
    shift
)

shift
goto PARSE_ARGS

:END_PARSE


for /f "usebackq delims=" %%a in (`call ipv4`) do set "HOST=%%a"

set "URL=qrenco.de/%PROT%://%HOST%:%PORT%/%ROUTE%"

if %VERBOSE%==1 (
	if %SEC%==1 (echo Secure?: true) else (echo Secure?: false)
	echo Port: %PORT%
	echo Host: !HOST!
	echo Route: %ROUTE%
	echo curling: %URL%
)

curl %URL%

endlocal