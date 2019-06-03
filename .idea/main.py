
# Audio Test Automation
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
import os
import Settings
from Setup import *
from Soracom_Pharmacy import *
from Soracom_Customer import *

blank_space = ' ' # One empty space

start_time = datetime.datetime.now()
print(start_time)

stop_time = None


root = Tk()
root.title(25*blank_space+'Remote Medicine Management')
nb = ttk.Notebook(root)

def unhide_root():
    if OTS_exit_flag == 1:
        root.deiconify()

class MainWindow():

    def __init__(self,master):
        self.master = master
        self.page1 = ttk.Frame(self.master)
        self.master.add(self.page1, text='REMOTE MEDICINE MANAGEMENT')
        Setup_Gui(self.page1)
        self.master.pack(expand=True,fill="both")
        self.run()

    def run(self):

        if Settings.Enable_Page2 == 1:
            self.Open_Page2()
        elif Settings.Enable_Page2 == -1:
            self.Close_Page2()
        else:
            pass

        root.after(100,self.run)

    def Open_Page2(self):
        Settings.Enable_Page2 = 0
        self.master.hide(self.page1)
        if Settings.Mode == "Pharmacy":
            self.pharmacy_page()
        if Settings.Mode == "Customer":
            self.customer_page()

    def pharmacy_page(self):
        self.page2 = ttk.Frame(self.master)
        self.master.add(self.page2, text=Settings.item)
        if Settings.item.find('Pharmacy') != -1:
            Soracom_Pharmacy_Gui(self.page2)
        self.master.pack(expand=True,fill="both")

    def customer_page(self):
        self.page2 = ttk.Frame(self.master)
        self.master.add(self.page2, text=Settings.item)
        if Settings.item.find('Customer') != -1:
            Soracom_Customer_Gui(self.page2)
        self.master.pack(expand=True,fill="both")


    def Close_Page2(self):
        self.master.add(self.page1)
        self.master.hide(self.page2)

    
def main():
    myGuiMain = MainWindow(nb)
    root.mainloop()

if __name__ == '__main__':
    main()
