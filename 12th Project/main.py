# -*- coding: utf-8 -*-
"""

@author: Sahil Agarwal
@class: 12B
@why: CS Project
@what: POS System with frontend and backend

"""

#To import modules
from tkinter import * #GUI
import mysql.connector as sql #BACKEND
import tkinter.messagebox #UI
import datetime as dt #UI
import time #UI
import random #INVOICE GENERATION
import os #INVOICE GENERATION

#Connecting to backend MySQL database 'store', and precreated tables 'inventory' and 'invoice'
conn = sql.connect(host = 'localhost', user = 'root', passwd = 'password', database = 'store') #Connector variable
c = conn.cursor() #Cursor variable

#Date for POS (Program 3)
date = dt.datetime.now().date()
datetime = dt.datetime.now() #For INVOICE

#List initialization for POS (Program 3)
products_list = []
amounts_list = []

#Accessing inventory from MySQL database (Program 1 and 2)
def id():
    c.execute('select max(id) from inventory;')
    id = c.fetchone()
    conn.commit()
    return id[0]

#Startup GUI to select which program to start
class Startup:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master) #Using a frame and pack()
        
        #Placing objects in self.frame
        self.button1 = Button(self.frame, text = 'Add To Database', width = 25, command = self.addtodb_window)
        self.button1.pack(pady = 5, padx = 10)
        
        self.button2 = Button(self.frame, text = 'Update Database', width = 25, command = self.update_window)
        self.button2.pack(pady = 5, padx = 10)
        
        self.button3 = Button(self.frame, text = 'Open POS System', width = 25, command = self.main_window)
        self.button3.pack(pady = 5, padx = 10)
        
        self.frame.pack(pady = 5, padx = 10) #Placing fame in GUI

    #For program 1
    def addtodb_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = DatabaseAdd(self.newWindow)

    #For program 2
    def update_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = DatabaseUpdate(self.newWindow)

    #For program 3
    def main_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Application(self.newWindow)

#Program 1 - Add items to backend 'inventory' table in database 'store' with GUI
class DatabaseAdd:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        
        #Using grids without any frame in main window
        self.heading = Label(master, text = 'ADD TO DATABASE (BACK END)', font = ('Segoe UI Light', 24, 'bold'))
        self.heading.grid(column = 0, columnspan = 3, padx = 30, pady = 10)
        
        #Binding enter and escape keys to functions for better UI
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Escape>', self.clear_all)

        #Labels for the window (_l) - placed in master frame
        self.name_l = Label(master, text = 'Enter Product Name', font = 'calibri 14')
        self.name_l.grid(row = 1, sticky = 'W', padx = 5)
        
        self.inventory_l = Label(master, text = 'Enter Inventory', font = 'calibri 14')
        self.inventory_l.grid(row = 2, sticky = 'W', padx = 5)
        
        self.decription_l = Label(master, text = 'Enter Description', font = 'calibri 14')
        self.decription_l.grid(row = 3, sticky = 'W', padx = 5)
        
        self.cost_price_l = Label(master, text = 'Enter Cost Price', font = 'calibri 14')
        self.cost_price_l.grid(row = 4, sticky = 'W', padx = 5)
        
        self.selling_price_l = Label(master, text = 'Enter Selling Price', font = 'calibri 14')
        self.selling_price_l.grid(row = 5, sticky = 'W', padx = 5)
        
        self.supplier_name_l = Label(master, text = 'Enter Supplier Name', font = 'calibri 14')
        self.supplier_name_l.grid(row = 6, sticky = 'W', padx = 5)

        #Entries for the labels (_e)
        self.name_e = Entry(master, font = 'calibri 11')
        self.name_e.grid(row = 1, column = 1)

        self.inventory_e = Entry(master, font = 'calibri 11')
        self.inventory_e.grid(row = 2, column = 1)

        self.description_e = Entry(master, font = 'calibri 11')
        self.description_e.grid(row = 3, column = 1, ipady = 25, pady = 5, sticky = 'NW')

        self.cost_price_e = Entry(master, font = 'calibri 11')
        self.cost_price_e.grid(row = 4, column = 1)

        self.selling_price_e = Entry(master, font = 'calibri 11')
        self.selling_price_e.grid(row = 5, column = 1)

        self.supplier_name_e = Entry(master, font = 'calibri 11')
        self.supplier_name_e.grid(row = 6, column = 1)

        #Button to add to Database 'store' in MySQL
        self.btn_add = Button(master, text = 'Add To Database', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.get_items)
        self.btn_add.grid(row = 7, column = 0, pady = 10)

        #Button to clear all fields
        self.btn_clear = Button(master, text = 'Clear All Fields', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.clear_all)
        self.btn_clear.grid(row = 7, column = 1)

        #Textbox to show logs
        self.tBox = Text(master, width = 25, height = 10, font = 'calibri 11')
        self.tBox.grid(row = 1, column = 2, rowspan = 6, padx = 15, pady = 5)
        self.tBox.insert(END, 'ID has reached: ' + str(id()))

        #Button to quit to startup screen
        self.quitButton = Button(master, text = 'Quit', width = 15, bg = 'light gray', command = self.close_windows)
        self.quitButton.grid(row = 8, columnspan = 4, pady = 10)

    #Clears all entries - GUI feature
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.inventory_e.delete(0, END)
        self.description_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.selling_price_e.delete(0, END)
        self.supplier_name_e.delete(0, END)
        self.tBox.delete(1.0, END)
        self.tBox.insert(END, 'ID has reached: ' + (str(id()))) #Retain textbox (tBox) ID for GUI

    #Assigning values of entries into variables to insert into the database
    def get_items(self, *args, **kwargs):
        #Getting from entries
        self.name = self.name_e.get()
        self.inventory = self.inventory_e.get()
        self.description = self.description_e.get()
        self.cost_price = self.cost_price_e.get()
        self.selling_price = self.selling_price_e.get()
        self.supplier_name = self.supplier_name_e.get()

        #Dynamic entries
        #Error Handling
        if self.name == '' or self.inventory == '' or self.cost_price == '' or self.selling_price == '' or self.description == '' or self.cost_price == '' or self.selling_price == '':
            tkinter.messagebox.showinfo('Error', 'Some important entries are empty, please fill them and try again') #For GUI
        else:
            self.profit = (float(self.selling_price) - float(self.cost_price)) * float(self.inventory) #Calculating 'Assumed_Profits'
            
            #Finally inserting the values into 'inventory' table
            sql = 'INSERT INTO inventory(Name, Inventory, Description, Cost_Price, Selling_Price, Supplier_Name, Assumed_Profits) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            c.execute(sql, (self.name, self.inventory, self.description, self.cost_price, self.selling_price, self.supplier_name, self.profit))
            conn.commit() #Reset cursor
            
            #Exception handling for Program 3 (POS)
            profitsreset = 'UPDATE inventory SET Final_Profits = 0 WHERE Final_Profits is NULL'
            c.execute(profitsreset)
            conn.commit()
            
            #UI Elements
            self.clear_all
            tkinter.messagebox.showinfo('Operation Successful', 'Added to the database.')

            #Inserting into textbox for UI
            self.tBox.insert(END, '\n\nInserted ' + self.name + ' into the database with code ' + str(id()))
            self.tBox.insert(END, '\n\nID has reached: ' + str(id()))
        
    #Going back to Startup
    def close_windows(self):
        self.master.destroy()

#Program 2 - Updates existing database
class DatabaseUpdate:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        #Using grids in master frame
        self.heading = Label(master, text = 'UPDATE DATABASE (BACK END)', font = ('Segoe UI Light', 24, 'bold'))
        self.heading.grid(column = 0, columnspan = 3, padx = 30, pady = 10)

        #Binding enter and escape keys to functions for better UI
        self.master.bind('<Return>', self.search)
        self.master.bind('<Escape>', self.clear_all)

        #Labels and entry for id
        self.id_l = Label(master, text = 'Enter ID (Primary Key)', font = 'calibri 14')
        self.id_l.grid(row = 8, sticky = 'N', padx = 5)

        self.id_e = Entry(master, font = 'calibri 11', width = 5)
        self.id_e.grid(row = 8, column = 1, sticky = 'NW', pady = 5)
        
        #Labels for the window (_l) - master frame
        self.name_l = Label(master, text = 'Update Product Name', font = 'calibri 14')
        self.name_l.grid(row = 1, sticky = 'W', padx = 5)
        
        self.inventory_l = Label(master, text = 'Update Inventory', font = 'calibri 14')
        self.inventory_l.grid(row = 2, sticky = 'W', padx = 5)
        
        self.decription_l = Label(master, text = 'Update Description', font = 'calibri 14')
        self.decription_l.grid(row = 3, sticky = 'W', padx = 5)
        
        self.cost_price_l = Label(master, text = 'Update Cost Price', font = 'calibri 14')
        self.cost_price_l.grid(row = 4, sticky = 'W', padx = 5)
        
        self.selling_price_l = Label(master, text = 'Update Selling Price', font = 'calibri 14')
        self.selling_price_l.grid(row = 5, sticky = 'W', padx = 5)
        
        self.supplier_name_l = Label(master, text = 'Update Supplier Name', font = 'calibri 14')
        self.supplier_name_l.grid(row = 6, sticky = 'W', padx = 5)

        #Entries for the labels (_e)
        self.name_e = Entry(master, font = 'calibri 11')
        self.name_e.grid(row = 1, column = 1)

        self.inventory_e = Entry(master, font = 'calibri 11')
        self.inventory_e.grid(row = 2, column = 1)

        self.description_e = Entry(master, font = 'calibri 11')
        self.description_e.grid(row = 3, column = 1, ipady = 25, pady = 5, sticky = 'NW')

        self.cost_price_e = Entry(master, font = 'calibri 11')
        self.cost_price_e.grid(row = 4, column = 1)

        self.selling_price_e = Entry(master, font = 'calibri 11')
        self.selling_price_e.grid(row = 5, column = 1) 

        self.supplier_name_e = Entry(master, font = 'calibri 11')
        self.supplier_name_e.grid(row = 6, column = 1)

        #Button to update Database 'store' in MySQL
        self.btn_add = Button(master, text = 'Update Database', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.update)
        self.btn_add.grid(row = 7, column = 0, pady = 10)

        #Button to clear all fields - UI
        self.btn_clear = Button(master, text = 'Clear All Fields', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.clear_all)
        self.btn_clear.grid(row = 7, column = 1)

        #Textbox to show logs - UI
        self.tBox = Text(master, width = 25, height = 10, font = 'calibri 11')
        self.tBox.grid(row = 1, column = 2, rowspan = 6, padx = 15, pady = 5)
        self.tBox.insert(END, 'ID has reached: ' + str(id())) #Here

        #MAIN FEATURES
        #Button to search id
        self.btn_update = Button(master, text = "Search Database", width = 15, height = 1, command = self.search, bg = 'light gray')
        self.btn_update.grid(row = 8, column = 2, sticky = 'W', pady = 5)

        #Button to quit to startup screen
        self.quitButton = Button(master, text = 'Quit', width = 15, bg = 'light gray', command = self.close_windows)
        self.quitButton.grid(row = 9, columnspan = 4, pady = 10)

    #SALIENT FEATURE
    def search(self, *args, **kwargs):
        sql = 'SELECT * FROM inventory where id = %s'
        c.execute(sql, (self.id_e.get(), ))
        result = c.fetchone()
        
        #Exception handling - UI
        if result:
            result_list = []
            for r in result:
                result_list.append(r)
            
            #Assigning results into list and them into specific variables
            #From table 'inventory'
            self.n1 = result_list[1] #Name
            self.n2 = result_list[2] #Inventory
            self.n3 = result_list[3] #Description
            self.n4 = result_list[4] #Cost_Price
            self.n5 = result_list[5] #Selling_Price
            self.n6 = result_list[6] #Supplier_Name
            
            #Finalizing
            conn.commit()    
 b            
            #Inserting list values into entry fields for updating
            self.clear_all()
            self.name_e.insert(END, self.n1)
            self.inventory_e.insert(END, self.n2)
            self.description_e.insert(END, self.n3)
            self.cost_price_e.insert(END, self.n4)
            self.selling_price_e.insert(END, self.n5)
            self.supplier_name_e.insert(END, self.n6)
        
        #Exception handling - UI
        else:
            tkinter.messagebox.showinfo('Operation Failed', 'ID does not exist.')

    #UI feature
    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.inventory_e.delete(0, END)
        self.description_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.selling_price_e.delete(0, END)
        self.supplier_name_e.delete(0, END)
        self.tBox.delete(1.0, END)
        self.tBox.insert(END, 'ID has reached: ' + (str(id())))

    #MAIN FEATURE
    def update(self, *args, **kwargs):
        #Getting from entries
        self.name = self.name_e.get()
        self.inventory = self.inventory_e.get()
        self.description = self.description_e.get()
        self.cost_price = self.cost_price_e.get()
        self.selling_price = self.selling_price_e.get()
        self.supplier_name = self.supplier_name_e.get()
        self.id = self.id_e.get()

        #Dynamic entries
        if self.name == '' or self.inventory == '' or self.cost_price == '' or self.selling_price == '' or self.description == '' or self.cost_price == '' or self.selling_price == '':
            tkinter.messagebox.showinfo('Error', 'Some important entries are empty, please fill them and try again')
        else:
            self.profit = (float(self.selling_price) - float(self.cost_price)) * float(self.inventory)
            sql = 'UPDATE inventory SET Name = %s, Inventory = %s, Description = %s, Cost_Price = %s, Selling_Price = %s, Supplier_Name = %s, Assumed_Profits = %s WHERE id = %s'
            c.execute(sql, (self.name, self.inventory, self.description, self.cost_price, self.selling_price, self.supplier_name, self.profit, int(self.id)))
            conn.commit()
            self.clear_all()
            tkinter.messagebox.showinfo('Operation Successful', 'Updated database.')

            #Inserting into textbox - UI element
            self.tBox.insert(END, '\n\nUpdated ' + self.name + ' into the database belonging to ID ' + str(self.id))
    
    #Back to startup window
    def close_windows(self):
        self.master.destroy()

#Program 3 - POS System
#1. Updates database
#2. Reduces stocks when order of item done
#3. Adds final profits to compare with assumed profits - Using Program 1's Exception Handling
#4. Calculates change for money given
#GIVES INVOICE IN .TXT FORMAT - Saved with beautiful UI sorted by date and given invoice number
class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        
        #Initialization for add_to_invoice function
        self.total_bill = 0
        self.count = 0 #Debugging purposes
        
        #Frames inside main - 2
        self.left = Frame(master, bg = '#d1d8e0')
        self.left.pack(side = LEFT, fill = BOTH)

        self.right = Frame(master, bg = '#45aaf2')
        self.right.pack(side = RIGHT, fill = BOTH)

        #Components
        self.heading = Label(self.left, text = 'Sahil\'s Eatery', font = ('Segoe UI Light', 26, 'bold'), bg = '#d1d8e0')
        self.heading.grid(columnspan = 4)

        self.date_l = Label(self.right, text = str(date), font = 'calibri 16 bold', bg = '#45aaf2')
        self.date_l.grid()

        #Table invoice
        self.tproduct = Label(self.right, text = 'Products', font = ('Calibri Light', 14, 'bold'), bg = '#45aaf2')
        self.tproduct.grid(row = 1, column = 0, sticky = 'W')

        self.tamount = Label(self.right, text = 'Amount', font = ('Calibri Light', 14, 'bold'), bg = '#45aaf2')
        self.tamount.grid(row = 1, column = 1, padx = 5)

        #Buttons to add to invoice table
        #MENU ITEMS
        self.btn1 = Button(self.left, text = 'Cheese Pizza', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Cheese Pizza'))
        self.btn1.grid(row = 1, column = 0, padx = 2.5, pady = 2.5)

        self.btn2 = Button(self.left, text = 'Veggie Pizza', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Veggie Pizza'))
        self.btn2.grid(row = 1, column = 1, padx = 2.5, pady = 2.5)

        self.btn3 = Button(self.left, text = 'Non-Veggie Pizza', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Non-Veggie Pizza'))
        self.btn3.grid(row = 1, column = 2, padx = 2.5, pady = 2.5)

        self.btn4 = Button(self.left, text = 'Tomato Soup', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Tomato Soup'))
        self.btn4.grid(row = 2, column = 0, padx = 2.5, pady = 2.5)

        self.btn5 = Button(self.left, text = 'Sweet Corn Soup', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Sweet Corn Soup'))
        self.btn5.grid(row = 2, column = 1, padx = 2.5, pady = 2.5)

        self.btn6 = Button(self.left, text = 'Manchow Soup', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Manchow Soup'))
        self.btn6.grid(row = 2, column = 2, padx = 2.5, pady = 2.5)

        self.btn7 = Button(self.left, text = 'Basil Soup', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Basil Soup'))
        self.btn7.grid(row = 2, column = 3, padx = 2.5, pady = 2.5)

        self.btn8 = Button(self.left, text = 'Hakka Noodles', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Hakka Noodles'))
        self.btn8.grid(row = 3, column = 0, padx = 2.5, pady = 2.5)

        self.btn9 = Button(self.left, text = 'Manchurian', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Manchurian'))
        self.btn9.grid(row = 3, column = 1, padx = 2.5, pady = 2.5)

        self.btn10 = Button(self.left, text = 'Spring Roll', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Spring Roll'))
        self.btn10.grid(row = 3, column = 2, padx = 2.5, pady = 2.5)

        self.btn11 = Button(self.left, text = 'Chilly Paneer', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Chilly Paneer'))
        self.btn11.grid(row = 3, column = 3, padx = 2.5, pady = 2.5)

        self.btn12 = Button(self.left, text = 'Veg Burger', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Veg Burger'))
        self.btn12.grid(row = 4, column = 0, padx = 2.5, pady = 2.5)

        self.btn13 = Button(self.left, text = 'Cheese Burger', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Cheese Burger'))
        self.btn13.grid(row = 4, column = 1, padx = 2.5, pady = 2.5)

        self.btn14 = Button(self.left, text = 'Veg Momos', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Veg Momos'))
        self.btn14.grid(row = 4, column = 2, padx = 2.5, pady = 2.5)

        self.btn15 = Button(self.left, text = 'Paneer Momos', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Paneer Momos'))
        self.btn15.grid(row = 4, column = 3, padx = 2.5, pady = 2.5)

        self.btn16 = Button(self.left, text = 'Veg Sandwich', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Veg Sandwich'))
        self.btn16.grid(row = 5, column = 0, padx = 2.5, pady = 2.5)

        self.btn17 = Button(self.left, text = 'Cheese Sandwich', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Cheese Sandwich'))
        self.btn17.grid(row = 5, column = 1, padx = 2.5, pady = 2.5)

        self.btn18 = Button(self.left, text = 'French Fries', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('French Fries'))
        self.btn18.grid(row = 5, column = 2, padx = 2.5, pady = 2.5)

        self.btn19 = Button(self.left, text = 'Crispy Potato', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Crispy Potato'))
        self.btn19.grid(row = 5, column = 3, padx = 2.5, pady = 2.5)

        self.btn20 = Button(self.left, text = 'Deluxe Thali', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Deluxe Thali'))
        self.btn20.grid(row = 6, column = 0, padx = 2.5, pady = 2.5)

        self.btn21 = Button(self.left, text = 'Special Thali', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Special Thali'))
        self.btn21.grid(row = 6, column = 1, padx = 2.5, pady = 2.5)

        self.btn22 = Button(self.left, text = 'Tandoor Platter', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Tandoor Platter'))
        self.btn22.grid(row = 6, column = 2, padx = 2.5, pady = 2.5)

        self.btn23 = Button(self.left, text = 'Chinese Platter', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Chinese Platter'))
        self.btn23.grid(row = 6, column = 3, padx = 2.5, pady = 2.5)

        self.btn24 = Button(self.left, text = 'Plain Dosa', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Plain Dosa'))
        self.btn24.grid(row = 7, column = 0, padx = 2.5, pady = 2.5)

        self.btn25 = Button(self.left, text = 'Masala Dosa', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Masala Dosa'))
        self.btn25.grid(row = 7, column = 1, padx = 2.5, pady = 2.5)

        self.btn26 = Button(self.left, text = 'Paneer Dosa', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Paneer Dosa'))
        self.btn26.grid(row = 7, column = 2, padx = 2.5, pady = 2.5)

        self.btn27 = Button(self.left, text = 'Idli Sambar', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Idli Sambar'))
        self.btn27.grid(row = 7, column = 3, padx = 2.5, pady = 2.5)

        self.btn28 = Button(self.left, text = 'Tea', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Tea'))
        self.btn28.grid(row = 8, column = 0, padx = 2.5, pady = 2.5)

        self.btn29 = Button(self.left, text = 'Coffee', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Coffee'))
        self.btn29.grid(row = 8, column = 1, padx = 2.5, pady = 2.5)

        self.btn30 = Button(self.left, text = 'Lassi', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Lassi'))
        self.btn30.grid(row = 8, column = 2, padx = 2.5, pady = 2.5)

        self.btn31 = Button(self.left, text = 'Buttermilk', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Buttermilk'))
        self.btn31.grid(row = 8, column = 3, padx = 2.5, pady = 2.5)

        #To final order given
        self.btn32 = Button(self.left, text = 'Final Order', width = 20, height = 1, bg = 'yellow', font = 'calibri 16', command = self.final_order)
        self.btn32.grid(row = 9, columnspan = 4, padx = 2.5, pady = 2.5)
    
        #Total Label - dynamically updates later in Program 3
        self.total_l = Label(self.right, text = 'Total: Rs.0', font = 'calibri 16 bold', bg = '#45aaf2')
        self.total_l.grid(row = 0, column = 1, padx = 15)

        #Button to quit to startup screen
        self.quitButton = Button(self.left, text = 'Quit', width = 15, bg = 'light gray', command = self.close_windows)
        self.quitButton.grid(row = 13, columnspan = 4, pady = 10)

    #SALIENT FEATURE
    def add_to_invoice(self, *args, **kwargs):
        c.execute('SELECT * FROM inventory WHERE Name = %s', (*args, ))
        item = c.fetchone()
        conn.commit()
        
        #Exception Handling
        if item:
            self.count+=1 #Debugging purposes

            n1 = item[1] #Name
            n2 = item[2] #Inventory
            #n3 = item[3] #Description
            n4 = item[4] #Cost_Price
            n5 = item[5] #Selling_Price
            #n6 = item[6] #Supplier_Name

            profit = int(n5) - int(n4)
            self.total_bill += int(n5) #For later use

            #Update 'inventory' table
            sql = 'UPDATE inventory SET Inventory = %s, Final_Profits = (Final_Profits + %s) WHERE Name = %s'
            c.execute(sql, ((int(n2)-1), profit, *args))
            conn.commit()

            #To be diplayed in self.right Frame
            products_list.append(n1)
            amounts_list.append(n5)

            #Adding to right frame for UI
            #SALIENT FEATURE
            row_index = 2
            self.counter = 0
            for self.p in products_list:
                self.temp_name = Label(self.right, text = str(products_list[self.counter]), font = 'calibri 11', bg = '#45aaf2')
                self.temp_name.grid(row = row_index, column = 0, sticky = 'W')
                self.temp_amount = Label(self.right, text = str(amounts_list[self.counter]), font = 'calibri 11', bg = '#45aaf2')
                self.temp_amount.grid(row = row_index, column = 1)

                #Adding to the transactions MySQL table in store database
                sql = 'INSERT INTO transactions(Product_Name, Amount, Date) VALUES(%s, %s, %s)'
                c.execute(sql, (products_list[self.counter], amounts_list[self.counter], str(datetime)))
                conn.commit()

                row_index += 1
                self.counter += 1
                
                #Updating total label
                self.total_l.configure(text = 'Total: Rs.' + str(self.total_bill))
        else:
            tkinter.messagebox.showinfo('Operation Failed', 'Update database, item does not exist\nor has empty inventory.')
        
        #Debugging Purposes - Error Handling by Programmer (Sahil Agarwal)
        '''print(products_list)
        print(amounts_list)
        print(self.count)'''

    #To create .txt invoice for customer
    #MAIN FEATURE
    def final_order(self, *args, **kwargs):
        #Creating bill before copying it to the database
        directory = 'C:/12th Project/Invoice/' + str(date) + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        #Bill Template - for UI
        company = '           Sahil Eatery\n'
        address = '          Class 12B, RFS\n'
        phone = '          +91 9999999999\n'
        sample = '             Invoice\n'
        dt = '            ' + str(date)
        table_header = '\n--------------------------------------------\nS.No. Products                       Amount\n--------------------------------------------\n'
        
        #Creating str to insert as .txt
        products = ''
        for a in range(len(products_list)):
            products += (str((a+1)) + '     ')[:6] + str(products_list[a] + '            ')[:12] + '                   ' + str(amounts_list[a]) + '\n'
        final = company + address + phone + sample + dt + '\n' + table_header + products

        #To open a file and write to it
        #SALIENT FEATURE
        file_name = str(directory) + str(random.randrange(5000, 10000)) + '.txt'
        f = open(file_name, 'w')
        f.write(final)
        f.write('\nTotal: Rs.' + str(self.total_bill) + '\n' + 'Thanks for visiting.')
        f.close()

        #UI Element
        tkinter.messagebox.showinfo('Order Final', 'Bill total is: Rs.' + str(self.total_bill))
        self.money_given_l = Label(self.left, text = 'Money Given', font = ('Segoe UI Light', 12, 'bold'), bg = '#d1d8e0')
        self.money_given_l.grid(row = 10, columnspan = 2, sticky = 'E', padx = 5)
        self.money_given_e = Entry(self.left, font = 'calibri 11', width = 10)
        self.money_given_e.grid(row = 10, column = 2)
        self.btn_money = Button(self.left, text = 'Calculate Change', width = 13, height = 1, bg = 'white', command = self.change_calc)
        self.btn_money.grid(row = 11, columnspan = 4, padx = 2.5, pady = 2.5)
        
        #Disabling ordering buttons to final order without exceptions
        self.btn1.configure(state = 'disabled')
        self.btn2.configure(state = 'disabled')
        self.btn3.configure(state = 'disabled')
        self.btn4.configure(state = 'disabled')
        self.btn5.configure(state = 'disabled')
        self.btn6.configure(state = 'disabled')
        self.btn7.configure(state = 'disabled')
        self.btn8.configure(state = 'disabled')
        self.btn9.configure(state = 'disabled')
        self.btn10.configure(state = 'disabled')
        self.btn11.configure(state = 'disabled')
        self.btn12.configure(state = 'disabled')
        self.btn13.configure(state = 'disabled')
        self.btn14.configure(state = 'disabled')
        self.btn15.configure(state = 'disabled')
        self.btn16.configure(state = 'disabled')
        self.btn17.configure(state = 'disabled')
        self.btn18.configure(state = 'disabled')
        self.btn19.configure(state = 'disabled')
        self.btn20.configure(state = 'disabled')
        self.btn21.configure(state = 'disabled')
        self.btn22.configure(state = 'disabled')
        self.btn23.configure(state = 'disabled')
        self.btn24.configure(state = 'disabled')
        self.btn25.configure(state = 'disabled')
        self.btn26.configure(state = 'disabled')
        self.btn27.configure(state = 'disabled')
        self.btn28.configure(state = 'disabled')
        self.btn29.configure(state = 'disabled')
        self.btn30.configure(state = 'disabled')
        self.btn31.configure(state = 'disabled')
        self.btn32.configure(state = 'disabled')
        
        #Binding enter key to self.change_calc - better UI
        self.master.bind('<Return>', self.change_calc)
    
    #SALIENT FEATURE
    def change_calc(self, *args, **kwargs):
        self.change = -(self.total_bill - int(self.money_given_e.get()))
        if self.change >= 0:
            tkinter.messagebox.showinfo('Bill Final', 'Thank you for visiting.\nChange is: Rs.' + str(self.change))
        else:
            tkinter.messagebox.showinfo('Operation Failed', 'Not enough money given\nBill total is: Rs.' + str(self.total_bill))

    #Going back to startup window
    def close_windows(self):
        self.master.destroy()

#Finale - starting the program
def main(): 
    root = Tk()
    root.title('Sahil\'s GUI POS - Frontend and Backend')
    app = Startup(root)
    root.mainloop()

#Exception handling for UI - once again
if __name__ == '__main__':
    main()