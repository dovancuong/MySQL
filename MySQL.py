
import MySQLdb


class Mysql:
    def __init__(self, sv):
        # sv: host,user,passwd,db
        self.db=None
        self.cur = None
        self.sv=sv
        self.port=3306

    def openConnection(self):
        if len(self.sv)<4:
            return"Error: server data incorrect"
        try:
            self.closeConnection()
            self.db = MySQLdb.connect(host=self.sv[0],    # your host is localhost, server name or server IP 
                         user=self.sv[1],         # your username
                         passwd=self.sv[2],           # your password
                         db=self.sv[3], # name of the data base
                         port=self.port)     # using port of Mysql database
            self.cur = self.db.cursor()
            return "Completed"
        except Exception as ex:
            self.db=None
            self.cur=None
            return "Error: ",str(ex)

    def closeConnection(self):
        if self.cur is None:
            return
        self.db.close()
        # self.cur.close()
        
    def selectData(self, query):
        try:
            self.cur.execute(query)
            dt=self.cur.fetchall()
            
            return dt
        except Exception as ex:
            return "Error: ",str(ex)


    def noneQuery(self, cmd): # delete, insert, update...
        if isinstance(cmd,str) is True:
            query=(cmd)
        else:
            query=cmd # convert string to array 

        try:
            for q in query:
                self.cur.execute(q)
            self.db.commit()
            return"Completed"
        except Exception as ex:
            return"Error:",str(ex)

    def insertData(self, query):
        return self.noneQuery(query)

    def deleteData(self, query):
        return self.noneQuery(query)

    def updateData(self, query):
        return self.noneQuery(query)


class TestUnit:
    sv=["x250","root","abc@123","electrical"]
    def __init__(self):
        self.sql = Mysql(self.sv)
        self.conn=self.sql.openConnection()

    def select(self):
        cmd="select * from consuming order by Month desc"
        
        if self.conn!="Completed":
            print(self.conn)
            return
        print("Select result:", self.sql.selectData(cmd))
        

    def insert(self):
        if self.conn!="Completed":
            print(self.conn)
            return
        cmd=[]
        cmd.append("INSERT INTO consuming(Month, MeterKwh, MonthKwh, VND)VALUES ('2021-09', 1, 2, 3)")
        #cmd.append("INSERT INTO consuming(Month, MeterKwh, MonthKwh, VND)VALUES ('2021-10', 4, 5, 6)")
        #cmd.append("INSERT INTO consuming(Month, MeterKwh, MonthKwh, VND)VALUES ('2021-11', 7, 8, 9)")
        print("Insert result:", self.sql.insertData(cmd))

    def update(self):
        if self.conn!="Completed":
            print(self.conn)
            return
        cmd = "Update consuming set MeterKwh=124,MonthKwh=222 where ID=19"
        print("update result:", self.sql.updateData(cmd))

    def delete(self):
        if self.conn!="Completed":
            print(self.conn)
            return
        cmd=[]
        cmd.append("Delete from consuming where id=23")
        print("Delete result:",self.sql.deleteData(cmd))

    def finished(self):
        self.sql.closeConnection()

if __name__ =="__main__":
    test=TestUnit()
    #test.insert()
    #test.delete()
    #test.update()
    test.select()
    
    test.finished()
    
    
