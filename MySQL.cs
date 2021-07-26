using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data;
using MySql.Data.MySqlClient;
using System.Data;

namespace MysqlOracle
{
    class MySQL
    {
        public string[]db;
        private MySqlConnection conn=null;

        public string openConnection() {////////open connection
             //"server=x250;uid=root;pwd=abc@123;database=electrical";
            string conStr ="server="+db[0]+";uid="+db[1]+";pwd="+db[2]+";database="+db[3]+";port=3306;charset=utf8;";
            try
            {
                conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = conStr;
                conn.Open();
                return "Completed";
            }
            catch (MySqlException ex)
            {
                conn = null;
                return "Error:"+ex.Message;
            }
        }

        public string closeConnection() {/////////close connection
            if (conn == null) return "Completed";
            try
            {
                conn.Close();
                return "Completed";
            }
            catch (MySqlException ex){
                return "Error:" + ex.Message;
            }
        }

        public DataTable getDataTable(string query)
        {
            try
            {
                using (MySqlCommand cmd = new MySqlCommand(query, conn))
                {
                    cmd.CommandType = CommandType.Text;
                    using (MySqlDataAdapter sda = new MySqlDataAdapter(cmd))
                    {
                        using (DataTable dt = new DataTable())
                        {
                            sda.Fill(dt);
                            return dt;
                        }
                    }
                }
            }
            catch
            {
                return null;
            }
        }

        public string noneQuery(string query) {/// use for insert, update, delete 
            try{
                MySqlCommand cmd = new MySqlCommand(query, conn);  
                MySqlDataReader reader;   
                reader = cmd.ExecuteReader();  
                while (reader.Read())  
                {  
                }
                reader.Close();// Must to cloase for the next using.
                return "Completed";
            }  
            catch (Exception ex)  
            {   
                return "Error:"+ex.Message;  
            }  
            }  

    ///////////////////////////////the end of class///////////////////
    }
}
