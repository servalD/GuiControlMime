import win32gui, win32process, pywintypes
from win32api import EnumDisplayMonitors as edm,GetMonitorInfo
from time import sleep
import psutil
from numpy import array
from PIL import ImageGrab as ig
import logging

def wordMatchRatio(ref, toMatch):
    """ Percentage word matching """
    i=toMatch.lower()
    n=ref.lower()
    matchno=0
    for spt in n.split(" "):
        for right_name in i.split(" "):
            if spt == right_name:
                matchno+=1
    li=[len(n.split(" ")),len(i.split(" "))]
    return matchno/max(li)

def isValideWindow(res, hwnd, winTitle, word_match=0.5, exeName=None):
    title = win32gui.GetWindowText(hwnd)
    ra=wordMatchRatio(winTitle,title)
    exeSucess=0
    if exeName and False:
        try:
            name=psutil.Process(win32process.GetWindowThreadProcessId(hwnd)[-1]).name()
        except psutil._exceptions.NoSuchProcess:
            name=None
        if name==exeName and ra>=word_match:
            exeSucess=1
            res[ra+1]= hwnd
    if ra>=word_match and not exeSucess:
        res[ra]= hwnd 

def childWindowEnumerationHandler(hwnd, inputParams):
    if win32gui.IsWindowEnabled(hwnd): #win32gui.IsWindowVisible(whdl)
        res, winTitle, word_match, exeName=inputParams
        isValideWindow(res, hwnd, winTitle, word_match, exeName)

def windowEnumerationHandler(hwnd, inputParams):
    if win32gui.IsWindowEnabled(hwnd): #win32gui.IsWindowVisible(whdl)
        res, winTitle, word_match, exeName=inputParams
        isValideWindow(res, hwnd, winTitle, word_match, exeName)
        try:
            win32gui.EnumChildWindows(hwnd, childWindowEnumerationHandler, inputParams)
        except pywintypes.error:
            pass

def gethwnds(winTitle, word_match=0.5, exeName=None):
    """ if _in is false the title should be strictly the same as the givent """
    """ Recurcive letter by letter matching percentage (word_match) between existing windows (titles) and the given title"""
    """ exclude all different exe names setting up exeName with or without ".exe" """
    if exeName and not ".exe" in exeName:
        exeName+=".exe"
    res={}
    inputParams = [res, winTitle, word_match, exeName]
    win32gui.EnumWindows(windowEnumerationHandler, inputParams)
    return res[max(res)]
        
            
class window():
    def __init__(self):
        self.last=None
        self.monitor= edm()

    def hdl_filter(self,name_or_whdl="top_win",_in=True, exeName=None):
        #print(name_or_whdl)
        if name_or_whdl=="top_win":
            name_or_whdl,title,exeName=self.get_top()
        if type(name_or_whdl)==str:
            whdl = gethwnds(name_or_whdl,_in, exeName=exeName)
        else:
            whdl = name_or_whdl
        return whdl

    def screenShot(self,bbox=None):
        return array(ig.grab(bbox=bbox))

    def get_top(self):
        whdl = win32gui.GetForegroundWindow()
        try:
            name=psutil.Process(win32process.GetWindowThreadProcessId(whdl)[-1]).name()
            title = win32gui.GetWindowText(whdl)
            whdl = gethwnds(title, exeName=name)
        except psutil._exceptions.NoSuchProcess:
            name=None
            title=""
        print("get_top", whdl,title, name)
        return whdl,title, name

    def set_top(self,name_or_whdl,_in=True, exeName=None):
        whdl=self.hdl_filter(name_or_whdl,_in, exeName)
        win32gui.ShowWindow(whdl,5)
        win32gui.SetForegroundWindow(whdl)

    def get_rect(self,name_or_whdl="top_win",_in=True,exeName=None):
        whdl=self.hdl_filter(name_or_whdl,_in,exeName=exeName)
        return win32gui.GetWindowRect(whdl)

    def rect_corection(self,old_win_rect,name_or_whdl="top_win",_in=True,exeName=None):
        win_rect=self.get_rect(name_or_whdl,_in,exeName=exeName)
        old_win_size=(old_win_rect[2]-old_win_rect[0],old_win_rect[3]-old_win_rect[1])
        new_rect=(win_rect[0],win_rect[1],old_win_size[0],old_win_size[1])
        return new_rect

    def set_rect(self,win_rect,name_or_whdl="top_win",size_only=False, exeName=None,_in=True):
        whdl=self.hdl_filter(name_or_whdl,_in, exeName=exeName)
        if size_only:
            win_rect=self.rect_corection(win_rect,whdl,_in)
        else:
            win_rect=(win_rect[0],win_rect[1],win_rect[2]-win_rect[0],win_rect[3]-win_rect[1])
        x1,y1,x2,y2=win_rect
        try:
            win32gui.MoveWindow(whdl,x1,y1,x2,y2,True)
        except:
            return None
        return [x1,y1,x2,y2]

    def test(self,name_or_whdl,exeName=None):
        try:
            self.get_rect(name_or_whdl,exeName=exeName)
            return True
        except:
            logging.warning("window test failed on "+str(name_or_whdl))
            return False
        
if __name__=="__main__":
    a=window()
