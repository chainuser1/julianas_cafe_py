# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import MySQLdb
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
        
        
    def search_product(self, pname):
        sql="SELECT * FROM products WHERE pname LIKE '%s'" %("%"+pname+"%")
        try:
            Database.cursor.execute(sql)
            if(Database.cursor.rowcount>0):
                print "%d found" %(Database.cursor.rowcount)
                result=Database.cursor.fetchall()
                for row in result:
                    print "Product Name: %s Product Price: %.2f " %(row[1],row[2])
            else:
                print "None Found"
                
            Database.db.commit()
        except(MySQLdb.Error, MySQLdb.Warning) as e:
            print "An error occurred."
            
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
            
            
        
        
