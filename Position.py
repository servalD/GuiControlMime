from win32api import EnumDisplayMonitors as edm
class pos():
    def __init__(self): 
        monitors=edm()
        self.offset=[0,0]
        self.dif=0
        self.monitor=[0,0]#intern (pc),extern (file)
        self.l=[]
        self.m_lock=None
        self.Obbox=None
        self.Mybbox=None
        #self.factor=[1,1]
        #self.history=[]
        for i in reversed(monitors):
            self.l.append(i[2])
    def set_res(self,res):
        self.regres=res
    def NotRel(self):
        self.Obbox=None
        print("not rel")
    def setrectrelative(self,myrect,trackrect=None):
        """ myrect is the current window and trackrect is the window inside of the track """
        #print(myrect,trackrect)
        if trackrect!=None:
            self.Obbox=trackrect
        if self.Obbox==None:
            self.factor=[1,1]
            print("Bbox missing ",self.Obbox)
        self.myrect=myrect
        #self.factor=[(myrect[2]-myrect[0])/(self.Obbox[2]-self.Obbox[0]),
        #             (myrect[3]-myrect[1])/(self.Obbox[3]-self.Obbox[1])]
        #print(self.Obbox,myrect,self.offset,self.factor)
    def set_m(self,monitor):
        self.m_lock=monitor
    def isin_Obbox(self,pos):
        if self.Obbox!=None:
            x1,y1,x2,y2=self.Obbox
            if pos[0]<x1 or x2<pos[0] or pos[1]<y1 or y2<pos[1]:
                return False
            else:
                return True
        else:
            return True
    def pos(self,pos):
        ### find track monitor
        i=0
        while len(self.regres)-1>i and pos[0]>self.regres[i][2]:
            i+=1
        ### find displayed monitor
        if self.m_lock==None:
            if i<=len(self.l)-1:
                n=i
            else:
                n=len(self.l)-1
        else:
            if self.m_lock<=len(self.l)-1:
                n=self.m_lock
            else:
                n=len(self.l)-1
        self.monitor=[n,i]
        ### Obbox
        if self.Obbox!=None:
            Obbox=self.Obbox
            if not self.isin_Obbox(pos):
                return None
            ### normalise
            pos=[pos[0]-self.Obbox[0],pos[1]-self.Obbox[1]]
            Obbox=[self.Obbox[2]-self.Obbox[0],self.Obbox[3]-self.Obbox[1]]
            myrect=[self.myrect[2]-self.myrect[0],self.myrect[3]-self.myrect[1]]
            pos=[((pos[0]/Obbox[0])*myrect[0])+self.myrect[0],
                 ((pos[1]/Obbox[1])*myrect[1])+self.myrect[1]]
                
##                self.offset=[((self.Obbox[0]-self.regres[i][0])/(self.regres[i][2]-self.regres[i][0])),
##                             ((self.Obbox[1]-self.regres[i][1])/(self.regres[i][3]-self.regres[i][1]))]
##                ### recompute
##                self.offset=[self.myrect[1]+(self.l[n][0]+(self.offset[0]*(self.l[n][2]-self.l[n][0]))),
##                             self.myrect[1]+(self.l[n][1]+(self.offset[1]*(self.l[n][3]-self.l[n][1])))]
        else:        
            ### normalise
            pos[0]=(pos[0]-self.regres[i][0])/(self.regres[i][2]-self.regres[i][0])
            pos[1]=(pos[1]-self.regres[i][1])/(self.regres[i][3]-self.regres[i][1])
            ### recompute
            #print(self.offset)
            pos[0]=(self.l[n][0]+(pos[0]*(self.l[n][2]-self.l[n][0])))+self.offset[0]
            pos[1]=(self.l[n][1]+(pos[1]*(self.l[n][3]-self.l[n][1])))+self.offset[1]
        ### Mybbox
        if self.Mybbox!=None:
            #print("ok")
            Mybbox=self.Mybbox
            if Mybbox!=None:
                if Mybbox==True:
                    return None
                else:
                    x1,y1,x2,y2=Mybbox
                    if pos[0]<x1 or x2<pos[0] or pos[1]<y1 or y2<pos[1]:
                        return None
        #self.history.append(pos)
        return int(pos[0]),int(pos[1])
if __name__=="__main__":
    a=pos()
