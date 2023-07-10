import pynput
from time import time,sleep
from threading import Thread as th
from numpy import NaN
from Window import window
from Position import pos as Position
import logging
from math import ceil


class recorder():
    def __init__(self,mouse=None,keyboard=None):
        self.p=Position()
        self.statu="stop"
        self.Track=None
        if mouse==None:
            self.mouse=pynput.mouse.Controller()
        else:
            self.mouse=mouse
        if keyboard==None:
            self.keyboard=pynput.keyboard.Controller()
        else:
            self.keyboard=keyboard
        self.w=window()
        self.listen=[pynput.mouse.Listener(on_move=self.m_move, on_click=self.m_click, on_scroll=self.m_scroll),
                        pynput.keyboard.Listener(on_press=self.k_press,on_release=self.k_release)]
        self.listen[0].start()
        self.listen[1].start()

    def put_track(self,Track):
        self.Track=Track
        self.t0=time()
    def start(self,df=None):
        if type(df)!=type(None):
            self.put_track(df)
        if self.statu=="stop" and type(self.Track)!=type(None):
            logging.info("recorder statu to run")
            index = self.Track[self.Track["type"] == "click"].index
            self.lastTimeBeforeRec = self.Track[self.Track["type"] == "click"].index.shape[0]
            if "autorel" in self.Track.param["tasks"]:
                self.Track.relto(self.w.get_top()[1],self.w.get_rect())
            if self.Track.shape[0]>1:
                self.t0=time()-self.Track.index.max()
            else:
                self.t0=time()
            self.statu="run"
    def __del__(self):
        self.listen[0].stop()
        self.listen[1].stop()
    def stop(self):
        if self.statu=="run":
            logging.warning("Recorder Stoped")
            self.statu="stop"
            self.Track.remove_solo()
            self.Track.del_click(-1, "after")
            LTBFR = ceil(self.lastTimeBeforeRec/2)
            if self.lastTimeBeforeRec:
                self.Track.del_click([LTBFR, LTBFR+1], "drop")
            else:
                self.Track.del_click(LTBFR, "before")
            self.Track.remove_move()
             
            return True
        return False
            
    def m_click(self,x, y, button, pressed):
        if self.statu=="run":
            logging.info("clicked")
            x,y=self.mouse.position
            t=time()-self.t0
            self.Track.loc[t]=NaN
            self.Track.at[t, "type"]="click"
            self.Track.at[t, "x1"]=x
            self.Track.at[t, 'y1']=y
            self.Track.at[t, "button"]=button
            if pressed:
                self.Track.at[t, "stat"]=True
                if "screenshot" in self.Track.param["tasks"]:
                    self.Track.loc[t+0.0001]=NaN
                    self.Track["type"][t+0.0001]="screenshot"
                    self.Track["data"][t+0.0001]=self.w.screenShot()# To change, array not supported in cells
            else:
                self.Track.at[t, "stat"]=False
                if "screenshot" in self.Track.param["tasks"]:
                    self.Track.loc[t+0.0001]=NaN
                    self.Track.at[t+0.0001, "type"]="screenshot"
                    self.Track.at[t+0.0001, "data"]=self.w.screenShot()
                if "autorel" in self.Track.param["tasks"]:
                    #self.Track.relto(self.w.get_top()[1],self.w.get_rect())
                    n,title,exeName=self.w.get_top()
                    Condition = self.Track[self.Track["type"]=="relto"]
                    #print("condition",Condition)
                    if Condition.shape[0]==1:
                        ind=0
                    elif Condition.shape[0]!=0:
                        ind=Condition.shape[0]-1
                    if title=='':
                        self.Track.NotRel()
                        logging.warning("Access denided to window "+title+" so set relative to screen size")
                    elif (Condition.shape[0]==0) or (not (title in Condition["info"][Condition.index[ind]])):
                        ####  condition pour tester les autorisations
                        print("Condition at release Ok")
                        if self.w.test(n):
                            self.Track.relto(title,self.w.get_rect(n),exeName=exeName)
                            logging.info("relative "+str(t)+": "+title)
                        else:
                            self.Track.NotRel()
                            logging.warning("Access denided to window "+title+" so set relative to screen size")
            
                        
    def m_move(self,x, y):
        if self.statu=="run":
            x,y=self.mouse.position
            t=time()-self.t0
            self.Track.loc[t]=NaN
            self.Track.at[t, "type"]="move"
            self.Track.at[t, "x1"]=x
            self.Track.at[t, "y1"]=y
    def m_scroll(self,x, y, dx, dy):
        if self.statu=="run":
            x,y=self.mouse.position
            t=time()-self.t0
            self.Track.loc[t]=NaN
            self.Track.at[t, "type"]="scroll"
            self.Track.at[t, "x1"]=x
            self.Track.at[t, "y1"]=y
            self.Track.at[t, "x2"]=dx
            self.Track.at[t, "y2"]=dy
    def k_press(self,key):
        if self.statu=="run":
            t=time()-self.t0
            self.Track.loc[t]=NaN
            self.Track.at[t, "type"]="key"
            self.Track.at[t, "button"]=key
            self.Track.at[t, "stat"]=True
    def k_release(self,key):
        if self.statu=="run":
            t=time()-self.t0
            self.Track.loc[t]=NaN
            self.Track.at[t, "type"]="key"
            self.Track.at[t, "button"]=key
            self.Track.at[t, "stat"]=False
if __name__=="__main__":
    from Track import Track
    a=recorder()
    t=Track()
    a.start(t)
