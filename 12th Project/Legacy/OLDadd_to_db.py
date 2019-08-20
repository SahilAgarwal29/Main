#To import modules
from tkinter import *
import mysql.connector as sql
import tkinter.messagebox

conn = sql.connect(host = 'localhost', user = 'root', passwd = 'password', database = 'store')
c = conn.cursor()

def id():
    c.execute('select max(id) from inventory;') #Here
    id = c.fetchone()
    conn.commit()
    return id[0]

class Database:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text = 'ADD TO DATABASE (BACK END)', font = ('Segoe UI Light', 24, 'bold'))
        self.heading.place(x = 170)

        #Labels for the window (_l)
        self.name_l = Label(master, text = 'Enter Product Name', font = 'calibri 14')
        self.name_l.place(y = 50)
        
        self.inventory_l = Label(master, text = 'Enter Inventory', font = 'calibri 14')
        self.inventory_l.place(y = 80)
        
        self.decription_l = Label(master, text = 'Enter Description', font = 'calibri 14')
        self.decription_l.place(y = 110)
        
        self.cost_price_l = Label(master, text = 'Enter Cost Price', font = 'calibri 14')
        self.cost_price_l.place(y = 140)
        
        self.selling_price_l = Label(master, text = 'Enter Selling Price', font = 'calibri 14')
        self.selling_price_l.place(y = 170)
        
        self.supplier_name_l = Label(master, text = 'Enter Supplier Name', font = 'calibri 14')
        self.supplier_name_l.place(y = 200)

        #Entries for the labels (_e)
        self.name_e = Entry(master, width = 25, font = 'calibri 11')
        self.name_e.place(x = 190, y = 55)

        self.inventory_e = Entry(master, width = 25, font = 'calibri 11')
        self.inventory_e.place(x = 190, y = 85)

        self.description_e = Entry(master, width = 25, font = 'calibri 11')
        self.description_e.place(x = 190, y = 115)

        self.cost_price_e = Entry(master, width = 25, font = 'calibri 11')
        self.cost_price_e.place(x = 190, y = 145)

        self.selling_price_e = Entry(master, width = 25, font = 'calibri 11')
        self.selling_price_e.place(x = 190, y = 175)

        self.supplier_name_e = Entry(master, width = 25, font = 'calibri 11')
        self.supplier_name_e.place(x = 190, y = 205)

        #Button to add to Database 'store' in MySQL
        self.btn_add = Button(master, text = 'Add To Database', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.get_items)
        self.btn_add.place(x = 100, y = 310)

        #Button to clear all fields
        self.btn_clear = Button(master, text = 'Clear All Fields', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.clear_all)
        self.btn_clear.place(x = 250, y = 310)

        #Textbox to show logs
        self.tBox = Text(master, width = 25, height = 10, font = 'calibri 11')
        self.tBox.place(x = 470, y = 55)
        self.tBox.insert(END, 'ID has reached: ' + str(id())) #Here

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.inventory_e.delete(0, END)
        self.description_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.selling_price_e.delete(0, END)
        self.supplier_name_e.delete(0, END)
        self.tBox.delete(1.0, END)
        self.tBox.insert(END, 'ID has reached: ' + (str(id()))) #Here

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
            self.clear_all
            tkinter.messagebox.showinfo('Operation Successful', 'Added to the database.')

            #Inserting textbox
            self.tBox.insert(END, '\n\nInserted ' + self.name + ' into the database with code ' + str(id()))
            self.tBox.insert(END, '\n\nID has reached: ' + str(id()))

root = Tk()
b = Database(root)

root.geometry('800x600+0+0')
root.title('Add to the database')
root.mainloop()