from copy import deepcopy as dc
from os import getcwd, listdir, mkdir, path as osPath
from os.path import exists, isdir, isfile, sep
from shutil import rmtree
from threading import Thread as th
from time import sleep, time
from PIL import Image
import pandas._libs.tslibs.timedeltas, logging
from numpy import NaN
from pandas import DataFrame, MultiIndex, read_pickle, to_pickle, concat
from win32api import EnumDisplayMonitors as edm


def get_screen_size():
    monitors = edm()
    l = []
    for i in reversed(monitors):
        l.append(i[2])
    return l


def end_path(path):
    if "/" in path:
        for j, i in enumerate(reversed(path)):
            if i == "/":
                return path[-j:]
    return path


class Track(DataFrame):
    def __init__(self, data=None):
        if type(data) == str and isfile(self.path_ext(data, "ogc")):
            print("read pickle", data)
            data = read_pickle(self.path_ext(data, "ogc"))
            self.new_data(data)
            self.name = None
        elif type(data) != str:
            self.new_data(data)
            self.name = None
        else:
            self.new_data(None)
            self.name = self.filter_path(data)
        self.path = None
        self.param = None
        self.stack_interval = [0, 0, 0]
        self.stack_max = 4
        self.stack = {}
        self.index.name = "milis"
        self.read_param()
        self.stack_next(1, 1)
        self.last_window = 0
        self.tf = 1

        # self.tmp()

    def auto_relto(self,_bool):
        if ("autorel" in self.param["tasks"]) and (not _bool):
            self.param["tasks"].pop(self.param["tasks"].index("autorel"))
        elif (not ("autorel" in self.param["tasks"])) and _bool:
            self.param["tasks"].append("autorel")
    
    def screenshotAtRelease(self,_bool):
        if ("screenshot" in self.param["tasks"]) and (not _bool):
            self.param["tasks"].pop(self.param["tasks"].index("screenshot"))
        elif (not ("screenshot" in self.param["tasks"])) and _bool:
            self.param["tasks"].append("screenshot")

    def write_param(self):
        """ Write the param """
        p = DataFrame(columns=["type", "button", "stat", "x1", "y1", "x2", "y2", "data", "info"])
        p.loc["name"] = NaN
        p.at["name", "info"] = self.name
        p.loc["path"] = NaN
        p.at["path", "info"] = self.path
        r = 0
        for task in self.param["tasks"]:
            p.loc[task] = NaN
        for i in self.param["res"]:
            idx = "res_"+str(r)
            p.loc[idx] = NaN
            p.at[idx, "x1"] = i[0]
            p.at[idx, "y1"] = i[1]
            p.at[idx, "x2"] = i[2]
            p.at[idx, "y2"] = i[3]
            r += 1
        return p

    def read_param(self):
        if self.param == None:
            if len(self.index) == 0:
                self.param = {}
                self.param["tasks"]=[]
                self.param["res"] = get_screen_size()
                if self.name == None:
                    self.name = "UnNamed"
                self.path=self.path_ext(self.name,"ogc")
            else:
                i = 0
                while i < len(self.index) and type(self.index[i]) == str:
                    row = self.loc[self.index[i]]
                    if "path" in self.index[i]:
                        self.path = row["info"]
                    if "autorel" in self.index[i]:
                        self.param["tasks"].append(self.index[i])
                    if "screenshot" in self.index[i]:
                        self.param["tasks"].append(self.index[i])
                    if "name" in self.index[i]:
                        self.name = row["info"]
                        self.param = {}
                        self.param["tasks"] = []
                        self.param["res"] = []
                    if "res" in self.index[i]:
                        self.param["res"].append((row['x1'], row['y1'], row['x2'], row['y2']))
                    i += 1
                i = 0
                data = self
                while i < len(data.index) and type(data.index[i]) == str:
                    data = data.drop(data.index[i])
                self.new_data(data)

    def path_ext(self, path=None, ext="ogc"):
        if path == None:
            path = self.name
        if (path.count(sep) == 0 and path.count("/") == 0) or path[0] == sep or path[0] == "/" or not ":" in path:
            if path[0] == sep or path[0] == "/":
                path = path[1:]
            path = getcwd()+sep+path
        if ".ogc" not in path and ".tmp" not in path:
            path += "."+ext

        return path

    def filter_path(self, path):
        name = end_path(path)
        if ".ogc" in name:
            name = name.replace(".ogc", "")
        if ".tmp" in name:
            name = name.replace(".tmp", "")
        return name

    def rename(self, name):
        self.name = self.filter_path(name)

    def stack_next(self, head=False, init=False):
        if init:
            self.stack[self.stack_interval[1]] = self.copy()
        else:
            if head:
                if self.stack_interval[1] < self.stack_max-1:
                    self.stack_interval[1] += 1
                else:
                    self.stack_interval[1] = 0
                self.stack_interval[2] = 0
                if self.stack_interval[0] < self.stack_max-1:
                    self.stack_interval[0] += 1
                self.stack[self.stack_interval[1]] = self.copy()
            else:
                if self.stack_interval[2] > 0:
                    if self.stack_interval[1] < self.stack_max-1:
                        self.stack_interval[1] += 1
                    else:
                        self.stack_interval[1] = 0
                    if self.stack_interval[0] < self.stack_max-1:
                        self.stack_interval[0] += 1
                        self.stack_interval[2] -= 1
                    self.new_data(self.stack[self.stack_interval[1]])

    def new_data(self, data):
        DataFrame.__init__(self, data, columns=[
                           "type", "button", "stat", "x1", "y1", 'x2', 'y2', "data", "info"])
    
    def append_data(self,data, delay=0.0):
        data.index -= data.index.min()
        data.index+=self.index.max()+delay
        self.new_data(concat([self, data]))

    def stack_prev(self):
        if self.stack_interval[2] < self.stack_max-1 and self.stack_interval[0] > 0:
            if self.stack_interval[1] == 0:
                self.stack_interval[1] = self.stack_max-1
            else:
                self.stack_interval[1] -= 1
            self.stack_interval[0] -= 1
            self.stack_interval[2] += 1
            self.new_data(self.stack[self.stack_interval[1]])
    
    def exportImgs(self,path=None,callbackProg=None):
        if path == None:
            path=self.path.replace(osPath.basename(self.path))
        self.imdir=path+"\\"+self.name
        if not osPath.isdir(self.imdir):
            mkdir(self.imdir)
        inds=self[self["type"]=="screenshot"].index
        if callbackProg:
            prog=0
            step=100/len(inds)

        for ind in self[self["type"]=="screenshot"].index:
            im = Image.fromarray(self["data"][ind])
            if getattr(im,"__array_interface__",None):
                im.save(self.imdir+"\\"+str(ind)+"sec.png")
            if callbackProg:
                prog+=step
                callbackProg("exportImgs",prog)

    def save(self, path=None):
        if path != None:
            self.rename(path)
        else:
            if self.path != None:
                path = self.name
            else:
                path = self.path
        self.path = self.path_ext(path, "ogc")
        to_pickle(concat([self.write_param(), self]), self.path)

    def NotRel(self, last_press=True):
        if last_press:
            res = self.loc[self[self["type"] == "click"].index]
            t = res[res["stat"] == True].index
            if len(t) > 0:
                t = t[-1]
            else:
                t = 0.0000001
        elif self.shape[0] > 1:
            t = self.index.max()
        else:
            t = 0.0000001
        t -= 0.0000001
        self.loc[t] = NaN
        self.at[t, "type"] = "NotRel"
        self.new_data(self.sort_index())

    def relto(self, name, rect, last_press=True, ind=0, exeName=None):
        if last_press:
            res = self.loc[self[self["type"] == "click"].index]
            t = res[res["stat"] == True].index
            if len(t) > 0:
                t = t[-1]
            else:
                t = 0.0000003
        elif self.shape[0] > 1:
            t = self.index.max()
        else:
            t = 0.0000003
        t -= 0.0000003
        self.loc[t] = NaN
        self.at[t, "type"] = "resize"
        self.at[t, "info"] = name+"&0&0&"+str(exeName)
        self.at[t, "x1"] = rect[0]
        self.at[t, "y1"] = rect[1]
        self.at[t, "x2"] = rect[2]
        self.at[t, "y2"] = rect[3]
        t += 0.0000001
        self.loc[t] = NaN
        self.at[t, "type"] = "focus"
        self.at[t, "info"] = name+"&0&0&"+str(exeName)
        t += 0.0000001
        self.loc[t] = NaN
        self.at[t, "type"] = "relto"
        self.at[t, "info"] = name+"&0&"+str(ind)+"&"+str(exeName)
        self.at[t, "x1"] = rect[0]
        self.at[t, "y1"] = rect[1]
        self.at[t, "x2"] = rect[2]
        self.at[t, "y2"] = rect[3]
        self.new_data(self.sort_index())

    def update_mintime(self):

        self.index = self.index-self.index.min()

    def time_cut(self, interval, mode="bandepass"):
        if type(interval)!=list:
            interval=[interval]
        if mode=="bandepass":
            data = self.loc[(self.index > float(interval[0])) & (self.index < float(interval[1]))]
        if mode=="bandecut":
            data = self.loc[(self.index < float(interval[0])) & (self.index > float(interval[1]))]
        if mode=="lowpass":
            data = self.loc[self.index < float(interval[0])]
        if mode=="highpass":
            data = self.loc[self.index > float(interval[0])]
        m = data.index.min()
        data.index-= m
        self.new_data(data)
        #self.stack_next(1)

    def del_click(self, index, mode="after"):
        if type(index)!=list:
            index=[index]
        if mode=="after":
            t0=self[self["type"] == "click"].index[index[0]*2]+0.001
            self.time_cut(t0, "lowpass")
        if mode=="before":
            t0=self[self["type"] == "click"].index[index[0]*2]-0.001
            self.time_cut(t0, "highpass")
        if mode=="drop":
            t0=self[self["type"] == "click"].index[index[0]*2]
            t1=self[self["type"] == "click"].index[index[1]*2]
            self.time_cut([t0,t1], "bandecut")
        if mode=="get":
            t0=self[self["type"] == "click"].index[index[0]*2]
            t1=self[self["type"] == "click"].index[index[1]*2]
            self.time_cut([t0,t1], "bandepass")

    def remove_move(self, start=True, end=True, all=False):
        """ Only impact "move" typed row"""
        tmp_mov = self[self["type"] == "move"]
        torm = []
        if not all:
            if end:
                maxi = max([self[self["type"] == "click"].index.max(),
                            self[self["type"] == "key"].index.max()])
                torm.extend(list(tmp_mov[tmp_mov.index > maxi].index))
            if start:
                mini = min([self[self["type"] == "click"].index.min(),
                            self[self["type"] == "key"].index.min()])
                torm.extend(list(tmp_mov[tmp_mov.index < mini].index))
        else:
            torm = list(tmp_mov.index)
        self.new_data(self.drop(index=torm))

##    def remove_solo(self, release_at_start=True, press_at_end=True):
##        """ Remove all click and key types released at the start and/or pressed at the end """
##
##        if release_at_start and self.loc[self[self["type"] == "click"].index[0]]["stat"] == False:
##            self.new_data(
##                self.drop(index=[self[self["type"] == "click"].index[0]]))
##        if press_at_end and self.loc[self[self["type"] == "click"].index[-1]]["stat"] == True:
##            self.new_data(
##                self.drop(index=[self[self["type"] == "click"].index[-1]]))
    def remove_solo(self,release_at_start=True,press_at_end=True):
        """ Remove all click and key types released at the start and/or pressed at the end """
        ### extract the click and key lines
        tmp_clk=self[self["type"]=="click"]
        clk=tmp_clk[tmp_clk["stat"]==False]
        clk_invert=tmp_clk[tmp_clk["stat"]==True]
        del tmp_clk
        tmp_key=self[self["type"]=="key"]
        key=tmp_key[tmp_key["stat"]==False]
        key_invert=tmp_key[tmp_key["stat"]==True]
        del tmp_key
        ### 
        ind_todrop=[]
        if release_at_start:
            clk_first_ocur={}
            key_first_ocur={}

            if clk.shape[0]:
                for c in clk.index:
                    if not c in clk_first_ocur:
                        clk_first_ocur[clk["button"][c]]=c
                for fo in clk_first_ocur:
                    ### si le même bouton n'a pas d'autre ocurance ou que le relachement du click arrive avant la pression ()
                    if (clk_invert["button"]==fo).shape[0]==0 or clk_first_ocur[fo]<clk_invert[clk_invert["button"]==fo].index.min():
                        ind_todrop.append(clk_first_ocur[fo])
            if key.shape[0]:
                for k in key.index:
                    if not k in key_first_ocur:
                        key_first_ocur[key["button"][k]]=k
                for fo in key_first_ocur:
                    ### si le même bouton n'a pas d'autre ocurance ou que le relachement de la touche arrive avant la pression
                    if (key_invert["button"]==fo).shape[0]==0 or key_first_ocur[fo]<key_invert[key_invert["button"]==fo].index.min():
                        ind_todrop.append(key_first_ocur[fo])
        if press_at_end:
            clk_first_ocur={}
            key_first_ocur={}
            if clk.shape[0]:
                for c in clk_invert.index:
                    if not c in clk_first_ocur:
                        clk_first_ocur[clk_invert["button"][c]]=c
                for fo in clk_first_ocur:
                    ### si le même bouton n'a pas d'autre ocurance ou qu'une pression du click arrive a la fin
                    if (clk["button"]==fo).shape[0]==0 or clk_first_ocur[fo]>clk[clk["button"]==fo].index.max():
                        ind_todrop.append(clk_first_ocur[fo])
            if key.shape[0]:
                for k in key_invert.index:
                    if not k in key_first_ocur:
                        key_first_ocur[key_invert["button"][k]]=k
                for fo in key_first_ocur:
                    ### si le même bouton n'a pas d'autre ocurance ou qu'une pression de la touche arrive a la fin
                    if (key["button"]==fo).shape[0]==0 or key_first_ocur[fo]>key[key["button"]==fo].index.max():
                        ind_todrop.append(key_first_ocur[fo])
        self.new_data(self.drop(index=ind_todrop))


    # les limites de temps des res ne sont pas prise en compte
    def spacial_cut(self, Obbox, all_monitors=False):
        """ Obbox = [x1,y1,x2,y2] """
        x1, y1, x2, y2 = Obbox
        if all_monitors == True:
            Obbox = []
            for i in self.param['res']:
                Obbox.append((x1+i[0][0], y1+i[0][1], x2+i[1][0], y2+i[1][1]))
            data = DataFrame(
                columns=["type", "button", "stat", "x1", "y1", "x2", "y2", "data", "info"])
            for i in Obbox:
                x1, y1, x2, y2 = i
                data = data.append(self.loc[(self["x1"] > x1) & (
                    self["x1"] < x2) & (self["y1"] > y1) & (self["y1"] < y2)])
            data = data.sort_index(level=0)
        else:
            data = self.loc[(self["x1"] > x1) & (self["x1"] < x2) & (
                self["y1"] > y1) & (self["y1"] < y2)]
        self.new_data(data)
        self.stack_next(1)

    def tmp_clear(self):
        if self.name != "" and isdir(getcwd()+"/"+self.name):
            rmtree(getcwd()+"/"+self.name)

    def tmp(self, tmp_id=0, get=False, path=None):
        if path == None:
            path = self.name
        if not isdir(getcwd()+"/"+self.name):
            mkdir(getcwd()+"/"+self.name)
        if get and isfile(self.path_ext("/"+self.name+"/"+str(tmp_id), "tmp")):
            data = read_pickle(self.path_ext(
                "/"+self.name+"/"+str(tmp_id), "tmp"))
            self.new_data(data)
            self.stack_next(1)
        else:
            to_pickle(self, self.path_ext(
                "/"+self.name+"/"+str(tmp_id), "tmp"))


if __name__ == "__main__":
    a = Track("Testcylinder_extration_crash")
    print(a)
