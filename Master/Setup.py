from tkinter import *
from tkinter import messagebox
import time
import datetime
import os
import Settings

class Setup_Gui():
    def __init__(self,master):
        self.master = master

        self.Pharmacy_Sel = IntVar()
        self.Customer_Sel = IntVar()

        self.Ck_Customer_Sel = Checkbutton(self.master, text = "Select Customer Mode", variable = self.Remote_Sel, onvalue = 1, offvalue = 0, height=1, width = 20,font="Calibri 12 bold", command=self.Cmd_Customer_Mode_Sel)
        self.Ck_Pharmacy_Sel = Checkbutton(self.master, text = "Select Pharmacy Mode", variable = self.Blaster_Sel, onvalue = 1, offvalue = 0, height=1, width = 20,font="Calibri 12 bold", command=self.Cmd_Phamacy_Mode_Sel)

        self.Ck_Pharmacy1_Sel = Checkbutton(self.master, text = "Pharmacy 1", variable = self.ABOV_1703_Sel, onvalue = 1, offvalue = 0, height=1, width = 20,font="Calibri 12 bold", command=self.Cmd_Device_Sel)
        self.Ck_Pharmacy2_Sel = Checkbutton(self.master, text = "Pharmacy 2", variable = self.TELINK_UE671_Sel, onvalue = 1, offvalue = 0, height=1, width = 20,font="Calibri 12 bold", command=self.Cmd_Device_Sel)
        self.Ck_Customer1_Sel = Checkbutton(self.master, text = "Customer 1", variable = self.TELINK_UE571_Sel, onvalue = 1, offvalue = 0, height=1, width = 20,font="Calibri 12 bold", command=self.Cmd_Device_Sel)
        self.Ck_Customer2_Sel = Checkbutton(self.master, text = "Customer 2", variable = self.TELINK_UE572_Sel, onvalue = 1, offvalue = 0, height=1, width = 20,font="Calibri 12 bold", command=self.Cmd_Device_Sel)
        
        self.Label_Mode_Sel = Label(self.master,width=30,font="Calibri 12 bold",text="Set Mode (Pharmacy/Customer)",fg="black",bg="yellow",state='normal')
        self.Label_Item_Sel = Label(self.master,width=30,font="Calibri 12 bold",text="Select the intended Pharmacist/Customer",fg="black",bg="yellow",state='normal')
      

        self.Button_Set_Mode_Item = Button(self.master,width=30,font="Calibri 12 bold",text="Set Pharmacy/Customer value",fg="black",bg="yellow",state='normal',command=self.Cmd_Set_DeviceandMode)
        self.Button_Quit = Button(self.master,relief='raised',width=20,text="Quit",fg="white",bg="red",command=self.CmdQuit)

        self.Label_Device_Sel.grid(row=0,rowspan=5,column=2,padx=0,pady=0,sticky=E+W+N+S)
        self.Ck_Pharmacy1_Sel.grid(row=0,column=1,padx=0,pady=0,sticky=E+W+N+S)
        self.Ck_Pharmacy2_Sel.grid(row=1,column=1,padx=0,pady=0,sticky=E+W+N+S)
        self.Ck_Customer1_Sel.grid(row=2,column=1,padx=0,pady=0,sticky=E+W+N+S)
        self.Ck_Customer2_Sel.grid(row=3,column=1,padx=0,pady=0,sticky=E+W+N+S)

        self.Ck_Customer_Sel.grid(row=0,column=3,padx=0,pady=0,sticky=E+W+N+S)
        self.Ck_Pharmacy_Sel.grid(row=1,column=3,padx=0,pady=0,sticky=E+W+N+S)
        self.Label_Mode_Sel.grid(row=0,rowspan=2,column=4,padx=0,pady=0,sticky=E+W+N+S)

        self.Button_Set_Mode_Item.grid(row=2,rowspan=2,column=3,columnspan=2,padx=0,pady=0,sticky=E+W+N+S)
        self.Button_Quit.grid(row=9,rowspan=2,column=0,columnspan=3,padx=0,pady=0,sticky=E+W+N+S)

    def Cmd_Customer_Mode_Sel(self):
        if (self.Customer_Sel.get() == 1):
            # Set the Remote Mode OFF, Blaster Mode ON
            self.Pharmacy_Sel.set(0)
            self.Label_Mode_Sel.config(text='Customer Mode Selected',fg="black",bg="blue",state='normal')
            Settings.Mode = "Customer"

    def Cmd_Pharmacy_Mode_Sel(self):
        if self.Pharmacy_Sel.get() == 1:
            # Set the Remote Mode ON, Blaster Mode OFF
            self.Customer_Sel.set(0)
            self.Label_Mode_Sel.config(text='Pharmacy Mode Selected',fg="black",bg="blue",state='normal')
            Settings.Mode = "Pharmacy"

    def Cmd_Device_Sel(self):
        if self.Ck_Pharmacy1_Sel.get() == 1:
            # Set the Device to Pharmacy 1; Switch off the rest
            self.Ck_Pharmacy2_Sel.set(0)
            self.Ck_Customer1_Sel.set(0)
            self.Ck_Customer2_Sel.set(0)
            self.Label_Device_Sel.config(text='Item Selected: Pharamacy 1',fg="black",bg="blue",state='normal')
            Settings.old_device = Settings.device
            Settings.device = "Pharmacy 1"
            print("Selected Device: ", Settings.device)
        elif self.Ck_Pharmacy2_Sel.get() == 1:
            # Set the Device to Pharmacy 2; Switch off the rest
            self.Ck_Pharmacy1_Sel.set(0)
            self.Ck_Customer1_Sel.set(0)
            self.Ck_Customer2_Sel.set(0)
            self.Label_Device_Sel.config(text='Item Selected: Pharamacy 2',fg="black",bg="blue",state='normal')
            Settings.old_device = Settings.device
            Settings.device = "Pharmacy 2"
            print("Selected Device: ", Settings.device)
        elif self.Ck_Customer1_Sel.get() == 1:
            # Set the Device to Customer 1; Switch off the rest
            self.Ck_Pharmacy1_Sel.set(0)
            self.Ck_Pharmacy2_Sel.set(0)
            self.Ck_Customer2_Sel.set(0)
            self.Label_Device_Sel.config(text='Item Selected: Customer 1',fg="black",bg="blue",state='normal')
            Settings.old_device = Settings.device
            Settings.device = "Customer 1"
            print("Selected Device: ", Settings.device)
        elif self.Ck_Customer2_Sel.get() == 1:
            # Set the Device to Customer 1; Switch off the rest
            self.Ck_Pharmacy1_Sel.set(0)
            self.Ck_Pharmacy2_Sel.set(0)
            self.Ck_Customer1_Sel.set(0)
            self.Label_Device_Sel.config(text='Item Selected: Customer 2',fg="black",bg="blue",state='normal')
            Settings.old_device = Settings.device
            Settings.device = "Customer 2"
            print("Selected Device: ", Settings.device)

    def Cmd_Set_DeviceandMode(self):
        Settings.Enable_Page2 = 1

    def update(self):
        pass

    def CmdReset(self):
        pass

    def CmdQuit(self):
        exit()


