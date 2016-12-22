import winreg
from tkinter import *
import tkinter.messagebox as messagebox
from binascii import *
import re

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.keylist = {'HKEY_CLASSES_ROOT':winreg.HKEY_CLASSES_ROOT,
                        'HKEY_CURRENT_USER':winreg.HKEY_CURRENT_USER,
                        'HKEY_LOCAL_MACHINE':winreg.HKEY_LOCAL_MACHINE,
                        'HKEY_USERS':winreg.HKEY_USERS,
                        'HKEY_CURRENT_CONFIG':winreg.HKEY_CURRENT_CONFIG
                        }

        self.type = {'winreg.REG_SZ':winreg.REG_SZ,'winreg.REG_BINARY':winreg.REG_BINARY,'winreg.REG_DWORD':winreg.REG_DWORD}
        self.list = Listbox(height=6)
        for k,v in self.type.items():
            self.list.insert(0,k)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.label1 = Label(self, text='Path')
        self.label1.grid(row=1,column=0)
        self.path = Entry(self,width=40)
        self.path.grid(row=1,column=1)

        # res = self.path.get().split("\\", 1)
        # self.key = self.keylist[res[0]]
        # self.subkey = res[-1]

        self.list.grid(row=0,column=2)

        self.label4 = Label(self, text='Key')
        self.label4.grid(row=2,column=0)
        self.adk = Entry(self,width=40)
        self.adk.grid(row=2,column=1)

        self.label2 = Label(self, text='Name')
        self.label2.grid(row=3,column=0)
        self.name = Entry(self,width=40)
        self.name.grid(row=3,column=1)

        self.label3 = Label(self, text='Value')
        self.label3.grid(row=4,column=0)
        self.data = Entry(self,width=40)
        self.data.grid(row=4,column=1)
#----------------------------------------------------------------------------------
        self.addKeyButton = Button(self,text="Add",command=self.add)
        self.addKeyButton.grid(row=5,column=1,sticky=W,ipadx=15)
        self.queryButton = Button(self, text='Query', command=self.query)
        self.queryButton.grid(row=5,column=1,sticky=E,ipadx=15)
        self.setValueButton = Button(self,text="Set",command=self.set)
        self.setValueButton.grid(row=5,column=1,sticky=N+S,ipadx=15)

#----------------------------------------------------------------------

    def add(self):
        res = self.path.get().split("\\", 1)
        key = self.keylist[res[0]]
        subkey = res[-1]
        rtkey = winreg.OpenKey(key,subkey,0,winreg.KEY_ALL_ACCESS) #打开一个注册表项
        crtk = winreg.CreateKeyEx(rtkey, self.adk.get(), 0, winreg.KEY_ALL_ACCESS) #创建一个新的键

        k = self.list.get(self.list.curselection()) #选择数据类型
        if k == 'winreg.REG_DWORD':
            data = int(self.data.get())
        elif k == 'winreg.REG_SZ':
            data = self.data.get()
        else:
            data = a2b_hex(self.data.get())
        tp = self.type[k]
        print(k)
        winreg.SetValueEx(crtk,self.name.get(),0,tp,data)
        messagebox.showinfo('Message', 'Add %s finished, ' % data)

    def query(self):
        res = self.path.get().split("\\", 1)
        key = self.keylist[res[0]]
        subkey = res[-1]

        rtkey = winreg.OpenKey(key,subkey,0,winreg.KEY_ALL_ACCESS)
        crtk = winreg.CreateKeyEx(rtkey, self.adk.get(), 0, winreg.KEY_ALL_ACCESS) #创建一个新的键
        res = winreg.QueryValueEx(crtk,self.name.get())
        messagebox.showinfo('Message','The query returns: %s ' %res[0])

    def set(self):
        res = self.path.get().split("\\", 1)
        key = self.keylist[res[0]]
        subkey = res[-1]

        rtkey = winreg.OpenKey(key,subkey,0,winreg.KEY_ALL_ACCESS)
        crtk = winreg.CreateKeyEx(rtkey, self.adk.get(), 0, winreg.KEY_ALL_ACCESS) #创建一个新的键
        k = self.list.get(self.list.curselection())
        if k == 'winreg.REG_DWORD':
            data = int(self.data.get())
        elif k == 'winreg.REG_SZ':
            data = self.data.get()
        else:
            data = a2b_hex(self.data.get())
        tp = self.type[k]
        winreg.SetValueEx(crtk,self.name.get(),0,tp,data)
        messagebox.showinfo('Message','Set value successfully')



if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Register Operation')
    # 主消息循环:
    app.mainloop()
