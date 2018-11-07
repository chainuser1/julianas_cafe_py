# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import math
def display_main_menu(): 
    print "Main Menu:\n"
    print "1.)Search a product"
    print "2.)Enter a new product."
    print "3.)Terminate Program"

def get_menu_input():
    try:
        choice=input("Please enter choice: ")
        return choice
    except (NameError) as error:
        print error
        
          
def select_option():
    
    try:
        choice=input("Enter (1)-Edit, (2)Delete, (Any Number)Exit: ")
        return choice
    except (NameError) as error:
        print error
    
