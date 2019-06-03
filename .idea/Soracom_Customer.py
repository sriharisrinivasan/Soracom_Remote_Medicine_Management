from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
import Settings
import time
import threading
import Settings
import os
from binascii import hexlify
from soracom_library import *
from GPS_Data import *

class Soracom_Customer_Gui():
    def __init__(self,master):
        self.master = master
        self.Medicine_Qty = IntVar()

        self.Button_Open_Camera = Button(self.master,width=40,font="Calibri 12 bold",text="Open Camera",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Open_Camera)
        self.Button_Capture_Image = Button(self.master,width=40,font="Calibri 12 bold",text="Capture Image",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Capture_Image)
        self.Button_Send_GPS_Info = Button(self.master,width=40,font="Calibri 12 bold",text="Send GPS Data",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Send_GPS_Data)
        self.Button_Send_Medicine_Info = Button(self.master,width=40,font="Calibri 12 bold",text="Send Medicine Data to Cloud",fg="black",bg="yellow",state='normal',command=self.Cmd_Thread_Send_Medicine_Info)
        self.Button_Exit = Button(self.master,width=40,font="Calibri 12 bold",text="Exit",fg="black",bg="yellow",state='normal',command=self.Cmd_Exit)


        self.Label_Medicine = Label(self.master, width=40, text="Medicine", fg="brown", bg = "Green")
        self.Label_Quantity = Label(self.master, width=40, text="Quantity", fg="brown", bg = "Green")

        self.Listbox_Medicine = Listbox(self.master)
        self.Scrollbar_Medicine = Scrollbar(self.Listbox_Medicine)
        self.Enter_Medicine_Qty = Entry(self.master)

        # Create a list cum scroll bar for storing Instrument information, read on the fly by the script
        self.Scrollbar_Medicine = Scrollbar(self.master)
        self.Listbox_Medicine = Listbox(self.master,yscrollcommand=self.Scrollbar_Medicine.set,width=25,height=2)
        self.Listbox_Medicine.bind("<<ListboxSelect>>", self.Listbox_Medicine_callback)
        self.Scrollbar_Medicine.config(command=self.Listbox_Medicine.yview)
        self.Listbox_Medicine.config(yscrollcommand=self.Scrollbar_Medicine.set)
        self.Scrollbar_Medicine.config(command=self.Listbox_Medicine.yview)

        # Add the list of instruments read into the list box
        for i in Settings.medicine_list:
            self.Listbox_Medicine.insert(END, i)

        self.Button_Open_Camera.grid(row=0,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Capture_Image.grid(row=1,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Send_GPS_Info.grid(row=2,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Send_Medicine_Info.grid(row=3,column=0,padx=0,pady=0,sticky=E+W+N+S)
        self.Label_Medicine.grid(row=2,column=1,pady=5,sticky=E+W+N+S)
        self.Listbox_Medicine.grid(row=3,column=1,pady=5,sticky=N+S+W)
        self.Scrollbar_Medicine.grid(row=3,column=2,pady=5,sticky=N+S+W)
        self.Label_Quantity.grid(row=2,column=3,padx=0,pady=0,sticky=E+W+N+S)
        self.Enter_Medicine_Qty.grid(row=3,column=3,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Exit.grid(row=4,column=0,padx=0,pady=0,sticky=E+W+N+S)


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

    def Cmd_Thread_Open_Camera(self):
        self.u1 = threading.Thread(target=self.Cmd_Open_Camera)
        self.u1.start()

    def Cmd_Open_Camera(self):
        self.Button_Open_Camera.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Open_Camera.config(relief="raised",text="Camera Opened",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Thread_Capture_Image(self):
        self.u2 = threading.Thread(target=self.Cmd_Capture_Image)
        self.u2.start()

    def Cmd_Capture_Image(self):
        self.Button_Capture_Image.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Capture_Image.config(relief="raised",text="Image Captured",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Thread_Send_GPS_Data(self):
        self.u3 = threading.Thread(target=self.Cmd_Send_GPS_Data)
        self.u3.start()

    def Cmd_Send_GPS_Data(self):
        self.Button_Send_GPS_Info.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()

        [nmea_time,nmea_latitude,nmea_longitude] = GPS_Data_Read()
        send_gps_data_to_funnel_s3(nmea_time, nmea_latitude, nmea_longitude)
        
        self.Button_Send_GPS_Info.config(relief="raised",text="GPS Data Sent",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Cmd_Thread_Send_Medicine_Info(self):
        self.u4 = threading.Thread(target=self.Cmd_Send_Medicine_Info)
        self.u4.start()

    def Cmd_Send_Medicine_Info(self):
        self.Button_Send_Medicine_Info.config(relief="sunken",text="Running Test",bg="red",fg="black")
        self.disable(self.master.winfo_children())
        self.master.update_idletasks()
        
        self.Button_Send_Medicine_Info.config(relief="raised",text="Medicine Info Sent to Cloud",bg="green",fg="black")
        self.enable(self.master.winfo_children())
        self.master.update_idletasks()

    def Listbox_Medicine_callback(self,event):
        b = self.Listbox_Medicine.curselection()
        if self.Listbox_Medicine.curselection()!=None:
            if len(b)>0:
                # Assign the Selected Instrument on List to the Oscilloscope Instrument Identifier Variable
                Settings.Medicine = self.Listbox_Medicine.get(self.Listbox_Medicine.curselection()[0])
        else:
            messagebox.showinfo("\t\t\tError!","Select an Instrument first")

    def Cmd_Exit(self):
        # Setting this flag will call a function in the main app to close this page and reopen the main page
        Settings.Enable_Page2 = -1
