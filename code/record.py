import pyHook
import pythoncom
import sys

dict={
'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9',
'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 
'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z',
'Oem_3':'`', 'Tab':'tab', 'Capital':'capslock', 'Lshift':'shiftleft', 'Lcontrol':'ctrlleft', 'Oem_Minus':'-', 'Oem_Plus':'=', 'Back':'backspace', 
'Oem_4':'[', 'Oem_6':']', 'Oem_5':'\\', 'Oem_1':';', 'Oem_7':"'", 'Return':'enter', 'Oem_Comma':',', 'Oem_Period':'.',
'Oem_2':'/', 'Rshift':'shiftright', 'Up':'up', 'Down':'down', 'Left':'left', 'Right':'right', 'Prior':'pageup', 'Next':'pagedown', 
'Lmenu':'altleft', 'Rmenu':'altright', 'Rcontrol':'ctrlright', 'Escape':'esc', 'F1':'f1', 'F2':'f2', 'F3':'f3', 'F4':'f4', 'F5':'f5',
'F6':'f6', 'F7':'f7', 'F8':'f8', 'F9':'f9', 'F10':'f10', 'F11':'f11', 'F12':'f12', 'Home':'home', 'End':'end', 'Insert':'insert',
'Delete':'delete' 
}

global mouseLeftDownTime;
mouseLeftDownTime = 0;

global mouseLeftDownPosX;
mouseLeftDownPosX = 0;
global mouseLeftDownPosY;
mouseLeftDownPosY = 0;

def onMouseLeftDown(event):
   global mouseLeftDownTime;
   global mouseLeftDownPosX;
   global mouseLeftDownPosY;
   
   fp=open("cmd.py","a");
   if event.Time - mouseLeftDownTime > 500 and not(mouseLeftDownPosX == event.Position[0] and mouseLeftDownPosY == event.Position[1]):
      cmd = "    pyautogui.moveTo(" + str(event.Position[0]) + "," + str(event.Position[1]) +",duration=0.5,tween=pyautogui.easeInQuad" + ");\n"
      fp.write(cmd);
   mouseLeftDownPosX = event.Position[0];
   mouseLeftDownPosY = event.Position[1];
   mouseLeftDownTime = event.Time;

   cmd="    pyautogui.mouseDown(" + str(event.Position[0]) + "," + str(event.Position[1]) + ",button='left'" + ");\n";
   fp.write(cmd);
   fp.close();
   return True

def onMouseLeftUp(event):
   fp=open("cmd.py","a");
   global mouseLeftDownTime;
   if event.Time - mouseLeftDownTime > 300 and not(mouseLeftDownPosX == event.Position[0] and mouseLeftDownPosY == event.Position[1]):	  
      cmd = "    pyautogui.moveTo(" + str(event.Position[0]) + "," + str(event.Position[1]) +",duration=0.5,tween=pyautogui.easeInQuad" + ");\n"
      fp.write(cmd);

   cmd="    pyautogui.mouseUp(" + str(event.Position[0]) + "," + str(event.Position[1]) + ",button='left'" + ");\n";
   fp.write(cmd);
   fp.close();
   return True   

def onMouseRightDown(event):
   fp=open("cmd.py","a");
   cmd="    pyautogui.mouseDown(" + str(event.Position[0]) + "," + str(event.Position[1]) + ",button='right'" + ");\n";
   fp.write(cmd);
   fp.close();
   return True

def onMouseRightUp(event):
   fp=open("cmd.py","a");
   cmd="    pyautogui.mouseUp(" + str(event.Position[0]) + "," + str(event.Position[1]) + ",button='right'" + ");\n";
   fp.write(cmd);
   fp.close();
   return True

def onKeyDown(event):
   if event.Key == 'Escape':
      fp=open("cmd.py","a");
      fp.write("    os._exit(0);\n");
      fp.write("\n\n\n")
      fp.write("if __name__ == '__main__':\n");
      fp.write("    hookmanager = pyHook.HookManager()\n")
      fp.write("    hookmanager.KeyDown = onKeyDown\n")
      fp.write("    hookmanager.HookKeyboard()\n")
      fp.write("    thread.start_new_thread(invoke,(),{})\n")
      fp.write("    pythoncom.PumpMessages()\n")
      fp.close(); 
      sys.exit();
   fp=open("cmd.py","a");
   if event.Key == 'F2':
      cmd="    time.sleep(1);\n";
      fp.write(cmd);
      fp.close();   
      return True;      
   cmd="    pyautogui.keyDown('" + dict[str(event.Key)] + "');\n";
   fp.write(cmd);
   fp.close();   
   return True

def onKeyUp(event):
   if event.Key == 'F2':
      return True;
   fp=open("cmd.py","a");
   cmd="    pyautogui.keyUp('" + dict[str(event.Key)] + "');\n";
   fp.write(cmd);
   fp.close();   
   return True

if __name__ == '__main__':
    fp=open("cmd.py","a");
    fp.truncate();
    fp.write("import time\n");
    fp.write("import pyautogui\n");
    fp.write("import thread\n")
    fp.write("import pyHook\n")
    fp.write("import pythoncom\n")
    fp.write("import os\n")
    fp.write("import sys\n\n")
    fp.write("def onKeyDown(event):\n")
    fp.write("   if event.Key == 'Escape':\n")
    fp.write("      sys.exit();\n")
    fp.write("   return True\n\n")
    fp.write("def invoke():\n")
    fp.close();
    
    hookmanager = pyHook.HookManager()
    hookmanager.MouseLeftUp = onMouseLeftUp
    hookmanager.MouseLeftDown = onMouseLeftDown
    hookmanager.MouseRightUp = onMouseRightUp
    hookmanager.MouseRightDown = onMouseRightDown
    hookmanager.KeyDown = onKeyDown
    hookmanager.KeyUp = onKeyUp    
    hookmanager.HookMouse()
    hookmanager.HookKeyboard()
    pythoncom.PumpMessages()
