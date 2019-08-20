#To import modules
from tkinter import *
import mysql.connector as sql
import tkinter.messagebox
import datetime as dt
import time
import os
import random
import sys

conn = sql.connect(host = 'localhost', user = 'root', passwd = 'password', database = 'store')
c = conn.cursor()

#Date
date = dt.datetime.now().date()
datetime = dt.datetime.now()

#List initialization
products_list = []
amounts_list = []

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        
        #Initialization for add_to_invoice function
        self.total_bill = 0
        self.count = 0 #Debugging purposes
        
        #Frames
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
        self.btn1 = Button(self.left, text = 'Cheese Pizza', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Fries'))
        self.btn1.grid(row = 1, column = 0, padx = 2.5, pady = 2.5)

        self.btn2 = Button(self.left, text = 'Veggie Pizza', width = 13, height = 1, bg = 'white', command = lambda : self.add_to_invoice('Sahil'))
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

        self.btn32 = Button(self.left, text = 'Final Order', width = 20, height = 1, bg = 'yellow', font = 'calibri 16', command = self.final_order)
        self.btn32.grid(row = 9, columnspan = 4, padx = 2.5, pady = 2.5)
    
        #Total Label
        self.total_l = Label(self.right, text = 'Total: Rs.0', font = 'calibri 16 bold', bg = '#45aaf2')
        self.total_l.grid(row = 0, column = 1, padx = 15)

    def add_to_invoice(self, *args, **kwargs):
        c.execute('SELECT * FROM inventory WHERE Name = %s', (*args, ))
        item = c.fetchone()
        conn.commit()
        
        if item:
            self.count+=1 #Debugging purposes

            n1 = item[1] #Name
            n2 = item[2] #Inventory
            #n3 = item[3] #Description
            n4 = item[4] #Cost_Price
            n5 = item[5] #Selling_Price
            #n6 = item[6] #Supplier_Name

            profit = int(n5) - int(n4)
            self.total_bill += int(n5)

            sql = 'UPDATE inventory SET Inventory = %s, Final_Profits = (Final_Profits + %s) WHERE Name = %s'
            c.execute(sql, ((int(n2)-1), profit, *args))
            conn.commit()

            #To be diplayed in self.right Frame
            products_list.append(n1)
            amounts_list.append(n5)

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
        
        #Debugging Purposes
        '''print(products_list)
        print(amounts_list)
        print(self.count)'''

    def final_order(self, *args, **kwargs):
        #Creating bill before copying it to the database
        directory = 'C:/12th Project/Invoice/' + str(date) + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        #Bill Template
        company = '           Sahil Eatery\n'
        address = '          Class 12B, RFS\n'
        phone = '          +91 9999999999\n'
        sample = '             Invoice\n'
        dt = '            ' + str(date)
        
        table_header = '\n--------------------------------------------\nS.No. Products                       Amount\n--------------------------------------------\n'
        products = ''
        for a in range(len(products_list)):
            products += (str((a+1)) + '     ')[:6] + str(products_list[a] + '            ')[:12] + '                   ' + str(amounts_list[a]) + '\n'
        final = company+address+phone+sample+dt+'\n'+table_header+products

        #Open a file and write to it
        file_name = str(directory) + str(random.randrange(5000, 10000)) + '.txt'
        f = open(file_name, 'w')
        f.write(final)
        f.write('\nTotal: Rs.' + str(self.total_bill) + '\n' + 'Thanks for visiting.')
        f.close()

        tkinter.messagebox.showinfo('Order Final', 'Bill total is: Rs.' + str(self.total_bill))
        self.money_given_l = Label(self.left, text = 'Money Given', font = ('Segoe UI Light', 12, 'bold'), bg = '#d1d8e0')
        self.money_given_l.grid(row = 10, columnspan = 2, sticky = 'E', padx = 5)
        self.money_given_e = Entry(self.left, font = 'calibri 11', width = 10)
        self.money_given_e.grid(row = 10, column = 2)
        self.btn_money = Button(self.left, text = 'Calculate Change', width = 13, height = 1, bg = 'white', command = self.change)
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
        
        #Binding enter key to self.change for better UI
        self.master.bind('<Return>', self.change)
    
    def change(self, *args, **kwargs):
        self.change = -(self.total_bill - int(self.money_given_e.get()))
        if self.change >= 0:
            tkinter.messagebox.showinfo('Bill Final', 'Thank you for visiting.\nChange is: Rs.' + str(self.change))
            time.sleep(1)
            Button(self.left, text = 'Start New Session', bg = 'yellow', font = 'calibri 14', command = self.destroyer).grid(columnspan = 4)
        else:
            tkinter.messagebox.showinfo('Operation Failed', 'Not enough money given\nBill total is: Rs.' + str(self.total_bill))
        
    def destroyer(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

def main():
    root = Tk()
    b = Application(root)
    root.title('Sahil: Point Of Sale')
    root.mainloop()

main()