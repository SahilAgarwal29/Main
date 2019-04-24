# -*- coding: utf-8 -*-
"""
Created on Sat Feb 09 2019 13:26:22

@author: Sahil Agarwal
@project: CS PRACTICALS
@class: XI-B
"""
#A Menu-Driven Program for... a menu!
#Created by Sahil Agarwal - XI-B

#defining the cart value as zero for user to add items into
cart = 0
#defining the reciept for ordered items
reciept = ['Your Total Order Reciept:']
#sleep timer for fun
from time import sleep

''' DEFINING FUNCTIONS FOR MAIN PROGRAM'''
#main function describing the program
def order(cart):
    print(' ')
    print('******************************')
    print(' ')
    print('Your total order is: ',cart)
    order = input('This is the main menu\nWhat would you like to order?\n\
(D)rinks\n(P)izzas\n(B)urgers\n(E)xtras\n****************\n(V)iew Order\n\
(Q)uit to Start\nChoose: ')
    if order.lower() == 'd':             #taken in lowercase to support both 
        drinks(cart, reciept)            #uppercase and lowercase inputs
    elif order.lower() == 'p':
        pizza(cart, reciept)
    elif order.lower() == 'b':
        burger(cart, reciept)
    elif order.lower() == 'e':
        extras(cart, reciept)
    elif order.lower() == 'q':
        main(cart)
    elif order.lower() == 'v':
        reciept1(cart)
    else:
        main(cart)

#defining the drinks ordering menu function   
def drinks(cart, reciept):
    print(' ')
    print('******************************')
    drink_choice = input('This is the Drinks menu\n(S)elect a drink\n(Q)uit to\
 main menu\nChoose: ')
    if drink_choice.lower() == 's':
            print(' ')
            print('******************************')
            drink_select = input('Select a Drink - Each is Priced Rs. 120\n\n\
(C)oca-Cola\n(M)tn. Dew\n(S)prite\nEnter your choice: ')
            if drink_select.lower() == 'c' or drink_select.lower() == 'm' \
            or drink_select.lower() == 's':
                cart += 120
                reciept.append('Soft Drink ------- 120')
            else:
                print('oops!\n')
    print('Done!')
    drink_stay = ('(Q)uit to main menu, (S)elect another drink')
    if drink_stay.lower() == 'q':
            drink_stay = False
    else:
        order(cart)

#defining the pizza ordering menu function
def pizza(cart, reciept):
    print(' ')
    print('******************************')
    pizza_choice = input('This is the Pizza menu\n(S)elect a pizza\n(Q)uit to\
 main menu\nChoose: ')
    if pizza_choice.lower() == 's':
            print(' ')
            print('******************************')
            print(' ')
            pizza_select = input('Select a Pizza\n\n(M)argarita - 300\n\
(F)armhouse - 400\n(P)epperoni - 500\n(B)arbecue - 400\nEnter your choice: ')
            if (pizza_select).lower() == 'm':
                cart += 300
                reciept.append('Pizza Margarita ------- 300')
            elif pizza_select.lower() == 'f':
                cart += 400
                reciept.append('Pizza Farmhouse ------- 400')
            elif pizza_select.lower() == 'p':
                cart += 500
                reciept.append('Pizza Pepperoni ------- 500')
            elif pizza_select.lower() == 'b':
                cart += 400
                reciept.append('Pizza Barbecue ------- 400')
            else:
                print('oops!\n')
    print('Done!')
    print('Your total order is: ', cart)
    pizza_stay = ('(Q)uit to main menu, (S)elect another pizza')
    if pizza_stay.lower() == 'q':
        order()
    elif pizza_stay.lower() == 's':
        pizza(cart)
    else:
        order(cart)
        
#defining the burger ordering menu function
def burger(cart, reciept):
    print(' ')
    print('******************************')
    burger_choice = input('This is the Burger menu\n(S)elect a Burger\n\
(Q)uit to main menu\nChoose: ')
    if burger_choice.lower() == 's':
            print(' ')
            print('******************************')
            burger_select = input('Select a Burger\n\n(V)eggie - 300\n\
(N)on-Veggie - 400\n(E)ggie - 300\n(C)cheesie - 400\nEnter your choice: ')
            if (burger_select).lower() == 'v':
                cart += 300
                reciept.append('Burger Veggie ------- 300')
            elif burger_select.lower() == 'n':
                cart += 400
                reciept.append('Burger Non-Veggie ------- 400')
            elif burger_select.lower() == 'e':
                cart += 300
                reciept.append('Burger Eggie ------- 300')
            elif burger_select.lower() == 'c':
                cart += 400
                reciept.append('Burger Cheesie ------- 400')
            else:
                print('oops!\n')
    print('Done!')
    print('Your total order is: ', cart)
    burger_stay = ('(Q)uit to main menu, (S)elect another pizza')
    if burger_stay.lower() == 'q':
        order()
    elif burger_stay.lower() == 's':
        pizza(cart)
    else:
        order(cart)

#defining the extras ordering menu function
def extras(cart, reciept):
    print(' ')
    print('******************************')
    extras_choice = input('This is the Extras menu\n(S)elect an Extra\n(Q)uit\
 to main menu\nChoose: ')
    if extras_choice.lower() == 's':
            print(' ')
            print('******************************')
            extras_select = input('Select an Extra\n\n(M)ousse - 200\n\
(G)arlic Bread - 200\n(F)ries - 100\n(S)undae - 350\nEnter your choice: ')
            if (extras_select).lower() == 'm':
                cart += 200
                reciept.append('Extras Mousse ------- 200')
            elif extras_select.lower() == 'g':
                cart += 200
                reciept.append('Extras Garlic Bread ------- 200')
            elif extras_select.lower() == 'f':
                cart += 100
                reciept.append('Extras Fries ------- 100')
            elif extras_select.lower() == 's':
                cart += 350
                reciept.append('Extras Sundae ------- 350')
            else:
                print('oops!\n')
    print('Done!')
    burger_stay = ('(Q)uit to main menu, (S)elect another pizza')
    if burger_stay.lower() == 'q':
        order()
    elif burger_stay.lower() == 's':
        pizza(cart)
    else:
        order(cart)
        
#defining iteration script for reciept
def reciept1(cart):
    print(' ')
    print('******************************')
    for a in reciept:
        print(a)
    print('Your total order is now Rs.', cart)
    print('\nGoing to the Start Menu to Confirm your Order!')
    print(' ')
    print('******************************')
    sleep(5)
    main(cart)

            
'''FINAL PROGRAM'''
def main(cart):
    welc = input('''+----------------------------+
|                            |
|     Virtual Restaurant     |
|                            |
+----------------------------+
|Press (O) to Order          |
+----------------------------+
|Press (F) to finalise order |
+----------------------------+
|Press (Q) to quit           |
+----------------------------+

Enter here: ''')
    if welc.lower() == 'o':
        order(cart)
    elif welc.lower() == 'f':
        for a in reciept:
            print(a)
        print('Order Final! Thank You for being with us.')
        print('Your Total Order is Rs.', cart)
        sleep(10)
    else:
        print(' ')
        print('Thank You for being with us. Bye!')
        quit

'''CALLING MAIN FUNCTION AND STARTING PROGRAM'''
main(cart)

#le finit