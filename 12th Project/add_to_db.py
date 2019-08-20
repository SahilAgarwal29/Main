#To import modules
from tkinter import *
import mysql.connector as sql
import tkinter.messagebox

conn = sql.connect(host = 'localhost', user = 'root', passwd = 'password', database = 'store')
c = conn.cursor()

def id():
    c.execute('select max(id) from inventory;')
    id = c.fetchone()
    conn.commit()
    return id[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text = 'ADD TO DATABASE (BACK END)', font = ('Segoe UI Light', 24, 'bold'))
        self.heading.grid(column = 0, columnspan = 3, padx = 30, pady = 10)
        
        #Binding enter and escape keys to functions for better UI
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Escape>', self.clear_all)

        #Labels for the window (_l)
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

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.inventory_e.delete(0, END)
        self.description_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.selling_price_e.delete(0, END)
        self.supplier_name_e.delete(0, END)
        self.tBox.delete(1.0, END)
        self.tBox.insert(END, 'ID has reached: ' + (str(id())))

    def get_items(self, *args, **kwargs):
        #Getting from entries
        self.name = self.name_e.get()
        self.inventory = self.inventory_e.get()
        self.description = self.description_e.get()
        self.cost_price = self.cost_price_e.get()
        self.selling_price = self.selling_price_e.get()
        self.supplier_name = self.supplier_name_e.get()

        #Dynamic entries
        if self.name == '' or self.inventory == '' or self.cost_price == '' or self.selling_price == '' or self.description == '' or self.cost_price == '' or self.selling_price == '':
            tkinter.messagebox.showinfo('Error', 'Some important entries are empty, please fill them and try again')
        else:
            self.profit = (float(self.selling_price) - float(self.cost_price)) * float(self.inventory)
            sql = 'INSERT INTO inventory(Name, Inventory, Description, Cost_Price, Selling_Price, Supplier_Name, Assumed_Profits) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            c.execute(sql, (self.name, self.inventory, self.description, self.cost_price, self.selling_price, self.supplier_name, self.profit))
            conn.commit()
            profitsreset = 'UPDATE inventory SET Final_Profits = 0 WHERE Final_Profits is NULL'
            c.execute(profitsreset)
            conn.commit()
            self.clear_all
            tkinter.messagebox.showinfo('Operation Successful', 'Added to the database.')

            #Inserting textbox
            self.tBox.insert(END, '\n\nInserted ' + self.name + ' into the database with code ' + str(id()))
            self.tBox.insert(END, '\n\nID has reached: ' + str(id()))

root = Tk()
b = Database(root)

root.title('Add to the database')
root.mainloop()