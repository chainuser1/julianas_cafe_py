# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import MySQLdb
import string
class Database:
    cursor=0
    db=0
    def __init__(self):
        self.con=MySQLdb.connect("localhost","root","","julianas")
        Database.db=self.con
        Database.cursor=self.con.cursor()
    

    #insert the new product into the products table  
    def insert_product(self, pname, pprice, pstocks, man_id):
        sql="INSERT INTO products(pname,pprice,pstocks, man_id) VALUES('%s','%f','%d', '%d');" % (pname, pprice, pstocks, man_id)
        try:
            Database.cursor.execute(sql)
            Database.db.commit()
            return "The Product %s was added successfully" %(pname)
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            Database.db.rollback()
            return e
        Database.db.close()
    #search products    
    def search_products(self, pname):
        sql="SELECT products.pid,products.pname, products.pprice, products.pstocks, products.man_id FROM products WHERE products.pname LIKE '%s'" %\
        ("%"+pname+"%")
        try:
            Database.cursor.execute(sql)
            if(Database.cursor.rowcount>0):
                print "%d found" %(Database.cursor.rowcount)
                print "ID||Product Name||Price||Stocks||Manufacturer ID"
                result=Database.cursor.fetchall()
                for row in result:
                    print "%d||%s||%.2f||%d||%s" %(row[0],row[1],row[2],row[3], row[4])
                return result
            else:
                return "None Found"                
            Database.db.commit()
            
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            return e
        except:
            return "An unexpected error occurred."
        Database.db.close()    
        
    def delete_product(self, pid):
        sql="DELETE FROM products WHERE pid=%d" %(pid)
        try:
            Database.cursor.execute(sql)
            if(Database.cursor.rowcount>0):
                return "Product has been deleted successfully."
            else:
                return "The product does not exist in the database."
            Database.db.commit()
        except:
            Database.db.rollback()
            return "An error occurred while deleting..."
        Database.db.close()
        
    def update_product(self, pid, pname, pprice, pstocks):
        sql="UPDATE products SET pname='%s', pprice='%f', pstocks='%d' WHERE pid='%d'" %\
            (pname, pprice, pstocks, pid)
        try:
            Database.cursor.execute(sql)  
            Database.db.commit()
            return "Success!!!%d record/s updated." %(Database.cursor.rowcount)
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            Database.db.rollback()
            print e
        Database.db.close()
            
            
            
        
        
