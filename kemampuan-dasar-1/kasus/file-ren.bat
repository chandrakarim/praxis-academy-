@ECHO off
cls
:start

set choice=
set /p choice=nama-file.java ada, diganti namanya (y/t)?
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='y' goto y
if '%choice%'=='t' goto t

ECHO "%choice%" is not valid, try again
ECHO.
goto start
:y
ECHO jika y, maka input nama baru kemudian diganti
goto end
:t
ECHO jika t, maka lanjut ke proses berikutnya
goto end
:test
ECHO TEST
goto end
:end
pause