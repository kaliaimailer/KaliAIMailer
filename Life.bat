@echo off

REM Check for Python and the version
python --version 2>NUL
if %ERRORLEVEL% EQU 0 (
    echo Python is already installed.
    goto :end
)

echo Python is not installed. Attempting to download and install Python.

REM Set the Python version and installer URL
SET "PYTHON_VERSION=3.10.4"
SET "PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
SET "PYTHON_INSTALLER_PATH=%TEMP%\python_installer.exe"

REM Use PowerShell to download the Python installer
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_INSTALLER_URL%' -OutFile '%PYTHON_INSTALLER_PATH%'"

REM Check if download was successful
if exist "%PYTHON_INSTALLER_PATH%" (
    echo Download successful. Installing Python...
    REM Run the installer. Adjust the options as needed.
    start /wait "" "%PYTHON_INSTALLER_PATH%" /quiet InstallAllUsers=1 PrependPath=1
    echo Python has been installed.
) else (
    echo Failed to download the Python installer. Please check the download URL and try again.
)

REM Clean up the installer
if exist "%PYTHON_INSTALLER_PATH%" del /F "%PYTHON_INSTALLER_PATH%"

:end

Pause


