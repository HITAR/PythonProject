import winreg
from tkinter import *
import tkinter.messagebox as messagebox

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
        self.label1.grid(row=0,column=0)
        self.newkey = Entry(self)
        self.newkey.grid(row=0,column=1)
        self.data = Entry(self)
        self.data.grid(row=0,column=2)

        self.list.grid(row=1,column=1)

        self.addKeyButton = Button(self,text="add key",command=self.add)
        self.addKeyButton.grid(row=0,column=3)

#-=-=-=-=-=-=-===========================-----------------------------====-=-=-=-=-=-=-=-=-=

        self.label2 = Label(self, text='Query')
        self.label2.grid(row=1,column=0)
        self.value_name = Entry(self)
        self.value_name.grid(row=1,column=1)
        self.queryButton = Button(self, text='QueryValue', command=self.query)
        self.queryButton.grid(row=1,column=2)

#-=-=-=-=-=-=-===========================-----------------------------====-=-=-=-=-=-=-=-=-=

        self.label3 = Label(self, text='Set')
        self.label3.grid(row=2,column=0)
        self.subkey = Entry(self)
        self.subkey.grid(row=2,column=1)
        self.data3 = Entry(self)
        self.data3.grid(row=2,column=2)
        self.setValueButton = Button(self,text="set value",command=self.set)
        self.setValueButton.grid(row=2,column=3)

    def add(self):
        subkey = self.newkey.get()
        winreg.CreateKeyEx(self.key, subkey, 0, winreg.KEY_ALL_ACCESS)
        k = self.list.get(self.list.curselection())
        if k == 'winreg.REG_DWORD':
            data = self.data.get()
        elif k == 'winreg.REG_SZ':
            data = self.data.get()
        elif k == 'winreg.REG_BINARY':
            data = bin(self.data.get())
        tp = self.type[k]

        winreg.SetValue(self.key,subkey,tp,data)


    def query(self):
        res = winreg.QueryValueEx(self.key,self.value_name.get())
        messagebox.showinfo('Message','The query returns: %s ' %res[0])

    def set(self):
        tp = self.type[self.list.get(self.list.curselection())]
        dt = self.data3.get()
        winreg.SetValue(self.key,self.subkey.get(),tp,dt)



if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Register Operation')
    # 主消息循环:
    app.mainloop()

    # key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer",0,winreg.KEY_ALL_ACCESS)
    # newKeyName = "123"
    # newKey = winreg.CreateKeyEx(key,newKeyName,0,winreg.KEY_ALL_ACCESS)
    #
    # #给新创建的键添加键值
    # value = input("please input key's value:")
    # value_type = input("please input value's type:")
    # #if value_type == winreg.REG_BINARY
    #
    # winreg.SetValue(key,newKeyName,type,value_type)
    #
    # #winreg.DeleteKeyEx(key, "MyNewKey",winreg.REG_SZ,0)
    # a = winreg.QueryValue(key,newKeyName)
    # print(a)

    #winreg.DeleteValue(key,"123")