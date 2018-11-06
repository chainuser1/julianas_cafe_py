# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import main_menu
from database_trans import Database
__author__ = "Pareng Je"
__date__ = "$11 5, 18 8:31:19 AM$"

if __name__ == "__main__":
    print "Welcome to Juliana's Cafe!"
    main_menu.display_main_menu()
    choice=main_menu.get_menu_input()
    try: 
        assert choice<=3 
        product=Database()
        if choice==1:
            search=raw_input("Enter a product to search: ")
            result=product.search_products(search)
            if hasattr(result, "__iter__"):
                chx=main_menu.select_option()
                if (chx==1):
                    pid=input("Enter Product ID for product identification. Note: You cannot update the ID: ")
                    pname=raw_input("Enter the new product name: ")
                    pprice=float(raw_input("Enter the new product price: "))
                    pstocks=input("Enter the new product stocks: ")
                    print "%s" %(product.update_product(pid, pname, pprice, pstocks))
            else:
                print result
            
        elif choice==2:
            pname=raw_input("Enter the product name: ")
            pprice=float(raw_input("Enter product price: "))
            pstocks=input("Enter product stocks: ")
            print ("Result: %s" % (product.insert_product(pname,pprice,pstocks))) 
        
    except: 
        print "You inputted a number other than the choices given."
     
      
        
        
        
    
        
