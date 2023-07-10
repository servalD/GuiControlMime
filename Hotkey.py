from time import time,sleep
from threading import Thread as th
import pynput

class hotkey():
    def __init__(self):
        self.statu="stop"
        self.listen= pynput.keyboard.Listener(on_press=self.k_press,on_release=self.k_release)
        self.listen.start()
        self.evenkey={}
        self.keys={}
    def set_even(self,callback,key):
        if type(key)!=list:
            key=[key]
        if not "".join(key) in self.evenkey:
            for i in key:
                if not i in self.keys:
                    self.keys[i]=0
            self.evenkey["".join(key)]=[len(key),callback]
    def rm_even(self,key):
        key="".join(key)
        if key in self.evenkey:
            self.evenkey.pop(key)
    def checkout(self):
        for keys in self.evenkey:
            res=0
            for n in self.keys:
                if n in keys and self.keys[n]==1:
                    res+=1
            if res==self.evenkey[keys][0]:
                
                th(target=self.evenkey[keys][1]).start()
    def start(self):
        if self.statu=="stop":
            self.statu="run"
    def __del__(self):
        self.listen.stop()
    def stop(self):
        if self.statu=="run":
            self.statu="stop"
            return True
        return False
        
    def k_press(self,key):
        if self.statu=="run":
            if type(key)!=str:
                key=str(key).replace("Key.","")
                if "_" in key:
                    key=key[:key.index("_")]
                if "'" in key:
                    key=key[1:-1].lower()
            if key in self.keys:
                self.keys[key]=1
                self.checkout()
    def k_release(self,key):
        if self.statu=="run":
            if type(key)!=str:
                key=str(key).replace("Key.","")
                if "_" in key:
                    key=key[:key.index("_")]
                if "'" in key:
                    key=key[1:-1].lower()
            if key in self.keys:
                self.keys[key]=0
                self.checkout()
if __name__=="__main__":
    a=hotkey()
    
