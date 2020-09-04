import mysql.connector

# establishes connection
# executes query
# return data after query execution if necessary
# can be used for any tables providing values to parameters asked


class MyDb:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="suvanshu", password="9861099378",
                             host="localhost", port=3306, database='hotel management') #to access databse
        self.my_cursor = self.my_connection.cursor() #to execute query

    def iud(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True
        # except Exception as e:
        #     return False

    def insert_with_id_return(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid

    def show_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    def show_data_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data
