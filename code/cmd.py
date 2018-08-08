import time
import pyautogui
import thread
import pyHook
import pythoncom
import sys

def onKeyDown(event):
   if event.Key == 'Escape':
      sys.exit();
   return True

def invoke():
    pyautogui.moveTo(144,59,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(144,59,button='left');
    pyautogui.mouseUp(144,59,button='left');
    pyautogui.moveTo(506,51,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(506,51,button='left');
    pyautogui.mouseUp(514,51,button='left');
    pyautogui.mouseDown(826,53,button='left');
    pyautogui.mouseUp(828,53,button='left');
    pyautogui.moveTo(1190,229,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(1190,229,button='left');
    pyautogui.mouseUp(1190,229,button='left');
    pyautogui.mouseDown(1172,460,button='left');
    pyautogui.moveTo(1204,630,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseUp(1204,630,button='left');
    pyautogui.moveTo(1106,160,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(1106,160,button='left');
    pyautogui.moveTo(1239,433,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseUp(1239,433,button='left');
    pyautogui.moveTo(91,209,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(91,209,button='left');
    pyautogui.mouseUp(114,329,button='left');
    pyautogui.moveTo(39,243,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(39,243,button='left');
    pyautogui.moveTo(129,78,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseUp(129,78,button='left');
    pyautogui.moveTo(146,83,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(146,83,button='left');
    pyautogui.mouseUp(146,83,button='left');
    pyautogui.moveTo(113,29,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(113,29,button='left');
    pyautogui.moveTo(40,232,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseUp(40,232,button='left');
    pyautogui.moveTo(100,220,duration=0.5,tween=pyautogui.easeInQuad);
    pyautogui.mouseDown(100,220,button='left');
    pyautogui.mouseUp(100,220,button='left');



if __name__ == '__main__':
    hookmanager = pyHook.HookManager()
    hookmanager.KeyDown = onKeyDown
    hookmanager.HookKeyboard()
    thread.start_new_thread(invoke,(),{})
    pythoncom.PumpMessages()
