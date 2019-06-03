from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
import Settings
import time
import threading
import Settings
import os
from binascii import hexlify

class Soracom_Customer_Gui():
    def __init__(self,master):
        self.master = master

        self.Button_Open_Camera = Button(self.master,width=60,font="Calibri 12 bold",text="Open Camera",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Open_Camera)
        self.Button_Capture Image = Button(self.master,width=60,font="Calibri 12 bold",text="Capture Image",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Capture_Image)
        self.Button_Send_GPS_Info = Button(self.master,width=60,font="Calibri 12 bold",text="Send GPS Data",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Send_GPS_Data)
        self.Button_Send_Medicine_Info = Button(self.master,width=60,font="Calibri 12 bold",text="Send Medicine Data to Cloud",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Send_Medicine_Info)
        self.Button_Exit = Button(self.master,width=60,font="Calibri 12 bold",text="Exit",fg="black",bg="yellow",state='normal',command=self.Cmd_Exit)

        self.Button_Open_Camera.grid(row=0,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Capture.grid(row=1,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Send_GPS_Info.grid(row=2,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Send_Medicine_Info.grid(row=3,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Exit.grid(row=13,column=0,padx=0,pady=0,sticky=E+W+N+S)


    def enable(self, childList):
        for child in childList:
            if isinstance(child, Scrollbar):
                pass
            else:
                child.configure(state='normal')

    def disable(self, childList):
        for child in childList:
            if isinstance(child, Scrollbar):
                pass
            else:
                child.configure(state='disable')

    def Cmd_Thread_Open Camera(self):
        self.u1 = threading.Thread(target=self.Cmd_Open_Camera)
        self.u1.start()

    def Cmd_Open_Camera(self):
        self.Button_Set_Input.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Set_Input.config(relief="raised",text="Camera Opened",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Thread_Capture_Image(self):
        self.u2 = threading.Thread(target=self.Cmd_Capture_Image)
        self.u2.start()

    def Cmd_Capture_Image(self):
        self.Button_Set_Input_PullUp.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Set_Input_PullUp.config(relief="raised",text="Image Captured",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Thread_Send_GPS_Data(self):
        self.u3 = threading.Thread(target=self.Cmd_Send_GPS_Data)
        self.u3.start()

    def Cmd_Send_GPS_Data(self):
        self.Button_Set_Output_PushPull_High.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Set_Output_PushPull_High.config(relief="raised",text="GPS Data Sent",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Thread_Send_Medicine_Info(self):
        self.u4 = threading.Thread(target=self.Cmd_Send_Medicine_Info)
        self.u4.start()

    def Cmd_Send_Medicine_Info(self):
        self.Button_Set_Output_PushPull_Low.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Set_Output_PushPull_Low.config(relief="raised",text="Medicine Info Sent to Cloud",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Exit(self):
        # Setting this flag will call a function in the main app to close this page and reopen the main page
        Settings.Enable_Page2 = -1
