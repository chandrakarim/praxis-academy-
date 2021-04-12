@ECHO OFF
PowerShell.exe -ExecutionPolicy Bypass -Command "& '%~dpn0.ps1'"
PowerShell.exe -Command "& {Start-Process PowerShell.exe -ArgumentList '-ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%~dpn0.ps1'"
PAUSE
@ECHO OFF
PowerShell.exe -NoProfile -ExecutionPolicy Bypass -Command "& '%~dpn0.ps1'"
PAUSE
@ECHO OFF
PowerShell.exe -NoProfile -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""%~dpn0.ps1""' -Verb RunAs}"
PAUSE