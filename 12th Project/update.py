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
        
        #Labels for the window (_l)
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

        #Button to clear all fields
        self.btn_clear = Button(master, text = 'Clear All Fields', width = 15, height = 1, bg = 'light gray', fg = 'black', command = self.clear_all)
        self.btn_clear.grid(row = 7, column = 1)

        #Textbox to show logs
        self.tBox = Text(master, width = 25, height = 10, font = 'calibri 11')
        self.tBox.grid(row = 1, column = 2, rowspan = 6, padx = 15, pady = 5)
        self.tBox.insert(END, 'ID has reached: ' + str(id())) #Here

        #Button to search id
        self.btn_update = Button(master, text = "Search Database", width = 15, height = 1, command = self.search, bg = 'light gray')
        self.btn_update.grid(row = 8, column = 2, sticky = 'W', pady = 5)

    def search(self, *args, **kwargs):
        sql = 'SELECT * FROM inventory where id = %s'
        c.execute(sql, (self.id_e.get(), ))
        result = c.fetchone()
        if result:
            result_list = []
            for r in result:
                result_list.append(r)
            
            self.n1 = result_list[1] #Name
            self.n2 = result_list[2] #Inventory
            self.n3 = result_list[3] #Description
            self.n4 = result_list[4] #Cost_Price
            self.n5 = result_list[5] #Selling_Price
            self.n6 = result_list[6] #Supplier_Name
            conn.commit()    
            
            #Inserting list values into entry fields for updating
            self.clear_all()
            self.name_e.insert(END, self.n1)
            self.inventory_e.insert(END, self.n2)
            self.description_e.insert(END, self.n3)
            self.cost_price_e.insert(END, self.n4)
            self.selling_price_e.insert(END, self.n5)
            self.supplier_name_e.insert(END, self.n6)
        else:
            tkinter.messagebox.showinfo('Operation Failed', 'ID does not exist.')


    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.inventory_e.delete(0, END)
        self.description_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.selling_price_e.delete(0, END)
        self.supplier_name_e.delete(0, END)
        self.tBox.delete(1.0, END)
        self.tBox.insert(END, 'ID has reached: ' + (str(id())))

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

            #Inserting textbox
            self.tBox.insert(END, '\n\nUpdated ' + self.name + ' into the database belonging to ID ' + str(self.id))

root = Tk()
b = Database(root)

root.title('Add to the database')
root.mainloop()