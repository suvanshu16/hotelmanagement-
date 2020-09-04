from connection_db import MyDb

#items table- data insert, data retrieval, data change, findout data, delete data

class Login:
    def __init__(self):
        self.my_db = MyDb()

    def login_user(self, username, password):
        qry = "SELECT * FROM user WHERE user_name = %s AND password = %s"
        value = (username, password)
        return self.my_db.show_data_p(qry, value)

    def search_for_user(self, key):
        all = []
        try:
            qry = "SELECT * FROM user WHERE user_name LIKE '" + key + "%'"
            all = self.my_db.show_data(qry)
            return all
        except Exception as abc:
            print(abc)
            return all



class Item:
    def __init__(self):
        self.my_db = MyDb()

    def add_item(self, name, types, rate, uid):
        qry = "INSERT INTO restaurant (item_name, item_type, item_rate, c_id) VALUES (%s,%s,%s,%s)"
        values = (name, types, rate, uid)
        return self.my_db.iud(qry, values)

    def show_item(self):
        all_items = []
        try:
            qry = "SELECT * FROM restaurant"
            all_items = self.my_db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def search_item(self, key):
        all_items = []
        try:
            qry = "SELECT * FROM restaurant WHERE item_name LIKE '" + key + "%'"
            values = (key)
            all_items = self.my_db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def search_item_uid(self, key):
        all_items = []
        try:
            qry = "SELECT * FROM restaurant WHERE c_id LIKE '" + key + "%'"
            values = (key)
            all_items = self.my_db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def update_item(self, row, name, types, rate):
        try:
            qry = "UPDATE restaurant SET item_name = %s, item_type = %s, item_rate = %s WHERE item_id = %s"
            values = (name, types, rate, row)
            self.my_db.iud(qry, values)
            return True
        except Exception as abc:
            print(abc)
            return False

    def delete_item(self, row):
        qry = "DELETE FROM restaurant WHERE item_id = %s"
        values = (row,)
        self.my_db.iud(qry, values)
        return True


class Drinks:
    def __init__(self):
        self.my_db = MyDb()

    def add_drinks(self, name, rate, uid):
        qry = "INSERT INTO bar (drink_name, drink_rate, c_id) VALUES (%s,%s,%s)"
        values = (name, rate, uid)
        return self.my_db.iud(qry, values)

    def show_drinks(self):
        all_drinks = []
        try:
            qry = "SELECT * FROM bar"
            all_drinks = self.my_db.show_data(qry)
            return all_drinks
        except Exception as abc:
            print(abc)
            return all_drinks

    def search_drinks(self, key):
        all_items = []
        try:
            qry = "SELECT * FROM bar WHERE drink_name LIKE '" + key + "%'"
            all_items = self.my_db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def search_drinks_uid(self, key):
        all_items = []
        try:
            qry = "SELECT * FROM bar WHERE c_id LIKE '" + key + "%'"
            all_items = self.my_db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items

    def update_drinks(self, row, name, rate):
        try:
            qry = "UPDATE bar SET drink_name = %s, drink_rate = %s WHERE drink_id = %s"
            values = (name, rate, row)
            self.my_db.iud(qry, values)
            return True
        except Exception as abc:
            print(abc)
            return False

    def delete_drinks(self, row):
        qry = "DELETE FROM bar WHERE drink_id = %s"
        values = (row,)
        self.my_db.iud(qry, values)
        return True

class Register:
    def __init__(self):
        self.my_db = MyDb()

    def add_user(self, user_name, password, phone_no, email):
        qry = "INSERT INTO user (user_name, password, phone_no, email) VALUES (%s,%s,%s,%s)"
        values = (user_name, password, phone_no, email)
        return self.my_db.iud(qry, values)

    def extract_user_data(self, key):
        all_items = []
        try:
            qry = "SELECT * FROM user WHERE user_name LIKE '" + key + "%'"
            all_items = self.my_db.show_data(qry)
            return all_items
        except Exception as abc:
            print(abc)
            return all_items


class Customer:
    def __init__(self):
        self.my_db = MyDb()

    def add_customer(self, name, contact, address):
        qry = "INSERT INTO customer (c_name, contact, address) VALUES (%s,%s,%s)"
        values = (name, contact, address)
        return self.my_db.iud(qry, values)

    def update_customer(self, row, name, contact, address):
        try:
            qry = "UPDATE customer SET c_name = %s, contact = %s, address = %s WHERE c_id = %s"
            values = (name, contact, address, row)
            self.my_db.iud(qry, values)
            return True
        except Exception as abc:
            print(abc)
            return False

    def delete_customer(self, row):
        qry = "DELETE FROM customer WHERE c_id = %s"
        values = (row,)
        self.my_db.iud(qry, values)
        return True

    def search_customer_cid(self, key):
        try:
            qry = "SELECT * FROM customer WHERE c_id LIKE '" + key + "%'"
            values = key
            return self.my_db.show_data_p(qry, values)
        except Exception as abc:
            print(abc)

    def search_customer_name(self, key):
        try:
            qry = "SELECT * FROM customer WHERE c_name LIKE '" + key + "%'"
            values = key
            return self.my_db.show_data_p(qry, values)
        except Exception as abc:
            print(abc)

    def show_customer(self):
        all_customer = []
        try:
            qry = "SELECT * FROM customer"
            all_customer = self.my_db.show_data(qry)
            return all_customer
        except Exception as abc:
            print(abc)
            return all_customer

    def show_customer_orderby(self):
        all_customer = []
        try:
            qry = "SELECT * FROM customer ORDER BY c_name"
            all_customer = self.my_db.show_data(qry)
            return all_customer
        except Exception as abc:
            print(abc)
            return all_customer


class connect_table:
    def __init__(self):
        self.my_db = MyDb()

    def connect_customer_bar(self, key):
        try:
            qry = "SELECT * FROM bar JOIN customer ON bar.c_id = customer.c_id WHERE c_name LIKE '" + key + "%'"
            values = key
            return self.my_db.show_data_p(qry, values)
        except Exception as abc:
            print(abc)

    def connect_customer_restaurant(self, key):
        try:
            qry = "SELECT * FROM restaurant JOIN customer ON bar.c_id = customer.c_id WHERE c_name LIKE '" + key + "%'"
            values = key
            return self.my_db.show_data_p(qry, values)
        except Exception as abc:
            print(abc)
