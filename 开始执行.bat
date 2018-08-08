%1(start /min cmd.exe /c %0 :&exit)
cd code
for /l %%i in (1,1,1) do python cmd.py
