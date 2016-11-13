import winreg
from tkinter import *
import tkinter.messagebox as messagebox
from binascii import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer",0,winreg.KEY_ALL_ACCESS)
        self.type = {'winreg.REG_SZ':winreg.REG_SZ,'winreg.REG_BINARY':winreg.REG_BINARY,'winreg.REG_DWORD':winreg.REG_DWORD}
        self.list = Listbox()
        for k,v in self.type.items():
            self.list.insert(0,k)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text='Add')
        self.label1.grid(row=1,column=0)
        self.label11 = Label(self, text='subkey')
        self.label11.grid(row=0,column=1)
        self.label12 = Label(self, text='name')
        self.label12.grid(row=0,column=2)
        self.label13 = Label(self, text='data')
        self.label13.grid(row=0,column=3)

        self.subkey = Entry(self)
        self.subkey.grid(row=1,column=1)
        self.vname = Entry(self)
        self.vname.grid(row=1,column=2)
        self.data = Entry(self)
        self.data.grid(row=1,column=3)

        self.list.grid(row=0,column=5)

        self.addKeyButton = Button(self,text="add key",command=self.add)
        self.addKeyButton.grid(row=1,column=4)

#-=-=-=-=-=-=-===========================-----------------------------====-=-=-=-=-=-=-=-=-=

        self.label2 = Label(self, text='Query')
        self.label2.grid(row=2,column=0)
        self.value_name = Entry(self)
        self.value_name.grid(row=2,column=2)
        self.queryButton = Button(self, text='find value', command=self.query)
        self.queryButton.grid(row=2,column=4)

#-=-=-=-=-=-=-===========================-----------------------------====-=-=-=-=-=-=-=-=-=

        self.label3 = Label(self, text='Set')
        self.label3.grid(row=3,column=0)
        self.vname2 = Entry(self)
        self.vname2.grid(row=3,column=2)
        self.data3 = Entry(self)
        self.data3.grid(row=3,column=3)
        self.setValueButton = Button(self,text="set value",command=self.set)
        self.setValueButton.grid(row=3,column=4)

#----------------------------------------------------------------------
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=4,column=2)

    def add(self):
        winreg.CreateKeyEx(self.key, self.subkey.get(), 0, winreg.KEY_ALL_ACCESS)
        k = self.list.get(self.list.curselection())
        if k == 'winreg.REG_DWORD':
            data = int(self.data.get())
        elif k == 'winreg.REG_SZ':
            data = self.data.get()
        else:
            data = a2b_hex(self.data.get())
        tp = self.type[k]
        print(k)
        winreg.SetValueEx(self.key,self.vname.get(),0,tp,data)


    def query(self):
        res = winreg.QueryValueEx(self.key,self.value_name.get())
        messagebox.showinfo('Message','The query returns: %s %s ' %(res[0],res[1]))

    def set(self):
        k = self.list.get(self.list.curselection())
        if k == 'winreg.REG_DWORD':
            data = int(self.data3.get())
        elif k == 'winreg.REG_SZ':
            data = self.data3.get()
        else:
            data = a2b_hex(self.data3.get())
        tp = self.type[k]
        winreg.SetValueEx(self.key,self.vname2.get(),0,tp,data)




if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Register Operation')
    # 主消息循环:
    app.mainloop()
