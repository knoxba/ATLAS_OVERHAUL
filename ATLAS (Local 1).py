#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:12:40 2019
https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/
@author: bradlyallenknox
"""
#CODE
import pyautogui, sys, time, keyboard, os, xlrd, cv2, xlwt
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from xlwt import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from gtts import gTTS
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
pyautogui.FAILSAFE = True
atlas_Speech = ""
total_Logins = 0
LOGINS = list()
VEHICLE1=""
VEHICLE2=""
SPACE=""
cardX=50
cardY=95
cardZ=.5
searchX=52
searchY=604
searchZ=.5
modifyX=217
modifyY=606
modifyZ=.5
credX=132
credY=176
credZ=.5
fieldX=60
fieldY=310
fieldZ=.5
dual_fieldX=406
dual_fieldY=270    
dual_fieldZ=.5
counter = 0
i = 1
cumulative_program_start = time.time()
now = time.time()
filepath="H:\ATLAS\System\Performance Statistics.xls"
wb=Workbook()
sheet = wb.add_sheet('Performance Statistics', cell_overwrite_ok=True)
sheet.write(0, 0, "ROW")
sheet.write(0, 1, "CREDENTIALS")
sheet.write(0, 2, "CUMUL. DURATION (SEC)")
sheet.write(0, 3, "DURATION PER ENTRY (SEC)")
sheet.write(0, 4, "CUMUL. DURATION (MIN)")
sheet.write(0, 5, "DURATION PER ENTRY (MIN)")
class Window(Frame):

    def __init__(self, master, initialdir='', filetypes=()):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()
  
    # CREATING INIT_WINDOW
    def init_window(self):
        
        #CHANGES WINDOW TITLE
        self.master.title("ATLAS")
        
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH,expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        
        # ATLAS FILE MENU: FILE > EXIT
        file.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        
        
        # ATLAS CALIBRATION MENU: CALIBRATION > BULK IMPORT, CREDENTIAL TYPE, SET TAG, INPUT FIELDS, LATENCY, DUAL TAGGING MODE       
        calibration = Menu(menu)
        calibration.add_command(label='Bulk Import...',command=self.bulk_Import)
        calibration.add_command(label='Set Credential Inputs...',command=self.credential_Input_Parameters)
        calibration.add_command(label='Set Labeling Field...',command=self.label_Input_Parameters)
        calibration.add_command(label='Define Label...',command=self.label_Parameters)
        calibration.add_command(label='Set Tagging Mode...',command=self.dual_Tagging)
        calibration.add_command(label='Get Status',command=self.get_Status)
        menu.add_cascade(label='Calibration', menu=calibration)
        
        system = Menu(menu)
        system.add_command(label='Set Latency...',command=self.time_Parameters)
        system.add_command(label='Results',command=self.results)
        system.add_command(label='Reset',command=self.system_Reset)
        menu.add_cascade(label='System', menu=system)
   
    def _create_widgets(self):
        global image
        #self._entry = tk.Entry(self, textvariable=self.filepath)
        self._button = tk.Button(self, image=image, command=self.atlas)
   
    def _display_widgets(self):
        #self._entry.pack(fill='x', expand=True)
        self._button.pack()
    
    def browse(self):
        """ Browses a .csv file or all files and then puts it on the entry.
        """
        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir, filetypes=self._filetypes))
    
    def showImg(self):
        os.chdir('H:\\ATLAS\\Protocols')
        load = Image.open('atlas.png')
        render = ImageTk.PhotoImage(load)
        
        img = Label(self, image=render)
        img.image = render
        img.place(x=30,y=55)
    '''   
    def showTxt(self):
        text = Label(self, text="Hello world!")
        text.pack()
        '''
    def client_exit(self):
        root.destroy()

    # ATLAS PARAMETERS PASSED INTO TKINTER. IN ORDER OF CALIBRATION MENU:
            #---------------------------------------------------------------------
    # STEP 1: BULK IMPORT READS EXCEL FILE IN A STATIC DIRECTORY...
    # PROGRAM PROMPTS FOR USER INPUT, DEPENDING ON INPUT, IT WILL ASSIGN VAR: 'LOGINS' AS LOGINS...
    # BADGE NUMBERS, OR EMPLOYEE ID NUMBERS.
        
    def bulk_Import(self):
        global LOGINS
        global total_Logins
        user_Input = input("Which information do you want to import? Enter: 'LOGINS' , 'BADGES', or 'EMPLOYEES'...: ")
        if user_Input == "LOGINS" or user_Input == "logins":
            LOGINS = list()
            total_Logins = 0
            os.chdir('H:\ATLAS\Protocols')
            file = ("atlas_Main_import.xlsx")
            #file = ("atlas_Local1_import.xlsx")
            #file = ("atlas_Local2_import.xlsx")
            wb = xlrd.open_workbook(file)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            for i in range(sheet.nrows):
                LOGINS.append(sheet.cell_value(i, 0))
            spec = ['='+LOGINS for LOGINS in LOGINS]
            LOGINS = spec
            total_Logins = len(LOGINS)
            print(user_Input + ' have been imported.')
        elif user_Input == "BADGES" or user_Input == "badges":
            LOGINS = list()
            total_Logins = 0
            os.chdir('H:\ATLAS\Protocols')
            file = ("atlas_Main_import.xlsx")
            #file = ("atlas_Local1_import.xlsx")
            #file = ("atlas_Local2_import.xlsx")
            wb = xlrd.open_workbook(file)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 1)
            for i in range(sheet.nrows):
                LOGINS.append(sheet.cell_value(i, 1))
            spec = [int(LOGINS) for LOGINS in LOGINS]
            LOGINS = spec
            total_Logins = len(LOGINS)
            print(user_Input + ' have been imported.')
        elif user_Input == "EMPLOYEES" or user_Input == "employees":
            LOGINS = list()
            total_Logins = 0
            os.chdir('H:\ATLAS\Protocols')
            file = ("atlas_Main_import.xlsx")
            #file = ("atlas_Local1_import.xlsx")
            #file = ("atlas_Local2_import.xlsx")
            wb = xlrd.open_workbook(file)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 2)
            for i in range(sheet.nrows):
                LOGINS.append(sheet.cell_value(i, 2))
            spec = [int(LOGINS) for LOGINS in LOGINS]
            LOGINS = spec
            total_Logins = len(LOGINS)
            print(user_Input + ' have been imported.')
        else:
            None
                
    # STEP 2: CREDENTIAL PARAMETERS INITIALIZES THE GLOBAL VARIABLES ASSIGNED TO CREDENTIAL SEARCHES.
    # USER IS PROMPTED TO ENTER 'LOGINS', 'BADGES' or 'EMPLOYEES' AND DEPENDING ON INPUT, THE PROGRAM WILL...
    # SET THE APPROPRIATE COORDINATES TO SEARCH THAT CREDENTIAL.
                
    def credential_Input_Parameters(self):
        global credX
        global credY
        print('')
        print('.....CREDENTIAL INPUT.....')
        user_Input = input("Enter the credential field you want to use. Enter 'LOGINS', 'BADGES', or 'EMPLOYEES': ")
        if user_Input == "LOGINS" or user_Input == "logins":
            credX = 132
            credY = 176
            print(user_Input + ' are set for entry')
            print('')
        elif user_Input == "BADGES" or user_Input == "badges":
            credX = 815
            credY = 402
            print(user_Input + ' are set for entry')
            print('')
        elif user_Input == "EMPLOYEES" or user_Input == "employees":
            credX = 50
            credY = 175
            print(user_Input + ' are set for entry')
            print('')
        else:
            while user_Input != "VEHICLE1" or user_Input != "VEHICLE2" or user_Input != "SPACE":
                user_Input = input("Enter the tagging field you want to use. Enter 'VEHICLE1', 'VEHICLE2', or 'SPACE': ")
                if user_Input == "LOGINS" or user_Input == "logins":
                    credX = 132
                    credY = 176
                    print(user_Input + ' are set for entry')
                    print('')
                    break
                elif user_Input == "BADGES" or user_Input == "badges":
                    credX = 815
                    credY = 402
                    print(user_Input + ' are set for entry')
                    print('')
                    break
                elif user_Input == "EMPLOYEES" or user_Input == "employees":
                    credX = 50
                    credY = 175
                    print(user_Input + ' are set for entry')
                    print('')
                    break
                else:
                    continue
         
    # STEP 3: THE LABEL INPUT PARAMTERS IMPORTS GLOBAL VARIABLES 'FIELDX' AND 'FIELDY' THEN PROMPTS...
    # USER FOR INPUT. DEPENDING ON INPUT, THE PROGRAM WILL EXECUTE AUTOMATION TO THE SPECIFIC TAGGING FIELD.
    
    def label_Input_Parameters(self):
        global fieldX
        global fieldY
        print('.....SET LABELING FIELD.....')
        user_Input = input("Enter the tagging field you want to use. Enter 'VEHICLE1', 'VEHICLE2', or 'SPACE': ")
        if user_Input == "VEHICLE1" or user_Input == "vehicle1":
            fieldX = 60
            fieldY = 310
            print(user_Input + ' is set for entry')
            print('')
        elif user_Input == "VEHICLE2" or user_Input == "vehicle2":
            fieldX = 300
            fieldY = 310
            print(user_Input + ' is set for entry')
            print('')
        elif user_Input == "SPACE" or user_Input == "space":
            fieldX = 406
            fieldY = 270
            print(user_Input + ' is set for entry')
            print('')
        else:
            while user_Input != "VEHICLE1" or user_Input != "vehicle1" or user_Input != "VEHICLE2"  or user_Input != "vehicle2" or user_Input != "SPACE"  or user_Input != "space":
                user_Input = input("Enter the tagging field you want to use. Enter 'VEHICLE1', 'VEHICLE2', or 'SPACE': ")
                if user_Input == "VEHICLE1" or user_Input == "vehicle1":
                    fieldX = 60
                    fieldY = 310
                    print(user_Input + ' is set for entry')
                    print('')
                    break
                elif user_Input == "VEHICLE2" or user_Input == "vehicle2":
                    fieldX = 300
                    fieldY = 310
                    print(user_Input + ' is set for entry')
                    print('')
                    break
                elif user_Input == "SPACE" or user_Input == "space":
                    fieldX = 406
                    fieldY = 270
                    print(user_Input + ' is set for entry')
                    print('')
                    break
                else:
                    continue        
            
    # STEP 4: THE LABEL PARAMETERS WILL PROMPT USER INPUT FOR EITHER 'VEHICLE1', 'VEHICLE2'. OR 'SPACE'.
    # DEPNDING ON INPUT, THE USER WILL ALSO BE PROMPTED FOR THE TAG. ONCE THE TAG IS ENTERED...
    # THE TAG WILL BE ASSIGNED TO THE CHOSEN INPUT FIELDS (VEHICLE1, VEHICLE2, OR SPACE).
                    
    def label_Parameters(self): 
            global VEHICLE1
            global VEHICLE2
            global SPACE
            print('.....DEFINE LABEL.....')
            user_Input = input("Enter the tagging field you will be using. Enter 'VEHICLE1', 'VEHICLE2', or 'SPACE': ")
            if user_Input == "VEHICLE1" or user_Input == "vehicle1":
                user_Input = input("Enter the label you want to use: ")
                VEHICLE1 = user_Input
                print('The label for VEHICLE 1 is: ' + user_Input)
                print('')
            elif user_Input == "VEHICLE2" or user_Input == "vehicle2":
                user_Input = input("Enter the label you want to use: ")
                VEHICLE2 = user_Input
                print('The label for VEHICLE 2 is: ' + user_Input)
                print('')
            elif user_Input == "SPACE" or user_Input == "space":
                user_Input = input("Enter the label you want to use: ")
                SPACE == user_Input
                print('The label for SPACE is: ' + user_Input)
                print('')
            else:
                while user_Input != "VEHICLE1" or user_Input != "VEHICLE2" or user_Input != "SPACE":
                    user_Input = input("Enter the tagging field you want to use. Enter 'VEHICLE1', 'VEHICLE2', or 'SPACE': ")
                    if user_Input == "VEHICLE1" or user_Input == "vehicle1":
                        user_Input = input("Enter the label you want to use: ")
                        VEHICLE1 = user_Input
                        print('The label for VEHICLE 1 is: ' + user_Input)
                        print('')
                        break
                    elif user_Input == "VEHICLE2" or user_Input == "vehicle2":
                        user_Input = input("Enter the label you want to use: ")
                        VEHICLE2 = user_Input
                        print('The label for VEHICLE 2 is: ' + user_Input)
                        print('')
                        break
                    elif user_Input == "SPACE" or user_Input == "space":
                        user_Input = input("Enter the label you want to use: ")
                        SPACE = user_Input
                        print('The label for SPACE is: ' + user_Input)
                        print('')
                        break
                    else:
                        continue

   
                
    # STEP 5: THE TIME PARAMETERS PASS ALL GLOBAL TIMING VARIABLES AND THEN PROMPT...
    # FOR USER INPUT. USER INPUT IS RESTRICTED BETWEEN 1 AND 6, OTHER VALUES ARE REJECTED.
    # GLOBAL TIMING VARIABLES ARE REASSIGNED NEW VALUES.
                    
    def time_Parameters(self):
        global cardZ
        global searchZ
        global modifyZ
        global credZ
        global fieldZ
        user_Input = input('Enter password: ')
        if user_Input == "atlas_admin":
            while True:
                try:
                    print('.....SET LATENCY.....')
                    user_Input = int(input("Enter a value for program latency: "))
                    if 1 <= user_Input <= 6:
                        cardZ = user_Input
                        searchZ = user_Input
                        modifyZ = user_Input
                        credZ = user_Input
                        fieldZ = user_Input
                        print('You have entered: ' + user_Input + ' seconds')
                        print('')
                    elif user_Input < 1:
                        user_Input = print("You have entered a value that is not a number or is beyond the allowed scope. Please try again.")
                        while user_Input < 1:
                            user_Input = int(input("Enter a value for program latency: "))
                            if 1 <= user_Input <= 6:
                                cardZ = user_Input
                                searchZ = user_Input
                                modifyZ = user_Input
                                credZ = user_Input
                                fieldZ = user_Input
                                print('You have entered: ' + user_Input + ' seconds')
                                print('')
                                break
                            else:
                                continue    
                    elif user_Input > 6:
                        user_Input = print("You have entered a value that is not a number or is beyond the allowed scope. Please try again.")
                        while user_Input > 6:
                            user_Input = int(input("Enter a value for program latency: "))
                            if 1 <= user_Input <= 6:
                                cardZ = user_Input
                                searchZ = user_Input
                                modifyZ = user_Input
                                credZ = user_Input
                                fieldZ = user_Input
                                print('You have entered: ' + user_Input + ' seconds')
                                print('')
                                break
                            else:
                                continue     
                except ValueError:
                    user_Input = print("You have entered a value that is not a number or is beyond the allowed scope. Please try again.")
                    continue
                except TypeError:
                    user_Input = print("You have entered a value that is not a number or is beyond the allowed scope. Please try again.")
                    continue
                else:
                    break
        else:
            None
    # STEP 6: THE DUAL TAGGING PASSES IN GLOBAL SPACE VARIABLE AND CONDUCTS A CONDITION TEST...
    # TO DETERMINE WHETHER USER WANTS TO ACTIVATE DUAL TAGGING MODE. IF USER CHOOSES, 'y',...
    # THE USER IS PROMPTED TO ENTER A LABEL FOR SPACE, AND THEN SPACE IS REASSIGNED THAT NEW INPUT...
    # IF USER DECLINES DUAL TAGGING MODE, GLOBAL SPACE IS REASSIGNED A BLANK VALUE.
                
    def dual_Tagging(self):
        global SPACE
        print('.....SET TAGGING MODE.....')
        prompt = input("Do you want to calibrate ATLAS for dual tagging? Enter 'Y' for yes or 'N' for no: ")
        if prompt == "y" or prompt == "Y":
            prompt = input("Enter the tag you wish to set to be typed into SPACE: ")
            SPACE = prompt
            print("Okay. The second tag is set as: " + SPACE)
        elif prompt == "n" or prompt == "n":
            print("Ok. Program set to continue in single tagging mode.")
            SPACE=""
            
    def get_Status(self):
        global VEHICLE1
        global VEHICLE2
        global SPACE
        global total_Logins
        global credX
        global fieldX
        global credZ
        global fieldZ
        print("---------------------------------------------------------------------")
        print("---------------------------STATUS REPORT-----------------------------")
        print("---------------------------------------------------------------------")
        print("The current import shows a total of " + str(total_Logins) + " logins.")
        if credX == 132:
            print("The program is set to use LOGINS")
        elif credX == 815:
            print("The program is set to use BADGE NUMBERS")
        elif credX == 50:
            print("The program is set to use EMPLOYEE NUMBERS")
        else:
            print("There are no credential inputs currently calibrated")
        if fieldX == 60:
            print("The program is set to use VEHICLE 1")
        elif fieldX == 300:
            print("The program is set to use VEHICLE 2")
        elif fieldX == 406:
            print("The program is set to use SPACE")
        else:
            print("There are no field inputs currently calibrated")
        print("The program latency is set to " + str(credZ) + " seconds")
        if VEHICLE1 != "" and SPACE != "":
            print("The current tag for VEHICLE1 is: " + VEHICLE1)
            print("The current tag for SPACE is: " + SPACE)
        elif VEHICLE2 != "" and SPACE != "":
            print("The current tag for VEHICLE2 is: " + VEHICLE2)
            print("The current tag for SPACE is: " + SPACE)
        elif VEHICLE1 != "":
            print("The current tag is: " + VEHICLE1)
        elif VEHICLE2 != "":
            print("The current tag is: " + VEHICLE2)
        elif SPACE != "":
            print("The current tag is: " + SPACE)
        else:
            print("There are no defined labels")
    
    def system_Reset(self):
        global atlas_Speech
        global total_Logins
        global LOGINS
        global VEHICLE1
        global VEHICLE2
        global SPACE
        global cardX
        global cardY
        global cardZ
        global searchX
        global searchY
        global searchZ
        global modifyX
        global modifyY
        global modifyZ
        global credX
        global credY
        global credZ
        global fieldX
        global fieldY
        global fieldZ
        global dual_fieldX
        global dual_fieldY 
        global dual_fieldZ
        global counter
        atlas_Speech = ""
        total_Logins = 0
        LOGINS = list()
        VEHICLE1=""
        VEHICLE2=""
        SPACE=""
        cardX=50
        cardY=95
        cardZ=.5
        searchX=52
        searchY=604
        searchZ=.5
        modifyX=217
        modifyY=606
        modifyZ=.5
        credX=132
        credY=176
        credZ=.5
        fieldX=60
        fieldY=310
        fieldZ=.5
        dual_fieldX=406
        dual_fieldY=270    
        dual_fieldZ=.5
        counter = 0
        print('System is now reset')
               
    def results(self):
        global total_Logins
        file_location = "H:\ATLAS\System\Performance Statistics.xls"
        workbook = xlrd.open_workbook(file_location)
        atlas_Data = workbook.sheet_by_index(0)
        row = [atlas_Data.cell_value(i, 0) for i in range(atlas_Data.nrows)]
        time = [atlas_Data.cell_value(i, 3) for i in range(atlas_Data.nrows)]
        
        #plt.errorbar(credentials,time,fmt='r^')
        
        plt.axis()
        plt.plot(row, time, marker='x', markerfacecolor='red', markersize=6, color='skyblue', linewidth=2)
        plt.show()
    
    def atlas(self):
        global LOGINS
        global cardX
        global cardY
        global cardZ
        global searchX
        global searchY
        global searchZ
        global credX
        global credY
        global credZ
        global modifyX
        global modifyY
        global modifyZ
        global fieldX
        global fieldY
        global fieldZ
        global dual_fieldX
        global dual_fieldY
        global dual_fieldZ
        global VEHICLE1
        global VEHICLE2
        global SPACE
        global counter
        global total_Logins
        global i
        global program_starts
        global now
        global filepath
        global wb
        global sheet
        while counter <= total_Logins-1:
           if counter == 0:
               cumulative_program_start = time.time()
               program_start = time.time()
               pyautogui.moveTo(cardX,cardY,cardZ)
               pyautogui.click()
               pyautogui.moveTo(searchX,searchY,searchZ)
               pyautogui.click()
               pyautogui.moveTo(credX,credY,credZ)     
               pyautogui.click()
               keyboard.write(str(LOGINS[counter]))
               keyboard.press('enter')
               time.sleep(2)
           else: #IF COUNTER IS NOT ZERO, START FROM HERE
               os.chdir('H:\ATLAS\Protocols')
               latency = pyautogui.locateCenterOnScreen('latency.png', confidence=.9)
               while latency is None:
                   time.sleep(.5)
                   latency = pyautogui.locateCenterOnScreen('latency.png', confidence=.9)
               pyautogui.moveTo(searchX,searchY,searchZ)
               pyautogui.click()
               pyautogui.moveTo(credX,credY,credZ)
               pyautogui.click()
               keyboard.write(str(LOGINS[counter]))
               keyboard.press('enter')
               time.sleep(2)
           os.chdir('H:\ATLAS\Protocols')
           check_Profile=pyautogui.locateCenterOnScreen('check_Profile.png', confidence=.9)
           if check_Profile is None:
               check_Profile_Counter = 0
               try:
                   while check_Profile_Counter < 6:
                       next_Profile=pyautogui.locateCenterOnScreen('next_Profile.png', confidence=.9)
                       time.sleep(2)
                       pyautogui.moveTo(next_Profile)
                       time.sleep(1)
                       pyautogui.click()
                       time.sleep(1)
                       check_Profile=pyautogui.locateCenterOnScreen('check_Profile.png', confidence=.9)
                       time.sleep(1)
                       if check_Profile is None:
                           check_Profile_Counter = check_Profile_Counter + 1
                           continue
                       else:
                           raise StopIteration
               except StopIteration: pass
           elif check_Profile is not None:
               modify = pyautogui.locateCenterOnScreen('modify.png', confidence=.9)
               while modify is None:
                   time.sleep(.5)
                   modify = pyautogui.locateCenterOnScreen('modify.png', confidence=.9)
               pyautogui.moveTo(modifyX,modifyY,modifyZ)
               pyautogui.click()
               pyautogui.moveTo(fieldX,fieldY,fieldZ)     
               pyautogui.click()
               keyboard.press_and_release('ctrl+a')
               time.sleep(1)
               if VEHICLE1 != "":
                   keyboard.write(VEHICLE1)
               elif VEHICLE2 != "":
                   keyboard.write(VEHICLE2)
               elif SPACE != "":
                   keyboard.write(SPACE)
           if SPACE != "":
               pyautogui.moveTo(dual_fieldX,dual_fieldY,dual_fieldZ)
               pyautogui.click()
               keyboard.press_and_release('ctrl+a')
               time.sleep(1)
               keyboard.write(SPACE)
               keyboard.press('enter')
               now = time.time()
               print(str(LOGINS[counter]))
               print(str(round(now - cumulative_program_starts,2)))
               print(str(round(now - program_start,2)))
               counter = counter + 1
           else:
               keyboard.press('enter')
               now = time.time()
               print(str(LOGINS[counter]))
               print(str(round(now - cumulative_program_start,2)))
               print(str(round(now - program_start,2)))
               sheet.write(i, 0, i)
               sheet.write(i, 1, str(LOGINS[counter]))
               sheet.write(i, 2, round(now - cumulative_program_start,2))
               sheet.write(i, 3, round(now - program_start,2))
               sheet.write(i, 4, round((now - cumulative_program_start)/60,2))
               sheet.write(i, 5, round((now - program_start)/60,2))
               wb.save(filepath)
               program_start = now
               i = i + 1                   
               counter = counter + 1

root = Tk()
image = PhotoImage(file = 'H:/ATLAS/Protocols/atlas.png') # DEFINES IMAGE GLOBALLY AND IS PASSED INTO DEF CREATE_WIDGET()
root.geometry("590x600") # WINDOW SIZE
app = Window(root)
root.mainloop()

































