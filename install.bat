cd package
python-2.7.15.msi
pyHook-1.5.1.win32-py2.7.exe
pywin32-221.win32-py2.7.exe
cd setuptools-40.0.0
python setup.py install
cd ..
cd pip-18.0
python setup.py install
cd ..
setx path "%path%;C:\Python27\;C:\Python27\Scripts" /m
pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple
