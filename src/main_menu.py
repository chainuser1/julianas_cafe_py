# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def display_main_menu(): 
    print "Main Menu:\n"
    print "1.)Search a product"
    print "2.)Enter a new product."
    print "3.)Delete a product by its ID"

def get_menu_input():
    choice=input("Enter your choice: ")
    return choice   

def select_option():
    choice=input("Enter (1)-Edit, (2)Delete: ")
    return choice
    
