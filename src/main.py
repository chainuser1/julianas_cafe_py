# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import main_menu
from database_trans import Database

__author__ = "Pareng Je"
__date__ = "$11 5, 18 8:31:19 AM$"


if __name__ == "__main__":
    app_status=1 #sets status for program to terminate once it falls to zero
    def main():#main function
        print "Welcome to Juliana's Cafe!"
        main_menu.display_main_menu()#displays main menu
        choice=main_menu.get_menu_input() #asks user for choice input
        
        try: 
            assert choice<=3, "You inputted an invalid number!" 
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
                        man_id=input("Enter Manufacturer ID: ")
                        print product.update_product(pid, pname, pprice, pstocks, man_id)
                    elif (chx==2):
                        print product.delete_product(input("Enter the product ID to be deleted: "))
                    else:
                        pass
                else:
                    print result
            
            elif choice==2:
                pname=raw_input("Enter the product name: ")
                pprice=float(raw_input("Enter product price: "))
                pstocks=input("Enter product stocks: ")
                man_id=input("Enter manufacturer ID: ")
                print ("Result: %s" % (product.insert_product(pname,pprice,pstocks, man_id))) 
            elif choice==3:
                global app_status
                app_status=0
            
            else:
                pass
        except AssertionError as e: 
            print e
     
        finally:
            if app_status==0:
                exit(0)
            else:
                main()
            
    main()
        
        
        
    
        
