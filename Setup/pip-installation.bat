@echo off

REM Check if Python & pip are installed
python --version
IF %ERRORLEVEL% NEQ 0 GOTO installpython
pip --version
IF %ERRORLEVEL% NEQ 0 GOTO installpip

REM Install Python packages
echo Installing required Python packages...
pip install numpy scipy matplotlib pandas tensorflow pytorch keras scikit-learn notebook seaborn opencv-python nltk gensim spacy theano pybrain caffe mxnet cntk

echo Packages have been installed successfully.
GOTO end

:installpython
echo Python is not installed. Please install Python from https://www.python.org/downloads/ and ensure it is added to PATH.
GOTO end

:installpip
echo pip is not installed. Please ensure Python is installed correctly with pip.
GOTO end

:end
echo Installation script has finished.
pause
