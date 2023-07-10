
from PyQt5.QtWidgets import QTableWidgetItem

class IQDataFrameWidget():
    def __init__(self,QTable,columnH=True, RowH=False, flags=None):
        self.flags=flags
        self.ColumnH=columnH
        self.RowH=RowH
        self.QTable=QTable
        self.df=None
        self.lastR=None
        self.lastC=None
        #self.QTable.itemSelectionChanged.connect(lambda:self.checkAddRC())
        self.setCaddCallback(print)
        self.setRaddCallback(print)
        self.setAddRCLabel("Add Track","Add Info")
        #self.QTable.itemSelectionChanged.connect(lambda:self.checkAddRC(False,True))
        self.QTable.itemChanged.connect(lambda:self.checkAddRC(True,False))
        self.QTable.itemClicked.connect(self.clk)
        #self.checkAddRC(row=True, column=False,init=True)
        #self.QTable.itemEntered.connect(lambda:self.checkAddRC(True,False))
        #self.QTable.itemDoubleClicked
        self.rowClickedCallback=None
        self.Rrename_callback=None
        self.RemoveRowCallback=None
        self.lastTrack=None
        self.QTable.show()
        self.prog = 0
        self.progCallBack = None
    def setprogCallBack(self, cb):
        self.progCallBack = cb
    def setProg(self, prog, mode="abs"):
        if mode == "abs":
            self.prog=prog
        elif mode == "add":
            self.prog+=prog
        if self.progCallBack:
            self.progCallBack(int(self.prog))
    def setRowRenameCallback(self,cb):
        self.Rrename_callback=cb
    def setRowClickedCallback(self,cb):
        self.rowClickedCallback=cb
    def setRemoveRowCallback(self,cb):
        self.RemoveRowCallback=cb
    def clk(self,event=None):
        if event==None:
            self.lastR=self.QTable.currentRow()
            self.lastC=self.QTable.currentColumn()
            self.lastT=self.QTable.item(self.lastR,self.lastC).text()
            self.lastTrack=self.QTable.item(self.lastR,0).text()
        else:
            self.lastR=event.row()
            self.lastC=event.column()
            self.lastT=event.text()
            self.lastTrack=self.QTable.item(self.lastR,0).text()
        if self.rowClickedCallback:
            self.rowClickedCallback(self.QTable.item(self.lastR,0).text())
    def setCaddCallback(self,func):
        #print("Qdataframe setCaddCallback ",func)
        self.Cadd_callback=func
    def setRaddCallback(self,func):
        #print("Qdataframe setRaddCallback",func)
        self.Radd_callback=func
    def getDataFrame(self):
        #print("Qdataframe getDataFrame")
        for x,h in enumerate(self.df.columns):
            for y,v in enumerate(self.df.index):
                self.df[h][v]=self.QTable.item(x,y).text()
        return self.df
    def setAddRCLabel(self,Rlab,Clab):
        #print("Qdataframe setAddRCLabel ",Rlab,Clab)
        self.Raddlab=Rlab
        self.Caddlab=Clab
    def rmCurrentRow(self):
        if self.Raddlab and (self.lastTrack==self.Raddlab):
            return False
        print("Qdataframe rmCurrentRow from "+str(self.lastR)+" "+str(self.lastC)+" "+self.lastTrack)
        self.df=self.df[self.df["Track name"]!=self.lastTrack]
        print(self.df)
        self.QTable.removeRow(self.lastR)
        self.QTable.setCurrentCell(self.lastR,self.lastC)
        self.RemoveRowCallback()
        self.clk()
        print("Qdataframe rmCurrentRow to "+str(self.lastR)+" "+str(self.lastC)+" "+self.lastTrack)
        return True
        
    def checkAddRC(self,row=True, column=False,Rheader=None,Cheader=None,init=False):
        """ header = None or True / False """
        if self.flags:
            if self.flags["checkAddRC"]:
                return True
            self.flags["checkAddRC"]=True

        if column and (((self.QTable.columnCount()-1)==self.QTable.currentColumn()) or init):
            txt=self.QTable.item(self.QTable.currentColumn(),0)
            if txt==None:
                txt=""
            else:
                txt=txt.text()
            if txt!=self.Caddlab or init:
                self.Cadd_callback(txt)
                self.QTable.insertColumn(self.QTable.columnCount())
                if Cheader==(None or True):
                    self.QTable.setItem(self.QTable.columnCount(),0,QTableWidgetItem(self.Caddlab))
        if row==True and (((self.QTable.rowCount()-1)==self.QTable.currentRow()) or init):
            txt=self.QTable.item(self.QTable.currentRow(),0)
            if txt==None:
                self.QTable.setRowCount(self.QTable.rowCount()+1)
                #self.QTable.insertRow(self.QTable.rowCount()-1)
                self.QTable.setItem(self.QTable.rowCount()-1,0,QTableWidgetItem(self.Raddlab))
            else:
                txt=txt.text()
                condDF=self.df[self.df["Track name"]==txt].shape[0]==0
                if (txt!=self.Raddlab) and condDF:
                    self.QTable.setRowCount(self.QTable.rowCount()+1)
                    #self.QTable.insertRow(self.QTable.rowCount()-1)
                    self.Radd_callback(txt)
                    self.df.loc[self.df.shape[0]]=""
                    self.df["Track name"][self.df.shape[0]-1]=txt
                    self.QTable.setItem(self.QTable.rowCount()-1,0,QTableWidgetItem(self.Raddlab))
                    self.clk()
                elif not condDF and (self.lastTrack==self.Raddlab):
                    self.QTable.setItem(self.lastR,0,QTableWidgetItem(self.Raddlab))
        elif row:
            txt=self.QTable.item(self.QTable.currentRow(),0)
            if txt!=None:
                txt=txt.text()
                if self.lastTrack and txt!=self.lastTrack:
                    self.df["Track name"][self.lastR]=txt
                    if self.Rrename_callback:
                        self.Rrename_callback(txt)
                    self.clk()
                    
        if self.flags:
            self.flags["checkAddRC"]=False
    def setDataFrame(self,df,update=1):
        self.setProg(0)
        if update:
            dif=self.df!=df
        else:
            dif=df==df
        self.df=df
        if self.ColumnH:
            self.QTable.horizontalHeader().setVisible(1)
        else:
            self.QTable.horizontalHeader().setVisible(0)
        if self.RowH:
        
            self.QTable.verticalHeader().setVisible(1)
        else:
            self.QTable.verticalHeader().setVisible(0)
        self.QTable.setRowCount(df.shape[0])
        self.QTable.setColumnCount(df.shape[1])
        rowHOK=0
        if df.shape[0]>0:
            progStep = 100/(df.shape[0]*df.shape[1])
        else: 
            progStep = 100
        for x,h in enumerate(df.columns):
            if self.ColumnH:
                self.QTable.setHorizontalHeaderItem(x,QTableWidgetItem(str(h)))
            for y,v in enumerate(df.index):
                if self.RowH and not rowHOK:
                    self.QTable.setVerticalHeaderItem(y,QTableWidgetItem(str(v)))
                if (type(dif[h][v])==bool or type(dif[h][v])==int) and dif[h][v]==1:
                    self.QTable.setItem(y,x,QTableWidgetItem(str(df[h][v])))
                elif type(dif[h][v])!=bool and type(dif[h][v])!=int:
                    self.QTable.setItem(y,x,QTableWidgetItem(str(df[h][v])))
                self.setProg(progStep, "add")
            rowHOK=1
        self.setProg(progStep, "add")
        self.df=df
        self.QTable.show()
    