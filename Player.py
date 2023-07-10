import pynput, os
from Position import pos
from Window import window
from time import time,sleep,strftime
from threading import Thread as th
from PIL import Image

import logging

from numpy import arange, array


class player():
    def __init__(self,mouse=None,keyboard=None):
        self.cur_ind=0
        
        self.time=0
        self.cur_df=None
        if mouse==None:
            self.mouse=pynput.mouse.Controller()
        else:
            self.mouse=mouse
        if keyboard==None:
            self.key=pynput.keyboard.Controller()
        else:
            self.key=keyboard
        self.statu="stop"
        self.diff=0
        self.monitor_lock=None
        self.resfor=-1
        self.Type_filter=[]
        self.calling={}
        self.hwnd=None
        self.recttmp=None
        self.scrollf=120
        self.pos=pos()
        self.w=window()
        self.lastpos=None
        self.t0=0
        self.TimeArrayUpdated=1
        self.nextTimeArray=array([0])
        self.TimeArrayStep=0.005
        self.routinTimes=[]
        self.routint0=0
        self.screenshot=False
        self.screenshotPath=os.getcwd()+"\\GCM_playerScreenshots"
        if not os.path.isdir(self.screenshotPath):
            os.mkdir(self.screenshotPath)
        self.imPesistancy=50
    def offset(self,offset=[0,0]):
        self.pos.offset=offset
    def monitor(self,m=None):
        self.pos.m_lock=m
    def pause(self):
        self.statu="pause"
    def screenshotAtClick(self,_bool,path=None):
        self.screenshot=_bool
        if path:
            self.screenshotPath=path
            if self.screenshot and not os.path.isdir(self.screenshotPath):
                os.mkdir(self.screenshotPath)
            
    def getTimeArrayElement(self, TimeArrayStep=None):
        """ To use with a timer loop by step of TimeArrayStep (second) """
        if len(self.routinTimes)<50:
            self.routinTimes.append(time()-self.routint0)
        else:
            self.routinTimes.pop(0)
            self.routinTimes.append(time()-self.routint0)
        self.routint0=time()
        if self.nextTimeArray.shape==():
            return 0
        if len(self.routinTimes)==50:
            self.TimeArrayStep=sum(self.routinTimes)/len(self.routinTimes)
        if TimeArrayStep!=None:
            TimeArrayStep=self.TimeArrayStep
        if self.TimeArrayUpdated>0:
            #while self.TimeArrayUpdated==2:
            #    sleep(0.000001)
            self.TimeArrayIndex=0
            self.TimeArrayUpdated=0
        elif self.nextTimeArray.shape[0]>self.TimeArrayIndex+1:
            self.TimeArrayIndex+=1
        #print(self.nextTimeArray, self.TimeArrayIndex)
        return self.nextTimeArray[self.TimeArrayIndex]
    
    def start(self,df=None,at_time="current"):
        message="Unable to used as relative window: "
        if type(self.cur_df)==type(None) and type(df)==type(None):
            raise Exception("No data in the player!")
        if type(df)!=type(None):
            self.cur_df=df
            self.recttmp=None
        self.pos.set_res(self.cur_df.param["res"])
        size=self.cur_df.shape[0]
        if self.statu=="pause":
            self.statu="start"
            return True
        self.statu="start"
        if at_time=="current":
            if type(df)==type(None):
                at_time=self.cur_df.index[self.cur_ind]
            else:
                at_time=0
        self.t0=0
        if self.recttmp:
            self.pos.setrectrelative(self.w.get_rect(self.recttmp[0]),self.recttmp[1])
        
        while self.cur_ind<size and self.statu!="stop":
            if self.cur_df.index[self.cur_ind]>=at_time:
                self.t0=time()
                self.time=self.cur_df.index[self.cur_ind]
                while (self.time/self.cur_df.tf)-(self.cur_df.index[self.cur_ind-1]/self.cur_df.tf)>time()-self.t0:
                    sleep(0.01)
                if self.statu=='pause':
                    if self.hwnd!=None and __name__!="__main__":
                        try:
                            self.w.set_top("gui control mime")
                        except:
                            logging.warning("no ui to focus on pause")
                            pass
                    tp=time()
                    while self.statu=='pause':
                        sleep(0.2)
                        if self.statu=="stop":
                            return 0
                    self.t0+=time()-tp
                    if self.hwnd!=None:
                        self.w.set_top(self.hwnd)
                if self.cur_df.shape[0]>self.cur_ind+1:
                    self.TimeArrayUpdated=2
                    self.nextTimeArray=arange(self.cur_df.index[self.cur_ind],self.cur_df.index[self.cur_ind+1],self.TimeArrayStep)
                    self.TimeArrayUpdated=1
                else:
                    self.nextTimeArray=array(self.cur_df.index[self.cur_ind])
                if not (self.cur_df["type"][self.time] in self.Type_filter):
                    if "play" in self.calling:
                        self.calling["play"](self.time/1000)
                    if "rep" in self.calling:
                        self.calling["rep"](self.time/1000)
                    if self.cur_df["type"][self.time]=="relto":
                        #print("ok")
                        info=self.cur_df["info"][self.time].split("&")
                        if info[3]=="None":
                            info[3]=None
                        if info[1]=="True":
                            info[1]=1
                        elif info[1]=="False":
                            info[1]=0
                        self.hwnd=info[0]
                        logging.warning(info)
                        if self.w.test(self.hwnd,exeName=info[3]):
                            row = self.cur_df.loc[self.time]
                            rect = [row['x1'], row['y1'], row['x2'], row['y2']]
                            self.pos.setrectrelative(self.w.get_rect(self.hwnd,exeName=info[3]),rect)
                        else:
                            
                            logging.warning(message+self.hwnd+" relto")
                    if self.cur_df["type"][self.time]=="focus" and self.hwnd!=None:
                        info=self.cur_df["info"][self.time].split("&")
                        if info[3]=="None":
                            info[3]=None
                        self.hwnd=info[0]
                        logging.warning(info)
                        if self.w.test(self.hwnd,exeName=info[3]):
                            self.w.set_top(self.hwnd,exeName=info[3])
                        else:
                            logging.warning(message+self.hwnd+" focus")
                    if self.cur_df["type"][self.time]=="screenshot" and self.screenshot:
                        if len(os.listdir(self.screenshotPath))>=self.imPesistancy:
                            os.remove(self.screenshotPath+os.path.sep+os.listdir(self.screenshotPath)[0])
                        Image.fromarray(array(self.w.screenShot())).save(self.screenshotPath+"\\"+strftime("%y_%m_%d-%H-%M-%S")+"_"+str(time()-self.t0)+"sec.png")
                        
                    if self.cur_df["type"][self.time]=="NotRel":
                        self.pos.NotRel()
                    if self.cur_df["type"][self.time]=="resize":
                        logging.info("resize")
                        info=self.cur_df["info"][self.time].split("&")
                        if info[3]=="None":
                            info[3]=None
                        #print(info[3],"exeName on resize")
                        logging.warning(info)
                        self.hwnd=info[0]
                        if self.recttmp:
                            if self.w.test(self.recttmp[0]):
                                self.w.set_rect(self.recttmp[1],self.recttmp[0])
                            else:
                                logging.warning(message+self.hwnd+" resize temp")
                        if self.w.test(self.hwnd,exeName=info[3]):
                            self.recttmp=[self.hwnd,self.w.get_rect(self.hwnd,exeName=info[3])]
                            row = self.cur_df.loc[self.time]
                            rect = [row['x1'], row['y1'], row['x2'], row['y2']]
                            self.w.set_rect(rect,self.hwnd,1,exeName=info[3])
                        else:
                            logging.warning(message+self.hwnd+" resize")
                            
                    if self.cur_df["type"][self.time] in ["move","scroll","click"]:
                        row = self.cur_df.loc[self.time]
                        pos = [row['x1'], row['y1']]
                        self.lastpos=self.pos.pos(pos)
                        #print(self.lastpos,self.cur_df["pos"][self.time])
                        if self.lastpos!=None:
                            self.mouse.position=self.lastpos
                    if self.lastpos:
                        if self.cur_df["type"][self.time]=="scroll":
                            row = self.cur_df.loc[self.time]
                            delta = [ row['x2'], row['y2']]
                            self.mouse.scroll(delta[0]*self.scrollf, delta[1]*self.scrollf)
                        if self.cur_df["type"][self.time]=="click":
                            if self.cur_df["stat"][self.time]==True:
                                self.mouse.press(self.cur_df["button"][self.time])
                            if self.cur_df["stat"][self.time]==False:
                                self.mouse.release(self.cur_df["button"][self.time])
                        if self.cur_df["type"][self.time]=="key":
                            if self.cur_df["stat"][self.time]==True:
                                self.key.press(self.cur_df["button"][self.time])
                            if self.cur_df["stat"][self.time]==False:
                                self.key.release(self.cur_df["button"][self.time])
                    #print("ok",self.cur_df["type"][self.time])
                #print(self.cur_ind,size, self.statu)
                
            self.cur_ind+=1
        
        self.stop()
        self.recttmp=None
    
    def stop(self):
        if self.hwnd!=None:
            if self.recttmp:
                #print(self.recttmp)
                self.w.set_rect(self.recttmp[1],self.recttmp[0])
            try:
                self.w.set_top("gui control mime")
            except:
                logging.warning("no ui to focus on stop")
                pass
        self.statu="stop"
        self.cur_ind=0
        if "play" in self.calling:
            self.calling["play"](0.000)
