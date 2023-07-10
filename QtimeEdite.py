import logging
class tmanip():
    """Fast Qtedit timing interface"""
    def __init__(self,Qtedit):
        self.Qtedit=Qtedit
        self.uimode=None
        self.curentime=1
        self.isdecrem=0
        self.tmp=0
        self.debug=0
    def rst(self):
        """Reset the timer to the original value previously initalized"""
        self.setfromsec(self.tmp)
        self.isdecrem=0
    def decrem(self):
        """ Decrement of one init time """
        if self.isdecrem==0:
            self.isdecrem=1
            self.tmp=self.gettosec()
            
        else:
            self.setfromsec(self.gettosec()-self.curentime)
        if self.gettosec()<=0:
            self.setfromsec(self.tmp)
            self.isdecrem=0
            return 0
        return 1
    def setfromsec(self,sec,init=False):
        """ Set the timer to sec seconde. Inisialize the timer if init is true."""
        if init:
            self.curentime=sec
        elif self.uimode=='again':
            if self.curentime==0:
                sec=0
            else:
                sec=round(sec/self.curentime)
        if init==False:
            self.Qtedit.setText(self.sectotime(sec))
    def gettosec(self):
        """ Get the current time in second """
        t=self.Qtedit.text()
        if self.uimode=='during':
            if ':' in t:
                i0=t.index(':')+1
                if t.count(':')==2 and t.replace(":","").isdigit():
                    i1=t.index(':',i0)+1
                    if len(t[i1:])>0:
                        s=float(t[i1:])
                    if len(t[i0:i1-1])>0:
                        s+=float(t[i0:i1-1])*60
                else:
                    return self.curentime
            else:
                if t.isdigit():
                    s=int(t)
                    s=s*self.curentime
                else:
                    return self.curentime
        if self.uimode=='again':
            if ':' in t:
                i0=t.index(':')+1
                if ':' in t:
                    i1=t.index(':',i0)+1
                    s=float(t[i1+1:])*self.curentime
                else:
                    i1=i0
                    s=float(t[i1+1:])*self.curentime
            else:
                s=float(t)*self.curentime
        return s
    def switshformat(self,uimode):
        """ Sitsh the format of the time displayed to step (divided by initial time) or to time (HH:mm:ss)."""
        if self.uimode!=None:
            a=self.gettosec()
            self.uimode=uimode
        else:
            self.uimode=uimode
            a=self.gettosec()
        self.setfromsec(a)
    def sectotime(self,sec):
        """ Convert seconde to time format (HH:mm:ss)."""
        s=sec
        if self.uimode=='during':
            h=0
            m=0
            trigg=0
            while s>=60*60:
                h+=1
                s-=60*60
            while s>=60:
                m+=1
                s-=60
            if s<0:
                s=0
            s=str(int(s))
            m=str(m)
            h=str(h)
            return h+':'+m+':'+s
        if self.uimode=='again':
            return str(int(s))
