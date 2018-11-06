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

    
        
    def insert_product(self, pname, pprice, pstocks):
        sql="INSERT INTO products(pname,pprice,pstocks) VALUES('%s','%f','%d');" % (pname, pprice, pstocks)
        try:
            Database.cursor.execute(sql)
            Database.db.commit()
            return "The Product %s was added successfully" %(pname)
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            Database.db.rollback()
            return "An error occurred."
        
        
    def search_products(self, pname):
        sql="SELECT * FROM products WHERE pname LIKE '%s'" %("%"+pname+"%")
        pid=0
        try:
            Database.cursor.execute(sql)
            if(Database.cursor.rowcount>0):
                print "%d found" %(Database.cursor.rowcount)
                print "ID||Product Name||Price||Stocks"
                result=Database.cursor.fetchall()
                for row in result:
                    print "%d||%s||%.2f||%d" %(row[0],row[1],row[2],row[3])
                return result
            else:
                return "None Found"                
            Database.db.commit()
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            return "An error occurred."
            
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
        
    def update_product(self, pid, pname, pprice, pstocks):
        sql="UPDATE products SET pname='%s', pprice='%.2f', pstocks='%d' WHERE pid='%d'" %\
            (pname, pprice, pstocks, pid)
        try:
            Database.cursor.execute(sql)  
            print "%s has been updated successfully." %(pname.capwords())
            Database.db.commit()
            return "Success!!!"
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            Database.db.rollback()
            print e
            return "Sorry!Update failed..."
            
            
            
        
        
